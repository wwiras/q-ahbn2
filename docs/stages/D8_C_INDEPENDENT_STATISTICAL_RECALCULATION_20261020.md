# D8-C — Independent arithmetic recalculation (20 October 2026)

**Decision: STATISTICAL ARITHMETIC PASS (reconciliation dataset); full evidence-to-source verification PARTIAL; D8 final scientific release HOLD.**

## Input, provenance and independent method
Input was the 100-row `preliminary_comparison.json` available from the canonical RO4 Google Drive D8-A evidence set. It has one row for each unique seed (42–46) × method (Gossip, Structured, DC-SoC, AHBN, Q-AHBN2) × frozen endpoint (delivery_ratio, propagation_delay, duplicates, total_forwards), 25 coordinates × four metrics. Each row includes prior reported value, `archived` numeric value, and discrepancy. All 100 keys unique; maximum absolute discrepancy between original report and the data-set `archived` value = 3.9336138513146324e-11 (rounding-level). This file is a **secondary archived reconciliation dataset**, not independent byte-level authentication of all 25 raw `metrics.json` files.

Independent calculation used Python's `statistics.mean`, `statistics.stdev` (sample n−1) and `scipy.stats.t.ppf(0.975,4)` applied to five blocked seeds, without using the previously published aggregate figures. Two-sided unadjusted 95% Student-t confidence interval = mean ± t_{0.975,4} × sampleSD / sqrt(5). Q-AHBN2 minus AHBN paired contrasts are matched by seed.

## Computed five-seed method means
| Method | Delivery ratio | Delay (seconds) | Duplicates | Total forwards |
|---|---:|---:|---:|---:|
| Gossip | 0.876778999756 | 0.089327530265 | 3479.2 | 3958.4 |
| Structured | 0.081395644393 | 0.003677065174 | 0 | 152 |
| DC-SoC | 0.407185534243 | 0.093072122137 | 0 | 1710.6 |
| AHBN | 0.200718199146 | 0.017039564053 | 341.6 | 726 |
| Q-AHBN2 | 0.411666278612 | 0.037168088953 | 608 | 1738.2 |

## Independently reproduced primary paired contrasts
| Primary metric (Q-AHBN2 minus AHBN) | Mean | Sample SD | Two-sided 95% paired t interval |
|---|---:|---:|---|
| Delivery ratio | +0.210948079466 | 0.14969642 | [+0.02507542, +0.39682074] |
| Propagation delay (s) | +0.020128524899 | 0.01421117 | [+0.00248303, +0.03777402] |
| Duplicates | +266.4 | 176.10593403 | [+47.73560185, +485.06439815] |
| Total forwards | +1012.2 | 717.53236861 | [+121.26589035, +1903.13410965] |

Per-seed paired delivery differences for seeds 42–46: +0.20342100, −0.00774059, +0.15810241, +0.35397038, +0.34698719. Four positive, one negative. All computed means, sample SDs and intervals reproduce the rounded figures in `docs/stages/D8_K5Q_25RUN_PRELIMINARY_RECONCILIATION_20261020.md` to its printed precision.

## Boundary and scientific interpretation
This **does not** independently re-read all 25 actual `metrics.json`, all 25 `run_manifest.json`, their immutable SHA256 manifests, the missing local D8-C analysis code/report/per-seed tables, or raw controller/peer logs. Prior connected navigation found a potentially inconsistent Drive folder named `seed42` inside the timestamped seed43 evidence root; a folder label alone neither invalidates a run nor proves complete preservation. Do not promote arithmetic PASS to independent evidence-integrity PASS without original-content reconciliation.

Measured Q-AHBN2 delivery is higher than AHBN on average (mean +21.09 percentage points), with greater propagation delay, duplicates and total forwards. This is a trade-off; n=5 and multiple endpoints, intervals are unadjusted, no general superiority or causal neighbor-convergence claim. Keep low delivery and all outcomes; do not exclude runs. D8-A and D8-B remain PARTIAL; D8 final release HOLD.

**Next bounded offline action:** verify every archived source metrics/manifest identity and compare with the 100-row dataset; investigate the Drive folder label against manifest contents; inspect actual D8-C code and report when available. No GKE rerun, algorithm edit or result reclassification by performance.

Manuscript **under peer review** at *Journal of Cloud Computing*, no DOI and not accepted/published. No manuscript or thesis text edits made by this audit.
