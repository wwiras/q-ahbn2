# D8-C — Offline statistical analysis of the formal K5-Q matrix

**Date:** 20 October 2026
**Recommendation:** **PASS for the D8-C statistical-analysis gate only.** D8-A and D8-B remain **PARTIAL**; this result does not close either gate or establish final scientific release.

## Scope and decision

This report analyzes the original 25 formal runs in `output/evidence/`. Before calculating summaries, the four frozen primary metrics were independently reconstructed from each run’s archived logs and compared with:

1. that run’s archived `metrics.json`;
2. the existing D8-A `audit.csv`; and
3. the existing D8-A `preliminary_comparison.json`.

All **100/100** metric values matched exactly in the independent reconstruction and agreed with both existing reconciliation records. The 25 method-by-seed cells are complete, finite, and unique. No run was excluded, no value was imputed, and every low-delivery observation remains in the analysis. Statistical calculations passed the frozen K4-Q conventions.

PASS is limited to **source-to-metric reconciliation and correctness/reproducibility of these calculations against the currently archived bytes**. It is not a claim that historical byte integrity has been established: no trusted execution-time hash baseline exists. Recovery-definition ambiguity remains a secondary limitation. D8-A/B remain PARTIAL, and no manuscript claim is authorized by this analysis.

## Frozen design and statistical conventions

- Methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2.
- Seeds: 42–46; **seed is the independent unit**, n=5.
- One run per method-by-seed coordinate; no message-, peer-, or churn-level pseudoreplication.
- Metrics and original units: delivery ratio (proportion), propagation delay (seconds), duplicates (count), total forwards (count).
- Method summaries: arithmetic mean, sample standard deviation (n−1), and two-sided 95% Student-t confidence interval for the mean, df=4 and t critical value 2.7764451051977987.
- Paired comparison: per-seed Q-AHBN2 minus AHBN, followed by mean difference, sample SD of differences, and two-sided 95% Student-t CI with df=4.
- The specified t intervals are untransformed. Intervals for bounded or count-valued outcomes may extend beyond their physical ranges; they represent the frozen procedure, not feasible individual values.
- No p-values, null-hypothesis decisions, multiplicity correction, composite score, or winner ranking is used. These intervals are descriptive uncertainty summaries at n=5, not evidence of equivalence or universal superiority.

The K4-Q scenario is an implementation-valid Kubernetes counterpart (N=20, BA m=2, 240 messages on a planned 0.4-second grid, four churn events at +1/+26/+51/+76 seconds, seeds 42–46). It is not a literal numerical replication of the ControlSim scale or event semantics.

## Metric verification and provenance

The reproducible analysis script calls the existing independent D8-A reconstruction (`gke/scripts/audit_d8_a_offline.py`) over the archived merged logs. That reconstruction deduplicates exact duplicated log records, rebuilds delivery opportunities and the four endpoints, and checks them against the recorded metrics. D8-C then checks each reconstructed value against the archive and both D8-A reconciliation tables **before** aggregation.

The verification succeeded for 25/25 run coordinates and all 100 primary metric values. Every run reconstructed 240 source injections and 240 delivery opportunities. The propagation-delay estimator is the mean over injected messages with at least one logged reception, using the last logged reception time for each such message minus its injection time. Thus it is not an average of all peer latencies. No undefined or non-finite primary metric value was encountered; values were not imputed.

For each run, `metric_verification.json` stores the source path and current SHA256 of `metrics.json`, `run_manifest.json`, `topology.json`, and `logs.jsonl`, plus per-metric archive/reconstruction values and differences. These hashes identify the bytes read in this audit. They do not establish unchanged-since-execution integrity. The recorded source commit and expected image digest match the existing D8-A checks; build reproducibility is not claimed.

## Five-method summaries

Each cell below is **mean; sample SD; 95% Student-t CI**.

| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards |
|---|---|---|---|---|
| Gossip | 0.876779; 0.012188; [0.861646, 0.891912] | 0.089328; 0.029595; [0.052581, 0.126074] | 3479.2; 1262.506911; [1911.591, 5046.809] | 3958.4; 77.442237; [3862.243, 4054.557] |
| Structured | 0.081396; 0.000269; [0.081062, 0.081729] | 0.003677; 0.000824; [0.002654, 0.004700] | 0; 0; [0, 0] | 152; 0; [152, 152] |
| DC-SoC | 0.407186; 0.437704; [-0.136296, 0.950667] | 0.093072; 0.118831; [-0.054475, 0.240620] | 0; 0; [0, 0] | 1710.6; 2095.416379; [-891.203, 4312.403] |
| AHBN | 0.200718; 0.074113; [0.108694, 0.292742] | 0.017040; 0.009303; [0.005488, 0.028591] | 341.6; 200.342956; [92.841, 590.359] | 726; 354.732998; [285.541, 1166.459] |
| Q-AHBN2 | 0.411666; 0.182140; [0.185510, 0.637823] | 0.037168; 0.018099; [0.014695, 0.059642] | 608; 274.509563; [267.151, 948.849] | 1738.2; 873.423265; [653.702, 2822.698] |

