# P3G-V1 — Offline verification results and remaining release conditions (2026-10-18)

**Decision: PARTIAL PASS / P3G HOLD.** This is an evidence-backed local-integration result, not a formal D7/D8 release.

## Exact verified run
- GitHub Actions: https://github.com/wwiras/q-ahbn2/actions/runs/39125540345
- Head commit: `96207656f49f2b3252c25ee19e6db30836f0cd54`
- Runner: Python 3.11, Ubuntu GitHub Actions; dependencies installed from `gke/app/requirements.txt`; gRPC Python bindings generated from `peer.proto`.
- Syntax: `python -m compileall -q gke/app tests/test_p3g_recovery.py tests/test_p3g_peerstate_integration.py` — PASS.
- Execution: `PYTHONPATH=gke/app python -m unittest tests.test_p3g_recovery tests.test_p3g_peerstate_integration -v` — **26 tests, 26 passed** (18 helper-level labelled T01–T18 plus eight direct production-`PeerState` method integration tests). Job conclusion **success**. Original job logs remain accessible through the link above.
- Test evidence covers: real `PeerState.target_peers` exclusion/restoration after fake `GetStatus`; negative identity; no status-triggered `Forward`, receive/duplicate/forward counter change; forwarding ACK and failure transitions with exactly-once join/leave; disabled probe and non-neighbor; stale-positive epoch invalidation.

## Minimum confirmed correction
- `gke/app/Dockerfile.qahbn2` previously copied `peer.py` but not its new imported `recovery_availability.py`. Fixed in commit `833b712a0170cc66e2fdb541ed3482b4487e2a87`. This is packaging only; no frozen dissemination/learning algorithm change.

## Remaining blockers — no claim of P3G full PASS
1. **AHBN/Q-AHBN2 automatic rejoin trigger:** Current production `PeerService.ApplyDCSOCMaintenance` invokes the recovery probe only for DC-SoC. Tests prove `PeerState.probe_recovery` works when invoked for gossip-style topology; they do *not* demonstrate a production rejoin notification reaches AHBN or Q-AHBN2. Do not claim automatic recovery in those strategies.
2. **Frozen parity:** The above CI run did not execute a full frozen AHBN-controller/Q-AHBN2 learner parity regression. The previous S04 logical parity decision is not a replacement for current exact-commit verification.
3. **End-to-end/runtime:** No GKE deployment, no image digest parity, no automatic churn recovery or controlled delivery improvement measured here.
4. **Evidence:** GitHub job logs are available under the immutable run ID; a SHA256 digest for archived test logs and Drive upload are not yet present. Do not fabricate either.

## Next limited action
Provide one authorized, epoch-ordered rejoin indication to affected AHBN/Q-AHBN2 peer(s), using an existing approved controller/event pathway (do not infer availability merely from pod creation); add a direct test proving this reaches `PeerState.probe_recovery`, then rerun 18 tests + integrated checks and frozen parity, capturing logs/checksums and reviewing deployment image parity. Keep algorithms, experiments and old results frozen.

**D7-F / D8 HOLD.** Q-AHBN manuscript at Journal of Cloud Computing is under peer review; not published, no DOI.
