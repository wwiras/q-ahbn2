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
