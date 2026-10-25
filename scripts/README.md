# 대학원 강의 PDF → 학습용 Markdown 자동화 가이드 (`scripts/`)

Google Drive의 대학원 강의자료(인공지능, 컴퓨터 네트워크) PDF를 **읽기 전용(`drive.readonly`)** 으로 동기화하고, **Gemini CLI** 를 이용해 VitePress 학습용 Markdown 파일로 자동 변환·검증하는 파이프라인입니다.

---

## 1. 폴더 및 파일 구조

```text
/Users/jsoftware/edu/graduate-study/scripts/
├── .gitignore                              # 인증 토큰·로그·임시 파일 Git 커밋 원천 차단
├── README.md                               # 설치·인증·실행·스케줄링 매뉴얼 (현재 문서)
├── manifest.json                           # PDF 해시(SHA-256), 페이지 범위, 처리 상태, 검증 이력 DB
├── setup-gdrive-readonly.sh                # Google Drive 읽기 전용(drive.readonly) rclone 설정 스크립트
├── sync-and-convert.py                     # 메인 자동화 파이프라인 (동기화·해시감지·변환·검증·재시도)
├── run-pipeline.sh                         # CLI 수동/예약 실행용 쉘 래퍼
├── extract-pdf-figures.swift               # PDF 내 슬라이드 도식/실습 화면 크롭 추출 유틸리티
├── com.graduate-study.sync.plist.example   # macOS launchd 정기 자동 실행 설정 예시
└── prompts/
    └── common-lecture-prompt.md            # 전 과목(네트워크·인공지능) 재사용 공통 프롬프트 템플릿
```

---

## 2. 사전 설치 확인

현재 Mac에 필요한 도구가 모두 설치되어 있습니다:

| 도구 | 경로 | 버전 | 역할 |
|---|---|---|---|
| **rclone** | `/opt/homebrew/bin/rclone` | `v1.75.2` | Google Drive 읽기 전용 동기화 |
| **Gemini CLI** | `/opt/homebrew/bin/gemini` | `v0.65.0` | PDF $\rightarrow$ 학습용 Markdown 변환 |
| **Python 3** | `/Users/jsoftware/.pyenv/shims/python3` | `3.x` | 해시 비교, 매니페스트 관리, 검증 및 재시도 제어 |

---

## 3. Google Drive 읽기 전용(`rclone`) 인증 절차

Google Drive 원본 파일을 절대 수정·삭제하지 못하도록 **`drive.readonly` 권한 범위(Scope)** 로만 연결합니다. 인증 토큰은 Git 저장소 외부인 `~/.config/rclone/rclone.conf`에만 저장됩니다.

### 3.1 원클릭 인증 도우미 실행 (권장)

터미널에서 아래 스크립트를 실행하면 브라우저가 열리며 Google 계정 로그인 후 즉시 `gdrive:` 리모트가 읽기 전용으로 생성됩니다.

```zsh
cd /Users/jsoftware/edu/graduate-study
chmod +x scripts/setup-gdrive-readonly.sh scripts/run-pipeline.sh
./scripts/setup-gdrive-readonly.sh
```

### 3.2 수동 명령어로 인증하는 경우

```zsh
# 1. 읽기 전용(drive.readonly) 스코프로 gdrive 리모트 생성
rclone config create gdrive drive scope=drive.readonly

# 2. 연결된 Google Drive 폴더 확인
rclone lsd gdrive:
rclone lsf "gdrive:대학원/인공지능"
rclone lsf "gdrive:대학원/컴퓨터 네트워크"
```

> **참고**: 만약 Google Drive 내 폴더 경로가 `대학원/인공지능`과 다르다면 `scripts/manifest.json`의 `config.courses.<과목>.gdrive_subpath` 값만 실제 Drive 경로에 맞게 수정하면 됩니다.

---

## 4. 자동화 파이프라인 실행 방법

### 4.1 실행 계획 미리 보기 (`--dry-run`)
실제 파일을 생성하거나 수정하지 않고, 어떤 PDF가 신규/변경/스킵 대상인지 확인합니다.

```zsh
./scripts/run-pipeline.sh --dry-run
```

### 4.2 로컬 PDF 스캔 및 미처리 항목 변환 실행

```zsh
./scripts/run-pipeline.sh
```

### 4.3 Google Drive 동기화 + 변환 + 실패 항목 재시도 통합 실행

```zsh
./scripts/run-pipeline.sh --sync --retry-failed
```

### 4.4 특정 항목만 지정 실행 또는 전체 Markdown 품질 검증

```zsh
# 특정 manifest ID만 지정 실행 (예: 컴퓨터 네트워크 5장 후반부)
./scripts/run-pipeline.sh --entry-id cn-ch05-part2

# 등록된 모든 Markdown 파일의 구조·수식·표·예상문제 포함 여부 검증
./scripts/run-pipeline.sh --validate-only
```

---

## 5. 안전장치 및 중복·오류 처리 메커니즘

1. **기존 학습자료 보호 (`protected_existing: true`)**:
   - 이미 작성된 인공지능(`01`~`06`) 및 컴퓨터 네트워크(`01`~`05`) 파일은 `manifest.json`에 해시와 함께 보호 대상으로 등록되어 있어 **절대 덮어쓰거나 삭제하지 않습니다.**
2. **SHA-256 해시 기반 중복 및 변경 감지**:
   - 동일한 PDF(SHA-256 일치)는 자동으로 건너뜁니다(`[SKIP]`).
   - 만약 교수님이 필기를 추가하여 기존 PDF의 해시가 변경되면, 기존 `.md` 파일을 덮어쓰지 않고 `*-rev-<해시8자리>.md` 형태의 별도 파일로 생성하여 비교·검토할 수 있게 합니다.
3. **자동 검증(`validate_markdown`) 및 재시도(`--max-retries`)**:
   - 생성된 Markdown이 최소 분량(120줄/4,000자 이상), H1 제목, 목차, 원본 페이지 표기(`p.xx`), 비교표, 주요 용어, `<details>` 정답 토글이 포함된 예상문제를 모두 갖추었는지 자동 검사합니다.
   - 검증 실패 시 임시 파일에만 기록하고 지정된 횟수(기본 2회)만큼 자동 재시도하며, 모든 기록은 `scripts/manifest.json`과 `scripts/logs/pipeline-YYYYMMDD.log`에 남습니다.

---

## 6. macOS 정기 자동 실행 (`launchd`) 설정

매주 또는 매일 정해진 시각에 자동으로 새 강의 PDF를 감지하고 변환하려면 `launchd` 에이전트를 등록합니다.

```zsh
# 1. LaunchAgents 폴더로 예시 plist 복사
cp /Users/jsoftware/edu/graduate-study/scripts/com.graduate-study.sync.plist.example \
   ~/Library/LaunchAgents/com.graduate-study.sync.plist

# 2. 스케줄러 등록 (기본: 매일 21:00 실행)
launchctl load ~/Library/LaunchAgents/com.graduate-study.sync.plist

# 3. 상태 확인
launchctl list | grep com.graduate-study.sync

# (참고) 스케줄러 해제 시
launchctl unload ~/Library/LaunchAgents/com.graduate-study.sync.plist
```
