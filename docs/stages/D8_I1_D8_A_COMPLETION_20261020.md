# D8-I1 completion and D8-A independent reconciliation — 20 October 2026

## Decision

- **D8-I1 current-state file-read/hash acceptance: PASS.** The hydrated archive has 920/920 research files readable and hashed; three `.DS_Store` files are reported separately; no missing files, read errors, or extra research files remain.
- **Historical byte integrity: UNVERIFIED.** No trusted execution-time per-file checksum baseline was found. The current hashes and three same-day Drive reference matches do not establish that evidence bytes are unchanged since execution.
- **D8-A: PARTIAL.** All 25 run coordinates reconcile on primary metrics and run/protocol content checks. No performance-based exclusion or primary-metric contradiction was found. Recovery-window interpretation, historical checksum provenance, and remote/Drive freshness remain open.
- **D8-B:** D8-A supports proceeding to a bounded protocol/timing verification stage, but does not release timing or causal conclusions. The low-delivery timing/neighbour-state explanation is not established by the available observations.

The requested `D8_I1_D8_A_PARALLEL_DECISION_20261020.md` was not present in this checkout. This report therefore uses the available D8-I1 reports and the local D8-A materials; no online sources were consulted.

## D8-I1 administrative checks

### Hydration and final scan

The target file,
`output/evidence/20261020T041621Z-K5Q-formal/runs/seed44/ahbn/pod_readiness_evidence.txt`,
exists locally at 21,376 bytes. `ls -lO` showed no `dataless` flag (`flags=-`); no Finder action or file replacement was needed.

The requested command, `venv/bin/python gke/scripts/audit_d8_i1_sha256.py`, completed at 2026-10-20 07:51:39 UTC (15:51:39 +08:00). The audit used repository HEAD `ca4415ba5145d18a342497b549d42c26f68d557a`; scanner SHA256 was `7ae8c87d06d2289ba5eec63b9c0dd886ac78cbc12a5f3f17720bca1d1d2fca83`.

| Final scan measure | Result |
|---|---:|
| Formal roots / seed-method coordinates | 5/5 / 25/25 |
| Primary research files | 600/600 hashed |
| Supporting research files | 320/320 hashed |
| Research files discovered / hashed | 920 / 920 |
| `.DS_Store` Finder metadata | 3 separately listed, not counted as research files |
| Missing / read errors / research extras | 0 / 0 / 0 |
| Empty files | 25 `namespace_check_error.txt` files, hashed as empty |
| Same-day Drive fingerprints | 3 matches |
| Trusted execution-time SHA256 references | 0 |
| Comparison classification | 920 `BASELINE_UNAVAILABLE`; 0 `MATCH` or `MISMATCH` against a trusted execution-time baseline |

The machine-readable summary reports `CURRENT-STATE BASELINE COMPLETE`. This means the current scoped research corpus was readable and fingerprinted; it is not a historical integrity finding.

### Earlier scan records and unresolved chronology

The retained D8-I1 report records two 919/920 scans at 2026-10-20 06:26:05Z and 06:28:16Z, on revision `57511049a27db0034c5fefa29d5daef1e6207dc5`, using scanner SHA256 `d7446e0c5456c9df50f47b7c90182505731e05ddfb2ff114fd485202eaa4841e`. Both reports attribute the unread file to the seed44/AHBN cloud placeholder still marked `dataless`.

The committed follow-up records an operator-reported 07:10:44Z post-hydration run: 600 primary plus 320 supporting research files read, with three `.DS_Store` files additionally counted by the then-unmodified scanner (923 total hashed entries and an `EXTRA` classification). Its raw execution log is not present in the reviewed output.

The audit files already present in `output/d8_integrity/` when this task began were timestamped 15:16 +08:00. Their summary/log contents were not captured before the required rerun replaced them with the successful 15:51 +08:00 run. Thus the specific later 919/920 scan referenced in the task cannot be independently assigned a reliable timestamp, script revision, or error cause from surviving raw output. The retained reports do establish the earlier 06:26/06:28 919/920 scans, the 07:10:44Z operator-reported post-hydration scan, and this session's fresh complete scan. The gap in the later scan's raw provenance is recorded, not silently reconciled.

The final D8-I1 files are preserved outside the evidence roots in `output/d8_integrity/`: `sha256_current.csv`, `sha256_current.json`, `sha256_comparison.csv`, `sha256_summary.json`, `audit_execution.log`, `baseline_provenance.md`, and the resume journal. No source evidence was edited.

## D8-A scope, method, and provenance

The reconciliation independently read the five formal roots for seeds 42–46 and methods Gossip, Structured, DC-SoC, AHBN, and Q-AHBN2. It did not access a cluster, make network calls, rerun experiments, or invoke the evidence-writing validator. The existing untracked script reconstructs metrics from archived logs and cross-checks manifests, metrics, topology/configuration, target selection, controller and peer streams, snapshots, exit/cleanup records, and terminal validator results. Exact duplicate JSON records in merged logs are removed; distinct records are retained.

