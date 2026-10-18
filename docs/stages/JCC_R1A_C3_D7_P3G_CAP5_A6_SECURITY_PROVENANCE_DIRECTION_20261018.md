# P3G-CAP5-A6 — Approved security direction; implementation and timing freeze remain on HOLD (2026-10-18)

**Controlled decision:** Researcher accepts the proposed architecture direction: controller-authenticated RPC origin, Kubernetes-derived replacement pod UID, and fail-closed restart behavior until an authoritative generation source has been re-established. This is **DESIGN DIRECTION APPROVED / CONTRACT DETAIL OPEN**, **NOT** a statement that implementation, formal design freeze or GKE testing is authorized.

## Authority and provenance
- Predecessor: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A5_AUTH_PROVENANCE_TIMING_REVIEW_20261018.md`, commit `4ffb291f8b9ed2fbaa4efda388309e587603e4af`.
- A4 wire/timing test specification: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A4_IDENTITY_TIMING_OFFLINE_CONTRACT_20261018.md`, commit `9f3dfeda08e54f933dca83599dbdd7aff0a0f4ce`.
- GitHub is control/text authority; Google Drive is raw evidence corpus. No Drive source/results are changed by this decision.

## Approved direction and bounded trust
1. **Controller authentication:** `NotifyRecoveryRejoin` must verify a controller-only workload principal and explicitly authorize that principal to act for the current run and target. Preferred candidate is workload-bound mTLS with explicit authorization. The existing `grpc.insecure_channel` is *not* authenticated. Neither pod UID, generation, `reason` nor peer's GetStatus reply is sufficient to authenticate controller-origin.
2. **Pod incarnation identity:** the controller may issue a marker only after Kubernetes-observed old-to-new `metadata.uid` transition, replacement readiness and peer-local GetStatus identity. Bind at minimum `(run_id, target_peer, replacement_pod_uid, rejoin_generation)`; recipients must reject unknown run/target, unauthorized source, UID mismatch, stale generation and replay.
3. **Restart:** no process-local generation sequence is trusted following controller restart. On any lost/unverifiable generation authority, stop accepting/emitting recovery markers, invalidate pending checks and remain fail closed until a separately specified trustworthy generation source is re-established. Merely refreshing the same UID or restarting a process must not create a new generation. Restart-to-new-run reinitialization must have demonstrable run identity/epoch isolation and negative tests.
4. **ACK:** distinguish notification accepted, rejected and transport failure from independently proven recovery; legacy `Ack.ok` is not a recovered-neighbor assertion. Design a backward-compatible structured outcome and negative compatibility tests.
5. **Security specification still REQUIRED before freeze:** exact controller identity issuer and trust roots, credential provisioning/rotation/revocation, RPC authentication and authorization enforcement points, Kubernetes UID observation authorization/freshness, run identity lifecycle, durable or fail-closed restart reconciliation, wire result semantics, negative controller impersonation/replay/cross-run tests, and feature-OFF backward compatibility. No claim of security in current code.

## Timing review is deliberately separate
W=10.0 s and Δ=0.25 s remain **proposed deterministic offline values** and are NOT formally frozen. Existing GetStatus deadline=2.0 s; 1 late check per observer/target/generation; 0 automatic retries; at most one target inflight. These are bounded design constraints, not proven best settings. Freeze numerical values only after security/generation contract is unambiguous and researcher explicitly approves timing; retain exact boundary tests and marker expiry during probe.

## Gate and execution rules
- CAP5-A5: REVIEW RECORDED.
- CAP5-A6: SECURITY/PROVENANCE DIRECTION APPROVED; DETAILED CONTRACT AND DESIGN FREEZE HOLD.
- CAP5-A4 timing values: PROPOSED, NOT FROZEN.
- Implementation/protobuf changes/T19–T38: NOT AUTHORIZED BY THIS DECISION.
- Additional GKE, D7-F, D8: HOLD. Existing diagnostic CAP5 evidence does not establish end-to-end recovery benefit.
- Frozen AHBN EWMA, mode/fanout and Q-AHBN2 policy/reward remain unchanged.
- Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions*: submitted to **Journal of Cloud Computing**; under peer review; unpublished and no DOI.

**Next controlled action:** write and review exact controller-identity issuance/enforcement and restart-safe generation source/re-establishment contracts, plus interoperable ACK outcomes. Present any unresolved choice to researcher before timing freeze. No code or cloud execution under A6.
