# PixelClone Skill — 可验证的网页复刻

v0.3 候选版：支持图片、网站资源和视频参考；新增 Canvas/WebGL 渲染诊断、文字形变验收、控制台错误采集和触屏上下文。

**这是截至 2026-11-13 的完整进度快照，版本为 v0.3 候选版，尚未正式发布。** 首轮人工评分为视觉 70／完成度 60／动效 40，不接受；第二轮评分为 **100／99／99**，评论为“非常完美，已经接近完美像素级复刻了”，接受选项仍为“尚未决定”。第二轮桌面 8 个状态中 7 个达到全部所选区域容差，底部边界和移动端仍有失败项。人工评分不等于逐像素零差异。

第二轮按原站的文字栅格、位移与色散结构修复案例，并扩充 skill 的渲染证据流程。详见 [第二轮开发修复](docs/ROUND-1.md) 和 [首轮评测](docs/EVALUATION.md)。本轮增加源码诊断，不能直接与首轮比较并宣称 skill 泛化提升。**跨案例验证仅完成规划，12 个独立案例尚未正式运行。**

## 从哪里开始阅读

| 你要做什么 | 文件 |
|---|---|
| 使用中文或英文 skill | [中文版入口](skills/pixel-perfect-reference-ui-zh/SKILL.md)、[英文版入口](skills/pixel-perfect-reference-ui/SKILL.md) |
| 了解目前进度、已知问题 | [实施记录](docs/IMPLEMENTATION.md)、[第二轮报告](docs/ROUND-1.md) |
| 查看用户的两轮原始反馈 | [r0：70/60/40](docs/feedback/monopo-r0.json)、[r1：100/99/99](docs/feedback/monopo-r1.json) |
| 查看机器结果及历史产物 | [进度归档说明](progress/README.md)、[第二轮评测 JSON](progress/review/round-1/evaluation.json) |
| 接着开展新案例验证 | [跨案例验证计划](docs/plans/2026-11-13-cross-case-validation.md)、[已锁定案例](benchmarks/holdout.lock.json) |
| 查询任意一个仓库文件的用途 | [逐文件用途索引](docs/FILE-INDEX.md) |

## 目录与文件用途

| 路径 | 用途与维护规则 |
|---|---|
| `toolkit/pixelclone.mjs` | 工具统一入口：`collect`、`fonts`、`capture`、`compare`、`report`。 |
| `toolkit/browser.mjs` | Playwright 页面采集、实际字体检查、资源错误、交互及触屏环境。 |
| `toolkit/compare.mjs`、`report.mjs` | 像素与布局比较、差异图和 HTML 评测报告；机器指标与人工评分分开。 |
| `toolkit/render-audit.mjs` | 可选 Canvas/WebGL 诊断；会采集着色器源码，未来不读源码的验证必须关闭。 |
| `toolkit/python/` | Pillow 素材裁切、图片检查与布局蓝图脚本；是两种语言共用的源码。 |
| `toolkit/references/` | 命令、证据与字体、动效、渲染效果及冻结评测规范。 |
| `skills/` | 中英文可独立安装版本；公共脚本和参考文档由打包脚本同步，不能分别修改。 |
| `scripts/pack-skills.mjs` | 同步公共实现到两个安装目录，`--check` 检查一致性。 |
| `tests/` | Node 浏览器/CLI/比较测试及 Python 图片/视频测试。 |
| `examples/` | 页面采集、差异比较、评测记录的配置示例；运行前替换其中的 URL 和路径。 |
| `benchmarks/` | Monopo 参考配置、12 个独立案例的版本/来源/哈希锁定清单；清单不是通过证明。 |
| `cases/monopo-r1/` | 第二轮案例实现、9 项行为检查、渲染证据合同与资源来源；依赖未上传的原站素材。 |
| `docs/` | 进度、结果解释、用户反馈、后续计划及逐文件用途索引。 |
| `progress/review/` | 两轮评审页、三组首轮代码、数值结果、时间轨迹和冻结记录的历史快照；视觉媒体保留本地。 |
| `progress/historical-scripts/` | 当时采集、诊断、录屏、打包所用的辅助脚本；仅供追溯，不是当前支持的工具接口，部分会覆盖旧结果。 |
| `progress/packages/` | 当时交付的 v0.2/v0.3 中英文 skill 包及源码包；保留原 ZIP，不代表包含此次新增归档。 |
| `progress/delivery/` | 当时的交付说明和结果摘要，文中的“未推送”等状态描述对应历史日期。 |
| `progress/local-artifacts.json` | 本地保留的参考素材、截图、视频与原始诊断的相对路径、大小和哈希；不是下载链接。 |
| `.github/workflows/test.yml` | GitHub Actions：安装依赖，运行工具测试和双语打包一致性检查。 |
| `package.json`、`package-lock.json` | Node 工具命令与锁定依赖版本。 |
| `requirements.txt` | Python 图像、字体及 FFmpeg 辅助依赖。 |
| `.gitignore` | 排除依赖、虚拟环境、本地工作目录、凭据和原站素材。 |

