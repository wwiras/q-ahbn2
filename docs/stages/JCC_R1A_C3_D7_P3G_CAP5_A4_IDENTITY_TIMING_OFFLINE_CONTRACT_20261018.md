# P3G-CAP5-A4 — Recovery-generation identity, timing freeze and offline test contract (2026-10-18)

**Controlled decision: CONTRACT SPECIFIED / DESIGN FREEZE PROPOSED, IMPLEMENTATION HOLD.** This is a design artifact only, not implemented, compiled, tested or deployed. Review evidence is sufficient for a finite deterministic contract, but the numerical bounds are engineering choices for offline validation, **not empirically optimized parameters**.

## Basis and authority

- A3: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A3_BOUNDED_LATE_FAILURE_DESIGN_20261018.md` (commit `8c1530b17288e60d08c922b675b2fcc30649529f`).
- Source reviewed: `gke/app/peer.proto`, `gke/app/peer.py`, `gke/app/recovery_availability.py`, `gke/app/controller_shared.py`, `tests/test_p3g_recovery.py`.
- CAP5 nonformal GKE evidence: https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX
- Historical planned churn offsets: [1,26,51,76] seconds in `gke/experiments/k5_q_formal.yaml`, NOT empirical proof of a suitable late-failure window.
- Scientific boundary: none of these design controls alters frozen AHBN EWMA, score, mode threshold, fanout S5, Q policy, reward or simulator parity.

## A4-01 — Replacement identity and backward compatibility

**Chosen wire contract:** extend only the `NotifyRecoveryRejoin` request path by adding an optional `string replacement_pod_uid = 5` and `uint64 rejoin_generation = 6` to the existing protobuf `DCSOCMaintenanceRequest`; keep tags 1–4 unchanged. Other callers may omit fields. New recovery-enabled receivers **MUST NOT accept a missing or empty UID, zero generation, unknown controller identity, or invalid peer target** as a generation-qualified marker. Disabled baseline ignores marker entirely. Do not change `GetStatus` or `Forward` message format.

**Authority:** the churn controller obtains `metadata.uid` for the *replacement* StatefulSet pod after observing a different UID and verifies replacement readiness and peer-local GetStatus identity. A controller-local strictly increasing `rejoin_generation` per target (within run) is attached to the notification. If the controller restarts, counters are not trusted across processes: revalidate generation against authoritative run/pod UID and reject conflict; a controller restart without a durable generation source is an explicit HOLD condition for enabling late recovery. At minimum marker identity is (`run_id`, `target_peer`, `replacement_pod_uid`, `rejoin_generation`). `run_id` is obtained from local peer/controller run configuration (not trusted from caller-controlled `reason`).

**Controller sender authentication is an OPEN prerequisite:** protobuf fields alone are not authentication. Before implementation release, specify verifiable controller-only RPC origin (e.g. workload identity/mTLS plus authorization, or demonstrably equivalent ingress-restricted channel); controller-derived UID must match a Kubernetes-observed replacement. In current plaintext `grpc.insecure_channel` architecture, treat UID/generation as integrity correlation rather than cryptographic proof. Never assert authentication without adding and testing an actual caller-authentication control. **Fail closed on unverified origin**, and test negative callers. This is a **design-release blocker**, not permission to silently bypass identity validation.

**Freshness/order:** recipient stores last (generation, UID) per target for the current run, rejects lower generation; same pair is idempotent and cannot refresh TTL/check budget; equal generation with a different UID is rejected; strictly greater generation with same UID is rejected (no actual new incarnation). New verified generation supersedes marker and cancels pending worker/old probe eligibility. Reset only on verified new run identity; do not revive an expired marker by replay.

## A4-02 — Deterministic finite timing settings (proposed freeze)

| Setting | Proposed value | Intent | Status |
|---|---:|---|---|
| `W` marker lifetime | **10.0 seconds** from monotonic receipt | Limited late-failure correlation window | **PROPOSED / researcher freeze pending** |
| `Δ` settling delay | **0.25 seconds** | Deferred nonblocking check after exclusion | **PROPOSED / researcher freeze pending** |
| `GetStatus` RPC deadline | **2.0 seconds** | Existing peer-local timeout | **Existing/fixed** |
| Late checks per (observer,target,generation) | **1** | One-shot bounded verification | **Proposed** |
| Automatic retries | **0** | No uncontrolled probing | **Proposed** |
| In-flight per target | **1** | Maintain existing epoch/inflight guard | **Existing/proposed** |
| Clock | Monotonic local clock | TTL/worker scheduling, no cross-node clock assumption | **Proposed** |

**Rationale and limitation:** 10 s is long enough to cover the seconds-scale later failures observed in the CAP5 log (e.g. target 15 exclusion +5.24 s) and short relative to the planned 25 s churn separations, but is not optimized or proof of recovery. CAP5 target 5 notification duration itself was several seconds; the window starts at each receiver's *local verified marker receipt*, not from the controller's cumulative completion timestamp. 0.25 s is a bounded scheduler delay hypothesis, not a measured repair-time optimum. A4 therefore *specifies* values for deterministic unit tests but does not approve treating them as scientifically frozen or production-safe until reviewed.

**Deadline semantics:** marker must be unexpired when failure reservation is atomically made and at worker start. Complete positive verification only if marker/generation still current and epoch valid; expiry before start cancels; expiry during RPC also rejects a late result (explicit conservative policy). A late check occupies at most `Δ + 2.0 s` of work without any retry; no blocking of message-forward path. Run cancellation/feature disable prevents committing stale recovery; joining a stopped process is not assumed.

## A4-03 — Deterministic state-machine contract

Use per-observer-target metadata guarded by existing `RecoveryAvailability.lock`. State: `generation`, `pod_uid`, `received_at`, `expires_at`, `consumed`, `scheduled_epoch`, `reservation_id`, `inflight`. Workers carry immutable captured (run,target,UID,generation,epoch,reservation_id). Never permit a thread or timer per incoming duplicate; at most one reservation for a given marker and in-flight target.

1. **VALID_MARKER:** Verify run, target/neighbor, controller provenance, observed replacement UID, strictly newer (generation,UID), feature enabled; record local monotonic receipt; if target excluded, run existing single immediate GetStatus probe (consume marker allowance to prevent an additional late check); else log `SKIPPED_NOT_EXCLUDED` while retaining one late allowance.
2. **FAILURE:** Preserve existing failure side-effects and epoch increments. Only when the first *new* exclusion follows a valid unused marker within W, atomically consume and reserve one check. Repeated failures must not reserve another. If another failure increments epoch before or during worker, its old result cannot clear exclusion; no retry under same marker.
3. **WORKER:** At `received_failure_time + Δ`, recheck run, enabled, target topology, permission, UID, generation, reservation identity, failure epoch, exclusion, expiry, in-flight. On violation skip with reason; on pass call exactly one peer-local GetStatus with 2.0 s deadline. Probe success must satisfy correct peer_id, ready/alive and current epoch *and generation* under lock before removal and exactly one `record_join()`. No Forward RPC or learner update.
4. **ACK/REJOIN:** A normal message ACK is still handled by existing logic, but if an ACK already clears exclusion before worker executes, worker cancels without another join. New generation invalidates older worker. Disable and shutdown cancel all pending reservations without any availability mutation.
5. **LOG:** Distinguish `marker_accepted`, `marker_rejected`, `recovery_probe_skipped`, `recovery_probe_scheduled`, `recovery_probe_started`, `recovery_probe`, `neighbor_reenabled`. Include run_id, observer_peer, target_peer, replacement UID, generation, monotonic *relative* marker age, failure epoch, check epoch, result, reason, and source_trigger. Avoid using wall clocks for cross-pod ordering without uncertainty bounds.

**Controller ACK semantics:** `Ack.ok` means request processed (or, if legacy, transport accepted), never implies recovery. `Ack.message` is insufficient as a structured recovery guarantee. Add outcome-specific structured result in a backward-compatible future RPC shape (or explicit parsed response enum with exact values and negative compatibility tests); require controller counters `notified`, `marker_accepted`, `probe_confirmed` separately. Keep legacy recorded `acknowledged` label historically truthful; do not relabel old CAP5 evidence.

## A4-04 — Deterministic offline test contract

All tests use fake monotonic clock, injected GetStatus, deterministic manually driven worker queue/barriers, fake controller/UID authority and fake observation sink; **no sleep, real network, GKE or Docker required**. Assertions are on exact transition counts, trace tuples and side-effects, never only end-state. Proposed T19–T38 (new tests, not executed):

| ID | Scenario | Mandatory assertions |
|---|---|---|
| T19 | New verified marker, not excluded | accepted; `SKIPPED_NOT_EXCLUDED`; 0 probe; budget retained |
| T20 | Marker → first late failure within W | one reservation, one GetStatus after Δ, exactly one join |
| T21 | Exclusion → valid marker | one immediate GetStatus; no later second probe |
| T22 | Failure after W | no worker/no GetStatus, remains excluded |
| T23 | Exact W boundary | `now < expires_at` policy; at expiry skip |
| T24 | Exact Δ boundary | before Δ no RPC; at/after Δ at most one |
| T25 | Replayed same marker | cannot refresh expiry, budget or probe count |
| T26 | Older or same-generation/conflicting UID | rejected, no state mutation |
| T27 | New generation / UID | old reservation canceled, new marker eligible |
| T28 | Missing UID/zero generation/foreign run | rejected |
| T29 | Unauthorized caller/UID not observed | rejected with logged reason |
| T30 | Duplicate and repeated failures | epoch increments preserved; <=1 late probe/generation |
| T31 | Failure during in-flight probe | old positive result rejected; exclusion stays |
| T32 | Disabled mid-flight and shutdown | no join; pending work canceled |
| T33 | Wrong ID/not-ready/dead/timeout/RPC exception | no join; no retry |
| T34 | ACK clears exclusion before scheduled check | worker cancels; join not duplicated |
| T35 | TTL expires while GetStatus is pending | no join, stale result rejected |
| T36 | No marker/unrelated target | 0 recovery RPC; unchanged baseline failure |
| T37 | Health isolation | exactly 0 extra Forward, duplicate, Q update/reward; legitimate join once |
| T38 | Parity and evidence | frozen parity/recovery T01–T18 + new tests PASS, skip/outcome traces and SHA256 manifest |

**Additional integration contracts before any code release:** protobuf generation/backward-compatibility tests; checked controller caller identity and UID source; latency bounds with fake scheduler, peer-level resource cleanup, startup/shutdown, topology exclusions, cross-run isolation, feature OFF, and strategy-specific handling for AHBN/Q-AHBN2. Test both controller notification `ack.ok=True,message="recovery not confirmed"` and actual confirmed status without counting the former as recovery.

## Exit gates and scientific limits

A4 design can move to **PASS/FROZEN** only after researcher explicitly approves exact W/Δ and resolves the caller-authentication/UID authority mechanism and wire response semantics. Merely adding proto fields is not a security control. A5 would then implement under separate authorization and run all local tests with exact source SHA and SHA256. A new GKE canary is **not authorized by this gate**.

**Current status: A4 CONTRACT DRAFTED / CONDITIONAL REVIEW, FREEZE HOLD. A5 implementation HOLD; D7-F HOLD; D8 HOLD.** No new code changes or experiment; the nonformal CAP5 single run provides diagnostic timing, not recovered-neighbor validation or a performance improvement. Manuscript submitted to Journal of Cloud Computing; under peer review, unpublished, no DOI.
