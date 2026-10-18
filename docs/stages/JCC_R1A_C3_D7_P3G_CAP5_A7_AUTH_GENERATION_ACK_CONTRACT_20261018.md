# P3G-CAP5-A7 — Exact controller identity, enforcement, generation and ACK design review (18 October 2026)

**Gate decision: SPECIFICATION PREPARED / CONDITIONAL DESIGN REVIEW PASS; FORMAL FREEZE HOLD; IMPLEMENTATION HOLD.** No security implementation, proto generation, deterministic test, deployment or GKE run is claimed.

## 1. Authority and inspected baseline

A6 approved *direction*, not deployed security; commit `007af652c0e25c3f32b41ec9c5c57f0fbdf25042`. A4 proposed time values in `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A4_IDENTITY_TIMING_OFFLINE_CONTRACT_20261018.md`; A5 review commit `4ffb291f8b9ed2fbaa4efda388309e587603e4af`.

Source paths reviewed: `gke/app/peer.py` (current server `add_insecure_port`; `NotifyRecoveryRejoin` accepts unauthenticated request), `gke/app/controller_shared.py` (`grpc.insecure_channel`; notification increments legacy `acknowledged` on `Ack.ok`; Kubernetes pod `metadata.uid` read while deleting/observing replacement; readiness and notification), `gke/app/peer.proto` (request fields 1–4 only; `Ack(ok,message)`), `gke/app/recovery_availability.py` (local exclusion epoch and one-inflight GetStatus). No assertion of existing controller authentication.

Evidence corpus remains in Google Drive RO4 output/evidence; diagnostic CAP5 single-run logs do **not** prove forwarding recovery or any performance improvement.

## 2. Controller identity contract — exact proposed design

**Selected proposed security architecture: a distinct controller-only authenticated gRPC endpoint, not a plaintext bypass and not a global replacement of forwarding RPCs.**

- Define separate `RecoveryControlService.NotifyRecoveryRejoin` server listening on a **different configured port** with `grpc.ssl_server_credentials(..., require_client_auth=True)`. Use a private run-scoped CA trust root and **mutual TLS** (mTLS). The legacy `PeerService` remains on its existing port for frozen dissemination/health behavior; its old `NotifyRecoveryRejoin` handler MUST reject requests (e.g. `PERMISSION_DENIED`) whenever recovery security is enabled, so plaintext cannot bypass mTLS. Feature OFF must reproduce existing baseline behavior. The separate endpoint is a proposal needing deployment/mount/port review, not existing code.
- Client certificate shall carry one unambiguous run-scoped controller principal, **proposed URI SAN** `spiffe://ahbn.local/run/<run_id>/controller/churn`. Server authenticates the **verified** peer-certificate SAN from the gRPC TLS auth context (not request metadata, `reason`, source IP, DNS name or asserted `node_id`); reject absent, ambiguous, expired, wrong-run, wrong-role or unverified principal. The string `spiffe://...` is an identity-format proposal, **not** a claim that SPIFFE/SPIRE is deployed.
- Use a per-run offline/private CA or equivalent reviewed issuer; trusted CA bundle is distributed read-only to the authorized controller and receiver peers. Controller private key is made available only to the controller workload (separate Kubernetes ServiceAccount and restricted Secret/volume or equivalent). Peer server key/cert is distinct and client verifies the expected server identity. Do not put private keys in GitHub/Drive/logs.
- Certificate issue/expiry, run scope, trust bundle revision, controller workload identity, Kubernetes ServiceAccount and Secret mount RBAC, admission policy preventing unrelated workloads from mounting controller credentials, rotation/revocation and negative tests remain required deployment design evidence. TLS cert possession alone cannot prove Kubernetes pod UID.
- NetworkPolicy should additionally allow ingress to the dedicated control port only from controller-labelled pods; this is **defense in depth** and is not proof of authenticated caller identity. Control port must not be exposed via public ingress.
- Only one authorized churn-controller identity per run; if multiple controllers/restarts are possible, enforce a single elected active controller or disable recovery until safe, rather than trusting concurrent emitters. Fail closed on missing auth context, CA material or enforcement configuration.

**Security boundary:** existing Forward and GetStatus remain on their frozen port and channel for this targeted design. The new control endpoint prevents unauthenticated *recovery notifications* only; it does not make all peer RPCs, network communications or the experiment generally secure. No general production-security claim.

## 3. Replacement UID and generation authority contract