Reproducible commands:

```sh
venv/bin/python gke/scripts/audit_d8_a_offline.py \
  --output-dir output/d8_a_independent_20261020
venv/bin/python -m unittest \
  tests.test_d8_i1_sha256_audit tests.test_d8_a_offline -v
```

The D8-A execution finished at 2026-10-20 07:56:47Z. Provenance records audit-base HEAD `ca4415ba5145d18a342497b549d42c26f68d557a`, formal-run source commit `6433f7429e0342df44c272b236423c65203a9136`, and script SHA256 `e4c79bb4b618af4f5aeec3beca8dc01a88791aa2cb2597ece7bbf97f390f8f70`. The 25-run audit content checks passed 25/25; the 600 primary and 320 supporting files were readable. The code, test, and D8-A report files were already untracked when inspected; this report does not claim they are committed.

Machine-readable derived outputs and execution logs are in `output/d8_a_independent_20261020/` (outside `output/evidence/`): `audit.csv`, `audit.json`, `inventory.json`, `preliminary_comparison.json`, `discrepancies.json`, `timing_observations.jsonl`, `provenance.json`, `execution.log`, and `tests.log`. These derived files do not replace or modify the source evidence.

## Reconciled 25-run table

`F_success` matched the recorded `forward` count in every run; `F_attempt` is reported separately. Recovery is shown as recovered/censored events out of four. The table preserves low outcomes without treating them as invalid.

| Seed | Method | Delivery ratio | Propagation delay (s) | Duplicates | Forwards / F_success | F_attempt | Recovery (recovered/censored) | Max injection lateness (ms) |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 42 | Gossip | 0.863723 | 0.096576 | 2200 | 3848 | 6074 | 1/3 | 1.980 |
| 42 | Structured | 0.081132 | 0.003479 | 0 | 152 | 153 | 0/4 | 5.946 |
| 42 | DC-SoC | 0.088791 | 0.012492 | 0 | 188 | 197 | 0/4 | 7.536 |
| 42 | AHBN | 0.132844 | 0.009311 | 146 | 397 | 576 | 0/4 | 0.820 |
| 42 | Q-AHBN2 | 0.336265 | 0.028416 | 403 | 1380 | 1854 | 0/4 | 4.798 |
| 43 | Gossip | 0.885242 | 0.068797 | 4322 | 4011 | 8370 | 0/4 | 1.126 |
| 43 | Structured | 0.081791 | 0.004161 | 0 | 152 | 153 | 1/3 | 0.963 |
| 43 | DC-SoC | 0.886745 | 0.271862 | 0 | 4004 | 4016 | 0/4 | 1.134 |
| 43 | AHBN | 0.138912 | 0.009297 | 200 | 432 | 671 | 0/4 | 0.891 |
| 43 | Q-AHBN2 | 0.131172 | 0.009773 | 232 | 391 | 641 | 0/4 | 1.205 |
| 44 | Gossip | 0.885870 | 0.065771 | 3089 | 4014 | 7129 | 2/2 | 1.247 |
| 44 | Structured | 0.081251 | 0.004801 | 0 | 152 | 153 | 0/4 | 3.884 |
| 44 | DC-SoC | 0.088600 | 0.011168 | 0 | 184 | 197 | 0/4 | 4.683 |
| 44 | AHBN | 0.312067 | 0.030500 | 531 | 1257 | 1809 | 0/4 | 0.793 |
| 44 | Q-AHBN2 | 0.470170 | 0.044196 | 767 | 2020 | 2842 | 0/4 | 1.830 |
| 45 | Gossip | 0.885917 | 0.137712 | 5222 | 4014 | 9270 | 2/2 | 2.481 |
| 45 | Structured | 0.081257 | 0.002668 | 0 | 152 | 153 | 1/3 | 2.327 |
| 45 | DC-SoC | 0.886583 | 0.159694 | 0 | 4008 | 4016 | 0/4 | 1.523 |
| 45 | AHBN | 0.187775 | 0.013391 | 249 | 666 | 962 | 0/4 | 5.665 |
| 45 | Q-AHBN2 | 0.541745 | 0.049498 | 776 | 2362 | 3191 | 0/4 | 0.915 |
| 46 | Gossip | 0.863142 | 0.077781 | 2563 | 3905 | 6505 | 2/2 | 0.800 |
| 46 | Structured | 0.081547 | 0.003277 | 0 | 152 | 153 | 1/3 | 6.317 |
| 46 | DC-SoC | 0.085209 | 0.010144 | 0 | 169 | 178 | 0/4 | 3.336 |
| 46 | AHBN | 0.231993 | 0.022699 | 582 | 878 | 1531 | 0/4 | 1.049 |
| 46 | Q-AHBN2 | 0.578980 | 0.053958 | 862 | 2538 | 3453 | 0/4 | 0.919 |

