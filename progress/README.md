# 进度快照与历史归档

归档日期：2026-11-13。当前状态以根目录 README、`docs/ROUND-1.md` 和 `review/round-1/evaluation.json` 为准；历史文件保持其当时语义，不把尚未执行的评测写成完成。

| 目录/文件 | 内容 |
|---|---|
| `review/evaluation.json` | r0 三组结果；当时人工反馈为空，后续反馈见 [两轮人工反馈](../docs/feedback/)。 |
| `review/control/` | 首轮不使用 skill 的实现、笔记与检查结果。 |
| `review/old/` | 首轮旧版 skill 的实现、冻结指令、布局和检查结果。 |
| `review/candidate/` | 首轮 v0.2 候选的实现、中断草稿、冻结指令和检查结果。 |
| `review/reference/` | 首轮参考布局、资源来源和稳定性比较。 |
| `review/round-1/` | 第二轮评审页、最终与修复前数值、用户反馈、版本冻结、行为检查和连续操作时间轨迹。 |
| `review/round-1/evaluation-before-human-review.json` | 收到第二轮人工评分前的评测记录，便于核对机器指标未被评分覆盖。 |
| `historical-scripts/` | 原 `work/` 顶层辅助脚本；`round-1/` 对应原 `work/round-1/`。这些是历史实验脚本，不会由测试或安装自动执行。 |
| `packages/` | 原样保留四份历史 ZIP；v0.3 ZIP 在 2026-11-06 生成，不包含 11 月 13 日的反馈归档和新计划。 |
| `delivery/` | 历史交付摘要及报告副本；不要将历史“未推送”视为当前 Git 状态。 |
| `local-artifacts.json` | 未上传媒体、原资源和原始浏览器诊断的大小、SHA256、相对位置与保留原因。 |

## 如何使用历史文件

- `review/` 保留原相对路径以便和本地完整评审目录对应；未上传图片、录像、商业素材及原始 `capture.json`，所以这里的 HTML 仅用于查看结构/历史内容，不能作为完整在线预览。
- `historical-scripts/` 中的路径以当时仓库根目录为工作目录，依赖当时的 `work/` 和相邻 `outputs/`。不要在当前项目直接批量执行。`write_*`、`prepare-*`、`build-review.py`、`finalize_review.py`、打包脚本可能覆盖当前实现、反馈或冻结文件。
- 历史源码诊断脚本只用于解释 Monopo 开发过程；禁止把它们或其源码提取结果送入下一阶段“不读源码”的新案例实验。
- 上传副本中的两处机器用户路径被替换为 `<LOCAL_WORKSPACE>` / `<LOCAL_USER>`；本地原件未改变。其余归档内容保持原样，冻结哈希描述的是原始文件。
- `accepted: pending` 表示用户尚未选择接受。当前用户评分为 100/99/99，不能据此擅自改成接受，也不能据此宣布 12 个案例通过。

每个文件的用途见 [完整索引](../docs/FILE-INDEX.md)。可独立使用的公共工具入口是 `toolkit/`，不是此处历史脚本。
