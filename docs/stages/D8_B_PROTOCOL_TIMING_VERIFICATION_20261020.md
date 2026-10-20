# D8-B — Independent offline protocol and timing verification

**Date:** 20 October 2026
**Recommendation:** **PARTIAL**
**Scope:** Read-only verification of the frozen 25-run K5-Q experiment and its archived records. No GKE operation, experiment rerun, algorithm change, evidence rewrite, run exclusion, thesis edit, or manuscript edit was performed.

## Decision

The frozen configuration, run identity, workload, topology, churn targets, source/image records, exit records, and timing checks reconcile for **25/25 formal runs**. The independent audit reconstructs all **100 recovery-event records** and all **6,000 controller injection records**. It finds no confirmed protocol violation and no reason to exclude a run. Low delivery observations remain included.

D8-B is **PARTIAL**, not PASS, because recovery-event records do not have an event-relative censoring rule, and the archive cannot establish cluster-wide neighbour-state convergence or show that it caused dissemination outcomes. These limitations affect secondary recovery interpretation and causal explanations; they do not contradict the four primary endpoint records or the frozen 25-run schedule.

## Evidence labels

- **Observed** means directly present in the frozen source, archived manifest/configuration, or runtime records.
- **Inferred** means consistent with those records but requiring interpretation or assumptions.
- **Unresolved** means the archive does not contain enough evidence to decide.

The audit used the five formal timestamped roots in `output/evidence/`, not generated configurations or the separate smoke/remediation attempts. Paths below are relative to the repository root.

## B1 — Recovery definition and censoring

### Implemented calculation

**Observed:** The frozen recovery definition is “first post-rejoin opportunity full delivery to active ready peers” in `gke/experiments/k5_q_formal.yaml`. In `gke/app/k7_exp11_tools.py`, the validator builds delivery opportunities and, for each `churn_rejoined` record, selects the first later injection opportunity with full delivery. It then reports the completion time of that message minus the rejoin-event timestamp (`k7_exp11_tools.py`, lines 365–376).

The search:

1. Starts at the logged `churn_rejoined.ts`, which follows replacement-pod readiness and the controller’s gRPC liveness check.
2. Uses later message injection opportunities and the full-delivery condition.
3. Does **not** stop at 18 seconds.
4. Does **not** stop at the next churn event.
5. Sets `censored_at_s` to `topology.settle_time` only when no full-delivery opportunity is found.

### What 18 seconds means

**Observed:** `settleTime: 18.0` is in the frozen K5 configuration. The runtime use in `gke/app/controller_shared.py` is a sleep after the message workload, immediately before `run_finished` (line 794). Across the 25 runs, the measured interval from final `StartRun` completion to `run_finished` is **18.000281–18.002177 s**.

Therefore, 18 seconds is the **run-level post-workload settle delay**, not a timer begun separately at each peer rejoin. The recovery calculation copies that value into each unrecovered event’s `censored_at_s`; it does not record a measured event-relative censor timestamp. Periodic recovery-probe records are absent. The controller’s `grpc_alive_time` is a separate replacement-health check, not a dissemination recovery check.

The remaining injection-opportunity span varies by event. Across the 100 records, it ranges from **12.757994 to 93.312141 s**. **Twenty unrecovered event-4 records** have less than 18 seconds of later injection opportunities. The 18-second run-level sleep does not create additional message-injection opportunities for the recovery search.

### Seed44/Gossip m77

The independent reconstruction matches the archived metrics exactly:

| Event | Target | Rejoin event time | First full-delivery message | Message completion | Recorded recovery |
|---|---:|---:|---|---:|---:|
| 1 | 0 | 1792469844.774864 | m77 | 1792469872.213395 | 27.438531 s |
| 2 | 5 | 1792469869.231343 | m77 | 1792469872.213395 | 2.982053 s |

The m77 injection was at **1792469872.111156**. All 20 active peers received it; peer 0’s `received_new` record is at 1792469872.189118. Event 2’s leave began after event 1’s rejoin and before this m77 observation. This is why the same message can satisfy both event searches.

**Observed:** The 27.438531-second number is a later full-delivery observation measured from event 1’s rejoin, not the time for the replacement pod to become Ready or gRPC-alive. The code permits the same message identifier to anchor multiple events; the duplicate m77 association is present in the seed44/Gossip metrics and logs.

**Interpretation:** The m77 observation is a real late full-delivery record under the implemented calculation. Its attribution as an isolated event-1 recovery is ambiguous because event 2 intervened and the same message also anchors event 2. It must not be described as a 27.44-second Kubernetes recovery time.

### Recovery disposition