These are separate method summaries over five seeds. In particular, DC-SoC has substantial between-seed variability; its mean alone does not describe that heterogeneity. The zero duplicate counts for Structured and DC-SoC are the archived metric definition’s results, not independent evidence that no duplicate traffic occurred at the network layer.

## Prespecified paired Q-AHBN2 minus AHBN comparison

Positive delivery differences are higher Q-AHBN2 delivery. Positive delay, duplicate, and forward differences mean higher latency or overhead under Q-AHBN2.

| Metric | AHBN mean | Q-AHBN2 mean | Mean paired difference | SD of paired differences | Two-sided 95% paired t CI |
|---|---:|---:|---:|---:|---|
| Delivery ratio | 0.200718 | 0.411666 | +0.210948 | 0.149696 | [+0.025075, +0.396821] |
| Propagation delay (s) | 0.017040 | 0.037168 | +0.020129 | 0.014211 | [+0.002483, +0.037774] |
| Duplicates | 341.6 | 608 | +266.4 | 176.105934 | [+47.735602, +485.064398] |
| Total forwards | 726 | 1738.2 | +1012.2 | 717.532369 | [+121.265890, +1903.134109] |

The mean delivery difference is **+21.0948 percentage points**. The absolute paired differences and the intervals show a descriptive delivery-versus-cost trade-off in these five seeds: Q-AHBN2 has a higher mean delivery ratio, with higher mean propagation delay, duplicates, and total forwards. The intervals are not converted into a binary success rule; no causal or universal method-superiority claim follows.

### Per-seed paired values

Each entry is Q-AHBN2 minus AHBN. The full precision, including both method values, is in `paired_seed_differences.csv`.

| Seed | Delivery ratio | Delivery (percentage points) | Propagation delay (s) | Duplicates | Total forwards |
|---:|---:|---:|---:|---:|---:|
| 42 | +0.203421 | +20.3421 | +0.019105 | +257 | +983 |
| 43 | −0.007741 | −0.7741 | +0.000476 | +32 | −41 |
| 44 | +0.158102 | +15.8102 | +0.013695 | +236 | +763 |
| 45 | +0.353970 | +35.3970 | +0.036106 | +527 | +1696 |
| 46 | +0.346987 | +34.6987 | +0.031259 | +280 | +1660 |

The seed-level data retain the one negative delivery difference and the one negative forward difference. No outcome was selected or omitted.

## Interpretation limits

- **Small n:** Five seeds provide limited precision and do not support broad generalization beyond this frozen Kubernetes condition.
- **Multiplicity:** Four separate primary outcomes are reported under the frozen descriptive interval plan. The intervals are not multiplicity-adjusted and are not used as four independent declarations of a single winner.
- **Recovery is secondary:** The D8-B audit found 10 recovered and 90 censored event observations; one recorded recovery exceeds 18 seconds and two event observations reuse one message anchor. The 18 seconds is a post-workload settle delay, not an event-relative censor horizon. These recovery records were not used in the primary statistics.
- **Mechanism is untested:** Archived evidence does not establish cluster-wide neighbour-state convergence. This report does not claim that injection timing, pod readiness, peer reachability, or neighbour timing caused any delivery outcome.
- **Historical file integrity:** Current hashes are reproducibility fingerprints only; no trusted execution-time hash baseline is available.
- **Environment:** The K8s run matrix is an implementation-valid counterpart, not a literal numerical replication of ControlSim.

## Reproducibility and artifacts

From the repository root:

```sh
python3 gke/scripts/analyze_d8_c_offline.py \
  --output-dir docs/stages/d8_c_20261020
python3 -m unittest discover -s tests -p 'test_d8_c_statistics.py' -v
```

The analysis uses the Python standard library, reads original evidence without writing to it, and writes derived outputs under `docs/stages/d8_c_20261020/`.

- `verified_25_run_dataset.csv` / `.json`: all four endpoints and identities for all 25 cells.
- `metric_verification.json`: archived-vs-reconstructed values, current file hashes, and supporting paths.
- `method_summaries.csv` / `.json`: all 20 method-by-metric summaries.
- `paired_seed_differences.csv` / `.json`: all 20 seed-by-metric paired values.
- `paired_qahbn2_vs_ahbn_summaries.csv` / `.json`: four paired estimates and confidence intervals.
- `recovery_secondary_summary.json`: recovery caveat only.
- `discrepancy_register.json`, `summary.json`, `execution.log`, `tests.log`: audit status and reproducibility records.

The new D8-C unit tests pass **4/4**, including df=4 Student-t constant, zero-variance interval behavior, finite-input checks, and seed-paired contrast calculations.

## Recommendation

**D8-C PASS for offline statistical calculation and source-to-metric reconciliation.** The 25 runs and 100 primary metric values reconcile; the frozen summaries and paired comparisons are reproducible, and all outcomes are retained. This does not resolve the historical hash-baseline limitation or close D8-A/B. Recovery interpretation remains secondary and ambiguous; timing causation is not claimed. No experiment, algorithm, original evidence, thesis, or manuscript was modified, and no push was made.
