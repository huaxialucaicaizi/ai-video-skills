#!/usr/bin/env bash
# Zip each dist/<name>/ into release/<name>.zip for Claude desktop Skills upload.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="${ROOT}/dist"
OUT="${ROOT}/release"
NAMES=(video-router explainer data-story promo animation talking-head footage clip-long screencast)
for name in "${NAMES[@]}"; do
  if [[ ! -d "${DIST}/${name}" ]]; then
    echo "FAIL: missing dist/${name} — run python3 scripts/build_dist.py first"
    exit 1
  fi
done
rm -rf "${OUT}"
mkdir -p "${OUT}"
for name in "${NAMES[@]}"; do
  ( cd "${DIST}" && zip -r -q "${OUT}/${name}.zip" "${name}" )
  echo "OK ${OUT}/${name}.zip ($(wc -c < "${OUT}/${name}.zip" | tr -d ' ') bytes)"
done
echo "OK wrote zips under ${OUT}/ (not committed)"