- **Actual late observation:** Yes. m77 completes 27.438531 seconds after event 1’s `churn_rejoined` timestamp.
- **Event-anchor ambiguity:** Yes. m77 is assigned to both events 1 and 2; event 2’s leave occurs before event 1’s attributed full delivery.
- **Measurement-definition inconsistency:** Yes. The 18-second run-level settle delay is written into an event-level censor field without defining or measuring an event-relative censor boundary.
- **Confirmed protocol violation:** None established. The frozen recovery definition does not state an event-relative 18-second cutoff. The inconsistency limits the secondary recovery diagnostic; no value was changed, reclassified, or retrospectively censored.

All 100 recomputed rows, including the original 18-second labels, are in `docs/stages/d8_b_20261020/recovery_event_verification.csv` and `.json`.

## B2 — Experimental timing

### Message schedule

**Observed:** Each run has one controller epoch and 240 acknowledged `StartRun` calls. The actual planned timestamps equal `epoch + (message_index - 1) × 0.4 s` for all **6,000** records; maximum planned-grid error is **0 s**. Maximum difference between planned adjacent gaps and 0.4 s is **1.430511475 × 10⁻⁷ s**.

The independently calculated maximum injection lateness is **7.535934 ms** (seed 42, DC-SoC). This is exactly the maximum of `max(0, actual_injection_start_ts - planned_injection_ts) × 1000`, where start is when the controller begins the blocking `StartRun` gRPC call. It is **not** end-to-end message delay, network propagation delay, or evidence of neighbour-state synchronization. The call end and elapsed call duration are preserved separately.

The original controller implements an absolute schedule and does not shift subsequent planned times after a late call (`gke/app/k7_controller.py`, lines 112–135). Every individual planned and actual injection timestamp is in `message_injection_schedule.csv`.

### Churn, readiness, reachability, and end of run

**Observed:**

- Every run records one common epoch, four planned leave offsets **+1, +26, +51, +76 s**, and targets **0, 5, 10, 15**.
- All 100 leave dispatches are within **1.634360 ms** of their planned absolute times; all 100 unavailable, replacement, Ready, gRPC-alive, and rejoin records are present and ordered.
- All rejoin records report `COMPLETE`.
- Maximum observed interval from pod-unavailable to Ready is **28.202846 s**; maximum to controller gRPC-alive is **31.211582 s** (seed42/Gossip, event 1).
- Final injection completion is about **95.6 s** after each epoch. `run_finished` is about **113.6 s** after epoch, consistent with the separate 18-second post-workload settle.
- Pod snapshots, method/seed records, expected image digest, recorded runtime `imageID`, experiment exit status, cleanup status, controller pod phases, and seed-level K7 validator summaries pass the offline checks.

**Observed overlap:** In seed42/Gossip, event 2’s leave dispatch occurred before event 1’s rejoin. This is the only adjacent-cycle overlap in the 25 runs. **Inferred:** This is consistent with the written absolute schedule and the K7 implementation, which launches churn workers concurrently (`gke/app/k7_controller.py`, lines 176–186); the freeze does not require one target to rejoin before the next target leaves. It is retained as a realized condition, not treated as a violation or reason to exclude the run.

**Important distinction:** A Ready condition is a Kubernetes pod status. The `grpc_alive_time` is the controller’s GetStatus/liveness check to the replacement. Neither establishes that every peer can reach the replacement or has updated its local neighbor/availability state.

## B3 — Neighbour state, forwarding, and dissemination

The archive contains a static neighbor topology and per-peer `peer_availability` observations. Source code shows that these are local cache updates after forwarding failures or acknowledgements (`gke/app/recovery_availability.py`, lines 11–42). Forward attempts are separately emitted before the RPC in `gke/app/qahbn2_runtime.py` (line 146). Successful forwarding, duplicate acknowledgements, failed forwarding, and `received_new` records are distinct events.

There are **zero explicit cluster-wide neighbor-membership transition or convergence acknowledgements** in the 25-run logs. The controller’s replacement gRPC check is not a peer-to-peer reachability test. Cross-pod clock-skew bounds are also absent, so near-simultaneous events should not be assigned a causal order solely from small timestamp differences.

### Representative paired seed44 sequences

| Evidence | Gossip (higher observed delivery) | Structured (lower observed delivery) |
|---|---:|---:|
| Delivery ratio | 0.885870 | 0.081251 |
| Event-1 target | peer 0 | peer 0 |
| Pod unavailable | 1792469842.874730 | 1792470040.954943 |
| Replacement Ready | 1792469844.666851 | 1792470042.627493 |
| Controller gRPC-alive | 1792469844.759905 | 1792470042.641938 |
| Rejoin event | 1792469844.774864 | 1792470042.643103 |
| Post-rejoin attempts to/from target | 48 | 1 |
| Attempt outcomes recorded | 3 `forward`, 33 duplicate ACK, 12 failed | 1 failed |
| New-message deliveries to target after rejoin | 3 | 0 |

