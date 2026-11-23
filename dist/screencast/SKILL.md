---
name: screencast
description: "用户要软件教程录屏（混合路线）时用：口播/录屏主线 + 代码生成的步骤标注、放大框、键盘提示 overlays；产品界面只用真实录屏。Use for software tutorial screencasts: talking-head/screen main line plus code-generated step callouts, zoom boxes, and keyboard-hint overlays."
---

# screencast

学习路径位置：**用进工作**。路线：**混合**（古法剪主线 + 代码生成 overlays）。目前仅支持 **Mac**。叠层合成全流程：**待 Mac 实测**。

## 红线

1. 软件界面必须来自用户真实录屏
2. 不生成假界面冒充产品
3. 不生成真人；真人出镜只用用户素材

## 工作流

1. 收集录屏 + 可选口播轨
2. 写步骤表（时间码 + 操作）
3. 用 `overlays/` 生成步骤标注 / 放大框 / 键盘提示
4. 叠到主线时间轴（合成步骤待 Mac 实测）
5. 字幕 + 剪映精修清单

Overlays 见本包 `overlays/`（亦可对照 `shared/overlays/`）。
