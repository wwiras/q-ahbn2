# D8-A — Independent offline evidence reconciliation (20 October 2026)

**Recommendation: PARTIAL. All 25 coordinates have independently reconstructed primary metrics. No primary-metric contradiction or performance-based exclusion was found. Recovery-window interpretation and defined provenance comparisons remain open.** This is an evidence-content decision, not final scientific validation or manuscript release.

## Authority and scope

Control/code: `wwiras/q-ahbn2`, local committed `origin/main` snapshot `ca4415ba5145d18a342497b549d42c26f68d557a`. Thesis control remains `wwiras/MUM_FIT_ThesisWira`; no thesis control or manuscript file was edited. Canonical observations are the Google Drive RO4 archive, locally mirrored under `output/evidence/`. This audit used that mirror, not uncommitted analysis reports. No network, cluster commands, spending, reruns, algorithm changes or evidence writes occurred. Remote freshness and full direct Drive byte comparison are not claimed.

Only these roots were selected: seed42 `20261020T032934Z-K5Q-formal`; seed43 `20261020T035637Z-K5Q-formal`; seed44 `20261020T041621Z-K5Q-formal`; seed45 `20261020T043745Z-K5Q-formal`; seed46 `20261020T045636Z-K5Q-formal`. Each contributes Gossip, Structured, DC-SoC, AHBN and Q-AHBN2. Generated configurations for other seeds are supporting files, not extra runs. The earlier `20261020T023432Z-K5Q-formal` attempt and smoke evidence remain outside scope and untouched.

## Reproducible method and evidence

Run from the repository root:

```sh
python3 gke/scripts/audit_d8_a_offline.py --output-dir docs/stages/d8_a_20261020
python3 gke/scripts/audit_d8_i1_sha256.py --output-dir output/d8_a_i1_confirmation
python3 -m unittest discover -s tests -p 'test_d8*.py' -v
```

The independent reconstruction uses only Python standard-library code; it does not call the original validator, which writes evidence. Measurement definitions were read from committed `gke/app/k7_exp11_tools.py`, particularly `load_jsonl`, `active_at` and `validate_run`. Its SHA256 is `2862f8b6dfce5ae9f43808ae05e486d0a3d8c64ab9f557df0dda32d93a5f49e7`, identical at recorded execution source `6433f7429e0342df44c272b236423c65203a9136` and the audit base. This establishes the reviewed source definition, not proof of binary equivalence.

Derived artifacts are in [d8_a_20261020](d8_a_20261020/): `audit.csv` and `audit.json` (25 rows), `inventory.json` (paths/current SHA256), `preliminary_comparison.json` (100 exact archived-versus-reported comparisons), `discrepancies.json`, `timing_observations.jsonl`, `provenance.json`, `execution.log`, `tests.log` and `i1_sha256_summary.json`. These contain derived observations and fingerprints, not a copy of the evidence corpus. The script fingerprint and UTC execution timestamp are recorded in provenance. The containing Git commit identifies the final deliverable version.

## Verified findings

- All 600 expected primary files and 320 supporting research files are readable and SHA256-hashed. Three `.DS_Store` files are separately classified. The existing revised D8-I1 scanner independently confirms 920 research files, zero missing/read-error/EXTRA files, and three same-day reference matches. This closes the previously pending revised-classifier execution check only.
- All 25 manifests and metrics agree on seed/method/run identity. Workload is 240 messages at a planned 0.4 s grid; manifests specify four churn offsets +1/+26/+51/+76 s and targets 0/5/10/15. Topologies report N=20, BA(m=2); same-seed methods share adjacency, source and target-selection identity. Target artifact hashes are recomputed. Archived generated topology and configuration copies are checked against each run. Structured's implementation strategy is `cluster`, the explicit committed mapping; it is not a method mismatch.
- All 25 root commit records equal `6433f7429e0342df44c272b236423c65203a9136`. Expected digest is `sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`. Every recorded peer runtime imageID matches that digest; snapshots contain 20 ready peer containers per run. These are snapshot observations, not continuous readiness evidence or a reproducible image-build attestation.
- Experiment, cleanup, namespace cleanup and Helm cleanup exit records are zero; cleanup status is PASS in all 25 runs. Namespace deletion text is present and namespace-check error files are empty. Controller pod phases are Succeeded. Each seed terminal records five K7 validator PASS results. Execution success, cleanup success, protocol checks and scientific validity remain separate judgments.
- All four primary metrics, F_attempt, F_success and all 100 recovery results reconstruct exactly from archived merged logs under the committed definitions. Archived opportunity denominators/counts also match. All 240 source-injection records and 240 controller-injection records per run are present after exact-record deduplication. Planned grids meet the recorded 1 microsecond tolerance. No value was imputed, replaced or excluded.
- The merged event set equals the union of controller, streaming peer and final snapshot records. Overlap is expected: `run_k7_experiment.sh` concatenates these sources. Exact JSON record deduplication is required; counting concatenated lines would inflate observations. Deduplication preserves events with different timestamps or payloads. It cannot establish that unlogged events never occurred.
- All 100 per-coordinate preliminary primary values agree within their displayed precision. Exact numeric differences, including seed42 rounding, are retained in `preliminary_comparison.json`. The cross-check covers committed D7-F seed42–45 tables and the D8-A/B seed46 table. The earlier five-seed aggregate report remains historical and provisional; no new D8-C statistics were produced.

