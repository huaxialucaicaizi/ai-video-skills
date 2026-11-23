#!/usr/bin/env bash
# Zip each dist/<name>/ into release/<name>.zip for Claude desktop Skills upload.
# Does not commit the zips; release/ is gitignored.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="${ROOT}/dist"
OUT="${ROOT}/release"

if [[ ! -d "${DIST}/explainer" || ! -d "${DIST}/talking-head" || ! -d "${DIST}/video-router" ]]; then
  echo "FAIL: missing dist packages — run python3 scripts/build_dist.py first"
  exit 1
fi

rm -rf "${OUT}"
mkdir -p "${OUT}"

for name in video-router explainer talking-head; do
  (
    cd "${DIST}"
    zip -r -q "${OUT}/${name}.zip" "${name}"
  )
  echo "OK ${OUT}/${name}.zip ($(wc -c < "${OUT}/${name}.zip" | tr -d ' ') bytes)"
done

echo "OK wrote zips under ${OUT}/ (not committed)"
