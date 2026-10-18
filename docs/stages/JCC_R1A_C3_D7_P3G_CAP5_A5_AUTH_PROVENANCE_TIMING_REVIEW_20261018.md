# P3G-CAP5-A5 — Controller authentication, generation provenance and timing review (2026-10-18)

**Decision: READ-ONLY REVIEW COMPLETED / DESIGN FREEZE HOLD / IMPLEMENTATION HOLD.**

## Verified sources
- A4: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A4_IDENTITY_TIMING_OFFLINE_CONTRACT_20261018.md`, commit `9f3dfeda08e54f933dca83599dbdd7aff0a0f4ce`.
- A3: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A3_BOUNDED_LATE_FAILURE_DESIGN_20261018.md`.
- Current wire shape: `gke/app/peer.proto`; current probe: `gke/app/recovery_availability.py`; formal churn schedule: `gke/experiments/k5_q_formal.yaml`.
- Nonformal CAP5 evidence root: https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX. Distinguish planned schedule from observed proof.

## Authentication decision — BLOCKER
Current `NotifyRecoveryRejoin(DCSOCMaintenanceRequest)` uses fields node_id, available, explicit_du and reason; proposed replacement UID and rejoin generation are not present in current proto. Current plaintext gRPC/peer-identity checks are not verifiable controller authentication. Consequently, **no controller-only authenticated provenance is established**.

**Required release design:** a demonstrably authenticated and authorized controller principal on the notification RPC (preferred: workload-bound mTLS identity with explicit authorization; ingress restrictions alone require documented equivalence and negative verification). Do not trust caller-supplied reason, node_id, UID or generation by themselves. Reject unauthorized caller, wrong target, foreign run and unverified replacement UID. Ensure controller receipt means marker processed, not recovered. Concrete certificate identity, policy, provisioning, trust rotation and negative tests must be reviewed before freeze. No security claims for the current code.

## Generation provenance decision — BLOCKER
Adopt source of replacement identity from Kubernetes pod `metadata.uid` after verified old-to-new UID change and readiness; bind `(run_id,target_peer,replacement_pod_uid,rejoin_generation)` to this replacement. Require strictly increasing per-target generation, bound to the authoritative run. Duplicate pair idempotent without TTL refresh; lower generation rejected; equal generation/different UID rejected; greater generation/same UID rejected; stale pending workers canceled. A process-local counter **does not survive controller restart**. Freeze requires either a durable, uniquely scoped generation authority with atomic monotonic update/reconciliation, or fail-closed recovery disable after restart until a new independently verified run is established. Specify which option is selected and add crash/restart/cross-run negative tests.

## Timing review — CONDITIONAL ACCEPT AS OFFLINE TEST VALUES ONLY
| Parameter | Proposed | Decision |
|---|---:|---|
| W, receiver-local marker lifetime | 10.0 s | Reasonable bounded hypothesis; not statistically calibrated and NOT FROZEN |
| Δ, nonblocking settling delay | 0.25 s | Deterministic test value only, NOT FROZEN |
| GetStatus RPC deadline | 2.0 s | Existing peer probe default; preserve pending specific validation |
| Checks per observer,target,generation | 1 | Boundedness contract supported |
| Automatic retry | 0 | Boundedness contract supported |
| Concurrent inflight per target | 1 | Preserve existing guard |
| Clock | monotonic receiver-local | Appropriate; do not infer cross-node causal ordering |

10 s covers cited CAP5 late exclusion example (+5.24 s), but one observation cannot establish a statistically sufficient recovery window. The 25 s separations in `k5_q_formal.yaml` are **planned offsets** not independent validation. Test exact TTL deadline (`now < expires_at`), Δ boundary, expiry during RPC, preemption by ACK/new failure, and target generation replacement; fake clocks/barriers only. Investigate sensitivity of W and Δ under multiple runs *after* access/authentication and provenance are resolved; until then no optimum or production-safety claim.

## Gates
1. **A5 review:** evidence-based review recorded; blocker remains controller RPC authentication and verifiable durable generation authority / restart policy.
2. **A4 freeze:** HOLD pending explicit researcher choice of authenticated principal/control, restart provenance policy, exact W=10 s and Δ=0.25 s, and structured ACK/recovery-confirmation semantics.
3. **Implementation:** HOLD; proposed proto fields and T19–T38 not yet implemented/tested.
4. **Live GKE / formal D7-F / D8:** HOLD. No new cloud run authorized.
5. **Scientific:** diagnostic nonformal CAP5 observations are not proof of repaired forwarding or performance benefit. Frozen AHBN and Q-AHBN contracts must remain unchanged.
6. **Publication:** Q-AHBN manuscript submitted to Journal of Cloud Computing, **under peer review**; unpublished, no DOI.

Authority: GitHub control text; Drive stores raw experiment evidence. This report is a read-only review, not a design freeze or test result.
