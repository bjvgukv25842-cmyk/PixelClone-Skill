"""Generate the repository's tracked/non-ignored file-purpose index (no dependencies)."""
from pathlib import Path
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'docs/FILE-INDEX.md'

PURPOSES = {
    'README.md': '使用入口、当前状态、安装运行及目录说明。',
    '.gitignore': '排除本地依赖、工作目录、凭据与不分发的参考素材。',
    'package.json': 'Node 命令、版本与依赖声明。',
    'package-lock.json': '锁定 Node 依赖版本及完整性。',
    'requirements.txt': 'Python 图片、字体与视频辅助依赖。',
    'SKILL.md': '该版本/语言的技能入口与执行规范。',
    'SKILL.frozen.md': '旧版执行时使用的冻结技能指令。',
    'openai.yaml': '英文 skill 的展示信息与默认调用提示。',
    'pixelclone.mjs': 'collect/fonts/capture/compare/report 的统一命令入口。',
    'browser.mjs': '浏览器截图、交互、真实字体、资源与错误采集。',
    'compare.mjs': '像素/区域/布局比较及叠加、差异图输出。',
    'report.mjs': '汇总需求完成率、运行状态并生成 HTML 报告。',
    'render-audit.mjs': '有界 Canvas/WebGL 绘制诊断；包含着色器源码采集，assets-only 评测不得启用。',
    'prepare_reference_asset.py': '原图裁切、透明背景和输出尺寸处理。',
    'extract_layout_blueprint.py': '参考图布局区域及蓝图提取。',
    'inspect_reference.py': '图像、字体或视频参考检查与提帧支持。',
    'commands.md': '安装、工具命令、配置与退出码参考。',
    'evaluation.md': '冻结轮次、误差门槛、完成率和成功率定义。',
    'evidence.md': '素材来源、字体、输入模式和准备状态的证据规则。',
    'motion.md': '动效技术选择、状态控制、录像与减少动态效果规则。',
    'render-effects.md': '字形失真、透镜、色散和渲染证据合同。',
    'pack-skills.mjs': '同步两种语言的公共工具/依赖，或检查一致性。',
    'build-file-index.py': '生成本逐文件用途索引；仓库新增文件后重新运行。',
    'browser.test.mjs': '浏览器采集、错误、资源、超时及渲染诊断回归。',
    'cli.test.mjs': 'CLI 参数、退出行为与命令集成检查。',
    'compare.test.mjs': '图像/布局比较、需求与运行结果汇总检查。',
    'test_assets.py': '裁切越界、透明边缘及图像处理检查。',
    'test_media.py': '字体和视频提帧检查。',
    'holdout.lock.json': '12 个独立案例的来源、版本、哈希和未运行状态。',
    'monopo.reference.json': 'Monopo 参考页采集配置。',
    'EVALUATION.md': '首轮实验设置、失败原因和解释边界。',
    'IMPLEMENTATION.md': '按日期保存的开发与交付进度。',
    'ROUND-1.md': '第二轮根因修复、评测边界和后续人工反馈。',
    'DELIVERY.md': '当时的候选交付范围、结果与运行入口。',
    'evaluation-summary.md': '首轮三组实验的历史摘要。',
    'round-1-notes.md': '第二轮开发与反馈说明副本。',
    'monopo-r0.json': '首轮用户原始反馈：70/60/40，不接受。',
    'monopo-r1.json': '第二轮用户导出反馈：100/99/99，接受选项 pending。',
    'feedback-r0.json': '首轮反馈归档副本。',
    'feedback-r1.json': '第二轮反馈归档副本。',
    'gradient.mjs': '案例 WebGL 背景装配；依赖本地原始 shader。',
    'scene.mjs': '案例文字、遮罩、位移/色散、指针及触屏场景实现。',
    'verify.mjs': '案例 9 项行为/渲染因果检查；依赖本地案例资源。',
    'render-contract.json': '案例图层、字体、响应映射与验收证据合同。',
    'sources.json': '原素材及 shader 的来源 URL、哈希与用途。',
    'local-artifacts.json': '本地未上传资源/媒体/原始诊断的相对路径、大小、哈希和原因。',
    'comparison.json': '对应状态的像素/区域差异和容差结果。',
    'comparison-summary.json': '该轮多个状态的比较结果汇总。',
    'report.html': '对应比较的历史 HTML 展示；图片未随仓库上传。',
    'evaluation.json': '对应轮次/案例的评测数据；不要跨轮合并评分。',
    'evaluation-before-human-review.json': '第二轮收到人工反馈前的原始评测记录。',
    'freeze.json': '该轮版本、输入权限和实现文件哈希。',
    'source-hashes.json': '首轮来源与实现文件的冻结哈希。',
    'checks.json': '案例行为和渲染机制检查结果。',
    'developer-qa.json': '首轮各组开发阶段的功能与布局检查。',
    'qa.json': '历史实现的附加质量检查。',
    'notes.json': '对应执行组的过程记录、限制和已知差异。',
    'layout.json': '旧版案例的参考布局蓝图。',
    'dom.json': '首轮参考页面可观察的文字、字体和布局信息。',
    'resources.json': '首轮参考资源 URL/类型/状态清单，不含资源本体。',
    'stability.json': '参考重复采集的稳定性结果。',
    'timeline.json': '连续操作或录制帧的时间轨迹。',
    'independent-skill-check.json': '独立执行者应用渲染证据合同的检查，不是完整复刻评分。',
    'viewer-checks.json': '评审页控件、链接、媒体和反馈流程检查记录。',
    'asset-manifest.json': '首轮候选素材来源与使用记录。',
    'hashes.json': '首轮候选输入/产物哈希；上传副本将机器绝对路径改为占位路径。',
    'validation.json': '首轮候选的开发自检结果。',
}

