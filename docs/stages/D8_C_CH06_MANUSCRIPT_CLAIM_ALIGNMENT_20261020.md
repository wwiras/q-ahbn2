# RO4 D8-C claim alignment control — 20 October 2026

**Scope:** controlled claim qualification for Chapter 6 and the Q-AHBN2 manuscript; no amendment to algorithm, datasets, formal experiments, or submitted journal version.

## Source authority
- Frozen GKE validation: `wwiras/q-ahbn2`, `docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md`.
- D8-C independent arithmetic: `docs/stages/D8_C_INDEPENDENT_STATISTICAL_RECALCULATION_20261020.md`.
- D8-C direct-source caveats: `docs/stages/D8_C_INDEPENDENT_OFFLINE_EVIDENCE_CHECK_20261020.md`.
- D8-A and D8-B: **PARTIAL**. Statistical arithmetic: **PASS for secondary reconciliation dataset**, not 25-source integrity. Final D8 scientific release **HOLD**.
- Submitted Journal of Cloud Computing version remains under peer review, neither accepted nor published, no article DOI.

## Approved scientific interpretation
The existing five-seed GKE dataset (Gossip, Structured, DC-SoC, AHBN, Q-AHBN2; seeds 42–46) gives a *preliminary*, blocked-by-seed Q-AHBN2-minus-AHBN delivery difference of +0.210948 (21.09 percentage points), unadjusted 95% paired Student-t CI [+0.025075, +0.396821]. Four seeds favor Q-AHBN2; one favors AHBN. This is accompanied by higher propagation delay (+0.020129 seconds; CI [+0.002483, +0.037774]), duplicates (+266.4; CI [+47.736, +485.064]) and total forwards (+1012.2; CI [+121.266, +1903.134]). Inference is exploratory/conditional because n=5, endpoints are multiple/unadjusted, and original archived 25 metrics/manifests, hashes, and raw logs are not fully independently reconciled.

Do **not** say all paired GKE CIs cross zero for the *new* 25-run dataset. That statement belongs to the **earlier S17/S18 Kubernetes campaign**, if retained and explicitly attributed to it. Do not silently replace or pool the older campaign with the newly calculated one.

ControlSim eight-condition same-seed paired results remain a separate, previously frozen experiment; do not recast GKE as statistical replication or combine simulated seconds with measured GKE runtime seconds. Propagation delay is conditional on reached peers; lower delay with very low delivery must not be interpreted as faster network-wide dissemination.

## Proposed insertion — Chapter 6 GKE results/discussion (not inserted in this control-only gate)
'In the later five-method, five-seed GKE formal campaign, the current secondary reconciliation dataset yields a mean Q-AHBN2–AHBN delivery difference of +21.09 percentage points (unadjusted paired 95% CI [+2.51, +39.68] percentage points). The same paired analysis records longer propagation delay, more duplicates and more total forwarding activity for Q-AHBN2. These findings show a measured delivery–overhead trade-off in the tested runs, not overall or general performance superiority. The arithmetic has been independently recalculated, but final source-by-source evidence integrity and recovery-estimator interpretation remain under audit; therefore these results are preliminary and are not used to close scientific validation.'

## Proposed insertion — manuscript results/discussion (for a controlled revised version only)
'Additional formal Kubernetes results indicate a potentially meaningful delivery improvement for bounded Q-AHBN2 relative to AHBN under the tested configuration, alongside greater propagation delay and forwarding cost. The current n=5 blocked-seed paired estimates are unadjusted and have been reproduced from a secondary reconciliation dataset; complete independent verification against original run artifacts remains pending. We therefore treat this as preliminary condition-specific evidence, not a universal gain or a replacement for the earlier frozen simulator comparisons.'

## Specific revision guardrails
1. Distinguish *earlier corrected S17/S18 Kubernetes evidence* from the *later 25-run GKE campaign* and identify which dataset supports each assertion/table/figure.
2. Review abstract, contributions, results, discussion, limitations, conclusion and thesis RQ4 answer for general-superiority, reduced-overhead, and convergence claims. Preserve bounded-learning architecture claims where actually supported.
3. Timing / neighbour-update explanation remains a **plausible experimental mechanism**, not established sole cause. Recovery observations and non-observations must remain qualified.
4. Keep seed43 and all low-delivery observations; no filtering, recalculation of experimental outcomes, algorithm changes, new runs or gate promotion.
5. The earlier submitted manuscript PDF must not be silently overwritten. Journal text and submission are unchanged until separately reviewed and authorized. A Zenodo *data* DOI is not a manuscript/article DOI.
6. Before final claim release: inspect all 25 original metrics and run manifests, reconcile 100 primary metric values, verify run/seed identity and provenance, inspect analysis code/reports, and resolve the anomalous folder label against manifests.

**Decision:** CLAIM-ALIGNMENT CONTROL DOCUMENTED; Chapter 6 PH5 and D8 scientific release remain HOLD; no claims of journal acceptance/publication.
