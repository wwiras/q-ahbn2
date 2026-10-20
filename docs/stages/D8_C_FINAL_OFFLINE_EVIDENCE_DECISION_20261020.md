# D8-C — Final offline evidence integrity decision

**Decision: PARTIAL.** The 25-run matrix, all 100 primary values, and the statistical calculations reproduce from the currently available local archive. Current-file hashes agree with a prior D8-A audit inventory, but no trusted execution-time checksum baseline exists. Therefore, historical byte integrity is not established and D8-C is not closed.

## Scope and controls

This review was read-only with respect to original evidence and experimental code. It used the local `output/evidence/` mirror and the existing D8-A reconciliation dataset at `output/d8_a_independent_20261020/preliminary_comparison.json`. No live cluster, Kubernetes, cloud, Helm, or Docker operations were run; no experiment was started. Manuscript and thesis files were not modified.

The five selected formal roots are:

| Seed | Evidence root |
|---:|---|
| 42 | `20261020T032934Z-K5Q-formal` |
| 43 | `20261020T035637Z-K5Q-formal` |
| 44 | `20261020T041621Z-K5Q-formal` |
| 45 | `20261020T043745Z-K5Q-formal` |
| 46 | `20261020T045636Z-K5Q-formal` |

Each root contributes Gossip, Structured, DC-SoC, AHBN, and Q-AHBN2. The root, run-directory seed, `run_manifest.json`, and `metrics.json` identities agree for all **25/25** coordinates. The seed-43 root contains `runs/seed43/` and all five method records; their manifests identify seed 43. The earlier `20261020T023432Z-K5Q-formal` is a separate seed-42 root, outside this set. It was not deleted, renamed, or reclassified.

## Source, protocol, and file checks

- All 25 original manifests and metrics files parsed. Seed, method, and run ID agree across path, manifest, and metrics.
- The frozen K4-Q workload, topology, strategy, target-selection fingerprint, and churn schedule were checked. Each manifest records 240 messages at 0.4-second intervals, targets 0/5/10/15, and churn offsets +1/+26/+51/+76 seconds. Topology fingerprints and generated configuration copies were checked; same-seed methods have matching topology/source/target fingerprints.
- Each selected root records source commit `6433f7429e0342df44c272b236423c65203a9136` and expected image digest `sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`. Per-run peer image IDs match the digest; experiment and cleanup exit records are zero, cleanup is PASS, and the archived controller pods completed.
- **100 source files** were SHA256-checked: the 25 each of `metrics.json`, `run_manifest.json`, `topology.json`, and `logs.jsonl`. All **100/100** hashes match the corresponding earlier D8-A audit inventory fingerprints. The separate D8-I1 comparison labels the trusted reference baseline `BASELINE_UNAVAILABLE`; none of these current or prior audit hashes proves unchanged bytes since experiment execution.
- Missing/unreadable required files: none in the selected matrix. Confirmed scientific or frozen-protocol violations: none. No run was excluded for low delivery.

## Primary metric reconciliation

Every original `metrics.json` value was compared to the matching `reported` value and the `archived` source field in the 100-row reconciliation dataset. The predeclared absolute tolerance is **5 × 10⁻¹⁰**, appropriate for the displayed ten-decimal report precision.

**Result: 100/100 PASS.** Maximum absolute source-to-reported difference is **3.9336138513146324 × 10⁻¹¹**. No source was corrected or overwritten. The full row-level evidence, including original path, both values, difference, tolerance, and status, is in [metrics_comparison.csv](../../output/d8_c_final_offline_20261020T091547Z_final/metrics_comparison.csv).

## Statistical reproducibility

Independent recomputation used five blocked seeds (n=5), arithmetic mean, sample SD (n−1), and two-sided unadjusted 95% Student-t confidence intervals (df=4). Q-AHBN2−AHBN observations were matched by seed. Recomputed method summaries, paired contrasts, and per-seed tables agree with the existing D8-C CSVs and report at displayed precision.

| Metric | Mean paired difference | Sample SD | Unadjusted 95% paired t CI |
|---|---:|---:|---|
| Delivery ratio | +0.210948 | 0.149696 | [+0.025075, +0.396821] |
| Propagation delay (s) | +0.020129 | 0.014211 | [+0.002483, +0.037774] |
| Duplicates | +266.4 | 176.105934 | [+47.735602, +485.064398] |
| Total forwards | +1012.2 | 717.532369 | [+121.265890, +1903.134110] |

The higher observed mean delivery (about 21.09 percentage points) co-occurs with higher mean delay, duplicates, and forwards. This is a delivery-versus-overhead trade-off, not overall superiority. Results are limited to five seeds; intervals are unadjusted for multiplicity. No causal mechanism is established. The complete five-method summaries and all per-seed contrasts are in [audit_report.md](../../output/d8_c_final_offline_20261020T091547Z_final/audit_report.md) and [statistical_recalculation.csv](../../output/d8_c_final_offline_20261020T091547Z_final/statistical_recalculation.csv).

## Gate disposition

**PARTIAL rather than PASS:** source-to-report values, run identities, current-file checks, protocol fingerprints, and arithmetic reproduce, but trusted historical byte-integrity evidence is incomplete. No material value mismatch or confirmed protocol violation was found. The audit output is reproducible from the current local evidence bytes only.

D8-A and D8-B remain **PARTIAL** and are not upgraded by this decision. D8-B's recovery-window interpretation remains a secondary limitation; recovery outcomes were not used for the four primary metrics. D8-C closure for evidence reproducibility is not recommended until the integrity-evidence limitation is explicitly accepted or resolved. Final D8 scientific closure remains a separate bounded decision considering D8-A, D8-B, and the strength and limitations of the results.

The audit output directory is [d8_c_final_offline_20261020T091547Z_final](../../output/d8_c_final_offline_20261020T091547Z_final/). Its `discrepancies.md` records the remaining limitations and `audit_execution.log` records commands and tool versions.
