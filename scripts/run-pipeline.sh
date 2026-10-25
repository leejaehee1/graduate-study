#!/usr/bin/env zsh
# 대학원 강의자료 Google Drive 동기화 및 Gemini CLI Markdown 변환 실행 래퍼
set -euo pipefail

SCRIPT_DIR="${0:A:h}"
REPO_ROOT="${SCRIPT_DIR:h}"

cd "$REPO_ROOT"
python3 "${SCRIPT_DIR}/sync-and-convert.py" "$@"
