# P3G-V2 — Bounded rejoin notification and frozen regression verification (2026-10-18)

**Decision: OFFLINE REGRESSION PASS / GKE RELEASE HOLD.** No formal D7-F or D8 experiment was executed.

## Evidence / exact source
- GitHub Actions https://github.com/wwiras/q-ahbn2/actions/runs/39126082124 (completed SUCCESS).
- Exact tested revision `86b3a88f660a27a502a2b6ebd5cb3adae5236fd2`.
- Python 3.11 / Ubuntu, gRPC bindings generated, syntax checks PASS.
- `PYTHONPATH=gke/app python -m unittest tests.test_p3g_recovery tests.test_p3g_peerstate_integration -v`: 30 PASS (18 T01–T18 helper scenarios + 12 production PeerState-method integration checks).
- `PYTHONPATH=gke/app python -m unittest tests.test_k2_kubernetes_adapter tests.test_transition_bookkeeping tests.test_learning_schedule tests.test_s03_2a_trace_provenance tests.test_controlsim_event_bridge -v`: 22 PASS, 22 total. **52/52 passing offline regression assertions.** These are targeted frozen-learning regression checks, *not complete ControlSim–GKE empirical parity*.
- CI recorded file SHA256 in its immutable job log; examples: peer.py `33960c7355290c34c04275e0fdbf69145732a4eaa92713c7c668cc5c4ea4a3b4`; qahbn2_runtime.py `5d143497a0552179a897e0caba4b82c9ec34591f1631506a4fba989aa1836612`; controller_shared.py `d16bf1d21209c4438102c3fe82adc3aa1f2f82dd1852afaac29ad50daad85d02`.

## Minimal code correction
- `peer.proto`, `peer.py`: new `NotifyRecoveryRejoin` RPC. It cannot clear exclusion without independent `GetStatus`, epoch check and neighbor validation. Feature disabled by default.
- `controller_shared.py`, `k7_controller.py`: after controller-observed pod replacement readiness, notify only graph neighbors for AHBN/Q-AHBN2. No new Forward RPC, retry policy or Q-learning action.
- `qahbn2_runtime.py`: previously bypassed availability lock/epochs with direct unavailable-set mutations; now uses `self.recovery.ack/failure` consistently and ensures observation sink used by Q-AHBN2 receives exactly-once transitions.
- Production algorithm files defining AHBN weights/thresholds, S5 policy and Q-learner remain unchanged.

## Residual scientifically relevant limitations
- Controller-to-peer notification is wired in source, but the new controller broadcast path itself is **not yet fully end-to-end simulated** with fake gRPC transport and failure/rollback sweeps. A passing `PeerState` method test is not proof that the deployed controller reaches all peers.
- The rejoin-notification RPC does not authenticate event-origin identity at the application layer. Confirm existing namespace/network admission controls and threat model before formal release.
- Shared-controller simple churn path and K7 churn path both notify after readiness, but delivery improvement and any timing perturbation need an explicitly labeled nonformal canary with exact deployed image parity.
- These tests do not establish empirical GKE Q-AHBN2-versus-AHBN parity or experimental performance.
- Formal D7-F and D8 remain HOLD. Do not retroactively modify historical evidence.
- The Journal of Cloud Computing manuscript remains **under peer review**, not published, without DOI.

## Next
1. Add deterministic controller-to-peer fake-gRPC tests for AHBN/Q-AHBN2, disabled mode, failed notification, topology non-neighbors and repeated churn, then rerun exact-commit offline CI plus current frozen regression checks.
2. Preserve full CI logs/checksums into the canonical Google Drive `output/evidence` corpus and reconcile release register.
3. Review runtime deployment image digest and only then authorize one controlled nonformal canary; formal D7-F/D8 require separate evidence.
