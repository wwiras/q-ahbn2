# D8-A/B — Formal GKE Evidence Reconciliation and Provisional Statistics (2026-10-20)

**Status:** D7-F EXECUTION 25/25 REPORTED / D8 EVIDENCE AUDIT PARTIAL / STATISTICAL INTERPRETATION PROVISIONAL.

## Authority
- Code and control: `wwiras/q-ahbn2`.
- Experiment evidence: Google Drive q-ahbn2 `output/evidence/`.
- Frozen campaign: seeds 42–46, five methods (Gossip, Structured, DC-SoC, AHBN, Q-AHBN2), 25 method×seed coordinates. N=20, BA(m=2), 240 messages, planned interval 0.4 s, churn offsets +1/+26/+51/+76 s, target peers 0/5/10/15.
- Evidence roots: `20261020T032934Z-K5Q-formal` seed42; `20261020T035637Z-K5Q-formal` seed43; `20261020T041621Z-K5Q-formal` seed44; `20261020T043745Z-K5Q-formal` seed45; `20261020T045636Z-K5Q-formal` seed46.
- Seed42–45 records are in the repo's dated D7-F stage notes. Seed46 Drive contains five method folders each with `metrics.json`, `run_manifest.json`, archived controller/pod/churn logs, and exit/cleanup evidence; terminal.log finishes `K5-Q FORMAL SEED BATCH PASS seed=46`.

## Seed46 archived primary metrics
| Method | Delivery | Delay (s) | Duplicates | Forwards |
|---|---:|---:|---:|---:|
| Gossip | 0.8631424989552863 | 0.07778095602989196 | 2563 | 3905 |
| Structured | 0.08154686843211434 | 0.0032769441604614258 | 0 | 152 |
| DC-SoC | 0.08520934146854618 | 0.010144373774528504 | 0 | 169 |
| AHBN | 0.2319932998324958 | 0.022698521614074707 | 582 | 878 |
| Q-AHBN2 | 0.578980490874764 | 0.053957773248354594 | 862 | 2538 |

## Preliminary paired delivery calculation (Q-AHBN2 minus AHBN)
- Seeds 42–46 AHBN: 0.1328436516, 0.1389121338912134, 0.31206715634837356, 0.18777475402972577, 0.2319932998324958.
- Q-AHBN2: 0.3362646566, 0.1311715481171548, 0.4701695624869165, 0.5417451349654739, 0.578980490874764.
- AHBN mean approximately 0.2007182; Q-AHBN2 mean approximately 0.4116663.
- Paired mean difference approximately +0.2109481 (+21.09 percentage points); two-sided 95% Student-t interval approximately [0.0250754, 0.3968207] (+2.51 to +39.68 percentage points); n=5 seeds, df=4.
- Differences by seed approximately [0.203421, -0.007741, 0.158102, 0.353970, 0.346987].
- Positive delivery contrast in 4/5 seeds; seed43 negative must be preserved. This is a bounded preliminary observation, NOT final superiority, and the joint trade-off requires delay/duplicates/forwards.

## D8 unresolved checks
1. Verify all 25 original manifests and exit/cleanup statuses against pinned source/image and frozen seed/method configuration; inspect per-pod deployed image digest and independently verify each archive's SHA256.
2. Audit workload, churn timestamp fidelity, target mapping, maintenance invariants, Q-update and decision/reward traces without performance-based validity filtering.
3. Reconcile seed44 Gossip recovery_time_s=27.44 with 18 s censoring convention and repeated recovery message id m77. Keep the original records and classify only from underlying timestamps.
4. Preserve the observed DC-SoC seed variation (high in 43/45, low in 42/44/46), without post-hoc exclusion.
5. Complete four-metric per-method means/SD/95% t-CIs, same-seed paired AHBN/Q-AHBN2 contrasts and machine-readable reproducible summaries. Do not mix ControlSim and GKE datasets.
6. Verify presence and validity of any 25-coordinate matrix manifest: five distinct timestamped seed roots are not a single automatically verified campaign manifest.

No algorithm changes, reruns or exclusions are authorized on performance grounds. No scientific closure until D8 independently passes.

**Publication boundary:** RO4 Q-AHBN2 manuscript submitted to *Journal of Cloud Computing* (Springer), currently **under peer review**, without DOI. Neither accepted nor published.
