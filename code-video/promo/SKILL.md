---
name: promo
description: "用户要产品宣传片或文字快闪/金句卡短视频时用：套风格卡，用 HyperFrames 生成包装画面；产品界面只用用户真实截图或录屏，没有就用标明「示例」的中性占位。不生成真人、不用真实品牌素材。Use for product promo or kinetic-text/quote-card shorts. Real product UI only from user screenshots; otherwise a neutral 示例 placeholder."
---

# promo

学习路径位置：**用进工作**。路线：**代码生成**。覆盖：**产品宣传片**与**文字快闪 / 金句卡**。目前仅支持 **Mac**（待 Mac 实测完整验收）。

## 红线

1. 产品界面只用用户真实截图/录屏；没有则中性占位并标「示例」
2. 不使用真实品牌 Logo/商标素材
3. 不生成真人画面、不用数字人
4. 字体本地 OFL；渲染不依赖 CDN

## 模板

- `templates/short-promo/`：产品宣传短片骨架（占位框标「示例」）
- `templates/kinetic-cards/`：金句/文字快闪

## 工作流

1. 收束卖点/金句与时长
2. 索取真实截图；没有则占位
3. 渲染对应模板 → 逐帧自检 → 导出
