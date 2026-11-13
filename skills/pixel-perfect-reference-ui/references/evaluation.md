# Frozen-round evaluation / 冻结轮次评测

Before a run, freeze skill + toolkit hashes, model identifier (or unknown), prompt, input files/permissions, browser version, viewport/DPR, state sequence, requirements and work budget. Record unknowns honestly. Save each round in a new directory; do not overwrite the previous output. User review stays null until the user supplies it.

Run no-skill / old-skill / new-skill with the same input and budget in fresh contexts. Keep first attempt and limited-repair outcomes separate. Record actual usage; a tool-call ceiling does not imply identical token cost. A patched page demonstrates a page fix; rerun from clean inputs to demonstrate skill improvement.

Repeat reference capture three times. Compare all three pairs. If the reference varies more than configured tolerance, diagnose timing, randomness, font swaps or delayed resources first. Label comparisons diagnostic while instability remains. Never silently align, resize or mask regions to improve a score.

The `compare` command reports image metrics ONLY. Defaults: threshold 0.1, includeAA false, global and per-region mismatch <= 0.01. `exact` additionally requires raw RGBA equality including anti-aliasing. This is not a perceptual similarity percentage. Anchors <=2 CSS px and title/button line breaks are separate checks using capture records. Actual browser tests and human review remain separate gates.

Completion = passed predefined requirements / all predefined requirements. Unknown or blocked is not passed. Success = cases meeting ALL declared visual, functional and completeness gates / all scheduled cases. Track pending, timeouts, failures and infrastructure errors explicitly. An infrastructure retry retains its original record and belongs to the same case; do not inflate denominator by counting retries as new cases. Human score is never averaged into pixel metrics.

Sample evaluation.json:

```json
{"schemaVersion":1,"caseId":"example","round":"r0","requirements":[{"id":"menu","status":"pending","evidence":null}],"humanReview":null,"runs":[{"caseId":"example","status":"pending"}]}
```

Allowed run status: passed, failed, timeout, pending, infrastructure_error. Only assign passed after visual, behavior and completeness checks. `report` preserves the submitted status; it is not a judge. For pure pixel comparisons use comparison.json, not a task success label.

Repair order: structure -> assets/fonts -> text -> spacing -> colors/shadows -> motion. Default at most three repair rounds. Stop with an evidence-backed gap report when source resources are missing. Convert only generalizable findings into skill rules; keep site-specific measurements in the case.

Hold-out samples are not development prompts. Once used to tune a skill, mark them regression and replace them in future releases. Adapted Design2Code/DesignBench runs are internal evaluations, not official leaderboard scores. A small sample is not a general success-rate claim. Never inspect reference HTML during screenshot-only generation; reserve it for evaluator use.
