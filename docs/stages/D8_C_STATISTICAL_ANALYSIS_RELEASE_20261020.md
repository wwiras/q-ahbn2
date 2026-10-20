# D8-C — Offline statistical analysis release (20 October 2026)

**Decision:** Proceed with **offline** statistical analysis of the complete existing 25-run K5-Q matrix. Retain all outcomes and the frozen primary metrics. No algorithm modifications, GKE reruns, exclusions, altered evidence, or manuscript updates are authorized. D8-I1 remains closed for current-state file completeness (historical byte-integrity baseline unavailable); D8-A and D8-B remain PARTIAL with documented limitations, not scientific PASS by implication.

## Source authority
- Frozen K4-Q matrix and analysis contract: `docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md` in `wwiras/q-ahbn2`.
- Experimental evidence: `output/evidence` under https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5.
- Current audit disposition: `docs/stages/D8_B_OFFLINE_REVIEW_DECISION_20261020.md`. Local D8-A/B derived tables, scripts and reports are operator-reported and must be directly checked against original evidence when running D8-C.
- Thesis control/text: https://github.com/wwiras/MUM_FIT_ThesisWira ; corpus: https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR.

## Statistical plan: follow pre-frozen protocol, not post-hoc outcome optimisation
- Five methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2; seeds 42, 43, 44, 45, 46; 25 unique run coordinates. Same-seed paired comparisons, **n=5 seeds**, no message- or peer-level pseudoreplication.
- Primary metrics only: `delivery_ratio`, `propagation_delay`, `duplicates`, `total_forwards`; verify values directly against archived per-run `metrics.json` and existing reconciliation tables.
- K8s-VAL-Q primary comparison: per-seed `Q-AHBN2 - AHBN` for every primary metric. Report all five paired values, mean paired difference, sample SD, two-sided 95% Student-t interval (df=4), method means/SDs/intervals as frozen.
- Exp13-Q-K8s: report all five methods separately, means, sample SDs, two-sided 95% Student-t intervals (df=4), and only pre-frozen reference contrasts. Do not introduce outcome-selected tests, composite rankings or claims of universal superiority. State whether latency is computed only on delivered messages and whether any run has undefined values; do not impute.
- Address multiple endpoints/comparisons transparently. Distinguish descriptive/unadjusted intervals from any prespecified confirmatory interpretation; do not cherry-pick p-values or use non-overlapping individual CIs as a substitute for paired inference. Summarize practical trade-offs, especially delivery versus forwarding/duplicates/latency, without choosing a winner after seeing results.
- Preserve low delivery in all 25 runs; performance by itself is not a run-invalidity criterion. Retain D8-A/B recovery measurement limitation as a **secondary diagnostic caveat**, not a reason to modify four primary endpoints.
- Separate outcomes (observed), uncertainty (five-seed intervals) and mechanisms (untested causal explanation). No claim that neighbour-state timing *caused* the observed delivery ratios, because cluster-wide convergence evidence is missing.

## Offline execution/deliverables
1. Verify local worktree, stash and prior unpushed commits before writing; preserve `stash@{0}` and all untracked D8 artifacts.
2. Reconstruct 25-row machine-readable dataset from original archived metrics; provide file-level provenance/checksum/source paths and a discrepancy register.
3. Produce per-method summary table, five paired seed contrasts, intervals, reproducible analysis script/tests, and logs under a **new derived output directory** (not `output/evidence`). Record statistical conventions including zero variance, confidence distribution and units.
4. Create a bounded scientific report with limitations of n=5, multiplicity, the frozen K8s scenario, unresolved recovery estimator semantics and no execution-time checksum baseline. Include full results rather than only favourable figures.
5. Recommend D8-C PASS/PARTIAL/HOLD based on source reconciliation and correctness of calculations. Do not automatically close D8-A/B. Stop and ask for scientific decision only if source contradictions, invalidities or requested exclusions arise; otherwise complete offline work and report decisions/blockers.

## Manuscript status
*Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is **under peer review** at *Journal of Cloud Computing*, with **no DOI**; neither accepted nor published. PDF: https://drive.google.com/file/d/1NZKcOHtP4qW0AImbdvQgl8pqINe04qJ4/view ; repo: https://github.com/wwiras/QAHBN2-Manuscript ; Drive: https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj. No manuscript edit authorized.
