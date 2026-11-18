# ai-video-skills

中文办公视频 skill：知识科普（代码生成）与口播粗剪（半自动）。底层渲染默认 **HyperFrames**（[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)，以[官方文档](https://hyperframes.heygen.com/introduction)为准）。许可证 **Apache-2.0**。

**目前仅支持 Mac。** 云端可用于开发自检；凡标注「待 Mac 实测」的条目，不以 Linux 结果冒充已验收。部分项已在 iMac 实测，见下方「Mac 实测状态」。

作者：华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者

---

English office-video skills: code-generated knowledge explainers and semi-automated talking-head edits. Default renderer: **HyperFrames** ([heygen-com/hyperframes](https://github.com/heygen-com/hyperframes); follow the [official docs](https://hyperframes.heygen.com/introduction)). License: **Apache-2.0**.

**Mac only for v1.** Cloud Linux may be used for smoke tests; items marked「待 Mac 实测」are not claimed as accepted. Some items are already verified on an iMac — see「Mac 实测状态」below.

Author: 华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者

---

## 学习路径 / Learning path

```
知道看什么 → 会提问 → 装上工具 → 做出作品 → 【用进工作】→ 做自己的 skill
                                              ▲
                                   本仓库（视频）挂在这里
```

PPT / 数据分析 / 设计等同挂在「用进工作」下的其他仓库。

```
Know what to read → Ask better → Install tools → Ship a first build → 【Use it at work】→ Make your own skill
                                                                    ▲
                                                         This repo (video) sits here
```

PPT / data / design skills hang under the same「Use it at work」slot in other repos.

---

## 核心思路 / Core idea

按「画面素材是画出来的还是拍出来的」分两条路线（及混合）：

| 路线 / Route | 说明 / Meaning | 自动化 / Automation |
| --- | --- | --- |
| 代码生成 | 图形、文字、数据、界面用代码画出来 | 全自动 / Fully automatic |
| 古法剪辑 | 真人、实物、现场用用户素材；AI 粗剪 + 剪映精修 | 半自动 / Semi-automatic |
| 混合 | 古法剪主线，代码生成的包装件和 B-roll 叠上去 | 半自动 / Semi-automatic |

---

## 完整仓库结构 / Full repository layout

```
ai-video-skills/
├── video-router/           ✅ 本版：最简入口（只分科普 / 口播）
├── code-video/
│   ├── explainer/          ✅ 本版：知识科普 / 课件转视频
│   ├── data-story/         🔜 规划中
│   ├── promo/              🔜 规划中（下周再定是否复用 video-shotcraft）
│   └── animation/          🔜 规划中
├── edit-video/
│   ├── talking-head/       ✅ 本版：AI / 科技 / 工具类口播
│   ├── clip-long/          🔜 规划中
│   └── footage/            🔜 规划中
├── shared/
│   ├── subtitle-tts/       ✅ 本版：字幕 SRT；配音接口预留
│   ├── overlays/           ✅ 本版最小：概念 / 步骤 / 数据 / 截图卡
│   └── styles/             ✅ 本版：SCHEMA + 2 张风格卡
├── examples/
├── tests/
└── scripts/doctor.sh
```

Legend: ✅ supported in this release / 🔜 planned.

---

## 10 种视频怎么分 / Ten video types

来源：框架稿第 1 节。状态按本版如实标注。

| 视频类型 | 路线 | 交给谁 | 自动化程度 | 状态 |
| --- | --- | --- | --- | --- |
| 知识科普 / 动态图解 | 代码生成 | `code-video/explainer` | 全自动 | ✅ |
| 数据动画 | 代码生成 | `code-video/data-story` | 全自动 | 🔜 |
| 产品宣传片 | 代码生成 | `code-video/promo` | 全自动（产品界面只用真实截图或录屏） | 🔜 |
| 文字快闪 / 金句卡 | 代码生成 | `code-video/promo` | 全自动 | 🔜 |
| 动画短片 / MV | 代码生成 | `code-video/animation` | 全自动 | 🔜 |
| PPT / 课件转视频 | 代码生成 | `code-video/explainer` | 全自动 | ✅ |
| 口播 / 真人出镜 | 古法剪辑 | `edit-video/talking-head` | 半自动：AI 粗剪 + 剪映精修 | ✅（本版仅 AI/科技/工具类） |
| 实拍（Vlog、探店、开箱、带货） | 古法剪辑 | `edit-video/footage` | 半自动 | 🔜 |
| 长视频切片 | 古法剪辑 | `edit-video/clip-long` | 半自动 | 🔜 |
| 软件教程录屏 | 混合 | talking-head 主线 + overlays | 半自动 | 🔜 |

| Video type | Route | Skill | Automation | Status |
| --- | --- | --- | --- | --- |
| Knowledge explainer / animated diagram | Code generation | `code-video/explainer` | Fully automatic | ✅ |
| Data motion | Code generation | `code-video/data-story` | Fully automatic | 🔜 |
| Product promo | Code generation | `code-video/promo` | Fully automatic (real UI screenshots only) | 🔜 |
| Kinetic text / quote cards | Code generation | `code-video/promo` | Fully automatic | 🔜 |
| Short animation / MV | Code generation | `code-video/animation` | Fully automatic | 🔜 |
| PPT / lesson → video | Code generation | `code-video/explainer` | Fully automatic | ✅ |
| Talking-head | Classic editing | `edit-video/talking-head` | Semi-auto: AI rough cut + CapCut polish | ✅ (AI/tech/tools only in this release) |
| Live footage (vlog, shop, unbox, commerce) | Classic editing | `edit-video/footage` | Semi-automatic | 🔜 |
| Long-form clips | Classic editing | `edit-video/clip-long` | Semi-automatic | 🔜 |
| Software tutorial screencast | Hybrid | talking-head + overlays | Semi-automatic | 🔜 |

最简 `video-router`：只判断科普 vs 口播；上表中 🔜 类型回复「暂不支持」。

Minimal `video-router`: routes only explainer vs talking-head; replies「暂不支持」for 🔜 types.

---

## 口播按 B-roll 来源分 6 种 / Six talking-head subtypes by B-roll source

| 口播类型 | B-roll 从哪来 | 自动化程度 | 状态 |
| --- | --- | --- | --- |
| AI / 科技 / 工具类 | B-roll 大多用代码生成 | 基本全自动 | ✅ |
| 知识讲解 | B-roll 用代码生成 | 全自动 | 🔜 |
| 新闻资讯 | 代码生成 + 新闻截图标来源 | 全自动 | 🔜 |
| 观点 / 职场 / 情感 | 重点在字幕节奏和金句卡 | 粗剪 + 用户精修 | 🔜 |
| 测评 / 带货 | 用户实拍 + 代码做价格卡和对比表 | 半自动 | 🔜 |
| 访谈 / 对谈 | 多机位切换 | 古法为主 | 🔜 |

| Talking-head subtype | B-roll source | Automation | Status |
| --- | --- | --- | --- |
| AI / tech / tools | Mostly code-generated | Mostly automatic | ✅ |
| Knowledge lecture | Code-generated | Fully automatic | 🔜 |
| News | Code + sourced news screenshots | Fully automatic | 🔜 |
| Opinion / workplace / emotion | Caption rhythm + quote cards | Rough cut + user polish | 🔜 |
| Review / commerce | User footage + price/compare cards | Semi-automatic | 🔜 |
| Interview / dialogue | Multi-cam switching | Mostly manual | 🔜 |

---

## 本版已交付 skill / Skills in this release

| Skill | 路径 / Path | 做什么 / What it does |
| --- | --- | --- |
| **explainer**（优先） | `code-video/explainer/` | vibe 知识科普：分镜 → 风格卡 → HyperFrames → 字幕 → 逐帧自检 |
| **talking-head** | `edit-video/talking-head/` | AI/科技口播：转写 → 去口癖 → B-roll 标记 → overlays → 导出 + 剪映清单 |
| **video-router** | `video-router/` | 最简入口：只分科普 / 口播；其他「暂不支持」 |

Shared：`shared/overlays/`、`shared/styles/`（SCHEMA + 2 张卡）、`shared/subtitle-tts/`（字幕可用；配音接口预留）。

**本版不做 / Out of scope this week：** `promo`（下周再定）、`data-story`、数字人方案、Windows。

---

## 安装（Mac）/ Install (Mac)

环境检查（含 **ffmpeg**）/ Environment check (includes **ffmpeg**):

```bash
./scripts/doctor.sh
```

`doctor.sh` 已在 iMac 实测通过（`pass=7 fail=0 warn=0`）。详见 [`tests/mac/2026-11-18-imac.md`](tests/mac/2026-11-18-imac.md)。

### 适配的 agent / Supported agents (v1)

| 工具 / Tool | 项目级 skill 路径 / Project skill path |
| --- | --- |
| Claude Code | `.claude/skills/<name>/` |
| Codex | `.agents/skills/<name>/` |
| WorkBuddy | `.codebuddy/skills/<name>/`（用户级精确路径待 Mac 实测） |
| DeepSeek Harness | `.dsh/skills/<name>/` 或 `.agents/skills/<name>/` |

Node 版本（分工具报告，不要合成一条）：

- HyperFrames / 常见 Claude Code npm 路径：Node.js **22+**
- DeepSeek Harness：Node.js **>=24.9.0**（以 npm 包 `@deepseek-ai/dsh` 的 `engines` 为准；2026-11-18 查询版本 `0.2.2-rc.1`）

视频 skill 依赖本地脚本与渲染，不能只靠粘贴 `SKILL.md`。各工具触发实测：**待 Mac 实测**（本机未装 Claude Code / Codex / WorkBuddy / DeepSeek Harness）。

Video skills need local scripts/rendering—not paste-only `SKILL.md`. Per-agent trigger tests: **待 Mac 实测** (those tools were not installed on the test Mac).

---

## Mac 实测状态 / Mac verification status

记录：[`tests/mac/2026-11-18-imac.md`](tests/mac/2026-11-18-imac.md)（iMac · Apple M4 · 16GB · macOS 27.0.1 · head `e1398bb`）

| 项 / Item | 状态 / Status |
| --- | --- |
| `scripts/doctor.sh` | ✅ 已实测 — [记录](tests/mac/2026-11-18-imac.md) |
| `short-explainer` 渲染（9s） | ✅ 已实测 — [记录](tests/mac/2026-11-18-imac.md) |
| 截帧 1.5s / 4.5s / 7.5s 自查 | ✅ 已实测 — [记录](tests/mac/2026-11-18-imac.md) |
| 四工具触发 | 待 Mac 实测 |
| Qwen3-TTS vs CosyVoice | 待 Mac 实测 |
| 转写引擎与去口癖 | 待 Mac 实测 |
| talking-head 叠层导出 | 待 Mac 实测 |
| 剪映精修步骤与版本 | 待 Mac 实测 |
| 完整 30s explainer | 待 Mac 实测（仓库暂无 30s 模板） |
| 前后对比 | 待 Mac 实测 |
| WorkBuddy 用户级精确路径 | 待 Mac 实测 |

观察（不改代码）：竖屏里正文/卡片偏小、内容偏窄，建议 30s 完整版再放大。见实测记录。

---

## HyperFrames

- 要求 / Requires：Node.js 22+、系统 ffmpeg
- GSAP、字体均本地安装/打包，渲染不依赖外网 CDN
- 字体集中在 `shared/fonts/`（OFL）；短模板通过相对路径引用，不在模板内重复拷贝
- 渲染结束后，终端可能显示 HyperFrames 桌面 App 的推广文字——**只在终端，不进视频**
- 短示例模板 / Short template：`code-video/explainer/templates/short-explainer/`（**已在 iMac 实测**：HyperFrames 0.9.66，9.0s / 1080×1920，见 [记录](tests/mac/2026-11-18-imac.md)）

```bash
cd code-video/explainer/templates/short-explainer
npm install
npm run render
# writes ./renders/short-explainer.mp4 (gitignored)
```

---

## 配音 / Voiceover

第一版默认 **只出字幕、不配音**。预置音色 / 自有声音克隆接口见 `shared/subtitle-tts/`；**等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入**（仍为待 Mac 实测）。

v1 default: **captions only, no TTS**. Preset / self-clone hooks live in `shared/subtitle-tts/`; **wire after Qwen3-TTS vs CosyVoice Mac bake-off** (still pending).

---

## 红线（摘要）/ Guardrails (summary)

- 不生成真人画面；不模仿他人声音；不用数字人 / No synthetic humans, no cloning others' voices, no digital avatars
- 产品界面只用真实截图或录屏 / Product UI only from real screenshots or recordings
- 公开示例只用授权清楚的素材并注明出处；没有就不放 / Public samples only with clear licenses + attribution; otherwise omit
- 不编造数字和出处；查不到写「待核实」 / No invented numbers or sources; write「待核实」when unknown
- 剪映步骤未实测不写死路径（标「待 Mac 实测」） / CapCut steps stay unmarked until Mac-verified

---

## 公开示例与素材 / Public samples

当前仓库**不附带**第三方口播样片。若后续增加公开示例，仅使用 CC BY 等授权清楚、允许修改的素材，并在本 README 注明出处与协议。

No third-party talking-head clips are bundled. Future public samples must use clearly licensed, modification-allowed media (e.g. CC BY) with attribution here.

---

## 开发与 CI / Development & CI

```bash
python3 -m pip install pyyaml
python3 scripts/ci_validate.py
```

CI：校验各 `SKILL.md` frontmatter、`agents/openai.yaml`、examples「虚构示例」、触发测试 10+10、禁用词（对 `.codebuddy/` 路径白名单）、macOS 上跑 `doctor.sh`。

CI validates frontmatter, `agents/openai.yaml`, the「虚构示例」mark, 10+10 triggers, banned-token scan (`.codebuddy/` path whitelisted), and `doctor.sh` on macOS.

---

## 许可证 / License

Apache License 2.0。见 `LICENSE` 与 `NOTICE`。

See `LICENSE` and `NOTICE`.