- **Source:** The single authorized churn controller reads Kubernetes API `metadata.uid` for `peer-<target>` in the run namespace. It MUST previously record the original UID and confirm replacement UID `!=` old UID; verify pod Ready, expected labels/owner, run-scoped namespace/topology, and peer-local `GetStatus` response with matching `peer_id`, `ready` and `alive`. Authorize minimum RBAC `get/list/watch` pods in its namespace as needed; no recipient trust in free-form strings.
- **Run authority:** Generate a distinct non-reused `run_id` at run initialization and bind it to the immutable topology configuration and the run-scoped CA identity; avoid treating a user-controllable request string as run authority. Confirm this identity lifecycle in orchestration before freeze.
- **Generation:** For this bounded experiment, choose **fail closed on any controller crash/restart or lost in-process generation ledger** instead of assuming a durable counter. Before emitting a replacement marker, the controller records the observed old/new UID transition and increments strictly monotonic `rejoin_generation` per (run,target) only while the same authorized live controller process owns the run. Recipients maintain high-watermark generation/UID per run-target, reject stale, duplicate/conflicting identities as A4 specified, and invalidate old reservations on new verified generations. Counters are not authoritative across restarts.
- **Controller crash:** Recovery-marker issuance and acceptance are DISABLED for the affected run as soon as loss of the active-controller lease / restart epoch is established. A crashed controller cannot be assumed to transmit an invalidation: fail-closed correctness also requires **independent observer enforcement** such as a short-lived signed, run-scoped controller-epoch lease/heartbeat with bounded validity checked at marker acceptance and immediately before any recovery state commit. A plain gRPC mTLS identity reused by a restarted process does **not** detect an epoch change. No valid independently verifiable lease => no marker or delayed reenable. Exact lease issuer, trust, fencing, expiry and Kubernetes isolation must be reviewed before freeze.
- **Re-establish authority:** Simplest proposed option: terminate/release the affected run; issue a genuinely NEW immutable run ID, new control identity/epoch and cleanly initialize receiver/worker state. Do not silently resume old run, reuse the same UID as a new generation, or reset a generation counter while peers preserve old markers. If restarting *within* the same run is required, create a durable, linearizable epoch/generation source with fencing and independent observer verification under a separate amendment; **not authorized by A7**.
- **Important correctness limitation:** A pure process-local counter + controller certificate + sender-supplied restart flag is insufficient. Until independently verifiable fencing/lease mechanics exist, the default is **DISABLED** for the enhanced late-recovery feature. Mere notification arrival does not prove the Kubernetes API UID to receivers; acceptance must be backed by a trusted controller API observation and run-scoped attestation, checked against topology and authenticated sender. Define an integrity-protected binding for `run_id,target,UID,generation,controller_epoch` with replay controls.
- No more than one reservation/late verification per observer-target-generation, no renewal on duplicate markers, independent `GetStatus` still needed, and frozen forwarding and Q-metrics unaffected.

## 4. RPC wire and acknowledgement semantics

**Prefer a new dedicated versioned RPC to eliminate ambiguity**, `RecoveryControlService.NotifyRecoveryRejoin(RecoveryMarkerV1) returns (RecoveryMarkerAckV1)`; preserve existing `PeerService` methods, fields/tags and `Ack` for backward compatibility, with legacy recovery handler refusing recovery-enabled traffic. Do not reuse `DCSOCMaintenanceRequest.reason` for trusted run/UID. A4's proposed additional tags 5–6 describe a compatibility path but should be marked **SUPERSEDED FOR REVIEW** if researcher accepts the dedicated secure RPC; no schema has changed yet.

Proposed request fields with fixed types: `schema_version=1`, `run_id` (nonempty), `observer_peer_id`, `target_peer_id`, `replacement_pod_uid` (Kubernetes UID), `rejoin_generation` (positive uint64), `controller_epoch_id` (nonempty), `authority_evidence_ref` (identifier for independently verifiable replacement observation/epoch lease), `issued_at` (audit only; **not** cross-node TTL authority). An accepted marker is stamped with the **receiver's** monotonic clock; do not trust sender wall clock for local expiry.

