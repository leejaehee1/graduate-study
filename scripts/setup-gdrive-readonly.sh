#!/usr/bin/env zsh
# Google Drive 읽기 전용(drive.readonly) rclone 리모트 설정 도우미 스크립트
set -euo pipefail

REMOTE_NAME="${1:-gdrive}"

echo "================================================================"
echo " Google Drive 읽기 전용(Read-Only) rclone 연결 설정"
echo " 리모트 이름: ${REMOTE_NAME}"
echo " 권한 범위(Scope): drive.readonly (원본 수정·삭제 원천 차단)"
echo " 설정 저장 위치: ~/.config/rclone/rclone.conf (Git 저장소 외부)"
echo "================================================================"

if ! command -v rclone >/dev/null 2>&1; then
  echo "[오류] rclone이 설치되어 있지 않습니다. 'brew install rclone'을 먼저 실행해 주세요."
  exit 1
fi

if rclone listremotes | grep -q "^${REMOTE_NAME}:$"; then
  echo "[확인] 이미 '${REMOTE_NAME}:' 리모트가 설정되어 있습니다."
  echo "현재 설정된 scope 확인:"
  rclone config show "${REMOTE_NAME}" | grep -E "^(type|scope|root_folder_id)" || true
else
  echo ""
  echo "브라우저가 열리면 Google 계정으로 로그인하여 읽기 전용 권한을 승인해 주세요..."
  rclone config create "${REMOTE_NAME}" drive scope=drive.readonly
fi

echo ""
echo "================================================================"
echo " 연결 테스트: Google Drive 최상위 폴더 목록 조회 (최대 20개)"
echo "================================================================"
rclone lsd "${REMOTE_NAME}:" --max-depth 1 | head -n 20 || true

echo ""
echo "✅ 설정이 완료되었습니다!"
echo "대학원 폴더 확인 명령 예시:"
echo "  rclone lsf \"${REMOTE_NAME}:대학원\""
