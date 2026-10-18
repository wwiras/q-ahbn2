# P3G — Recovery Correction Implementation and Offline Regression

Date: 2026-10-18
Status: PARTIAL IMPLEMENTATION / OFFLINE TEST EXECUTION PENDING / GKE HOLD
Authority: P3E recovery requirements and P3F-M1 recommended GetStatus mechanism.
Scope: nonformal engineering correction, not a new scientific algorithm.

## Implemented on temporary branch
- `gke/app/recovery_availability.py`: separate locked unavailable set, failure generation, one in-flight probe per peer, identity/ready/alive/topology verification, no implicit clearing on structural rejoin, injected bounded status-call interface.
- `gke/app/test_recovery_availability_p3g.py`: 12 isolated unittest scenarios.
- Not yet wired to `gke/app/peer.py`; no runtime behavior changes; not merged to main.

## Critical outstanding engineering decisions
1. Wire only after reviewing all existing failure/success/duplicate paths and their observation semantics. Prevent double leave/join events.
2. Establish authoritative availability/rejoin trigger for all five strategies; a DC-SoC-only maintenance event is insufficient for AHBN and Q-AHBN2.
3. Implement the real existing `GetStatus` gRPC call with explicit deadline, peer-ID verification and generation guard; confirm topology permission from current runtime state.
4. Resolve concurrency/locking and telemetry before claiming runtime recovery.
5. Review feature-flag disabled baseline parity and rollback behavior.
6. Do not assume the existing timeout or retry settings are frozen. No retry or periodic polling in staged helper.

## Offline commands (researcher/local environment; not yet run)
```bash
python3 -m py_compile gke/app/recovery_availability.py gke/app/test_recovery_availability_p3g.py
PYTHONPATH=gke/app python3 -m unittest -v test_recovery_availability_p3g
```
Record exact Git commit, stdout/stderr, exit codes and SHA256 checksums.
Then perform P3E T01–T12 and P3F T13–T18 against integrated code, including controller parity and no probe-derived forwarding/duplicate/delivery/Q-reward changes.

## Gate decision
- Isolated helper and test-source staging: DONE on temporary branch.
- Local test execution: NOT RUN / UNVERIFIED.
- Full P3E/P3F regression matrix: NOT RUN.
- Integration with runtime: NOT STARTED.
- Smoke-test release: HOLD.
- D7-F: 0/25 HOLD; D8: HOLD.
- No GKE use, cloud spending, manuscript modification, or change to frozen scientific contracts.
- Original P3 evidence is immutable.

## 2026-10-18 — User local helper test report and staged runtime adapter

Researcher terminal reported successful `py_compile` and **12/12 isolated unittest PASS** on branch `work/p3g-recovery-offline`. This is user-supplied terminal evidence, not independently rerun by the assistant; full stdout/checksum archive pending.

A subsequent branch-only change stages `PeerState.request_recovery_check()` in `gke/app/peer.py` using existing `GetStatus`. `P3G_RECOVERY_ENABLED` defaults to off. The method is **not called by any lifecycle hook** and intentionally does **not** clear the runtime `unavailable_neighbors` set. Therefore **recovery is not fixed**, and this code is not ready for a smoke test.

Important outstanding defects/limitations of this staging adapter: the helper state is not yet atomically synchronized with the existing runtime set; each explicit call currently marks failure in helper state and thus must not be interpreted as final generation discipline; the membership check is only a necessary topology check, not full strategy-specific authorization; no production trigger exists. This must be corrected before enablement, and the real adapter requires offline fake-gRPC tests.

After pulling the latest branch, repeat syntax and unittest checks, then complete integrated T01–T18, concurrency and metric-invariance tests. **No live enablement, main merge, formal trials, or GKE spending authorized.**

## 2026-10-18 — Atomic transition staging

Branch-only code updates:
- `RecoveryAvailability` now accepts the existing unavailable-neighbor set as its shared backing store; transition methods hold an internal RLock and increment per-peer generation.
- `PeerState.forward_to_peer` routes successful/duplicate acknowledgements through `mark_neighbor_recovered`, and failed/rejected forwarding through `mark_neighbor_failed`, with one observation on actual set membership change.
- `request_recovery_check` no longer creates a synthetic failure generation; a successful, identity-matched, ready/alive, current-ticket GetStatus result removes the same shared exclusion and records a join observation. Default feature flag is off; no lifecycle trigger is wired.
- Three more unit cases staged: shared-set/ACK, stale in-flight check after ACK/new failure, failed probe preserving exclusion.

**Evidence limitation:** 12/12 earlier helper tests were reported by the researcher *before* these changes. The expanded 15-test suite and updated `peer.py` have **not yet been executed**. Atomicity is established for state *transitions via the manager*, but legacy unlocked membership reads and runtime scheduling require separate concurrency/behavioural audit. `GetStatus` peer membership check is not full strategy-specific eligibility validation. Probe trigger authority, frequency and timing remain unresolved. This is not a completed recovery fix or GKE release.

**Required offline checks:** syntax, 15 unit tests, integrated fake-gRPC lifecycle and metrics invariance, frozen parity, concurrency/stale-response tests, exact commit and hashes. All GKE/D7-F/D8 remain HOLD.
