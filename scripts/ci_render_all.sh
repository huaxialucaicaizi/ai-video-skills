#!/usr/bin/env bash
# Render every HyperFrames template under dist/*/templates/*
# Strict: lint must report 0 errors before each render.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_ROOT="${1:-${ROOT}/dist}"
mapfile -t TPLS < <(find "${SRC_ROOT}" -type f -path "*/templates/*/package.json" | sort)
if [[ ${#TPLS[@]} -eq 0 ]]; then
  echo "FAIL: no templates under ${SRC_ROOT}"
  exit 1
fi
mkdir -p "${ROOT}/tmp-render"
REPORT="${ROOT}/tmp-render/render-report.txt"
: > "${REPORT}"
for pkg_json in "${TPLS[@]}"; do
  TPL="$(dirname "${pkg_json}")"
  NAME="$(basename "${TPL}")"
  echo "== ${TPL#$SRC_ROOT/} =="
  cd "${TPL}"
  if grep -E "url\([\"']?\.\./" index.html; then
    echo "FAIL: parent-traversal URL in ${TPL}/index.html"
    exit 1
  fi
  test -f fonts/OFL.txt || { echo "FAIL: missing fonts/OFL.txt in ${TPL}"; exit 1; }
  npm install --silent
  set +e
  LINT_OUT="$(npx hyperframes lint 2>&1)"
  set -e
  printf "%s\n" "${LINT_OUT}"
  ERR_COUNT="$(printf "%s\n" "${LINT_OUT}" | sed -nE "s/.*([0-9]+) error\(s\).*/\1/p" | tail -n1)"
  if [[ -z "${ERR_COUNT}" ]]; then
    echo "FAIL: could not parse lint error count for ${NAME}"
    exit 1
  fi
  if [[ "${ERR_COUNT}" -gt 0 ]]; then
    echo "FAIL: ${NAME} lint ${ERR_COUNT} error(s); refusing render"
    exit 1
  fi
  npm run render
  OUT="$(ls -1 renders/*.mp4 | head -n1)"
  DUR="$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "${OUT}")"
  WH="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "${OUT}")"
  SIZE="$(wc -c < "${OUT}" | tr -d " ")"
  echo "SUMMARY ${NAME}: ${DUR}s ${WH} bytes=${SIZE}"
  echo "${NAME}\t${DUR}\t${WH}\t${SIZE}\t${OUT}" >> "${REPORT}"
done
echo "OK all templates rendered; report ${REPORT}"
