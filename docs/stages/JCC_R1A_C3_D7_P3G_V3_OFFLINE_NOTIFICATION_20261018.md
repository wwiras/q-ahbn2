# P3G-V3 — End-to-end offline notification verification (2026-10-18)

**Decision: V3 OFFLINE PASS / D7-F AND D8 HOLD.** This evidence does not constitute GKE runtime or image parity.

## Actual tested revision and logs
- Tested commit: `2f3d66ac7fc9ffb3653cc8005f00bd167c3232b5`.
- GitHub Actions run: https://github.com/wwiras/q-ahbn2/actions/runs/39126351325 (checks PASS).
- Exact-commit syntax and generated gRPC binding checks PASS.
- Tests: 18 T01–T18 adapter cases + 12 production PeerState integration checks + 9 controller-to-peer fake-gRPC notification checks = **39 PASS**.
- Frozen Q-AHBN2 learning/adapter/event regression test selection = **22 PASS**.
- Total **61 PASS**; not complete empirical ControlSim↔GKE parity.
- Job logs record SHA256 hashes including `tests/test_p3g_v3_notification.py` = `1063ad7cdf3035c9acc403e476f5bb417014946b5db318c41edc3b870bf7cb99`, `gke/app/peer.py` = `33960c7355290c34c04275e0fdbf69145732a4eaa92713c7c668cc5c4ea4a3b4`, and controller = `d16bf1d21209c4438102c3fe82adc3aa1f2f82dd1852afaac29ad50daad85d02`.

## Covered
Fake gRPC checks exercise production `controller_shared.notify_recovery_rejoin` -> `PeerService.NotifyRecoveryRejoin` -> `PeerState.notify_recovery_rejoin` -> `GetStatus` -> epoch-protected availability change. AHBN and Q-AHBN2 strategy filters, graph non-neighbor exclusion, failure reporting, wrong readiness, stale replies, repeat notifications, no forward metrics and disabled rollback are checked.

## First-run failure and resolution
Run https://github.com/wwiras/q-ahbn2/actions/runs/39126300841 failed because isolated test imported `controller_shared` without the launcher-provided `k5_exp10_tools` alias. Fixed test fixture by reusing existing `k7_exp11_tools` alias, identical to `k7_controller` import setup; no production algorithm change. Reran green at exact commit above.

## Important limitations and release controls
- Actual Kubernetes pod replacement, notification race/timing under real churn, GKE-deployed image digest and cross-node runtime verification still not checked.
- A successful notification ACK is only delivery of a request, not proof that peer recovered; peer-local status probe is separately authoritative. Failure outcomes are recorded; any missing notification does not automatically retry.
- Test of full Q-AHBN2 runtime Q-table side-effect isolation under a health check is not in these V3 tests; tested adapter-regression contracts remain PASS.
- External manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions*, submitted to Journal of Cloud Computing, is **under peer review, no DOI, not published**.
- No formal D7-F/D8, no GKE cost, no new performance conclusions; algorithms remain frozen.

**Next decision:** P3G-V3 may close as OFFLINE PASS; proceed only to exact-image/admission review and one separately authorized nonformal GKE canary. Formal D7-F and D8 stay HOLD until release evidence is met.
