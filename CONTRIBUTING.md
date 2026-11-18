# 贡献指南

感谢关注 ai-video-skills。

## 原则

1. 需求以上游总需求与本仓库 README 为准；不扩大本周范围（不做 promo / Windows / 数字人）。
2. 不编造数字与出处；未知写「待核实」或「待 Mac 实测」。
3. examples 必须标注「虚构示例」。
4. 安装路径可写 `.codebuddy/skills/`（CI 对应该路径片段白名单）；正文不要提前后公司相关产品名，不要加第三方推广。
5. 公开音视频素材须授权清楚并注明出处；没有就不放。

## 本地检查

```bash
./scripts/doctor.sh
python3 scripts/ci_validate.py
```

## PR

- 基于 `main` 开分支
- 描述改了什么、如何自测
- 不要提交 `node_modules/`、MP4、自检截帧
