# P3G-CAP5-A9 — Recovery-correctness scope reset and design review (2026-10-18)

**Decision: SCOPE RESET APPROVED / READ-ONLY RECOVERY-CORRECTNESS REVIEW PASS / IMPLEMENTATION HOLD.**

## Research scope, authority and historical records
This gate follows the researcher's explicit correction: transport neighbor re-enablement following churn, **not workload security**, is the objective. Do not require mTLS, certificate issuance, SAN, NetworkPolicy, cryptographic authentication, independent lease issuer or security threat model to complete this research recovery fix. This is a bounded experimental correctness contract, not a claim of production security. Existing transport and trusted controlled-experiment orchestration remain assumptions; scope and limitations must be accurately stated.

Retain previous files without deleting history:
- CAP5-A7: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A7_AUTH_GENERATION_ACK_CONTRACT_20261018.md` (commit `30462663ac1a85dac61b17be10e5499da01eb8e0`) = **SUPERSEDED AS ACTIVE RECOVERY REQUIREMENTS**.
- CAP5-A8: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A8_MTLS_MANIFEST_AUTHORITY_RECONCILIATION_20261018.md` (commit `8af11b53ee79343d49bd66ab626225a8c71f58d7`) = **SUPERSEDED AS ACTIVE RECOVERY REQUIREMENTS**.
- A4/A5/A6 are retained as provenance; any security-prescriptive elements are nonbinding for this scoped correction. Preserve their valid observational/epoch/recovery tests.
- GitHub is authority for control/code; Google Drive contains experimental evidence; CAP5 diagnostic folder `https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX` was identified via connected Drive. Existing evidence was not edited.
- The submitted Q-AHBN manuscript remains under review at **Journal of Cloud Computing**; unpublished, no DOI.

## Verified code basis
- `gke/app/controller_shared.py`: controller notifies graph neighbors after churn restoration; currently `grpc.insecure_channel`, legacy Ack increments `acknowledged` for `ok=True`.
- `gke/app/peer.py`: `NotifyRecoveryRejoin` calls peer's `probe_recovery` and returns `Ack(ok=True, message="recovered"|"recovery not confirmed")`. This is not structured proof of recovery and not necessarily an attempted probe.
- `gke/app/recovery_availability.py`: `probe()` returns without RPC if target is not yet in `unavailable_neighbors`; later `failure()` adds exclusion without scheduling another probe. Exclusion state uses per-target epoch, one in-flight probe, one `record_leave()` or `record_join()` on actual transition; GetStatus requires matching peer_id, ready and alive.
- Thus the confirmed software gap: rejoin notification may arrive before observer records a failed neighbor, leaving future exclusion uncleared. A valid notifier response cannot alone establish subsequent forwarding success. No fresh test/execution in A9.

## Scoped correctness contract — proposed for implementation review

1. **Replacement evidence**: controlled churn controller uses observed Kubernetes `metadata.uid` old/new mismatch plus replacement Ready and matching `GetStatus`. Bind `run_id, target_peer, replacement_uid, generation` as *correlation identifiers*, not an authentication mechanism. Reject mismatching run/topology/unknown UID or inappropriate target in the test-controlled runtime. Never claim malicious caller resistance.
2. **Generation**: monotonic per target in one known run. Keep per-observer latest generation/UID and marker spent/expiry state. Identical notification is idempotent and cannot extend expiry or one-shot budget; lower/conflicting generation ignored; newer UID supersedes old pending work. **Restart policy:** if controller loses generation memory mid-run, disable late-recovery extension for that run; restarting a process or reusing the same UID is not a new generation. If the run is relaunched with distinct run_id and fresh peer state, reset safely; do not claim detection of undetectable external controller crash by an otherwise unaware observer. A new-run-only restart policy is sufficient for this controlled experiment if launcher/job semantics and receiver lifetimes are verified.
3. **Late failure**: accept valid marker while target is not excluded without probing; retain one bounded opportunity. When target first enters unavailable set before marker expiry, reserve exactly one deferred GetStatus without holding Forward path; repeated failures consume no second allowance. If excluded when marker arrives, perform one current guarded immediate probe; no additional late probe for same generation.
4. **Probe safety**: `GetStatus` exactly once per reservation (existing 2 s deadline), verify correct target peer_id, ready/alive; before reenable atomically check run, UID/generation, failure epoch, target still excluded/permitted, feature enabled, expiry and lifecycle; expiry during RPC is a failed opportunity. No retries or extra message forwarding.
5. **ACK/log semantics**: request handled ≠ marker stored ≠ GetStatus success ≠ neighbor reenabled ≠ successful later payload forwarding. Record these separately; do not count controller `Ack.ok` as delivered or recovered. Prefer a minimal backward-compatible structured status field (or clearly enumerated `Ack.message` values plus strict parser and tests) within existing transport; a dedicated secure endpoint is **not required**. Choose precise schema before coding; no wire changes in A9.
6. **Scientific isolation**: unchanged AHBN normalization/EWMA/mode/fanout S5, Q-AHBN2 reward/action/Q updates, ordinary Forward/duplicates count, seed/topology and strategy handling. No claim of recovery improvement until verified at least by offline tests and then separately approved GKE evidence.
7. **Finite timing**: W=10 s and Δ=0.25 s are review candidates, not frozen or optimized. Local receiver monotonic time only. Bound workers/checks; 1 per observer-target-generation, 0 automatic retries, at most one in-flight per target. Exact-boundary and cancellation tests required.

## Offline test release criteria
Use fake monotonic clock/scheduler/GetStatus/Kubernetes UID records, no live network; run existing T01–T18 and proposed T19–T38 **with security-specific test cases replaced** by run/generation/UID/restart-correctness tests. Assert exact event counts, initial-before-exclusion then late failure, concurrent failure epoch, duplicate marker, expiry, disabled/teardown, controller crash/fresh run, normal ACK cancellation, recoverable vs unrecoverable GetStatus; measure number of Forward calls, duplicate counts, Q updates/rewards unchanged and recorded join once only. Preserve SHA/logs after actual execution. No tests performed under this review.

## A9 decision
- **PASS**: evidence-backed scope reset and corrected read-only recovery state-machine direction.
- **SUPERSEDED**: A7/A8 as mandatory security plans. They remain archived/linked, not deleted or retrospectively rewritten.
- **OPEN**: minimal exact wire response representation; observer process restart and clean run teardown invariants; exact W/Δ researcher freeze; reproducible offline tests.
- **HOLD**: implementation, protobuf edits, T19–T38 execution, live GKE CAP5 retest, D7-F and D8.

**Recommended next gate: CAP5-A10 — finalize minimal runtime wire/marker representation, check controller process restart/run-lifecycle assumptions and deterministic test cases; separately ask for W/Δ freeze before implementation.** No change to research scope or frozen algorithms.