## Measurement definitions and interpretation

Delivery is the sum of unique active-peer deliveries divided by the sum of active-peer opportunities at each source `message_injected` timestamp. Availability follows recorded pod-unavailability and rejoin events, not an inferred state from empty logs. A peer active at injection may count if its reception is logged later. This matches the executed calculation; it does not independently validate that this availability model is the best scientific estimand.

Propagation delay is the mean, over injected messages with receptions, of latest `received_new.ts` minus source injection timestamp, in seconds. It is not a mean of all peer latencies. Duplicates count deduplicated `received_duplicate` records. Total forwards and F_success count `forward` records; F_attempt counts `k7_forward_attempt` records. The audit verifies these recorded event estimands, not an independent packet capture or all physical network traffic. In particular, DC-SoC's zero duplicate metric is not proof of zero duplicate wire traffic.

Recovery is the first full-delivery opportunity injected after each rejoin. The executed search scans subsequent opportunities without an 18 s upper bound and does not stop at the next churn event. If no candidate exists, the stored record is censored at the topology settle time, 18 s. Therefore recovered values greater than 18 s and repeated message IDs across joins can follow the code. They are not automatically corrupt records. They do expose an unresolved observation-window/censoring interpretation.

For Gossip seed44, event1 is `27.438531398773193` s and event2 is `2.982052803039551` s, both anchored to message `m77`. Both reconstruct exactly. Events3/4 remain unrecovered and censored at 18 s. No censor value was converted to a recovery time, and unrecovered observations remain in the audit table. D8-B must determine whether the labels and observation horizons support the intended interpretation before recovery comparisons.

## Timing handoff and discrepancies

`timing_observations.jsonl` preserves each controller injection's planned/actual start/end, lateness and ACK status; leave/unavailability/rejoin records; infrastructure-ready/gRPC timestamps; rejoin notifications; all recovery outcomes; and per-rejoin summaries of later forwarding attempts involving the target and peer-availability records. Each summary names the source log. Original neighbor updates and other events remain in the fingerprinted logs for D8-B; the audit does not claim a complete independent reconstruction of neighbor-state propagation or causal ordering across distributed clocks.

The discrepancy register records the recovery-definition ambiguity at every run coordinate and campaign-wide administrative limits. No primary-metric contradiction was found. Low Structured/AHBN results and alternating DC-SoC results remain observations. Timing and neighbor-state interaction is a hypothesis requiring timestamp-level D8-B verification; neither an algorithm defect nor a harmless timing explanation is established here.

## Provenance boundaries and stash

There is no trusted execution-time per-file SHA256 baseline for any of the 920 research files. Current hashes and three same-day Drive comparisons do not prove unchanged bytes since execution. Archived root `git_status.txt` files are fingerprinted but not treated as proof that every executed source file matched the recorded commit. Runtime image identity is verified from pod snapshots; source-to-image build reproducibility remains outside this check.

`stash@{0}` remains `0b396448451ce35b41778466b29588e9290eefa9`. Read-only Git inspection found its tracked tree identical to its first parent `566bdfa3f00825ccfee57a5eb19fe3ec6f86eb0d`; no untracked third parent exists. Compared with the local committed snapshot, the relevant D8-I1 reports differ by later committed additions: inventory +9 lines, SHA256 report +8 lines, documentation reconciliation +33 lines. No stashed content was applied or merged. Live GitHub equality remains unverified under the offline constraint.

The Q-AHBN2 manuscript remains under peer review at Journal of Cloud Computing, with no DOI; no manuscript findings or claims were changed.

## Gate criteria and next decision

PASS is not recommended: although primary content reconciliation is complete for 25/25 runs, the recovery-window interpretation and broader timing/neighbor-state verification remain incomplete, and live archive/remote comparisons are explicitly limited. HOLD is not recommended on present evidence: there is no demonstrated material contradiction preventing interpretation of the four recorded primary endpoints. PARTIAL distinguishes these verified observations from unresolved scientific interpretation.

Proceed next to **D8-B — Protocol Configuration and Experimental Timing Verification**, using the preserved timestamps and complete logs. Verify actual timing, neighbor-state updates, forwarding opportunities, clock assumptions and censor boundaries before causal explanations or downstream recovery inference. D8-C paired statistics, D8-D fanout source verification, D8-E supported exploratory fanout distributions and D8-F conclusions remain later controlled gates. No rerun or manuscript change is authorized by this report.
