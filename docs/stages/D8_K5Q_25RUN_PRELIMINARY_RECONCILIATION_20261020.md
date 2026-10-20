# D8 — Five-seed evidence reconciliation and preliminary paired statistical analysis (20 October 2026)

**Decision:** All 25 formal coordinates have reported K7 validator PASS. Google Drive folder inventory confirms five distinct timestamped evidence roots, each with five method folders, and each method folder contains 24 archive files including metrics, manifest, churn events, pod snapshots, controller logs, cleanup records and experiment exit status. **Inventory PASS / statistical calculations completed from reported metrics / independent content-and-hash integrity audit OPEN.** This is not a final D8 scientific release.

## Authority and method

Scientific contract: [K4-Q frozen Kubernetes validation](K4_Q_K8S_VALIDATION_FREEZE.md). Methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2. Seeds: 42–46. N=20, BA(m=2), 240 messages with 0.4-second planned grid, four leave/rejoin cycles at +1/+26/+51/+76 s. Seed is the independent blocked comparison unit (n=5), not individual messages, peers or churn events. Report arithmetic means, sample SD (n−1), two-sided 95% Student-t confidence intervals (df=4, t critical 2.776445). All four frozen primary endpoints retain original measurement units. No multiple-comparison-adjusted significance claim is made. Confidence intervals for naturally bounded quantities may extend outside physical bounds, reflecting the stipulated untransformed Student-t procedure rather than possible population values.

Drive roots:
- 42: `20261020T032934Z-K5Q-formal`
- 43: `20261020T035637Z-K5Q-formal`
- 44: `20261020T041621Z-K5Q-formal`
- 45: `20261020T043745Z-K5Q-formal`
- 46: `20261020T045636Z-K5Q-formal`

All five located directly in the canonical RO4 Drive `output/evidence` hierarchy. Generated configurations for seeds42–46 in every run root do **not** represent additional executed coordinates. The 25 observations below are taken from the user-supplied per-seed terminal outcome logs; they have **not** yet been reconciled byte-for-byte against each archived `metrics.json` and manifest.

## Five-seed primary summary

Columns display **mean; sample SD; 95% Student-t CI**.

| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards |
|---|---|---|---|---|
| Gossip | 0.876779; 0.012188; [0.861646, 0.891912] | 0.089328; 0.029595; [0.052581, 0.126074] | 3479.2; 1262.5; [1911.6, 5046.8] | 3958.4; 77.4; [3862.2, 4054.6] |
| Structured | 0.081396; 0.000269; [0.081062, 0.081729] | 0.003677; 0.000824; [0.002654, 0.004700] | 0; 0; [0, 0] | 152; 0; [152, 152] |
| DC-SoC | 0.407186; 0.437704; [-0.136296, 0.950667] | 0.093072; 0.118831; [-0.054475, 0.240620] | 0; 0; [0, 0] | 1710.6; 2095.4; [-891.2, 4312.4] |
| AHBN | 0.200718; 0.074113; [0.108694, 0.292742] | 0.017040; 0.009303; [0.005488, 0.028591] | 341.6; 200.3; [92.8, 590.4] | 726.0; 354.7; [285.5, 1166.5] |
| Q-AHBN2 | 0.411666; 0.182140; [0.185510, 0.637823] | 0.037168; 0.018099; [0.014695, 0.059642] | 608.0; 274.5; [267.2, 948.8] | 1738.2; 873.4; [653.7, 2822.7] |

## Prespecified Q-AHBN2 minus AHBN paired contrasts

| Primary metric | Mean paired difference | Sample SD of paired differences | 95% paired t CI | Direction on observed seeds |
|---|---:|---:|---|---|
| Delivery ratio | +0.210948 | 0.149696 | [+0.025075, +0.396821] | Q-AHBN2 higher average delivery |
| Propagation delay (s) | +0.020129 | 0.014211 | [+0.002483, +0.037774] | Q-AHBN2 higher delay |
| Duplicates | +266.4 | 176.1 | [+47.7, +485.1] | Q-AHBN2 more duplicates |
| Total forwards | +1012.2 | 717.5 | [+121.3, +1903.1] | Q-AHBN2 more forwards |

Paired per-seed delivery deltas (Q-AHBN2 minus AHBN) for seeds 42–46: **+0.203421, −0.007741, +0.158102, +0.353970, +0.346987**, respectively. Four positive and one negative. This shows a bounded delivery-versus-overhead trade-off in the reported five-seed GKE data. The unadjusted paired t-CI for delivery excludes zero, but n=5, multiple endpoints, archived-evidence audit still open and no broad/general superiority claim is justified.

## Exploratory descriptive contrasts — Q-AHBN2 minus other methods

Paired mean delivery differences and two-sided 95% paired t-CIs; report as supplementary context, not winner rankings:

| Comparator | Mean delivery difference | 95% paired CI |
|---|---:|---|
| Gossip | −0.465113 | [−0.695068, −0.235157] |
| Structured | +0.330271 | [+0.103956, +0.556585] |
| DC-SoC | +0.004481 | [−0.658489, +0.667450] |

**Material heterogeneity:** DC-SoC delivery alternates across seeds (approximately 0.089, 0.887, 0.089, 0.887, 0.085), with SD 0.438; a simple average is insufficient to characterize its behavior and a superiority interpretation against DC-SoC is unsupported. Its all-zero reported duplicate counts must also be checked against the metric definition and trace provenance rather than interpreted as unequivocal absence of duplicate traffic.

## Validity and remaining checks (no algorithm modification)

1. **Archive content audit OPEN:** Fetch/parse each of 25 `metrics.json` and `run_manifest.json`, reconcile exact numeric values and seed/method IDs, confirm identical per-seed topology/source/target-selection hash, workload, planned/actual churn, and independent protocol invariants. Check all `experiment_exit_status.txt`, `cleanup_status.txt`, and namespace evidence.
2. **Reproducibility/integrity OPEN:** Confirm each root's Git commit and immutable image digest against 25 recorded manifests and per-pod `imageID`; produce SHA256 manifest and completeness register. File presence alone is not hash verification.
3. **Timing and event definitions OPEN:** Inspect actual injection timing, live churn and peer maintenance logs. Gossip seed44 reports recovery event1 time 27.44 s while unrecovered observations are censored at 18 s, with message `m77` also used for event2. Explain observed event anchors and recovery definition without retroactively modifying outcomes.
4. **Q-learning trace interpretation OPEN:** Verify Q-AHBN2 decision/action, reward and realized fanout traces against frozen semantics. No performance-conditioned run exclusion or parameter changes.
5. **Final D8 scientific release HOLD:** Results here are preliminary computations from executed log values. Only close after independent record-level verification and discrepancy resolution. Any exclusion requires independent evidence under K4; low delivery is never an invalidity reason.

**Environment separation:** GKE K8s-VAL-Q/Exp13-Q-K8s is an implementation-valid counterpart, **not** a literal numerical replication of ControlSim.

**Editorial status:** *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is submitted to the *Journal of Cloud Computing* and **under peer review**; no DOI, acceptance or publication is claimed. Do not insert these provisional results into the manuscript as final.

## Additional five-root provenance cross-check

Read all five Drive-root `git_commit.txt` files: each reports **`6433f7429e0342df44c272b236423c65203a9136`**. Read all five Drive-root `expected_image_digest.txt` files: each reports **`sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`**. Thus the *recorded root-level* commit and expected image digest are consistent across seeds 42–46 (**root metadata parity PASS**). This does **not** yet verify the actual per-pod runtime `imageID`, manifest contents or source binary integrity.