HISTORY = {
    'bench_metadata.py': '查询公开 benchmark 元数据。', 'check_server.py': '检查本地预览服务。',
    'datasets.py': '探索数据集结构。', 'design_files.py': '列出 DesignBench 样例路径。',
    'download_holdouts.py': '下载锁定的独立静态参考图。', 'encode_previews.py': '编码首轮对照预览视频。',
    'finalize_review.py': '整理首轮评审产物。', 'frameworks.py': '检查数据集框架分类。',
    'hard.py': '查询 Design2Code-Hard 样例。', 'investigate-r1.mjs': '第二轮原站渲染诊断。',
    'lock_benchmarks.py': '生成独立案例锁定清单。', 'no_video.py': '处理无录像的历史采集配置。',
    'package_delivery.py': '生成首轮候选分发包。', 'prepare_review.py': '准备首轮评审目录和展示。',
    'probe.mjs': '采集首轮参考图、DOM 摘要和资源来源。', 'record_local.mjs': '录制首轮本地实现。',
    'reference_motion.mjs': '录制参考页面交互。', 'refresh_candidate.py': '刷新历史候选评审副本。',
    'review_checks.mjs': '首轮页面功能与视觉证据检查。', 'smoke_copy.py': '准备独立安装烟雾检查目录。',
    'stability.mjs': '重复采集参考并比较稳定性。', 'test_viewer.mjs': '检查首轮评审页交互。',
    'write_readme.py': '写入当时版本 README，会覆盖当前说明。', 'write_skills.py': '写入当时双语 skill，会覆盖当前版本。',
    'build-review.py': '重建当时第二轮报告、冻结记录和 ZIP，会覆盖后续人工评价。',
    'capture-pair.mjs': '采集第二轮参考/复刻的成对状态。', 'check-contexts.mjs': '检查移动触屏及减少动态效果。',
    'debug-filter.mjs': '诊断 Pixi 滤镜编译与输出。', 'encode-motion.py': '按录制时间戳编码连续视频。',
    'final-candidate-captures.mjs': '采集第二轮最终候选状态。', 'inspect-runtime.mjs': '读取原站运行时诊断；不用于 assets-only 评测。',
    'layout-inspect.mjs': '检查案例文字布局与测量。', 'prepare-case.mjs': '准备原素材和初版案例，会覆盖后续修复。',
    'recompare.mjs': '按修订后的固定区域重新比较第二轮截图。', 'record-feedback.py': '归档首轮反馈截图，原机器路径已替换占位符。',
    'record-motion.mjs': 'CDP 连续录帧和实际时间记录。', 'test-review.mjs': '检查第二轮评审页和反馈流程。',
    'test-scene.mjs': '第二轮场景行为检查的开发脚本。',
}


