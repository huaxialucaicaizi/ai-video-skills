# short-explainer（HyperFrames 短模板）

虚构示例主题：「什么是 token？」约 9 秒、1080×1920、30fps、只出字幕不配音。

## 要求

- Node.js 22+
- 系统已安装 ffmpeg（见仓库 `scripts/doctor.sh`）
- 字体：仓库 `shared/fonts/`（OFL），渲染不访问外网字体 CDN
- GSAP：本目录 `npm install` 本地依赖，不从 jsDelivr 加载

## 命令

```bash
cd code-video/explainer/templates/short-explainer
npm install
npx hyperframes render --output /tmp/short-explainer.mp4
```

渲染结束后终端可能出现 HyperFrames 桌面 App 推广文字——只在终端，不进视频。

## 自检

用 ffmpeg 在约 1.5s / 4.5s / 7.5s 截帧，**打开图片**检查：文字不重叠、不出安全区。
