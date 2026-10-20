# D8-C provisional statistical disposition — 20 October 2026

**Decision: D8-C PROVISIONAL PASS only; final scientific release HOLD. D8-A PARTIAL; D8-B PARTIAL.** This is a control decision, not an independent reproduction or a claim of definitive statistical validation.

## Basis and verification status
- Frozen protocol: `docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md`; D8-C statistical release: `docs/stages/D8_C_STATISTICAL_ANALYSIS_RELEASE_20261020.md`; D8-B limitations: `docs/stages/D8_B_OFFLINE_REVIEW_DECISION_20261020.md`.
- Retain all 25 original formal runs: Gossip, Structured, DC-SoC, AHBN and Q-AHBN2, seeds 42–46. Four frozen primary metrics: `delivery_ratio`, `propagation_delay`, `duplicates`, `total_forwards`.
- D8-C local report, analysis script and per-seed output tables remain **unverified against original archived run metrics** in this decision. They were not located as remotely committed D8-C deliverables at review time. This control record does not assert that their calculations, data provenance, or test output independently passed.
- Canonical archived experimental evidence: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5 (`output/evidence`). GitHub `wwiras/q-ahbn2` is authoritative for committed code/control records. Local unpushed files/stash and archived evidence must be preserved.

## Release checklist — offline, read-only
1. Inspect exact local D8-C report, script, per-seed tables, test/logs and file provenance. Identify immutable evidence paths and source hashes where available; do not imply historical byte-level integrity without an execution-time checksum baseline.
2. Independently reconcile every method/seed/metric value to archived run `metrics.json` (25 coordinates); explicitly record missing/undefined values or discrepancies.
3. Independently reproduce means, sample SD, two-sided 95% t intervals (df=4), and each of five same-seed Q-AHBN2-minus-AHBN paired values per primary metric; verify no pseudoreplication, outcome-selected tests or inappropriate imputation.
4. Preserve all observed endpoints and unfavorable results. Discuss multiplicity, n=5 precision, dissemination trade-offs, and the frozen single GKE scenario; describe timing/neighbor-state causality as unproven.
5. Carry forward D8-A evidence-integrity limitations and D8-B secondary recovery measurement/observation-window limitations unchanged. No automatic promotion of D8-A/B to PASS.
6. Only after completing this independent check, record an explicit D8-C final PASS/PARTIAL/HOLD with signed-off findings, unresolved discrepancies and reproducible evidence pointers. Final scientific release stays HOLD until that separate decision.

No GKE runs, algorithm or harness modifications, new experiment gates, evidence exclusions or manuscript scientific-claim edits are authorized. Do not modify `output/evidence`.

## Manuscript status
*Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* remains **under peer review** at *Journal of Cloud Computing* (https://link.springer.com/journal/13677), **without DOI**, not accepted or published. Manuscript PDF: https://drive.google.com/file/d/1NZKcOHtP4qW0AImbdvQgl8pqINe04qJ4/view; manuscript repository: https://github.com/wwiras/QAHBN2-Manuscript. Thesis control: https://github.com/wwiras/MUM_FIT_ThesisWira ; thesis corpus: https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR.
