# Changelog

## 0.2.0 — 2026-11-24

- 10 种办公视频风格均交付对应 skill：`explainer` / `data-story` / `promo` / `animation` / `talking-head` / `footage` / `clip-long` / `screencast` + `video-router`
- 代码生成模板均可本地渲染短样片（9s / 1080×1920）；半自动剪辑流程文档齐全，客户端触发与部分合成步骤标「待 Mac 实测」
- `dist/` 按显式清单生成 9 个安装包；`make release` 打 zip 供 Claude 桌面版上传（zip 不入库）
- README：双语技能名 + 使用场景；去掉徽章；主路径 Claude 桌面版 zip 安装

## 0.1.0 — 2026-11-18

- 第一版：`explainer` + `talking-head` + 最简 `video-router`
- `shared/styles` / `overlays` / `subtitle-tts`
- CI：frontmatter、触发、禁用词、macOS doctor、dist 冒烟
- 许可证 Apache-2.0；仅支持 Mac
