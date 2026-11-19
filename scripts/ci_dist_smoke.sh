#!/usr/bin/env bash
# CI: prove dist/explainer is self-contained.
# Strict: hyperframes lint must report 0 errors BEFORE render; otherwise fail.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${ROOT}/dist/explainer"
if [[ ! -d "${SRC}" ]]; then
  echo "FAIL: missing dist/explainer — run python3 scripts/build_dist.py first"
  exit 1
fi

TMP="$(mktemp -d /tmp/ai-video-skills-explainer-XXXXXX)"
cleanup() { rm -rf "${TMP}"; }
trap cleanup EXIT

echo "== copy dist/explainer → ${TMP} =="
cp -R "${SRC}/." "${TMP}/"

python3 "${ROOT}/scripts/ci_package_check.py" "${SRC}"

TPL="${TMP}/templates/short-explainer"
cd "${TPL}"

if grep -E 'url\(["'\'']?\.\./' index.html; then
  echo "FAIL: parent-traversal asset URL in packaged index.html"
  exit 1
fi
test -f fonts/OFL.txt || { echo "FAIL: missing fonts/OFL.txt"; exit 1; }

echo "== npm install =="
npm install

echo "== hyperframes lint (STRICT: 0 errors required before render) =="
set +e
LINT_OUT="$(npx hyperframes lint 2>&1)"
LINT_EC=$?
set -e
printf '%s\n' "${LINT_OUT}"
ERR_COUNT="$(printf '%s\n' "${LINT_OUT}" | sed -nE 's/.*([0-9]+) error\(s\).*/\1/p' | tail -n1)"
if [[ -z "${ERR_COUNT}" ]]; then
  echo "FAIL: could not parse hyperframes lint error count"
  exit 1
fi
if [[ "${ERR_COUNT}" -gt 0 ]]; then
  echo "FAIL: hyperframes lint reported ${ERR_COUNT} error(s); refusing to render"
  exit 1
fi
echo "OK hyperframes lint (errors=0, exit=${LINT_EC}; warnings allowed)"

echo "== npm run render (smoke, only after lint 0 errors) =="
npm run render
OUT="${TPL}/renders/short-explainer.mp4"
if [[ ! -f "${OUT}" ]]; then
  echo "FAIL: missing render output ${OUT}"
  exit 1
fi
SIZE="$(wc -c < "${OUT}" | tr -d ' ')"
echo "OK render smoke: ${OUT} (${SIZE} bytes)"
