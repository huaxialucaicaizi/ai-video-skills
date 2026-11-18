#!/usr/bin/env bash
# Mac video toolchain check for ai-video-skills (first version: Mac only).
# Reports which tool requires which version — do not collapse into one Node line.
# Note: always use ${VAR} before non-ASCII text; macOS /bin/bash 3.2 mishandles
# $VAR next to fullwidth punctuation under `set -u`.
set -euo pipefail

OS="$(uname -s)"
echo "== ai-video-skills doctor =="
echo "OS: ${OS} ($(uname -m))"

if [[ "${OS}" != "Darwin" ]]; then
  echo "WARN: 第一版仅支持 Mac。当前不是 Darwin；结果仅供参考，正式验收以 Mac 为准（待 Mac 实测）。"
fi

pass=0
fail=0
warn=0

ok() { echo "OK   $1"; pass=$((pass + 1)); }
bad() { echo "FAIL $1"; fail=$((fail + 1)); }
note() { echo "WARN $1"; warn=$((warn + 1)); }

# --- Node.js: report per-tool requirements separately ---
if command -v node >/dev/null 2>&1; then
  NODE_VER="$(node -v | sed 's/^v//')"
  NODE_MAJOR="${NODE_VER%%.*}"
  ok "Node.js ${NODE_VER} 已安装"
  if [[ "${NODE_MAJOR}" -ge 22 ]]; then
    ok "HyperFrames 要求 Node.js 22+：满足（当前 ${NODE_VER}）"
  else
    bad "HyperFrames 要求 Node.js 22+：当前 ${NODE_VER}"
  fi
  # Claude Code npm 安装路径也常要求 Node 22+（以官方文档为准）
  if [[ "${NODE_MAJOR}" -ge 22 ]]; then
    ok "Claude Code（npm 安装路径）常见要求 Node.js 22+：满足"
  else
    note "Claude Code（npm 安装路径）常见要求 Node.js 22+：当前 ${NODE_VER}（以官方文档为准）"
  fi
  # DeepSeek Harness 文档曾写 24.9+（待核实是否仍适用）
  if [[ "${NODE_MAJOR}" -ge 24 ]]; then
    ok "DeepSeek Harness 文档要求（曾写 24.9+）：当前主版本 ${NODE_MAJOR} 可能满足（待核实完整版本）"
  else
    note "DeepSeek Harness 文档曾写 Node.js 24.9+：当前 ${NODE_VER}（待核实；仅在使用该工具时需要）"
  fi
else
  bad "未找到 Node.js（HyperFrames / 渲染需要；Claude Code npm 路径也常需要）"
fi

# --- FFmpeg（总需求：环境检查必须包含）---
if command -v ffmpeg >/dev/null 2>&1; then
  FF="$(ffmpeg -version 2>/dev/null | head -n1 || true)"
  ok "ffmpeg 已安装：${FF}"
else
  bad "未找到 ffmpeg（HyperFrames 本地渲染需要；请先安装后再渲染）"
fi

# --- Python（转写等）---
if command -v python3 >/dev/null 2>&1; then
  PYV="$(python3 --version 2>&1)"
  ok "Python3：${PYV}"
else
  bad "未找到 python3（talking-head 转写流程需要）"
fi

# --- Optional: hyperframes CLI availability ---
if command -v npx >/dev/null 2>&1; then
  ok "npx 可用"
else
  note "未找到 npx（通常随 npm 提供）"
fi

echo
echo "摘要：pass=${pass} fail=${fail} warn=${warn}"
if [[ "${fail}" -gt 0 ]]; then
  echo "有缺失项：可交给 setup-doctor（ai-from-zero 仓库）继续排障。"
  exit 1
fi
echo "基础环境检查通过。"
exit 0
