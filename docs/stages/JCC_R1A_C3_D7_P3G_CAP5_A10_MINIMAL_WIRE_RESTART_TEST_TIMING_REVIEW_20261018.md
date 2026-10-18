# CAP5-A10 — Minimal recovery wire, restart lifecycle, offline tests and timing review (2026-10-18)

**Decision: READ-ONLY CONTRACT COMPLETE / IMPLEMENTATION-READY SUBJECT TO EXPLICIT TIMING APPROVAL / IMPLEMENTATION HOLD.** Recovery correctness only; A7/A8 security expansion remains superseded by A9.

## Source verification
A9 commit `6cb9b208e707c95001713b7d1d917afd4b25bb79`. Reviewed `gke/app/peer.proto`, `peer.py`, `recovery_availability.py`, `controller_shared.py`, `tests/test_p3g_recovery.py`, and `gke/helm/ahbn/templates/job-controller.yaml`. Current `DCSOCMaintenanceRequest` has tags 1–4; `Ack` has `ok=1,message=2`. Current churn controller deletes pod, waits GetStatus-ready, notifies, but `delete_peer_pod()` does NOT itself return/persist old-to-new UID; separate `delete_peer_pod_observed()` does observe original UID for failure experiments but not the final Ready replacement. Rejoin notifications can precede observer's later failure; `RecoveryAvailability.probe` returns immediately when target not excluded.

## A10-1 — Canonical minimal wire (proposed final)
Keep **existing** `PeerService.NotifyRecoveryRejoin(DCSOCMaintenanceRequest) returns (Ack)` and existing port. Extend the request **only** with:
```proto
// existing 1..4 unchanged
string run_id = 5;
string replacement_pod_uid = 6;
uint64 rejoin_generation = 7;
```
Maintain `node_id` as target. `run_id` is compared to observer's current topology run; UID is obtained by controller from Kubernetes old/new pod observation; generation per target strictly positive and increasing within the run. No authentication/security capability claimed. No change to `Forward` or `GetStatus`.

Extend existing `Ack` with **one additive** `string recovery_outcome = 3`. Exact literal values: `ACCEPTED_PENDING` (valid marker stored, no proof of restored peer); `ACCEPTED_PROBE_STARTED` (marker accepted while excluded, independent probe scheduled/started, NOT recovered); `DUPLICATE_NOOP` (same marker, does not reset TTL/budget); `REJECTED` (invalid/disabled/conflicting marker; details logged); `UNSUPPORTED_LEGACY` (recovery-enabled caller omitted required fields). `Ack.ok` continues to signal RPC-level handling/legacy semantics only; it is never proof of restoration. `Ack.message` remains human diagnostic. No `RECOVERED` notification outcome. Actual outcome comes from peer event `neighbor_reenabled` after successful, current GetStatus. Existing controller `acknowledged` historical counter remains unchanged in legacy evidence; new controller tallies `attempted, accepted_pending, probe_started, duplicate, rejected, rpc_error` separately. A controller must not infer later Forward success from these counts.

Proto wire compatibility: additive tags, unchanged legacy service and method. When feature OFF, preserve baseline behavior and allow old clients with absent added fields to receive inert `recovery disabled`; feature ON rejects missing fields and cannot interpret old `Ack.ok` as recovery. Test old/new request/response decoder compatibility and unknown fields.

## A10-2 — Controller replacement evidence and lifecycle
During churn, capture `original_pod_uid` **before** pod deletion; after `wait_for_peer_ready`, read current pod metadata again and require `replacement_pod_uid != original_pod_uid`, Kubernetes Ready, correct pod name/run namespace, and GetStatus matching target ID + ready/alive. If any check fails, **skip notification** and record reason, rather than manufacture a generation. Existing `wait_for_peer_ready` checks readiness; caller must explicitly bind the resulting correct replacement UID, not reuse earlier `delete_peer_pod_observed` intermediate return.

Keep a monotonically increasing per-target generation in the single controller *process* for the run. Controller Helm Job currently `restartPolicy: Never` and `backoffLimit: 0`, but this does not prove no new Job/manual resumption. Preserve unique run ID and run-start fresh observer state. **No same-run automatic resume:** if controller process exits/crashes and generation ledger is lost, stop additional enhanced recovery notifications and mark that run recovery-incomplete/HOLD. Operators must not restart a controller with same run ID expecting continued marker ordering. A new run requires distinct run_id and fresh pod/observer state. Current observers may retain already accepted markers until their bounded local expiry; this experimental policy does **not** claim instant crash detection or general restart safety. Explicitly record this limit.

