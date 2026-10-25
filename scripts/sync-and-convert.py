#!/usr/bin/env python3
"""
graduate-study 강의 PDF -> 학습용 Markdown 자동 변환 파이프라인
- Google Drive 읽기 전용 동기화 (rclone copy --ignore-existing)
- SHA-256 해시 기반 신규/변경 PDF 감지 및 중복 처리 방지
- 기존 학습자료 덮어쓰기 원천 차단 (protected_existing 및 파일 존재 검사)
- Gemini CLI 헤드리스 변환 + 생성된 Markdown 구조/품질 검증
- 성공/실패 이력 기록 (manifest.json, logs/) 및 재시도(--retry-failed) 지원
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path("/Users/jsoftware/edu/graduate-study")
SCRIPTS_DIR = REPO_ROOT / "scripts"
MANIFEST_PATH = SCRIPTS_DIR / "manifest.json"
LOG_DIR = SCRIPTS_DIR / "logs"
GEMINI_BIN = "/opt/homebrew/bin/gemini"
RCLONE_BIN = "/opt/homebrew/bin/rclone"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).isoformat(timespec="seconds")


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = now_iso()
    line = f"[{timestamp}] {msg}"
    print(line)
    log_file = LOG_DIR / f"pipeline-{dt.date.today().strftime('%Y%m%d')}.log"
    with log_file.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def compute_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest() -> Dict[str, Any]:
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_manifest(manifest: Dict[str, Any]) -> None:
    manifest["updated_at"] = now_iso()
    tmp_path = MANIFEST_PATH.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write("\n")
    tmp_path.replace(MANIFEST_PATH)


def rclone_remote_configured(remote_name: str) -> bool:
    rclone_cmd = RCLONE_BIN if Path(RCLONE_BIN).exists() else shutil.which("rclone")
    if not rclone_cmd:
        return False
    res = subprocess.run([rclone_cmd, "listremotes"], capture_output=True, text=True)
    if res.returncode != 0:
        return False
    remotes = [r.strip().rstrip(":") for r in res.stdout.splitlines() if r.strip()]
    return remote_name in remotes


def sync_from_gdrive(manifest: Dict[str, Any], dry_run: bool = False) -> None:
    remote = manifest["config"].get("rclone_remote", "gdrive")
    if not rclone_remote_configured(remote):
        log(
            f"[WARN] rclone 리모트('{remote}:')가 아직 인증되지 않았습니다. "
            f"'./scripts/setup-gdrive-readonly.sh' 실행 후 원격 동기화가 활성화됩니다. (로컬 PDF 스캔으로 계속 진행)"
        )
        return

    rclone_cmd = RCLONE_BIN if Path(RCLONE_BIN).exists() else "rclone"
    courses = manifest["config"].get("courses", {})
    for course_key, cfg in courses.items():
        remote_path = f"{remote}:{cfg['gdrive_subpath']}"
        local_dir = Path(cfg["local_dir"])
        local_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            rclone_cmd,
            "copy",
            remote_path,
            str(local_dir),
            "--include",
            "*.pdf",
            "--ignore-existing",
            "--verbose",
        ]
        if dry_run:
            cmd.append("--dry-run")
        log(f"[SYNC] Google Drive 읽기 전용 다운로드: {' '.join(cmd)}")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            log(f"[WARN] '{course_key}' 원격 폴더 동기화 실패 또는 경로 없음: {res.stderr.strip()}")
        else:
            log(f"[SYNC] '{course_key}' 동기화 완료.")


def infer_target_md_name(course_key: str, pdf_name: str) -> str:
    stem = Path(pdf_name).stem
    if course_key == "artificial-intelligence":
        m = re.match(r"(?i)^AI-ch(\d+)(.*)$", stem)
        if m:
            ch_num = m.group(1).zfill(2)
            rest = re.sub(r"[^a-zA-Z0-9가-힣]+", "-", m.group(2)).strip("-").lower()
            suffix = f"-{rest}" if rest else "-notes"
            return f"docs/{course_key}/ch{ch_num}{suffix}.md"
    elif course_key == "computer-networks":
        m = re.match(r"(?i)^ch(\d+)\.\s*(.+)$", stem)
        if m:
            ch_num = m.group(1).zfill(2)
            slug = re.sub(r"[^a-zA-Z0-9가-힣]+", "-", m.group(2)).strip("-").lower()
            return f"docs/{course_key}/{ch_num}-{slug}.md"

    safe_slug = re.sub(r"[^a-zA-Z0-9가-힣]+", "-", stem).strip("-").lower()
    return f"docs/{course_key}/{safe_slug}.md"


def discover_pdfs(manifest: Dict[str, Any]) -> int:
    """로컬 강의자료 폴더를 스캔하여 신규 또는 변경된 PDF를 manifest에 등록한다."""
    courses = manifest["config"].get("courses", {})
    entries: List[Dict[str, Any]] = manifest.get("entries", [])
    added_or_updated = 0

    for course_key, cfg in courses.items():
        local_dir = Path(cfg["local_dir"])
        if not local_dir.exists():
            continue

        for pdf_path in sorted(local_dir.glob("*.pdf")):
            pdf_name = pdf_path.name
            current_sha = compute_sha256(pdf_path)

            matching = [
                e for e in entries
                if e.get("course") == course_key and e.get("source_pdf") == pdf_name
            ]

            if not matching:
                target_md = infer_target_md_name(course_key, pdf_name)
                target_abs = REPO_ROOT / target_md
                if target_abs.exists():
                    target_md = target_md.replace(".md", f"-auto-{current_sha[:8]}.md")

                new_id = f"{course_key[:2]}-{Path(pdf_name).stem.lower().replace(' ', '-')}"
                new_entry = {
                    "id": new_id,
                    "course": course_key,
                    "source_pdf": pdf_name,
                    "full_sha256": current_sha,
                    "page_range": "all",
                    "chapter_title": f"{cfg['course_title']} - {Path(pdf_name).stem}",
                    "target_md": target_md,
                    "status": "pending",
                    "protected_existing": False,
                    "attempts": 0,
                    "last_run_at": None,
                    "notes": "신규 감지된 PDF 자동 등록",
                }
                entries.append(new_entry)
                added_or_updated += 1
                log(f"[DISCOVER] 신규 PDF 등록: {pdf_name} -> {target_md}")
            else:
                # 이미 등록된 PDF의 해시가 변경되었는지 확인 (기존 파일 덮어쓰기 없이 새 엔트리 생성)
                same_hash = any(e.get("full_sha256") == current_sha for e in matching)
                if not same_hash:
                    base_target = matching[-1]["target_md"]
                    rev_target = base_target.replace(".md", f"-rev-{current_sha[:8]}.md")
                    rev_id = f"{matching[-1]['id']}-rev-{current_sha[:8]}"
                    rev_entry = {
                        "id": rev_id,
                        "course": course_key,
                        "source_pdf": pdf_name,
                        "full_sha256": current_sha,
                        "page_range": "all",
                        "chapter_title": f"{cfg['course_title']} - {Path(pdf_name).stem} (개정판)",
                        "target_md": rev_target,
                        "status": "pending",
                        "protected_existing": False,
                        "attempts": 0,
                        "last_run_at": None,
                        "notes": f"원본 PDF 해시 변경 감지 (기존 파일 보존, 신규 파일로 분리 생성)",
                    }
                    entries.append(rev_entry)
                    added_or_updated += 1
                    log(f"[DISCOVER] 변경된 PDF 감지: {pdf_name} -> {rev_target} (기존 노트 보호)")

    return added_or_updated


def validate_markdown(md_path: Path) -> Tuple[bool, List[str]]:
    """생성된 학습용 Markdown 파일의 구조·분량·수식·예상문제 포함 여부를 검증한다."""
    issues: List[str] = []
    if not md_path.exists():
        return False, ["파일이 존재하지 않습니다."]

    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if len(lines) < 120 or len(text) < 4000:
        issues.append(f"분량 부족 (현재 {len(lines)}줄, {len(text)}자 / 최소 120줄, 4000자 필요)")

    if not re.search(r"^#\s+.+", text, re.MULTILINE):
        issues.append("H1 제목('# ...')이 없습니다.")

    if not re.search(r"^##\s+.*목차", text, re.MULTILINE):
        issues.append("목차 섹션('## 📌 목차' 또는 '## 목차')이 없습니다.")

    if not re.search(r"p\.\s*\d+", text):
        issues.append("원본 PDF 페이지 출처 표기(예: p.10)가 없습니다.")

    if not re.search(r"^\|.+\|\s*\n\|[-:\s|]+\|", text, re.MULTILINE):
        issues.append("비교표(Markdown Table)가 포함되어 있지 않습니다.")

    if not re.search(r"(주요\s*용어|핵심\s*용어|용어\s*정리)", text):
        issues.append("주요 용어 정리 섹션이 없습니다.")

    if not re.search(r"(예상\s*문제|자기\s*점검|Review)", text, re.IGNORECASE):
        issues.append("예상문제/자기점검 섹션이 없습니다.")

    open_details = len(re.findall(r"<details>", text))
    close_details = len(re.findall(r"</details>", text))
    if open_details == 0 or open_details != close_details:
        issues.append(f"<details> 태그 불일치 또는 누락 (열림 {open_details}개, 닫힘 {close_details}개)")

    fence_count = len(re.findall(r"^```", text, re.MULTILINE))
    if fence_count % 2 != 0:
        issues.append(f"코드 블록(```) 짝이 맞지 않습니다 (총 {fence_count}개).")

    return (len(issues) == 0), issues


def build_prompt(manifest: Dict[str, Any], entry: Dict[str, Any], pdf_path: Path) -> str:
    template_rel = manifest["config"].get("prompt_template", "scripts/prompts/common-lecture-prompt.md")
    template_path = REPO_ROOT / template_rel
    template = template_path.read_text(encoding="utf-8")

    course_key = entry["course"]
    course_cfg = manifest["config"]["courses"][course_key]
    replacements = {
        "{{COURSE_NAME}}": course_cfg["course_title"],
        "{{SOURCE_PDF}}": entry["source_pdf"],
        "{{PAGE_RANGE}}": entry.get("page_range", "all"),
        "{{TARGET_MD}}": entry["target_md"],
        "{{CHAPTER_TITLE}}": entry.get("chapter_title", f"{course_cfg['course_title']} - {entry['source_pdf']}"),
        "{{NAV_LINKS}}": entry.get("nav_links", "이전 장 및 과목 목차 링크 포함"),
        "{{EXTRA_INSTRUCTIONS}}": entry.get("notes", ""),
    }
    prompt = template
    for k, v in replacements.items():
        prompt = prompt.replace(k, str(v))

    prompt += (
        f"\n\n---\n"
        f"원본 PDF 경로: @{pdf_path}\n"
        f"변환할 페이지 범위: {entry.get('page_range', 'all')}\n"
        f"주의: 앞뒤 인사말이나 코드블록 래핑 없이 순수 Markdown 본문(`# 제목`으로 시작)만 출력하세요.\n"
    )
    return prompt


def run_gemini_conversion(
    manifest: Dict[str, Any],
    entry: Dict[str, Any],
    max_retries: int = 2,
    dry_run: bool = False,
) -> bool:
    course_key = entry["course"]
    course_cfg = manifest["config"]["courses"][course_key]
    pdf_path = Path(course_cfg["local_dir"]) / entry["source_pdf"]
    target_md = REPO_ROOT / entry["target_md"]

    if not pdf_path.exists():
        log(f"[ERROR] 원본 PDF 파일을 찾을 수 없습니다: {pdf_path}")
        entry["status"] = "failed"
        entry["last_run_at"] = now_iso()
        entry.setdefault("error_history", []).append({"time": now_iso(), "error": "Source PDF not found"})
        return False

    # 안전장치: 보호된 기존 파일이거나 이미 완료된 기존 파일이면 절대 덮어쓰지 않음
    if entry.get("protected_existing") and target_md.exists():
        log(f"[SKIP] 보호된 기존 학습자료입니다 (덮어쓰기 차단): {entry['target_md']}")
        return True

    # 만약 이미 target_md가 존재하고 검증을 통과한다면 재검증 후 완료 처리 (덮어쓰지 않음)
    if target_md.exists():
        ok, issues = validate_markdown(target_md)
        if ok:
            log(f"[VALIDATE-OK] 대상 파일이 이미 존재하며 모든 품질 검증을 통과했습니다: {entry['target_md']}")
            entry["status"] = "completed"
            entry["last_run_at"] = now_iso()
            entry["output_sha256"] = compute_sha256(target_md)
            entry["validation"] = {"passed": True, "checked_at": now_iso(), "issues": []}
            return True
        else:
            log(f"[WARN] 기존 대상 파일이 존재하나 검증 이슈가 있습니다 ({issues}). 원본 보호를 위해 .draft.md로 생성합니다.")
            target_md = target_md.with_suffix(".draft.md")

    if dry_run:
        log(f"[DRY-RUN] 변환 예정: {pdf_path.name} (p.{entry.get('page_range', 'all')}) -> {target_md.relative_to(REPO_ROOT)}")
        return True

    prompt = build_prompt(manifest, entry, pdf_path)
    include_dirs = f"{pdf_path.parent},{target_md.parent}"

    for attempt in range(1, max_retries + 1):
        entry["attempts"] = entry.get("attempts", 0) + 1
        entry["last_run_at"] = now_iso()
        log(f"[CONVERT] ({attempt}/{max_retries}) Gemini CLI 실행 중: {entry['id']} -> {target_md.name}")

        tmp_out = SCRIPTS_DIR / "tmp" / f"{entry['id']}.tmp.md"
        tmp_out.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            GEMINI_BIN,
            "--include-directories",
            include_dirs,
            "-p",
            prompt,
            "--output-format",
            "text",
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            err_msg = res.stderr.strip() or f"Exit code {res.returncode}"
            log(f"[ERROR] Gemini CLI 호출 실패 (시도 {attempt}): {err_msg}")
            entry.setdefault("error_history", []).append({"time": now_iso(), "error": err_msg})
            time.sleep(2 * attempt)
            continue

        output_text = res.stdout.strip()
        # 혹시 ```markdown ... ``` 코드블록으로 감싸져 출력된 경우 벗겨냄
        if output_text.startswith("```"):
            output_text = re.sub(r"^```(?:markdown|md)?\s*\n", "", output_text)
            output_text = re.sub(r"\n```\s*$", "", output_text)

        tmp_out.write_text(output_text + "\n", encoding="utf-8")
        ok, issues = validate_markdown(tmp_out)
        if ok:
            target_md.parent.mkdir(parents=True, exist_ok=True)
            tmp_out.replace(target_md)
            entry["status"] = "completed"
            entry["output_sha256"] = compute_sha256(target_md)
            entry["validation"] = {"passed": True, "checked_at": now_iso(), "issues": []}
            log(f"[SUCCESS] 변환 및 검증 완료: {target_md.relative_to(REPO_ROOT)}")
            return True
        else:
            err_msg = f"검증 실패: {', '.join(issues)}"
            log(f"[WARN] 생성된 파일 검증 미통과 (시도 {attempt}): {err_msg}")
            entry.setdefault("error_history", []).append({"time": now_iso(), "error": err_msg})
            time.sleep(2 * attempt)

    entry["status"] = "failed"
    entry["validation"] = {"passed": False, "checked_at": now_iso()}
    log(f"[FAILED] 최대 재시도 횟수({max_retries}) 초과: {entry['id']}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="대학원 강의 PDF -> 학습용 Markdown 자동화 파이프라인")
    parser.add_argument("--sync", action="store_true", help="Google Drive(rclone)에서 신규 PDF 동기화 수행")
    parser.add_argument("--dry-run", action="store_true", help="실제 변환 없이 감지 및 실행 계획만 출력")
    parser.add_argument("--retry-failed", action="store_true", help="이전에 실패(failed)한 작업도 재시도")
    parser.add_argument("--entry-id", type=str, default=None, help="특정 manifest entry ID만 지정 실행")
    parser.add_argument("--validate-only", action="store_true", help="manifest에 등록된 모든 Markdown 파일 검증만 수행")
    parser.add_argument("--max-retries", type=int, default=2, help="실패 시 최대 재시도 횟수 (기본값: 2)")
    args = parser.parse_args()

    manifest = load_manifest()

    if args.validate_only:
        all_ok = True
        for entry in manifest.get("entries", []):
            md_path = REPO_ROOT / entry["target_md"]
            ok, issues = validate_markdown(md_path)
            status_str = "PASS" if ok else f"WARN ({'; '.join(issues)})"
            log(f"[VALIDATE] {entry['id']} ({entry['target_md']}): {status_str}")
            if not ok and entry.get("status") == "completed" and not entry.get("protected_existing"):
                all_ok = False
        return 0 if all_ok else 1

    if args.sync:
        sync_from_gdrive(manifest, dry_run=args.dry_run)

    discovered = discover_pdfs(manifest)
    if discovered > 0 and not args.dry_run:
        save_manifest(manifest)

    target_statuses = {"pending"}
    if args.retry_failed:
        target_statuses.add("failed")

    entries = manifest.get("entries", [])
    ran_count = 0
    failed_count = 0

    for entry in entries:
        if args.entry_id and entry.get("id") != args.entry_id:
            continue

        # 해시 대조: 기존 파일의 실제 SHA-256과 manifest의 full_sha256 비교
        course_cfg = manifest["config"]["courses"][entry["course"]]
        pdf_path = Path(course_cfg["local_dir"]) / entry["source_pdf"]
        if pdf_path.exists():
            actual_sha = compute_sha256(pdf_path)
            if entry.get("status") == "completed" and entry.get("full_sha256") == actual_sha and not args.entry_id:
                log(f"[SKIP] 이미 처리 완료된 PDF입니다 (해시 일치): {entry['id']} -> {entry['target_md']}")
                continue

        if entry.get("status") not in target_statuses and not args.entry_id:
            continue

        ran_count += 1
        ok = run_gemini_conversion(manifest, entry, max_retries=args.max_retries, dry_run=args.dry_run)
        if not ok:
            failed_count += 1
        if not args.dry_run:
            save_manifest(manifest)

    log(f"[SUMMARY] 처리 대상: {ran_count}건 | 실패: {failed_count}건")
    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
