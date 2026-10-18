# P3G-CAP5-A3 — Bounded late-failure recovery design review (18 October 2026)

**Decision: CONDITIONAL DESIGN PASS / IMPLEMENTATION HOLD.** This is a read-only design specification. No runtime changes, CI claims, or new GKE deployment.

## Evidence and problem boundary

Source of truth: `gke/app/recovery_availability.py`, `gke/app/peer.py`, `gke/app/controller_shared.py`, `tests/test_p3g_recovery.py`; CAP5-A2: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A2_TRIGGER_TIMING_INVESTIGATION_20261018.md`; nonformal CAP5 log corpus: https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX.

Observed controller notifications after churn are not GetStatus recovery receipts. `NotifyRecoveryRejoin` currently returns `Ack(ok=True, message="recovery not confirmed")` when no recovery is confirmed, while controller counts `ok` only. `RecoveryAvailability.probe` returns without logging when the target is not yet excluded. `failure()` records subsequent exclusions without scheduling a later probe. The late-failure gap is code-confirmed; its exclusive causal contribution to CAP5 is not proven.

## Proposed mechanism: one-shot, event-bound late-failure check

**Local state per (observer, target), not global:** `last_verified_rejoin` marker (target, controller-authorized generation token or replacement UID, local receipt monotonic time, expiry), `last_consumed_marker`, current failure epoch, `inflight`, and a single delayed-check reservation. Markers are scoped to *this observer's actual topology neighbor* and a verified replacement identity. A newly rejoining node is not itself implicitly proof of forward connectivity.

**Trust and identity prerequisite (OPEN design blocker):** Existing request `DCSOCMaintenanceRequest(node_id, available, reason)` carries no unique pod-incarnation/epoch identifier. Controller log has replacement UID, but current notification payload does not. Prefer a backward-compatible, optional, controller-issued generation token/UID transmitted with rejoin notice and bound to the target; reject older, duplicated, or unrelated markers. Until token authenticity/order and authorization are specified, treat this as an unapproved design, not a safe runtime patch. It is not enough to trust a free-form `reason` string.

**Safety state transition proposal:**
1. Controller sees replacement UID and peer-local GetStatus readiness; sends a generation-bound rejoin marker to graph neighbors. A receipt only means marker accepted, not recovered.
2. Observer records marker with strictly finite TTL `W` and at most one permitted late verification for that marker/target. It immediately calls the *existing* bounded probe only if target is currently excluded; otherwise records `SKIPPED_NOT_EXCLUDED` and preserves its one-shot late-failure allowance until expiry.
3. If a Forward attempt later fails and newly excludes that same target *within W*, and the marker generation remains current, atomically consume the allowance for that marker. Schedule exactly one peer-local `GetStatus` check **after** a short bounded settling delay `Δ` (not inside the forwarding callback, which must remain nonblocking). Before RPC, recheck feature-enabled state, topology permission, target exclusion, marker generation, epoch, deadline and in-flight reservation.
4. The existing `RecoveryAvailability.probe` remains authoritative: `GetStatus` peer_id must match, ready and alive true; only the same current exclusion epoch may be cleared. On mismatch, failed RPC, expired marker, duplicate signal, stale generation or concurrent newer failure, retain exclusion; no auto-retry. If the probe succeeds, record exactly one observation join and restore eligibility under existing selection rules without changing mode/fanout/controller logic.
5. A new, strictly newer authenticated replacement generation may create a fresh allowance; duplicates, out-of-order generations, or repeated failures of the same generation never replenish it. Clear markers/reservations on feature disable, shutdown or invalid topology. No periodic polling and no RPC on ordinary unrelated failures.

**Proposed bounds are subject to controlled calibration, NOT frozen constants:** `W` finite rejoin-correlation window; `Δ` nonnegative bounded settling delay; the existing GetStatus call timeout is **2.0 s**. Exactly one late check per observer/target/rejoin generation; 0 retries; 1 in-flight check per target. Do not choose numerical W/Δ without evidence and explicit freeze. The controller's present notification timeout is 3 s per neighbor. Adding any new retry or periodic loop requires a separate scope decision.

**Race / observability rules:** Distinguish `marker_received`, `probe_skipped(reason)`, `probe_scheduled`, `probe_started`, `probe_result`, and `neighbor_reenabled`. Include run ID, observer, target, trusted generation/UID, marker age, failure epoch and checked epoch. Controller receipts must have outcome-specific semantic fields (`notification_accepted` versus `recovery_confirmed`); do not translate legacy `ack.ok` into confirmed recovery. Late worker must carry captured marker identity and exclusion epoch; if exclusion epoch advances while RPC is in flight, reject stale success and preserve unavailable state. If a newer failure arrives after a positive response but before commitment, only lock-protected epoch equality permits recovery. Note `failure()` already increases epochs on repeated failures even when exclusion unchanged.

**Algorithm and metrics isolation:** No Forward RPC by a health check, no synthetic message, no change to topology selection, AHBN EWMA/mode/fanout, or tabular Q learning and reward updates. A successful verified transition may legitimately call existing `observations.record_join()` once; no fabricated ACK or increments to user-message forward/duplicate counters. Measure before/after counters and controller parity explicitly.

## Alternatives rejected at design stage

- **Unbounded retry/poll loop:** causes uncontrolled traffic and may mask failures.
- **Clearing exclusion solely on rejoin notification or controller ACK:** unverified transport restoration, unsafe.
- **Immediate synchronous check from forwarding exception without marker/epoch gates:** can block forwarding and treat unrelated failures as recovery.
- **Controller-side broad broadcast retry alone:** does not inherently bind later exclusions or guarantee state correction, and requires more controller activity.

## Mandatory offline tests before implementation release

| Test family | Required observable assertion |
|---|---|
| Order A | Exclusion before verified notification → existing probe path works; no double join |
| Order B | Notification before first exclusion → skip recorded then one late check within W |
| Boundary | Failure after W → zero late RPC and exclusion remains |
| Replay | Duplicate or older marker → no allowance reset, no repeated RPC |
| Generation | Newer authorized replacement may create a new allowance; unrelated target cannot |
| Boundedness | Multiple same-epoch failures → <=1 late GetStatus / marker; 0 retries |
| Concurrency | In-flight failure increments epoch; stale successful response cannot clear |
| Identity | Wrong ID, not-ready, dead, timeout or RPC error → no join; explicit reason |
| Disabled | Feature OFF indistinguishable from frozen baseline; no late worker |
| Isolation | No extra Forward, duplicate, reward or Q update from health probe; exactly-once joins |
| Observability | Skip and successful/failed probe decisions have target, generation, epoch and reason |
| Parity | Existing frozen AHBN/Q-AHBN2 controller and simulator parity tests remain PASS |
| Negative control | No marker/unrelated failure never initiates late check |

Proposed tests are **not executed**. Build the deterministic offline state-machine test harness first, then inspect trace-level outcomes; a passing test of a mock alone is not GKE recovery validation.

## Release conditions and scope

1. Approve design constants W and Δ, generation-token compatibility/authentication model, safe worker lifecycle, event schemas, and ACK semantics before implementation.
2. Separate implementation approval required. Re-run integrated offline tests and parity; preserve Git SHAs, logs and hashes.
3. A new GKE canary is a **separate** researcher decision; historical CAP5 approval covered one completed run only.
4. Report nonformal evidence as diagnostic; do not make performance or causal claims until independent verification.

**CAP5-A3 DESIGN DOCUMENTED / CONDITIONAL PASS; implementation NOT APPROVED, GKE retest NOT APPROVED, D7-F HOLD, D8 HOLD.**

Manuscript: *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions*, submitted to Journal of Cloud Computing, under peer review, unpublished, no DOI.