Observer restart: a new pod must not reuse prior run's marker/epoch/watermark; in-place observer process restart under same pod/run without evidence of fresh observation state cannot claim continuous recovery correctness, so fail closed or restart the entire experimental run. Per-observer active markers and one-shot budgets are memory bounded and cleaned at run shutdown/feature disable.

## A10-3 — Recovery transitions and invariants
A marker `(run_id,target,UID,generation)` accepted only for current run, known neighbor, positive gen, nonempty replacement UID and eligible strategy/feature. New UID and higher generation supersede prior reservations. Duplicate same pair is idempotent; lower generation, same generation with different UID, or higher generation with same UID reject. The *first* valid marker for a returning target:
- target excluded: reserve and launch exactly one immediate guarded GetStatus; no late second opportunity.
- target not excluded: log `marker_accepted`, retain bounded unused allowance; no GetStatus yet.
- first later new exclusion within marker lifetime: atomically consume allowance, reserve one deferred check at failure-time + Δ; repeated failures never generate another check.
- optional normal Forward ACK re-enables neighbor first: scheduled check aborts without duplicate join.
- positive GetStatus must match peer_id and ready/alive. Commit only if exclusion still present and topology permitted, feature active, run/UID/gen current, failure epoch unchanged, TTL valid and reservation still current. A new failure, new generation, shutdown, or TTL expiry while RPC runs rejects stale positive result. A successful commit removes unavailable exactly once, records one join, and does not call Forward or Q update. A GetStatus confirmation proves transport/health eligibility only, **not successful payload dissemination**.

## A10-4 — Offline deterministic verification matrix, not run
Reuse current T01–T18 unchanged. Implement T19–T38 with injected fake monotonic clock, manual scheduler, fake Kubernetes UID observations, controlled GetStatus stub, fake sink/counters and deterministic concurrency barriers—zero sleep or GKE. Scope tests:
- T19 marker-before-exclusion, no premature probe; T20 later first failure reserves exactly once and re-enables on valid status; T21 exclusion-before-marker immediate probe only;
- T22 after-expiry no probe; T23 W equality rejected; T24 Δ exact scheduling; T25 duplicate cannot refresh W/budget; T26 stale/conflict gen rejects; T27 newer UID/new gen supersedes old worker;
- T28 wrong run/missing UID/zero gen/non-neighbor reject; T29 controller UID evidence missing or not Ready => no emitted marker (replaces superseded authentication tests); T30 repeated failures cannot make second reservation; T31 failure-in-flight rejects result;
- T32 disable/shutdown cancels; T33 wrong status ID/not-ready/dead/error no join; T34 ordinary ACK cancels without extra join; T35 TTL expires during status call => reject; T36 no marker/unrelated target => unchanged baseline;
- T37 exact metric isolation: no new Forward, duplicates, learner Q update/reward, one leave/join on transitions; T38 legacy wire/proto decode + T01–T37 + frozen parity + SHA256 logs, controller interrupted/no same-run resume + fresh new-run isolation.
Mandatory additional assertion: demonstrated later **actual Forward targeting** after GetStatus reenable in isolated integration test (as applicable), to connect `unavailable` removal to dissemination eligibility, without claiming delivery ratio improvement from synthetic tests.

## A10-5 — Timing review, freeze withheld
Proposals **W = 10.0 s** receiver-local monotonic marker lifetime; **Δ = 0.25 s** bounded deferred-check delay; existing GetStatus timeout **2.0 s**; 1 check per observer-target-generation; 0 retries; at most one in-flight target. `now < expiry` required at failure reservation, worker start and post-RPC commit. Existing CAP5 target-15 later exclusion ~5.24 s after notice illustrates a covered observation, not calibration or optimality evidence. Expiry may occur during a 2 s RPC; reject rather than extend. W and Δ *not frozen*: researcher must separately approve fixed values before implementation. Preserve relative monotonic traces and resource cleanup. Never present W/Δ as scientifically optimized.

## Gate
**A10 design review PASS / numeric timing freeze PENDING / implementation T19–T38 GKE D7-F D8 HOLD.** No runtime code, Helm, proto or cloud changes; no test results claimed. A7/A8 retained but superseded as active requirements; security not an RO. Existing Google Drive CAP5 diagnostic evidence is unchanged. Manuscript under peer review at Journal of Cloud Computing, unpublished, no DOI.

**Next controlled decision: explicit accept/adjust W=10.0 s and Δ=0.25 s for *offline deterministic validation* (not optimized parameters); then separately authorize implementation and T19–T38.**
