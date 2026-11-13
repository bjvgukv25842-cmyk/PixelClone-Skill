from pathlib import Path
readme='''# PixelClone Skill — 可验证的网页复刻

v0.2 候选版：支持图片、网站资源和视频参考；增加字体审计、浏览器采集、图像对比与冻结轮次评测。

**当前不是已达到像素级的正式发布。** 首轮 Monopo 实战发现旧版会依赖截图裁片，新版仍会近似重绘背景/透镜。三组结果都未通过完整还原要求；详见 [首轮评测](docs/EVALUATION.md)。

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

## 参考与素材

公开评测：[Design2Code](https://github.com/NoviScl/Design2Code)、[DesignBench](https://github.com/WebPAI/DesignBench)、[Animation Bench](https://www.physera.ai/research/animation)。内部适配结果不等于官方榜单成绩。

原站字体、图片和品牌素材属于各自权利人；本仓库分发的 skill 不包含 Monopo 的商业字体或素材。开发评审包仅供本次本地复刻核验。仓库未新增许可证授权条款。
'''
Path('README.md').write_text(readme,encoding='utf8')
