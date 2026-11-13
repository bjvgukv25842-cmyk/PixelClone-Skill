# Implementation ledger

Baseline: 91bca5d. Approved plan: PixelClone 增强与实战评测计划 in chat, 2026-10-29.

- Work in the user-requested clone on feat/pixelclone-evaluation; retain original baseline archive in work/.
- Freeze each evaluated skill version; human ratings remain null until supplied.
- Deliver toolkit and development round first; held-out success cannot be claimed until those runs actually execute.
- Benchmark inputs distinguish screenshot-only and website-resource access. Never compare unlike tracks.
- Dependencies local to project. No publishing or globally installing skills.

Tasks: reference/baseline; tested toolkit; bilingual skill packaging; development case; independent review; review bundle.

## Delivery checkpoint — 2026-11-03

- Toolkit: 17 Node/browser/CLI tests and 6 Python tests passed.
- Standalone Chinese package: clean npm ci, CLI help and image collect passed.
- Packaging parity check passed for both languages.
- Review viewer: all three selectors, images and feedback export passed, no JavaScript errors.
- Independent code review findings fixed with regression tests: readiness timeout, browser cleanup, static-animation metadata, delayed CSS backgrounds, source/output aliases (including junctions), duplicate case records, collapsed layout regions.
- Three independent reconstruction trials completed; all fail faithful visual reconstruction. Candidate trial interruption and overwritten first-attempt screenshots disclosed. No claim of skill uplift.
- Human feedback remains pending. 12 holdout cases selected; 8 pinned image inputs downloaded without inspection, 4 dynamic packages pending snapshot. No holdout runs executed.
- Ruling: stop at concrete first-round review before tuning the frozen skill further, as the approved workflow requires the user's ratings between rounds.
- Changes remain on local feat/pixelclone-evaluation. No push, global installation or release.

## R1 delivery checkpoint — 2026-11-06

- User r0 feedback archived: 70 visual, 60 completion, 40 motion; rejected.
- v0.3 candidate adds opt-in renderer auditing, bounded console errors, touch/mobile context configuration, advanced font settings in evidence, and rendered-typography contracts.
- Source-assisted Monopo repair implements Pixi text/masks/displacement/RGB split and the reference gradient; scoped native controls retained. No original app bundle is loaded.
- Final checks: 19 Node + 6 Python tests, 9 case behavior checks, both skill validators, package parity and isolated standalone capture passed. Browser review checked 8 states, 14 links, media loading, feedback persistence/export; r1 humanReview remains null.
- Seven of eight desktop sampled states meet all selected image-region tolerances. Boundary lens and mobile critical regions remain failures; continuous motion and entry timing are not accepted automatically. Stationary reference repeated three times; all pairwise comparisons within configured tolerance.
- Fresh-context skill application test produced a usable evidence contract. Independent code review found object coercion and BFCache teardown bugs, both reproduced and fixed.
- Input permissions expanded to runtime/published-source diagnosis; this is a maintainer repair, not a clean r0-to-r1 skill-uplift experiment. Holdouts remain untouched/unrun.
- Local review and ZIPs delivered; no remote push, release or global skill installation.

## Progress backup checkpoint — 2026-11-13

- R1 human feedback is now archived: visual 100, completion 99, motion 99; acceptance remains pending. The previous checkpoint describes its historical state.
- Cross-case validation was planned (4 then 12 cases, 40 runs total, assets/visual evidence only); no formal holdout runs have started. See docs/plans/2026-11-13-cross-case-validation.md.
- User requested a new GitHub branch containing current progress. This snapshot adds public-safe reports, historical scripts, original delivery ZIPs, local artifact hashes, and a complete file-purpose index. It does not include original site assets, captured shaders, raw app bundles, media, dependencies or credentials.
- No new skill behavior or benchmark score is introduced by this archival change. Historical ZIPs and freeze manifests remain evidence of their original dated snapshots.