For seed44/Gossip event 1, the later m77 injection at 1792469872.111156 reached all 20 active peers by 1792469872.213395. For seed44/Structured, m77 was received only by the source peer (1 of 20); no full-delivery recovery anchor was found. These are timestamped observations, not evidence that Ready or local availability updates caused the difference.

### Check across the 25-run dataset

Across the 100 rejoin events, the logs show:

- Local peer-availability updates after rejoin in **70/100** events.
- Forward attempts to/from the target after rejoin in **68/100** events.
- At least one `received_new` delivery to the rejoined target in **56/100** events.
- Explicit neighbor-membership transition records in **0/100** events.

| Method | Mean observed delivery ratio (five seeds) | Rejoins with local availability updates | Rejoins with attempts | Rejoins with new delivery to target |
|---|---:|---:|---:|---:|
| Gossip | 0.876779 | 19/20 | 19/20 | 17/20 |
| Structured | 0.081396 | 5/20 | 5/20 | 3/20 |
| DC-SoC | 0.407186 | 6/20 | 4/20 | 0/20 |
| AHBN | 0.200718 | 20/20 | 20/20 | 16/20 |
| Q-AHBN2 | 0.411666 | 20/20 | 20/20 | 20/20 |

The low/high example is consistent with a broader difference in the presence of forwarding opportunities, but the records do not establish why those opportunities differ or prove a causal role for neighbor-state timing. Accurate injection timing alone does not show that neighbor synchronization completed before forwarding. Low delivery is not a protocol violation.

The full timestamped event sequences and per-event attempt/outcome/delivery summaries are in `neighbour_forwarding_analysis.json`.

## B4 — Frozen protocol and run validity

The independent matrix checks all 25 coordinates against the frozen K4/K5 records:

- Five methods (Gossip, Structured, DC-SoC, AHBN, Q-AHBN2) by seeds 42–46.
- N=20, Barabási–Albert, m=2; same-seed methods share adjacency, source, and target-selection identity.
- 240 messages on the 0.4-second absolute common-epoch grid.
- Four churn targets and offsets as frozen; no target is the message source.
- Recorded source commit `6433f7429e0342df44c272b236423c65203a9136` and expected image digest `sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`; pod snapshot image IDs match the expected digest.
- Structured’s recorded strategy is `cluster`; dynamic structural maintenance is enabled only for DC-SoC.
- Experiment and cleanup exits, controller phases, and five seed-level validator PASS records are consistent.

**Result:** 25/25 protocol matrices pass; no confirmed protocol violation was found. The checks validate recorded source/image identity, not reproducible source-to-image build equivalence. Final pod snapshots are not continuous readiness histories.

## Discrepancies and limitations

`discrepancy_register.json` records:

1. The recovery censor field uses a run-level settle value, not an event-relative censor duration.
2. Seed44/Gossip m77 is a reused anchor across an intervening churn event.
3. Archived logs do not establish cluster-wide neighbor convergence or causal timing.
4. No trusted execution-time file-hash baseline or fresh Drive/GitHub comparison is available in this offline audit. Current local fingerprints cannot prove historical byte integrity or remote freshness.

These points do not change original metrics, discard unfavorable outcomes, or establish an invalid run.

## Reproducibility and tests

Run from the repository root:

```sh
python3 gke/scripts/audit_d8_b_offline.py \
  --output-dir docs/stages/d8_b_20261020
PYTHONPATH=gke/app python3 -m unittest discover -s tests -p 'test_d8*.py' -v
```

The auditor is standard-library-only, reads but does not modify `output/evidence/`, and writes derived results separately. The D8-focused regression set passed **17/17**. A full-suite run was attempted: **152 tests ran with two import errors** because the available runtime lacks `grpc`; the system Python also lacks `yaml`. No packages were installed because this gate was offline. The full output, including configured reruns, is preserved in `full_regression.log`.

Derived outputs:

- `protocol_timing_matrix.csv` and `protocol_timing_matrix.json` — all 25 runs.
- `message_injection_schedule.csv` — all 6,000 planned/actual controller injection records.
- `recovery_event_verification.csv` and `.json` — all 100 event observations.
- `neighbour_forwarding_analysis.json` — all-run summaries and timestamp-grounded representative sequences.
- `discrepancy_register.json`, `summary.json`, `execution.log`, `tests.log`, and `full_regression.log`.

## Next gate

**D8-B: PARTIAL.** No confirmed scientific protocol violation requires a run exclusion, measurement modification, or rerun, so no such action was taken. Keep the primary observations intact. Before making recovery-based comparative or causal claims, define and prospectively validate an event-relative recovery observation/censor rule; do not retroactively recensor these records. The neighbor-state timing explanation remains unresolved and must not be stated as established.