逐文件的完整对应关系见 [FILE-INDEX.md](docs/FILE-INDEX.md)，包括历史脚本和同名分发副本。

## 快速开始

Node.js 20.11+、Python 3.10+。仓库根目录：

```text
npm ci
npx playwright install chromium
python -m venv .venv
```

用虚拟环境的 Python 安装 `requirements.txt`。Windows：

```powershell
.venv/Scripts/python -m pip install -r requirements.txt
$env:PIXELCLONE_PYTHON = (Resolve-Path .venv/Scripts/python.exe).Path
```

macOS/Linux：

```sh
.venv/bin/python -m pip install -r requirements.txt
export PIXELCLONE_PYTHON="$PWD/.venv/bin/python"
```

```text
node toolkit/pixelclone.mjs collect --type image --src reference.png --out evidence/reference
node toolkit/pixelclone.mjs capture --config examples/capture.json --out evidence/actual
node toolkit/pixelclone.mjs compare --reference reference.png --actual evidence/actual/screenshot.png --out evidence/diff
node toolkit/pixelclone.mjs report --out evidence/diff
```

`compare` 返回 2 表示超过图像容差，1 表示输入或运行错误，0 仅表示本命令成功；不是完整网页验收通过。配置格式见 [命令参考](toolkit/references/commands.md)。布局对比可同时传 `--reference-capture` 和 `--actual-capture`，检查命名区域、文字行数和 2 CSS px 锚点容差。

可明确选择系统 Edge：`PIXELCLONE_BROWSER_CHANNEL=msedge`。报告记录实际浏览器版本，不能将不同环境结果当作严格对照。视频提帧使用 FFmpeg，浏览器录屏另需 Playwright FFmpeg 组件；录屏完成超时会报错，不伪造视频。

## 安装 skill

中文：`skills/pixel-perfect-reference-ui-zh`；英文：`skills/pixel-perfect-reference-ui`。
复制需要的整个文件夹到个人 skills 目录，然后在该文件夹运行 `npm ci`、安装浏览器和 Python requirements。两个安装包各自独立，不依赖仓库的相对位置。调用 `$pixel-perfect-reference-ui-zh` 或 `$pixel-perfect-reference-ui`。

```text
请使用 $pixel-perfect-reference-ui-zh，依据给定截图/URL/视频复刻指定页面。
保留现有业务行为；记录缺失素材；对桌面、移动端和动态状态分别验收。
```

## 维护与测试

- `toolkit/` 是唯一工具源码；不要分别修改两个 skill 下的复制品。
- `npm run pack:skills` 同步公共脚本、参考文档和锁定依赖。
- `npm run check:skills` 检查分发文件是否漂移。
- `npm test` 运行浏览器、CLI、差异与报告测试。
- 虚拟环境 Python 运行 `-m unittest discover -s tests -p 'test_*.py'`。
- 原 `prepare_reference_asset.py` 和 `extract_layout_blueprint.py` 命令继续可用。

评测规则见 [冻结评测](toolkit/references/evaluation.md)。每轮冻结 skill；用户评分保持独立，不将像素误差包装成相似度百分比。正式验证用例见 `benchmarks/holdout.lock.json`，未运行的案例不算通过。

## 仓库快照与本地评审的区别

这次上传包含可维护源码、独立安装包、历史实现、评测数值、两轮用户反馈、后续计划和逐文件说明。`work/` 中的依赖/虚拟环境、原站应用代码、字体、纹理、着色器、截图和录像不作为公开分发素材上传；保留的文件清单见 [本地素材索引](progress/local-artifacts.json)。Git 克隆不会恢复这部分文件。

因此 `cases/monopo-r1/` 和 `progress/review/` **不是下载后即可离线运行的完整 Monopo 网站**。复刻源码和评审页都保留了原来的资源引用，缺少本地素材时会缺图或无法启动效果。工具测试使用自己的临时样例，不依赖这些原站资源。现有工作机上的完整评审仍位于仓库相邻的 `outputs/pixelclone-review/`；本机启动方式：

```text
python -m http.server 8765 --bind 127.0.0.1 --directory ../outputs/pixelclone-review
```

然后打开 `http://127.0.0.1:8765/round-1/index.html`。该地址只对运行服务的电脑有效，GitHub 分支不是已部署网站。

## 参考与素材来源

公开评测：[Design2Code](https://github.com/NoviScl/Design2Code)、[DesignBench](https://github.com/WebPAI/DesignBench)、[Animation Bench](https://www.physera.ai/research/animation)。内部适配结果不等于官方榜单成绩。

原站字体、图片和品牌素材属于各自权利人；本仓库分发的 skill 不包含 Monopo 的商业字体或素材。开发评审包仅供本次本地复刻核验。仓库未新增许可证授权条款。
