# ai-video-skills

中文办公视频 skill：知识科普（代码生成）与口播粗剪（半自动）。底层渲染默认 **HyperFrames**（[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)，以[官方文档](https://hyperframes.heygen.com/introduction)为准）。许可证 **Apache-2.0**。

**目前仅支持 Mac。** 云端可用于开发自检；凡标注「待 Mac 实测」的条目，不以 Linux 结果冒充已验收。

作者：华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者

---

## 学习路径

```
知道看什么 → 会提问 → 装上工具 → 做出作品 → 【用进工作】→ 做自己的 skill
                                              ▲
                                   本仓库（视频）挂在这里
```

PPT / 数据分析 / 设计等同挂在「用进工作」下的其他仓库。

---

## Learning path (EN)

Know what to read → Ask better → Install tools → Ship a first build → **Use it at work** (this repo) → Make your own skill.

---

## 本周范围（第一版）

| Skill | 路径 | 做什么 |
| --- | --- | --- |
| **explainer**（优先） | `code-video/explainer/` | vibe 知识科普：分镜 → 风格卡 → HyperFrames 渲染 → 字幕 → 逐帧自检 |
| **talking-head** | `edit-video/talking-head/` | AI/科技口播：转写 → 去口癖 → B-roll 标记 → overlays → 导出 + 剪映清单 |
| **video-router** | `video-router/` | 最简入口：只分科普 / 口播；其他类型回复「暂不支持」 |

Shared：`shared/overlays/`、`shared/styles/`（SCHEMA + 2 张卡）、`shared/subtitle-tts/`（字幕可用；配音接口预留）。

**不做本周：** `promo`（下周再定）、`data-story`、数字人方案、Windows。

---

## 视频类型路由表

| 类型 | 状态 |
| --- | --- |
| 知识科普 / 动态图解 / 课件转视频 | → explainer |
| AI/科技/工具类口播 | → talking-head |
| 数据动画、宣传片、Vlog、长视频切片等 | 暂不支持 |

---

## 安装（Mac）

环境检查（含 **ffmpeg**）：

```bash
./scripts/doctor.sh
```

### 适配的 agent（第一版）

| 工具 | 项目级 skill 路径 |
| --- | --- |
| Claude Code | `.claude/skills/<name>/` |
| Codex | `.agents/skills/<name>/` |
| WorkBuddy | `.codebuddy/skills/<name>/`（用户级精确路径待 Mac 实测） |
| DeepSeek Harness | `.dsh/skills/<name>/` 或 `.agents/skills/<name>/` |

视频 skill 依赖本地脚本与渲染，不能只靠粘贴 `SKILL.md`。各工具触发实测：**待 Mac 实测**。

---

## HyperFrames 说明

- 要求：Node.js 22+、系统 ffmpeg
- GSAP、字体均本地安装/打包，渲染不依赖外网 CDN
- 渲染结束后，终端可能显示 HyperFrames 桌面 App 的推广文字——**只在终端，不进视频**
- 短示例模板：`code-video/explainer/templates/short-explainer/`

```bash
cd code-video/explainer/templates/short-explainer
npm install
npx hyperframes render --output /tmp/short-explainer.mp4
```

---

## 配音

第一版默认 **只出字幕、不配音**。预置音色 / 自有声音克隆接口见 `shared/subtitle-tts/`；**等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入**。

---

## 红线（摘要）

- 不生成真人画面；不模仿他人声音；不用数字人
- 产品界面只用真实截图或录屏
- 公开示例只用授权清楚的素材并注明出处；没有就不放
- 不编造数字和出处；查不到写「待核实」
- 剪映步骤未实测不写死路径（标「待 Mac 实测」）

---

## 公开示例与素材

当前仓库**不附带**第三方口播样片。若后续增加公开示例，仅使用 CC BY 等授权清楚、允许修改的素材，并在本 README 注明出处与协议。

---

## 开发与 CI

```bash
python3 -m pip install pyyaml
python3 scripts/ci_validate.py
```

CI：校验各 `SKILL.md` frontmatter、`agents/openai.yaml`、examples「虚构示例」、触发测试 10+10、禁用词（对 `.codebuddy/` 路径白名单）、macOS 上跑 `doctor.sh`。

---

## 许可证

Apache License 2.0。见 `LICENSE` 与 `NOTICE`。
