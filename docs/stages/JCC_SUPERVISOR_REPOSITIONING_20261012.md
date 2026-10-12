# JCC-SR — Supervisor Publication-Positioning Review (12 October 2026)

## Objective
Record supervisor feedback before revision of the Q-AHBN Journal of Cloud Computing manuscript. This is a scoped publication-positioning review, not scientific reopening.

## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md` and its §9.5 reconciliation/readback workflow.
- `docs/01_CANONICAL_AHBN_CONTRACT.md`; `docs/02_QAHBN2_DESIGN_FREEZE.md`.
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`, S13, S14, and `docs/stages/JCC_FINAL_CONTROLLED_SUBMISSION_AUDIT.md`.
- Manuscript: `wwiras/QAHBN2-Manuscript` root `sn-main.tex`; `docs/MANUSCRIPT_MASTER.md`; `docs/PROVENANCE.md`.
- Scientific baseline: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.
- Scientific Drive root `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`; manuscript workspace root `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`.

## Trigger
Supervisor's 12 October 2026 preliminary review highlights: insufficient parameter selection explanations; thesis-like rather than journal-paper presentation; AHBN is not yet published/citable; reviewers may regard Q-AHBN as dependent or incrementally novel; proposal to describe underlying deterministic hybrid scheme without foregrounding AHBN.

## Reconciliation and findings
- Frozen architecture genuinely executes AHBN first, retains an independent AHBN mode/fanout proposal, and applies bounded Q-learning refinement afterward. Mere renaming does not remove that dependency.
- The active manuscript prominently names AHBN in the abstract, Introduction, Related Work, Method, and primary paired comparisons.
- The primary causal evidence is AHBN vs Q-AHBN (40 same-seed pairs across eight ControlSim conditions); a separate five-method benchmark supplies limited external positioning; Kubernetes is complementary operational realization, not pooled evidence.
- Sensitivity evidence exists for gamma selection (0.70/0.80/0.90). Other parameters need explanations assigned to empirical, architectural, or fixed-design rationale without inventing unperformed selection experiments.
- A preprint of the AHBN work, subject to coauthor agreement, manuscript version rules and publication-policy verification, could supply a reviewable citation. A preprint is not peer-reviewed publication.
- AHBN cannot be presented as an unrelated published SOTA method or replaced by another method in descriptions of experiments that actually used the frozen canonical AHBN implementation.
- Current scientific claims, statistics, parameters, results and experiment provenance remain frozen.

## Publication recommendation (provisional, requires supervisor/author decision)
1. Self-contained paper framing: explain the deterministic hybrid controller's mathematics and mechanism, while making AHBN lineage transparently explicit but not the central novelty claim.
2. Emphasize the bounded post-controller learning intervention, attributable local outcomes, separation of retained proposal from intervention, and observed trade-offs.
3. Audit parameter choices in a compact rationale table; distinguish sensitivity-supported values from architectural/fixed choices; no claims of globally optimal hyperparameters.
4. Reduce thesis chronology/RO language; lead with a paper-level problem, gap, question, contribution and limitations.
5. Investigate AHBN preprint with coauthors and journal policy before using a DOI/reference.
6. Preserve AHBN paired-comparator labels and truthful provenance in Results and Methods.
7. Address Overleaf supervisor comments individually before a revised PDF or new submission release.

## Gate status
**REVIEW RECORDED / REVISION HOLD — 2026-10-12.** No scientific or manuscript-text amendments authorized by this record. Do not treat historical JCC GO status as applying to a newly revised manuscript. Revalidate the submission package after approved editorial revisions.

## Next permitted task
Supervisor-comment-by-comment manuscript audit with traceability to frozen design/evidence; prepare a bounded editorial change map for researcher/coauthor approval. Do not change canonical algorithm, experimental data, parameters, statistics, or frozen claims.