Additional checks passed for all coordinates: run/seed/method IDs; 240-message workload and planned 0.4 s grid; four scheduled churn targets; seed/topology/configuration and target-selection consistency; experiment and cleanup exit records; cleanup status; namespace evidence; controller completion; and five terminal validator PASS results per root. Controller records, peer stream, final snapshots, merged logs, and archived opportunity counts were cross-checked. Planned injection-grid error was 0 s in each run. Maximum recorded injection lateness across all runs was 7.536 ms.

## Timing, neighbour-state, and recovery findings

The evidence does **not** establish that timing or neighbour-state effects explain low delivery. Controller logs show the planned injection grid was met, with observed per-run maximum lateness of 0.793–7.536 ms. Merged logs contain actual `neighbor_unavailable_observed` and `peer_availability` events; the former occurs after recorded forwarding failures. Their presence confirms some local observations, not a complete neighbour table at each injection or a causal link from a stale/updated neighbour state to every undelivered opportunity. No inference that the low Structured/AHBN outcomes are harmless timing effects, or that they indicate an algorithm defect, is justified here. Low delivery remains an observation.

The independent recovery reconstruction follows the archived executable metric logic: for each rejoin, it searches forward for the first later full-delivery opportunity without an 18 s upper bound; if none exists, the audit reports censoring at the topology's 18 s settle time. Across 100 recovery records, 10 were classified recovered and 90 censored. Seed44/Gossip event 1 reconstructs as 27.438531 s and event 2 as 2.982053 s, both anchored to `m77`; events 3 and 4 remain censored at 18 s. This matches the recorded computation but leaves the meaning of the nominal 18 s observation horizon, post-rejoin search, and reused message anchor unresolved. These recovery records should not support a cross-method recovery claim until D8-B resolves the contract/interpretation.

## Discrepancy register

The machine-readable register is `output/d8_a_independent_20261020/discrepancies.json` (27 entries):

| Register group | Count | Finding / impact | State |
|---|---:|---|---|
| Per-run recovery interpretation | 25 | Recovery search is not bounded by 18 s although no-result censoring is recorded at 18 s; D8-B must determine the intended horizon/estimand. No primary-metric mismatch was detected. | Open |
| Historical integrity | 1 | No trusted execution-time per-file checksum baseline for the 920 research files. | Documented limitation |
| Remote/source freshness | 1 | Offline comparison cannot establish live GitHub or complete Drive-to-local freshness/parity. | Open |
| Prior later 919/920 raw scan provenance | 1 additional report-level limitation | Prior 15:16 +08 output contents were replaced by the required rerun before their summary/log content was captured; the exact later scan cannot be independently reconciled from surviving raw outputs. | Open |

## D8-I1 commit, test, stash, and worktree review

- Branch was `main`, tracking `origin/main`, at `ca4415ba5145d18a342497b549d42c26f68d557a`.
- Commit `57511049a27db0034c5fefa29d5daef1e6207dc5` adds the offline SHA256 scanner and focused tests. The reported 919/920 execution used the scanner version before the later `.DS_Store` classification fix. `git show --check` reported no whitespace errors.
- Commit `5cb6880585790915fee5c5301596f68976e9dd47` changes only the two D8-I1 reports to document the unresolved placeholder and scan provenance; no evidence or executable code changes. `git show --check` reported no whitespace errors.
- The focused D8-I1 and D8-A suites passed **14/14 tests**. D8-I1 scanner SHA256: `7ae8c87d06d2289ba5eec63b9c0dd886ac78cbc12a5f3f17720bca1d1d2fca83`; D8-A script SHA256: `e4c79bb4b618af4f5aeec3beca8dc01a88791aa2cb2597ece7bbf97f390f8f70`.
- `stash@{0}` (`0b396448451ce35b41778466b29588e9290eefa9`) was inspected read-only and not applied, dropped, or modified. Its working-tree tree matches its first parent `566bdfa`; its index parent contains changes to the two D8-I1 reports. There is no third/untracked parent.
- No commits were created or pushed. The worktree has pre-existing untracked D8-A artifacts; a `.vscode/settings.json` also appeared in the final status and was left untouched.

## Gate and limitations

The content checks justify D8-B as the next bounded verification step, focused on protocol timing, injection lateness, churn/rejoin ordering, and the recorded neighbour/availability observations. They do not release D8-B conclusions or repair the recovery-window ambiguity. Preserve all 25 outcomes, including the low-delivery values.

The RO4 manuscript remains under peer review at the *Journal of Cloud Computing*. It has no DOI and is not described as accepted or published. No thesis/manuscript claims, algorithms, or experimental evidence were changed.