Proposed typed outcome enum: `ACCEPTED` (validated marker stored, **not** restored neighbor); `DUPLICATE_NOOP` (same valid pair, no renewal/no extra probe); `REJECTED_UNAUTHORIZED`; `REJECTED_BAD_RUN`; `REJECTED_BAD_TARGET`; `REJECTED_BAD_UID`; `REJECTED_STALE_GENERATION`; `REJECTED_BAD_EPOCH`; `REJECTED_DISABLED`; `REJECTED_INVALID`. For unauthenticated client, terminate RPC with `UNAUTHENTICATED` or `PERMISSION_DENIED`; do not send sensitive internal details to rejected clients. Transport timeout/failure is a separate controller outcome `RPC_ERROR`, not an acknowledgement. `RECOVERY_CONFIRMED` is **not** a notification response value: log only after observer's current-generation, current-epoch GetStatus succeeds and exclusion is removed under lock.

Metrics counters: `notifications_attempted`, `markers_accepted`, `markers_duplicate`, `markers_rejected{reason}`, `transport_errors`, `recovery_probes_started`, `neighbors_reenabled`. Preserve historical `acknowledged` in old CAP5 logs without rewriting it to `recovered`. The controller may aggregate observable peer recovery results only from verified observer events, not from `Ack.ok` or receiver intent.

## 5. Required design verification and negative matrix (NOT RUN)

1. Correct controller SAN/trust/run/authorization accepts a valid marker; wrong certificate, non-controller SAN, invalid CA, expired/revoked cert, missing TLS, legacy/plaintext handler and spoofed metadata all reject without changing availability.
2. Duplicate marker does not replenish W or probe budget; stale/equal-conflict/greater-generation-same-UID and cross-run replay reject; unverifiable UID/target/topology reject.
3. Controller restart/crash, stale controller lease, two concurrent controllers, missing fencing identity, observer restart, lost in-memory watermark and reassigned run identity fail closed; only clean NEW-run initialization re-enables authority. Deterministic fake lease issuer/barriers required to test races.
4. Notification accepted while neighbor available yields `ACCEPTED` and `SKIPPED_NOT_EXCLUDED`; later first new failure can reserve exactly once while marker, lease, generation and epoch remain valid.
5. `Ack` success, typed `ACCEPTED`, transport timeout, malformed/legacy response, and independent `GetStatus` recovery create distinguishable traces; zero false `neighbors_reenabled` from notification alone.
6. Run existing recovery T01–T18 and proposed T19–T38, proto backward compatibility, frozen controller/Q parity, and no extra Forward, duplicate, reward or Q update. Use fake clock/RPC/UID evidence; reserve live proof for separately approved GKE gate.
7. Detailed threat model, secret handling, peer server identity, trust rotation, controller epoch lease/fencing and Kubernetes RBAC/NetworkPolicy manifest review remain prerequisites before final freeze.

## 6. Reviewed alternatives and risk

- **Plaintext notification + NetworkPolicy only:** rejected as a statement of authenticated controller identity.
- **Same insecure PeerService NotifyRecoveryRejoin with new UID fields:** rejected for recovery-enabled path (bypass possible).
- **One process-local generation sequence with controller restart:** rejected; unsafe across restart.
- **Persistent counter without fencing:** insufficient if two controllers can emit concurrently.
- **GKE API UID without attestation to receiver:** does not prove receiver has verified API observation.
- **Controller `ack.ok` interpreted as successful recovery:** rejected.

## 7. Decisions, constraints and next gate

**A7 result: CONTRACT DRAFTED / REVIEW CONDITIONALLY PASS; FORMAL DESIGN FREEZE HOLD.** Approval of A6's direction remains valid. The *new* proposals (dedicated mTLS control service, SAN, separate port, run-scoped CA, independent controller-epoch lease/fencing and typed ACK) require explicit controlled design approval and concrete manifest/authority design checks. Until they are demonstrably enforceable, feature remains off and code unchanged.

**Timing remains UNFROZEN:** W=10 s and Δ=0.25 s are deterministic testing hypotheses; GetStatus deadline=2 s existing, 1 check per generation, 0 retry. A separate freeze decision follows resolved security generation and negative-test contracts.

**All HOLD:** runtime/proto implementation, T19–T38 execution, additional GKE CAP5 canary, D7-F and D8. This gate authorizes no deployment or expenditures. No new scientific performance/causality claim. The Q-AHBN manuscript is under review at Journal of Cloud Computing, unpublished, no DOI.

**Next controlled gate proposed: CAP5-A8 — researcher approval of concrete separate-control-RPC/mTLS identity and independent restart-fencing policy, followed by security-deployment manifest read-only reconciliation; only then timing freeze review.**
