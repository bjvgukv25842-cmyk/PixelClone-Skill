# First development round — 2026-10-29

This is an internal adapted evaluation, not a public benchmark submission.

## Fixed inputs and scope

Monopo London desktop screenshot 1440×900, extracted DOM metadata and resource URL inventory. Screenshot and metadata were supplied equally to no-skill, old-skill and new-skill workers. Source application bundles were not supplied. The old skill itself prevented original resource downloads; that restriction is an observed treatment effect, not unequal input access.

Navigation, hero, pointer lens and cookie dismissal; mobile layout at 390×844 is functional/inferred because the generation inputs contain no mobile reference. Maximum 20 tool invocations, one build and two correction attempts per worker; inherited model settings, exact model ID and token usage unavailable. Tool counts vary and are not equal compute budgets.

## Findings

- Old skill: functional controls and screenshot crops, but rasterized hero/lens, crop seams and clipped mobile typography. Fails faithful dynamic reconstruction.
- No skill: functional draft with original fonts, but hand-approximated background and lens. Fails faithful reconstruction.
- Candidate skill: original fonts and source records, real DOM, working lens follow and menus, but guessed background/lens despite strict source policy. Fails fidelity and source-policy gates.
- Candidate run was interrupted by an account usage limit and later resumed. It disclosed overwriting initial screenshots during a correction. Keep this deviation visible; this round cannot establish clean first-attempt improvement.
- The reference was captured three times with a stationary pointer. All pairs were within 1% pixel tolerance; this is stationary reproducibility, not proof of time-synchronized animation.
- Pixel comparison can reward the old screenshot crop over a real but inaccurate reconstruction. Thus rasterized functional content, motion fidelity, source policy and behavior remain independent gates.

## Release status

Toolkit tests and local demos are delivered as a candidate. Human review is pending. No claim of pixel-perfect reconstruction or improved general success rate. No release/push or global skill installation has occurred.

The 12 holdout cases are listed in `benchmarks/holdout.lock.json`: eight dataset image paths/revisions/hashes are locked and downloaded without inspection; four dynamic source URLs are selected but their reference packages are not yet frozen. None has been used for skill tuning or scored. Candidate release evaluation waits for the development feedback round; this is not reported as 12 passed cases.

Next round: user rates the runnable drafts, fixes are classified, then a new skill version is frozen and reconstructed from clean inputs. Do not silently change the current frozen skill to make its failed run look compliant.

## Human review received — 2026-11-05

Visual 70/100, completion 60/100, motion 40/100, rejected. User identified absent distorted typography and mock-like pointer behavior. Raw transcription: `feedback/monopo-r0.json`. Historical machine results above remain unchanged. Follow-up development repair is recorded in [ROUND-1.md](ROUND-1.md); r1 is source-assisted and not a clean matched-budget comparison.
