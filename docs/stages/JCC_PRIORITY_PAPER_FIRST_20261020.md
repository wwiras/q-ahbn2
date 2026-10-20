# JCC-PRIORITY-PAPER-01 — Manuscript-first revision gate (20 October 2026)

**Decision: APPROVED PRIORITY ORDER; gate OPEN/NEXT, not scientific PASS.** Revise and verify the paper **before** incorporating its reviewed wording into thesis Chapter 6. This sequencing amends the 15 October JCC-R1–R5 unified programme but does not supersede its scientific protections or historic gate decisions.

## Current true position (not the superseded 15 October snapshot)
- Corrected fanout and Docker technical checks: historic PASS.
- Formal five-method × five-seed GKE campaign: **25/25 reported executed**, not 0/25. Keep every outcome; no repeat experiment authorized by this priority change.
- D8-C: paired statistical **arithmetic PASS on a secondary reconciliation dataset**, but 25-source independent evidence-to-original reconciliation **PARTIAL**. D8-A and D8-B **PARTIAL**; final D8 scientific release **HOLD**.
- Manuscript submitted to *Journal of Cloud Computing*, **under peer review**; not accepted/published, **no manuscript/article DOI**. The current priority is preparing a **prospective controlled revision**, not resubmitting an already submitted manuscript or asserting journal approval.

## Revised gate order and release rules

| Gate | Task | Status / release requirement |
|---|---|---|
| **JCC-PAPER-P0** | Freeze submitted manuscript, PDF, original source SHA, evidence vintages, supervisor comments and D8 caveats | **NEXT**; audit/readback must precede prose changes |
| **JCC-R1A-CLOSE** | Classify original-evidence integrity and adequacy caveats (D8-A/B/C) | **HOLD** on full evidence reconciliation; cannot be declared PASS from secondary statistics |
| **JCC-R2** | Scientific positioning, scope, bounded canonical-AHBN and fanout 1–7 rationale | **NEXT after P0** as draft-only; no universal/optimality claim |
| **JCC-R3** | Methods, references, results provenance and earlier-versus-later GKE campaign separation | **HOLD for verified source claims**; draft with visibly marked preliminary results |
| **JCC-R4** | Results, discussion, limitations, conclusion and abstract audit | **HOLD for final validation**; report delivery–overhead trade-off, not universal superiority |
| **JCC-R5** | Full manuscript claim–evidence map, LaTeX compilation, PDF visual check, supervisor-ready review package | **HOLD** pending verified evidence and source consistency |
| **JCC-JOURNAL** | Separate external revision/submission decision | **HOLD**; no journal action without explicit authorization |
| **C06-MANUSCRIPT-ALIGN** | Align thesis Chapter 6 against reviewed manuscript scientific wording and actual evidence, then build/visual audit | **DEFERRED until paper R5 reviewed**; preserve Chapter 6 PH5 HOLD |

**Nonblocking drafting:** P0/R2/R3 editorial work may be prepared while D8 source-integrity audit is pending. Only evidence-backed claims may be promoted to release. A failure to reconcile original records blocks R1A closure, final R3/R4 claims, R5 release and any journal action.

## Exact source and change boundaries
1. Manuscript repository `wwiras/QAHBN2-Manuscript` is the **publication-source authority**; scientific evidence and experiment contracts remain subordinate to `wwiras/q-ahbn2`.
2. Retain root `sn-main.tex` unchanged as the submitted baseline; prospective revision in **new** root `sn-main1.0.tex` (per manuscript master's 5 October rule). Preserve root bibliography `references.bib`. Do not overwrite the 7 October submitted Drive PDF.
3. The existing ControlSim eight-condition study, older corrected S17/S18 Kubernetes operational evidence, and later 25-run GKE results are **distinct campaigns**; do not pool them.
4. Preliminary latter-campaign Q-AHBN2 minus AHBN: delivery **+0.210948** (95% unadjusted paired t CI [+0.025075,+0.396821]); delay **+0.020129 s**, duplicates **+266.4**, forwards **+1012.2**. Paired n=5; four positive delivery seeds and one negative. Independent arithmetic from a secondary dataset is **not** 25 original-artifact verification.
5. Retain low delivery, timing and neighbour-state caveats, recovery-estimator limits and multiplicity. No optimization, convergence, universal superiority, general reduced forwarding cost or proved sole-cause timing claims.
6. Review journal/supervisor comments in R2–R5; compile actual revision PDF; compare text/citations/tables/figures/abstract; no claims of acceptance. Dataset Zenodo DOI is not an article DOI.
7. No code/algorithm modification, GKE operations, exclusions, raw evidence overwrites, or automatic thesis/manuscript content promotion.

## Evidence pointers
- Independent arithmetic: https://github.com/wwiras/q-ahbn2/blob/main/docs/stages/D8_C_INDEPENDENT_STATISTICAL_RECALCULATION_20261020.md
- Source audit: https://github.com/wwiras/q-ahbn2/blob/main/docs/stages/D8_C_INDEPENDENT_OFFLINE_EVIDENCE_CHECK_20261020.md
- Manuscript claim map: https://github.com/wwiras/QAHBN2-Manuscript/blob/main/docs/D8C_CLAIM_ALIGNMENT_20261020.md
- Submitted PDF: https://drive.google.com/file/d/1NZKcOHtP4qW0AImbdvQgl8pqINe04qJ4/view
- RO4 original experiment archives: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5
- Thesis control: https://github.com/wwiras/MUM_FIT_ThesisWira

**Next active controlled task: JCC-PAPER-P0**; then R2–R5 authoring/review as evidence permits; Chapter 6 only afterward. This is an ordering decision, not permission to submit a revised manuscript to the journal.