def purpose(name):
    p = Path(name)
    if name == 'docs/FILE-INDEX.md':
        return '本逐文件用途索引。'
    if name.startswith('docs/plans/'):
        return '已确认输入/预算/对照/验收条件的下一阶段计划；尚未执行。'
    if name.startswith('.github/'):
        return 'GitHub Actions 工具测试和双语分发一致性检查。'
    if name.startswith('progress/historical-scripts/'):
        return '历史脚本：' + HISTORY[p.name] + ' 依赖原 work/outputs 环境，勿直接批量执行。'
    if name.startswith('progress/packages/'):
        return '原样历史 ZIP：' + ('中英文独立 skill 安装包。' if p.name.startswith('pixelclone-skills') else '工具/技能/案例源码包，不含原站素材。')
    if name == 'progress/README.md':
        return '归档目录用途、历史语义、路径脱敏和本地资源依赖说明。'
    if name == 'cases/monopo-r1/README.md' or name.endswith('round-1/candidate/README.md'):
        return '第二轮案例范围、运行前提和历史限制；最新反馈见 docs/ROUND-1.md。'
    if name.startswith('examples/'):
        return {'capture.json':'页面截图/交互/区域配置示例。','compare.json':'图像容差和区域配置示例。','evaluation.json':'需求状态和人工评价记录示例。'}[p.name]
    if p.name in {'index.html', 'interrupted-draft.html', 'round-0.html'}:
        if 'candidate' in p.parts or 'control' in p.parts or 'old' in p.parts or name.startswith('cases/'):
            return '该组/轮次网页实现' + ('的中断草稿' if p.name=='interrupted-draft.html' else '') + '；需原本地资源，不能视为完整离线网站。'
        return '历史评审页/入口；媒体与原资源保留本地，仓库副本不提供完整视觉预览。'
    result = PURPOSES.get(p.name)
    if result is None:
        raise ValueError('Missing file description: ' + name)
    if name.startswith('skills/') and p.name not in {'SKILL.md', 'openai.yaml'}:
        result = '独立安装分发副本：' + result + ' 由 pack:skills 同步。'
    return result


def main():
    raw = subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'], cwd=ROOT)
    paths = {p for p in raw.decode('utf8').split('\0') if p and (ROOT/p).is_file()}
    paths.add('docs/FILE-INDEX.md')
    lines = ['# 仓库逐文件用途索引', '', '由 `python scripts/build-file-index.py` 生成。覆盖 Git 已跟踪及未忽略的待提交文件；不包含本地原素材、依赖和工作缓存。', '',
             '当前进度见 [根 README](../README.md)，历史文件语义见 [归档 README](../progress/README.md)。', '',
             f'共 {len(paths)} 个文件。每个路径均可点击；同名文件按所属目录区分。', '', '| 文件 | 用途 |', '|---|---|']
    for name in sorted(paths):
        lines.append(f'| [{name}]({quote("../"+name, safe="/.-_")}) | {purpose(name)} |')
    DEST.write_text('\n'.join(lines)+'\n', encoding='utf8')
    print(f'Indexed {len(paths)} files')


if __name__ == '__main__':
    main()
