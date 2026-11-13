# 仓库逐文件用途索引

由 `python scripts/build-file-index.py` 生成。覆盖 Git 已跟踪及未忽略的待提交文件；不包含本地原素材、依赖和工作缓存。

当前进度见 [根 README](../README.md)，历史文件语义见 [归档 README](../progress/README.md)。

共 237 个文件。每个路径均可点击；同名文件按所属目录区分。

| 文件 | 用途 |
|---|---|
| [.github/workflows/test.yml](../.github/workflows/test.yml) | GitHub Actions 工具测试和双语分发一致性检查。 |
| [.gitignore](../.gitignore) | 排除本地依赖、工作目录、凭据与不分发的参考素材。 |
| [README.md](../README.md) | 使用入口、当前状态、安装运行及目录说明。 |
| [benchmarks/holdout.lock.json](../benchmarks/holdout.lock.json) | 12 个独立案例的来源、版本、哈希和未运行状态。 |
| [benchmarks/monopo.reference.json](../benchmarks/monopo.reference.json) | Monopo 参考页采集配置。 |
| [cases/monopo-r1/README.md](../cases/monopo-r1/README.md) | 第二轮案例范围、运行前提和历史限制；最新反馈见 docs/ROUND-1.md。 |
| [cases/monopo-r1/gradient.mjs](../cases/monopo-r1/gradient.mjs) | 案例 WebGL 背景装配；依赖本地原始 shader。 |
| [cases/monopo-r1/index.html](../cases/monopo-r1/index.html) | 该组/轮次网页实现；需原本地资源，不能视为完整离线网站。 |
| [cases/monopo-r1/render-contract.json](../cases/monopo-r1/render-contract.json) | 案例图层、字体、响应映射与验收证据合同。 |
| [cases/monopo-r1/scene.mjs](../cases/monopo-r1/scene.mjs) | 案例文字、遮罩、位移/色散、指针及触屏场景实现。 |
| [cases/monopo-r1/sources.json](../cases/monopo-r1/sources.json) | 原素材及 shader 的来源 URL、哈希与用途。 |
| [cases/monopo-r1/verify.mjs](../cases/monopo-r1/verify.mjs) | 案例 9 项行为/渲染因果检查；依赖本地案例资源。 |
| [docs/EVALUATION.md](../docs/EVALUATION.md) | 首轮实验设置、失败原因和解释边界。 |
| [docs/FILE-INDEX.md](../docs/FILE-INDEX.md) | 本逐文件用途索引。 |
| [docs/IMPLEMENTATION.md](../docs/IMPLEMENTATION.md) | 按日期保存的开发与交付进度。 |
| [docs/ROUND-1.md](../docs/ROUND-1.md) | 第二轮根因修复、评测边界和后续人工反馈。 |
| [docs/feedback/monopo-r0.json](../docs/feedback/monopo-r0.json) | 首轮用户原始反馈：70/60/40，不接受。 |
| [docs/feedback/monopo-r1.json](../docs/feedback/monopo-r1.json) | 第二轮用户导出反馈：100/99/99，接受选项 pending。 |
| [docs/plans/2026-11-13-cross-case-validation.md](../docs/plans/2026-11-13-cross-case-validation.md) | 已确认输入/预算/对照/验收条件的下一阶段计划；尚未执行。 |
| [examples/capture.json](../examples/capture.json) | 页面截图/交互/区域配置示例。 |
| [examples/compare.json](../examples/compare.json) | 图像容差和区域配置示例。 |
| [examples/evaluation.json](../examples/evaluation.json) | 需求状态和人工评价记录示例。 |
| [package-lock.json](../package-lock.json) | 锁定 Node 依赖版本及完整性。 |
| [package.json](../package.json) | Node 命令、版本与依赖声明。 |
| [progress/README.md](../progress/README.md) | 归档目录用途、历史语义、路径脱敏和本地资源依赖说明。 |
| [progress/delivery/DELIVERY.md](../progress/delivery/DELIVERY.md) | 当时的候选交付范围、结果与运行入口。 |
| [progress/delivery/evaluation-summary.md](../progress/delivery/evaluation-summary.md) | 首轮三组实验的历史摘要。 |
| [progress/delivery/round-1-notes.md](../progress/delivery/round-1-notes.md) | 第二轮开发与反馈说明副本。 |
| [progress/historical-scripts/bench_metadata.py](../progress/historical-scripts/bench_metadata.py) | 历史脚本：查询公开 benchmark 元数据。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/check_server.py](../progress/historical-scripts/check_server.py) | 历史脚本：检查本地预览服务。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/datasets.py](../progress/historical-scripts/datasets.py) | 历史脚本：探索数据集结构。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/design_files.py](../progress/historical-scripts/design_files.py) | 历史脚本：列出 DesignBench 样例路径。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/download_holdouts.py](../progress/historical-scripts/download_holdouts.py) | 历史脚本：下载锁定的独立静态参考图。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/encode_previews.py](../progress/historical-scripts/encode_previews.py) | 历史脚本：编码首轮对照预览视频。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/finalize_review.py](../progress/historical-scripts/finalize_review.py) | 历史脚本：整理首轮评审产物。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/frameworks.py](../progress/historical-scripts/frameworks.py) | 历史脚本：检查数据集框架分类。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/hard.py](../progress/historical-scripts/hard.py) | 历史脚本：查询 Design2Code-Hard 样例。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/investigate-r1.mjs](../progress/historical-scripts/investigate-r1.mjs) | 历史脚本：第二轮原站渲染诊断。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/lock_benchmarks.py](../progress/historical-scripts/lock_benchmarks.py) | 历史脚本：生成独立案例锁定清单。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/no_video.py](../progress/historical-scripts/no_video.py) | 历史脚本：处理无录像的历史采集配置。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/package_delivery.py](../progress/historical-scripts/package_delivery.py) | 历史脚本：生成首轮候选分发包。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/prepare_review.py](../progress/historical-scripts/prepare_review.py) | 历史脚本：准备首轮评审目录和展示。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/probe.mjs](../progress/historical-scripts/probe.mjs) | 历史脚本：采集首轮参考图、DOM 摘要和资源来源。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/record_local.mjs](../progress/historical-scripts/record_local.mjs) | 历史脚本：录制首轮本地实现。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/reference_motion.mjs](../progress/historical-scripts/reference_motion.mjs) | 历史脚本：录制参考页面交互。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/refresh_candidate.py](../progress/historical-scripts/refresh_candidate.py) | 历史脚本：刷新历史候选评审副本。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/review_checks.mjs](../progress/historical-scripts/review_checks.mjs) | 历史脚本：首轮页面功能与视觉证据检查。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/build-review.py](../progress/historical-scripts/round-1/build-review.py) | 历史脚本：重建当时第二轮报告、冻结记录和 ZIP，会覆盖后续人工评价。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/capture-pair.mjs](../progress/historical-scripts/round-1/capture-pair.mjs) | 历史脚本：采集第二轮参考/复刻的成对状态。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/check-contexts.mjs](../progress/historical-scripts/round-1/check-contexts.mjs) | 历史脚本：检查移动触屏及减少动态效果。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/debug-filter.mjs](../progress/historical-scripts/round-1/debug-filter.mjs) | 历史脚本：诊断 Pixi 滤镜编译与输出。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/encode-motion.py](../progress/historical-scripts/round-1/encode-motion.py) | 历史脚本：按录制时间戳编码连续视频。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/final-candidate-captures.mjs](../progress/historical-scripts/round-1/final-candidate-captures.mjs) | 历史脚本：采集第二轮最终候选状态。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/inspect-runtime.mjs](../progress/historical-scripts/round-1/inspect-runtime.mjs) | 历史脚本：读取原站运行时诊断；不用于 assets-only 评测。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/layout-inspect.mjs](../progress/historical-scripts/round-1/layout-inspect.mjs) | 历史脚本：检查案例文字布局与测量。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/prepare-case.mjs](../progress/historical-scripts/round-1/prepare-case.mjs) | 历史脚本：准备原素材和初版案例，会覆盖后续修复。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/recompare.mjs](../progress/historical-scripts/round-1/recompare.mjs) | 历史脚本：按修订后的固定区域重新比较第二轮截图。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/record-feedback.py](../progress/historical-scripts/round-1/record-feedback.py) | 历史脚本：归档首轮反馈截图，原机器路径已替换占位符。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/record-motion.mjs](../progress/historical-scripts/round-1/record-motion.mjs) | 历史脚本：CDP 连续录帧和实际时间记录。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/stability.mjs](../progress/historical-scripts/round-1/stability.mjs) | 历史脚本：重复采集参考并比较稳定性。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/test-review.mjs](../progress/historical-scripts/round-1/test-review.mjs) | 历史脚本：检查第二轮评审页和反馈流程。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/round-1/test-scene.mjs](../progress/historical-scripts/round-1/test-scene.mjs) | 历史脚本：第二轮场景行为检查的开发脚本。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/smoke_copy.py](../progress/historical-scripts/smoke_copy.py) | 历史脚本：准备独立安装烟雾检查目录。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/stability.mjs](../progress/historical-scripts/stability.mjs) | 历史脚本：重复采集参考并比较稳定性。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/test_viewer.mjs](../progress/historical-scripts/test_viewer.mjs) | 历史脚本：检查首轮评审页交互。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/write_readme.py](../progress/historical-scripts/write_readme.py) | 历史脚本：写入当时版本 README，会覆盖当前说明。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/historical-scripts/write_skills.py](../progress/historical-scripts/write_skills.py) | 历史脚本：写入当时双语 skill，会覆盖当前版本。 依赖原 work/outputs 环境，勿直接批量执行。 |
| [progress/local-artifacts.json](../progress/local-artifacts.json) | 本地未上传资源/媒体/原始诊断的相对路径、大小、哈希和原因。 |
| [progress/packages/PixelClone-Skill-v0.2-source.zip](../progress/packages/PixelClone-Skill-v0.2-source.zip) | 原样历史 ZIP：工具/技能/案例源码包，不含原站素材。 |
| [progress/packages/PixelClone-Skill-v0.3-source.zip](../progress/packages/PixelClone-Skill-v0.3-source.zip) | 原样历史 ZIP：工具/技能/案例源码包，不含原站素材。 |
| [progress/packages/pixelclone-skills-v0.2-candidate.zip](../progress/packages/pixelclone-skills-v0.2-candidate.zip) | 原样历史 ZIP：中英文独立 skill 安装包。 |
| [progress/packages/pixelclone-skills-v0.3-candidate.zip](../progress/packages/pixelclone-skills-v0.3-candidate.zip) | 原样历史 ZIP：中英文独立 skill 安装包。 |
| [progress/review/candidate/comparison/comparison.json](../progress/review/candidate/comparison/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/candidate/comparison/report.html](../progress/review/candidate/comparison/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/candidate/developer-qa.json](../progress/review/candidate/developer-qa.json) | 首轮各组开发阶段的功能与布局检查。 |
| [progress/review/candidate/evidence/asset-manifest.json](../progress/review/candidate/evidence/asset-manifest.json) | 首轮候选素材来源与使用记录。 |
| [progress/review/candidate/evidence/comparison.json](../progress/review/candidate/evidence/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/candidate/evidence/hashes.json](../progress/review/candidate/evidence/hashes.json) | 首轮候选输入/产物哈希；上传副本将机器绝对路径改为占位路径。 |
| [progress/review/candidate/evidence/validation.json](../progress/review/candidate/evidence/validation.json) | 首轮候选的开发自检结果。 |
| [progress/review/candidate/frozen-skill/SKILL.md](../progress/review/candidate/frozen-skill/SKILL.md) | 该版本/语言的技能入口与执行规范。 |
| [progress/review/candidate/frozen-skill/references/commands.md](../progress/review/candidate/frozen-skill/references/commands.md) | 安装、工具命令、配置与退出码参考。 |
| [progress/review/candidate/frozen-skill/references/evaluation.md](../progress/review/candidate/frozen-skill/references/evaluation.md) | 冻结轮次、误差门槛、完成率和成功率定义。 |
| [progress/review/candidate/frozen-skill/references/evidence.md](../progress/review/candidate/frozen-skill/references/evidence.md) | 素材来源、字体、输入模式和准备状态的证据规则。 |
| [progress/review/candidate/frozen-skill/references/motion.md](../progress/review/candidate/frozen-skill/references/motion.md) | 动效技术选择、状态控制、录像与减少动态效果规则。 |
| [progress/review/candidate/index.html](../progress/review/candidate/index.html) | 该组/轮次网页实现；需原本地资源，不能视为完整离线网站。 |
| [progress/review/candidate/interrupted-draft.html](../progress/review/candidate/interrupted-draft.html) | 该组/轮次网页实现的中断草稿；需原本地资源，不能视为完整离线网站。 |
| [progress/review/candidate/notes.json](../progress/review/candidate/notes.json) | 对应执行组的过程记录、限制和已知差异。 |
| [progress/review/candidate/recording/timeline.json](../progress/review/candidate/recording/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/control/comparison/comparison.json](../progress/review/control/comparison/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/control/comparison/report.html](../progress/review/control/comparison/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/control/developer-qa.json](../progress/review/control/developer-qa.json) | 首轮各组开发阶段的功能与布局检查。 |
| [progress/review/control/index.html](../progress/review/control/index.html) | 该组/轮次网页实现；需原本地资源，不能视为完整离线网站。 |
| [progress/review/control/notes.json](../progress/review/control/notes.json) | 对应执行组的过程记录、限制和已知差异。 |
| [progress/review/control/recording/timeline.json](../progress/review/control/recording/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/evaluation.json](../progress/review/evaluation.json) | 对应轮次/案例的评测数据；不要跨轮合并评分。 |
| [progress/review/holdout.lock.json](../progress/review/holdout.lock.json) | 12 个独立案例的来源、版本、哈希和未运行状态。 |
| [progress/review/index.html](../progress/review/index.html) | 历史评审页/入口；媒体与原资源保留本地，仓库副本不提供完整视觉预览。 |
| [progress/review/old/SKILL.frozen.md](../progress/review/old/SKILL.frozen.md) | 旧版执行时使用的冻结技能指令。 |
| [progress/review/old/comparison/comparison.json](../progress/review/old/comparison/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/old/comparison/report.html](../progress/review/old/comparison/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/old/developer-qa.json](../progress/review/old/developer-qa.json) | 首轮各组开发阶段的功能与布局检查。 |
| [progress/review/old/index.html](../progress/review/old/index.html) | 该组/轮次网页实现；需原本地资源，不能视为完整离线网站。 |
| [progress/review/old/layout.json](../progress/review/old/layout.json) | 旧版案例的参考布局蓝图。 |
| [progress/review/old/notes.json](../progress/review/old/notes.json) | 对应执行组的过程记录、限制和已知差异。 |
| [progress/review/old/qa.json](../progress/review/old/qa.json) | 历史实现的附加质量检查。 |
| [progress/review/old/recording/timeline.json](../progress/review/old/recording/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/reference/dom.json](../progress/review/reference/dom.json) | 首轮参考页面可观察的文字、字体和布局信息。 |
| [progress/review/reference/motion/timeline.json](../progress/review/reference/motion/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/reference/resources.json](../progress/review/reference/resources.json) | 首轮参考资源 URL/类型/状态清单，不含资源本体。 |
| [progress/review/reference/stability-1-2/comparison.json](../progress/review/reference/stability-1-2/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/reference/stability-1-3/comparison.json](../progress/review/reference/stability-1-3/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/reference/stability-2-3/comparison.json](../progress/review/reference/stability-2-3/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/reference/stability.json](../progress/review/reference/stability.json) | 参考重复采集的稳定性结果。 |
| [progress/review/round-0.html](../progress/review/round-0.html) | 历史评审页/入口；媒体与原资源保留本地，仓库副本不提供完整视觉预览。 |
| [progress/review/round-1/candidate/README.md](../progress/review/round-1/candidate/README.md) | 第二轮案例范围、运行前提和历史限制；最新反馈见 docs/ROUND-1.md。 |
| [progress/review/round-1/candidate/checks.json](../progress/review/round-1/candidate/checks.json) | 案例行为和渲染机制检查结果。 |
| [progress/review/round-1/candidate/gradient.mjs](../progress/review/round-1/candidate/gradient.mjs) | 案例 WebGL 背景装配；依赖本地原始 shader。 |
| [progress/review/round-1/candidate/index.html](../progress/review/round-1/candidate/index.html) | 该组/轮次网页实现；需原本地资源，不能视为完整离线网站。 |
| [progress/review/round-1/candidate/recording/timeline.json](../progress/review/round-1/candidate/recording/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/round-1/candidate/render-contract.json](../progress/review/round-1/candidate/render-contract.json) | 案例图层、字体、响应映射与验收证据合同。 |
| [progress/review/round-1/candidate/scene.mjs](../progress/review/round-1/candidate/scene.mjs) | 案例文字、遮罩、位移/色散、指针及触屏场景实现。 |
| [progress/review/round-1/candidate/sources.json](../progress/review/round-1/candidate/sources.json) | 原素材及 shader 的来源 URL、哈希与用途。 |
| [progress/review/round-1/candidate/timeline.json](../progress/review/round-1/candidate/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/round-1/candidate/verify.mjs](../progress/review/round-1/candidate/verify.mjs) | 案例 9 项行为/渲染因果检查；依赖本地案例资源。 |
| [progress/review/round-1/comparison-summary.json](../progress/review/round-1/comparison-summary.json) | 该轮多个状态的比较结果汇总。 |
| [progress/review/round-1/comparisons/center/comparison.json](../progress/review/round-1/comparisons/center/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/center/report.html](../progress/review/round-1/comparisons/center/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/exit/comparison.json](../progress/review/round-1/comparisons/exit/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/exit/report.html](../progress/review/round-1/comparisons/exit/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/initial/comparison.json](../progress/review/round-1/comparisons/initial/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/initial/report.html](../progress/review/round-1/comparisons/initial/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/left/comparison.json](../progress/review/round-1/comparisons/left/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/left/report.html](../progress/review/round-1/comparisons/left/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/mobile/comparison.json](../progress/review/round-1/comparisons/mobile/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/mobile/report.html](../progress/review/round-1/comparisons/mobile/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/quarter/comparison.json](../progress/review/round-1/comparisons/quarter/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/quarter/report.html](../progress/review/round-1/comparisons/quarter/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/reduced/comparison.json](../progress/review/round-1/comparisons/reduced/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/reduced/report.html](../progress/review/round-1/comparisons/reduced/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/reverse/comparison.json](../progress/review/round-1/comparisons/reverse/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/reverse/report.html](../progress/review/round-1/comparisons/reverse/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/right/comparison.json](../progress/review/round-1/comparisons/right/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/right/report.html](../progress/review/round-1/comparisons/right/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/comparisons/three-quarter/comparison.json](../progress/review/round-1/comparisons/three-quarter/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/comparisons/three-quarter/report.html](../progress/review/round-1/comparisons/three-quarter/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparison-summary.json](../progress/review/round-1/drafts/before-shader-fix/comparison-summary.json) | 该轮多个状态的比较结果汇总。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/center/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/center/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/center/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/center/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/exit/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/exit/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/exit/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/exit/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/initial/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/initial/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/initial/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/initial/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/left/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/left/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/left/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/left/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/quarter/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/quarter/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/quarter/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/quarter/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/reverse/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/reverse/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/reverse/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/reverse/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/right/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/right/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/right/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/right/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/three-quarter/comparison.json](../progress/review/round-1/drafts/before-shader-fix/comparisons/three-quarter/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/drafts/before-shader-fix/comparisons/three-quarter/report.html](../progress/review/round-1/drafts/before-shader-fix/comparisons/three-quarter/report.html) | 对应比较的历史 HTML 展示；图片未随仓库上传。 |
| [progress/review/round-1/evaluation-before-human-review.json](../progress/review/round-1/evaluation-before-human-review.json) | 第二轮收到人工反馈前的原始评测记录。 |
| [progress/review/round-1/evaluation.json](../progress/review/round-1/evaluation.json) | 对应轮次/案例的评测数据；不要跨轮合并评分。 |
| [progress/review/round-1/feedback-r0.json](../progress/review/round-1/feedback-r0.json) | 首轮反馈归档副本。 |
| [progress/review/round-1/feedback-r1.json](../progress/review/round-1/feedback-r1.json) | 第二轮反馈归档副本。 |
| [progress/review/round-1/freeze.json](../progress/review/round-1/freeze.json) | 该轮版本、输入权限和实现文件哈希。 |
| [progress/review/round-1/independent-skill-check.json](../progress/review/round-1/independent-skill-check.json) | 独立执行者应用渲染证据合同的检查，不是完整复刻评分。 |
| [progress/review/round-1/index.html](../progress/review/round-1/index.html) | 历史评审页/入口；媒体与原资源保留本地，仓库副本不提供完整视觉预览。 |
| [progress/review/round-1/reference/recording/timeline.json](../progress/review/round-1/reference/recording/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/round-1/reference/stability/pair-1-2/comparison.json](../progress/review/round-1/reference/stability/pair-1-2/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/reference/stability/pair-1-3/comparison.json](../progress/review/round-1/reference/stability/pair-1-3/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/reference/stability/pair-2-3/comparison.json](../progress/review/round-1/reference/stability/pair-2-3/comparison.json) | 对应状态的像素/区域差异和容差结果。 |
| [progress/review/round-1/reference/stability/stability.json](../progress/review/round-1/reference/stability/stability.json) | 参考重复采集的稳定性结果。 |
| [progress/review/round-1/reference/timeline.json](../progress/review/round-1/reference/timeline.json) | 连续操作或录制帧的时间轨迹。 |
| [progress/review/round-1/viewer-checks.json](../progress/review/round-1/viewer-checks.json) | 评审页控件、链接、媒体和反馈流程检查记录。 |
| [progress/review/source-hashes.json](../progress/review/source-hashes.json) | 首轮来源与实现文件的冻结哈希。 |
| [requirements.txt](../requirements.txt) | Python 图片、字体与视频辅助依赖。 |
| [scripts/build-file-index.py](../scripts/build-file-index.py) | 生成本逐文件用途索引；仓库新增文件后重新运行。 |
| [scripts/pack-skills.mjs](../scripts/pack-skills.mjs) | 同步两种语言的公共工具/依赖，或检查一致性。 |
| [skills/pixel-perfect-reference-ui-zh/SKILL.md](../skills/pixel-perfect-reference-ui-zh/SKILL.md) | 该版本/语言的技能入口与执行规范。 |
| [skills/pixel-perfect-reference-ui-zh/package-lock.json](../skills/pixel-perfect-reference-ui-zh/package-lock.json) | 独立安装分发副本：锁定 Node 依赖版本及完整性。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/package.json](../skills/pixel-perfect-reference-ui-zh/package.json) | 独立安装分发副本：Node 命令、版本与依赖声明。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/references/commands.md](../skills/pixel-perfect-reference-ui-zh/references/commands.md) | 独立安装分发副本：安装、工具命令、配置与退出码参考。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/references/evaluation.md](../skills/pixel-perfect-reference-ui-zh/references/evaluation.md) | 独立安装分发副本：冻结轮次、误差门槛、完成率和成功率定义。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/references/evidence.md](../skills/pixel-perfect-reference-ui-zh/references/evidence.md) | 独立安装分发副本：素材来源、字体、输入模式和准备状态的证据规则。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/references/motion.md](../skills/pixel-perfect-reference-ui-zh/references/motion.md) | 独立安装分发副本：动效技术选择、状态控制、录像与减少动态效果规则。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/references/render-effects.md](../skills/pixel-perfect-reference-ui-zh/references/render-effects.md) | 独立安装分发副本：字形失真、透镜、色散和渲染证据合同。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/requirements.txt](../skills/pixel-perfect-reference-ui-zh/requirements.txt) | 独立安装分发副本：Python 图片、字体与视频辅助依赖。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/extract_layout_blueprint.py](../skills/pixel-perfect-reference-ui-zh/scripts/extract_layout_blueprint.py) | 独立安装分发副本：参考图布局区域及蓝图提取。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/prepare_reference_asset.py](../skills/pixel-perfect-reference-ui-zh/scripts/prepare_reference_asset.py) | 独立安装分发副本：原图裁切、透明背景和输出尺寸处理。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/browser.mjs](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/browser.mjs) | 独立安装分发副本：浏览器截图、交互、真实字体、资源与错误采集。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/compare.mjs](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/compare.mjs) | 独立安装分发副本：像素/区域/布局比较及叠加、差异图输出。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/pixelclone.mjs](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/pixelclone.mjs) | 独立安装分发副本：collect/fonts/capture/compare/report 的统一命令入口。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/python/extract_layout_blueprint.py](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/python/extract_layout_blueprint.py) | 独立安装分发副本：参考图布局区域及蓝图提取。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/python/inspect_reference.py](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/python/inspect_reference.py) | 独立安装分发副本：图像、字体或视频参考检查与提帧支持。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/python/prepare_reference_asset.py](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/python/prepare_reference_asset.py) | 独立安装分发副本：原图裁切、透明背景和输出尺寸处理。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/render-audit.mjs](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/render-audit.mjs) | 独立安装分发副本：有界 Canvas/WebGL 绘制诊断；包含着色器源码采集，assets-only 评测不得启用。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui-zh/scripts/toolkit/report.mjs](../skills/pixel-perfect-reference-ui-zh/scripts/toolkit/report.mjs) | 独立安装分发副本：汇总需求完成率、运行状态并生成 HTML 报告。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/SKILL.md](../skills/pixel-perfect-reference-ui/SKILL.md) | 该版本/语言的技能入口与执行规范。 |
| [skills/pixel-perfect-reference-ui/agents/openai.yaml](../skills/pixel-perfect-reference-ui/agents/openai.yaml) | 英文 skill 的展示信息与默认调用提示。 |
| [skills/pixel-perfect-reference-ui/package-lock.json](../skills/pixel-perfect-reference-ui/package-lock.json) | 独立安装分发副本：锁定 Node 依赖版本及完整性。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/package.json](../skills/pixel-perfect-reference-ui/package.json) | 独立安装分发副本：Node 命令、版本与依赖声明。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/references/commands.md](../skills/pixel-perfect-reference-ui/references/commands.md) | 独立安装分发副本：安装、工具命令、配置与退出码参考。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/references/evaluation.md](../skills/pixel-perfect-reference-ui/references/evaluation.md) | 独立安装分发副本：冻结轮次、误差门槛、完成率和成功率定义。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/references/evidence.md](../skills/pixel-perfect-reference-ui/references/evidence.md) | 独立安装分发副本：素材来源、字体、输入模式和准备状态的证据规则。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/references/motion.md](../skills/pixel-perfect-reference-ui/references/motion.md) | 独立安装分发副本：动效技术选择、状态控制、录像与减少动态效果规则。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/references/render-effects.md](../skills/pixel-perfect-reference-ui/references/render-effects.md) | 独立安装分发副本：字形失真、透镜、色散和渲染证据合同。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/requirements.txt](../skills/pixel-perfect-reference-ui/requirements.txt) | 独立安装分发副本：Python 图片、字体与视频辅助依赖。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/extract_layout_blueprint.py](../skills/pixel-perfect-reference-ui/scripts/extract_layout_blueprint.py) | 独立安装分发副本：参考图布局区域及蓝图提取。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/prepare_reference_asset.py](../skills/pixel-perfect-reference-ui/scripts/prepare_reference_asset.py) | 独立安装分发副本：原图裁切、透明背景和输出尺寸处理。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/browser.mjs](../skills/pixel-perfect-reference-ui/scripts/toolkit/browser.mjs) | 独立安装分发副本：浏览器截图、交互、真实字体、资源与错误采集。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/compare.mjs](../skills/pixel-perfect-reference-ui/scripts/toolkit/compare.mjs) | 独立安装分发副本：像素/区域/布局比较及叠加、差异图输出。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/pixelclone.mjs](../skills/pixel-perfect-reference-ui/scripts/toolkit/pixelclone.mjs) | 独立安装分发副本：collect/fonts/capture/compare/report 的统一命令入口。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/python/extract_layout_blueprint.py](../skills/pixel-perfect-reference-ui/scripts/toolkit/python/extract_layout_blueprint.py) | 独立安装分发副本：参考图布局区域及蓝图提取。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/python/inspect_reference.py](../skills/pixel-perfect-reference-ui/scripts/toolkit/python/inspect_reference.py) | 独立安装分发副本：图像、字体或视频参考检查与提帧支持。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/python/prepare_reference_asset.py](../skills/pixel-perfect-reference-ui/scripts/toolkit/python/prepare_reference_asset.py) | 独立安装分发副本：原图裁切、透明背景和输出尺寸处理。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/render-audit.mjs](../skills/pixel-perfect-reference-ui/scripts/toolkit/render-audit.mjs) | 独立安装分发副本：有界 Canvas/WebGL 绘制诊断；包含着色器源码采集，assets-only 评测不得启用。 由 pack:skills 同步。 |
| [skills/pixel-perfect-reference-ui/scripts/toolkit/report.mjs](../skills/pixel-perfect-reference-ui/scripts/toolkit/report.mjs) | 独立安装分发副本：汇总需求完成率、运行状态并生成 HTML 报告。 由 pack:skills 同步。 |
| [tests/browser.test.mjs](../tests/browser.test.mjs) | 浏览器采集、错误、资源、超时及渲染诊断回归。 |
| [tests/cli.test.mjs](../tests/cli.test.mjs) | CLI 参数、退出行为与命令集成检查。 |
| [tests/compare.test.mjs](../tests/compare.test.mjs) | 图像/布局比较、需求与运行结果汇总检查。 |
| [tests/test_assets.py](../tests/test_assets.py) | 裁切越界、透明边缘及图像处理检查。 |
| [tests/test_media.py](../tests/test_media.py) | 字体和视频提帧检查。 |
| [toolkit/browser.mjs](../toolkit/browser.mjs) | 浏览器截图、交互、真实字体、资源与错误采集。 |
| [toolkit/compare.mjs](../toolkit/compare.mjs) | 像素/区域/布局比较及叠加、差异图输出。 |
| [toolkit/pixelclone.mjs](../toolkit/pixelclone.mjs) | collect/fonts/capture/compare/report 的统一命令入口。 |
| [toolkit/python/extract_layout_blueprint.py](../toolkit/python/extract_layout_blueprint.py) | 参考图布局区域及蓝图提取。 |
| [toolkit/python/inspect_reference.py](../toolkit/python/inspect_reference.py) | 图像、字体或视频参考检查与提帧支持。 |
| [toolkit/python/prepare_reference_asset.py](../toolkit/python/prepare_reference_asset.py) | 原图裁切、透明背景和输出尺寸处理。 |
| [toolkit/references/commands.md](../toolkit/references/commands.md) | 安装、工具命令、配置与退出码参考。 |
| [toolkit/references/evaluation.md](../toolkit/references/evaluation.md) | 冻结轮次、误差门槛、完成率和成功率定义。 |
| [toolkit/references/evidence.md](../toolkit/references/evidence.md) | 素材来源、字体、输入模式和准备状态的证据规则。 |
| [toolkit/references/motion.md](../toolkit/references/motion.md) | 动效技术选择、状态控制、录像与减少动态效果规则。 |
| [toolkit/references/render-effects.md](../toolkit/references/render-effects.md) | 字形失真、透镜、色散和渲染证据合同。 |
| [toolkit/render-audit.mjs](../toolkit/render-audit.mjs) | 有界 Canvas/WebGL 绘制诊断；包含着色器源码采集，assets-only 评测不得启用。 |
| [toolkit/report.mjs](../toolkit/report.mjs) | 汇总需求完成率、运行状态并生成 HTML 报告。 |
