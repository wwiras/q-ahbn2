# P3G-CAP5-A2 — Read-only recovery trigger and event-ordering investigation (2026-10-18)

**Gate decision: CODE-LEVEL TIMING GAP CONFIRMED; LIVE CAUSAL ATTRIBUTION PARTIAL / HOLD. No runtime patch, no new GKE execution.**

## Authority and evidence
- Frozen code in `wwiras/q-ahbn2`: `gke/app/recovery_availability.py`, `gke/app/peer.py`, `gke/app/controller_shared.py`, and `tests/test_p3g_recovery.py`. Read on 2026-10-18.
- Prior audit: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A1_RECOVERY_FORWARD_CORRELATION_20261018.md`.
- Nonformal raw evidence: https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX (`run/controller.log`, peer stream and snapshots). Existing evidence, not a new run.

## Code trace / source-specific findings

1. `PeerState` initializes `unavailable_neighbors=set()` per peer incarnation, and recovery flag is strictly `P3G_RECOVERY_ENABLED=="1"` (`peer.py`, initialization).
2. An unsuccessful forwarding RPC calls `self.recovery.failure(dst_peer)` and logs `forward_failed`; a rejected response also calls `failure`. This increments the epoch even if already excluded and records a leave only on first exclusion (`peer.py`, forwarding branches; `recovery_availability.py:failure`).
3. Controller `notify_recovery_rejoin` walks graph neighbors after replacement readiness and calls each peer's `NotifyRecoveryRejoin` with one RPC timeout 3 s. The controller counts `ack.ok`; it does **not** inspect `ack.message`. `peer.py:NotifyRecoveryRejoin` returns `Ack(ok=True,message="recovery not confirmed")` even when probe was skipped or failed. Therefore controller `acknowledged` counts **notification RPC acceptance, not recovered peers**.
4. `PeerState.notify_recovery_rejoin` invokes `probe_recovery`, which uses `RecoveryAvailability.probe` with GetStatus timeout 2 s. The probe **returns before performing any RPC or logging `recovery_probe`** when disabled, target not currently in `unavailable_neighbors`, target already in-flight, or permission rejected (`recovery_availability.py:probe`). Thus absence of `recovery_probe` can be legitimate skipped requests rather than missing log collection. The audit cannot distinguish these without request/skip telemetry.
5. `RecoveryAvailability.probe` has epoch check, in-flight suppression, and exactly-once state/observation transition on confirmed `peer_id`, `ready`, `alive`. Successful forward/duplicate ACK also calls `recovery.ack`, but forward selection removes excluded neighbors, so an excluded neighbor normally cannot be selected for a new forward solely via this path.
6. No scheduled or deferred re-probe is evident in the reviewed AHBN P3G `failure()` or `notify_recovery_rejoin()` path. Specifically, when notification precedes the **first** failed-forward exclusion, no later P3G notification is guaranteed. The target may stay excluded until some other explicit availability-changing event. This is the **confirmed code-level missing late-failure recovery trigger**; it is not a definitive exclusive cause of the particular canary outcomes.
7. Existing `tests/test_p3g_recovery.py` T01–T18 cover exclude→probe and epoch/inflight safety but do not explicitly exercise notify-before-failure→deferred verification and do not assert skip-reason observability.

## Captured chronology / interpretation

| Target | Controller notify timestamp (Unix s) | Notification acceptance | Relevant observation from A1 |
|---|---:|---:|---|
| 0 | 1792331935.1776187 | 13/13 | Later forward success then failures/exclusions |
| 5 | 1792331963.403391 | 3/4 | One `_InactiveRpcError` when notifying peer0; two later successful ordinary forwards |
| 10 | 1792331985.3468735 | 2/2 | Later failed forwarding and exclusion, no demonstrated restoration |
| 15 | 1792332010.248298 | 2/2 | Later failed forwarding and exclusion, no demonstrated restoration |

These are controller notification end timestamps rather than separate per-receiver start/ACK timestamps. A1 reported 0 `recovery_probe` in saved overlapping peer streams, 12 changed=true availability events all exclusions, no confirmed unavailable→available recovery transition. These observations support a timing/visibility investigation but cannot establish exactly which RPCs were skipped, whether feature flag propagated to every running peer, or the unique root cause. Verify actual StatefulSet env and peer image captures independently; do not infer `NotifyRecoveryRejoin` ACK is successful transport verification.

## Design choices for subsequent separate approval

**Preferred design review candidate: bounded late-failure verification with event identity.** Preserve the frozen dissemination/controller/Q-learning contract. After a failure *subsequent to an authenticated, same-peer rejoin marker*, consider a bounded peer-local GetStatus revalidation with explicit epoch guards; avoid immediate repeated retries, false-positive churn joins, and probing unrelated failures. A one-shot notification marker and finite TTL/epoch binding may be necessary, but precise lifetime, deduplication, race safety, and metrics impact require an explicit design review before implementation.

**Alternative:** controller follow-up/re-notification only when verified new exclusion is observable (requires event transport or controller polling). Avoid uncontrolled periodic probing or treating ACK as recovered.

Mandatory future offline tests: notification-before-first-failure, failure-before-notification, delayed late failure, repeated same-epoch failures, stale probe response, concurrent failure during probe, wrong ID/not-ready/dead GetStatus, feature-off baseline, exactly-once join and zero health-check impact on forwards/Q-learning, per-target skip telemetry, and frozen-controller parity. A future live retest needs **separate** researcher authorization.

## Controlled outcome

**P3G-CAP5-A2 REVIEW PASS** for identification of a reproducible code-path gap and explicit unresolved runtime attribution; **P3G recovery correction NOT VERIFIED**, **D7-F HOLD**, **D8 HOLD**. The prior nonformal GKE canary is not formal or publication evidence. No evidence of a performance improvement has been established.

Manuscript: *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions*, submitted to Journal of Cloud Computing; under peer review, unpublished, no DOI.
