# P3F — Recovery Mechanism Selection and Contract Review

**Date:** 2026-10-18
**Classification:** NONFORMAL / READ-ONLY CONTRACT REVIEW / IMPLEMENTATION HOLD
**Context:** D7-SM Exp11-style churn smoke (not formal Exp11); pinned deployed source `68aa0830873b9d8cb231d9a27bff1bbc19477128`.
**Prior gate:** `docs/stages/JCC_R1A_C3_D7_SM_RECOVERY_REQUIREMENT_P3E_20261018.md`.

## 1. Existing protocol verified at deployed revision

`gke/app/peer.proto` defines `rpc GetStatus(Empty) returns (StatusReply)`. `StatusReply` includes `ready`, `alive`, `peer_id`, `is_cluster_head`, `mode`, `fanout`, and `seen_count`. In `gke/app/peer.py`, `PeerService.GetStatus` returns `ready=self.state.ready`, `alive=not self.state.failed`, `peer_id=self.state.peer_id`. Existing `gke/app/controller_shared.py` uses `GetStatus` with a timeout; therefore the protocol is already used operationally.

`GetStatus` is a candidate for *application-level peer RPC reachability*, not a guarantee that a subsequent `Forward` will succeed. The channel in pinned code is `grpc.insecure_channel`; no cryptographic peer authentication is established by the inspected code. A matching peer ID is a necessary check but is not a cryptographic proof of identity.

## 2. Mechanism selection (recommended, not approved for implementation)

**P3F-M1: Bounded on-demand `GetStatus` recovery probe.** Retain existing protobuf and existing service; no new RPC, no controller/learner modifications. When an already-excluded neighbor has a relevant rejoin/availability signal, enqueue at most one bounded probe for that peer. Permit a positive local transition only when:
1. RPC completed successfully within configured timeout;
2. returned `peer_id` matches requested peer;
3. `ready=true` and `alive=true`;
4. response belongs to the current local failure/recovery generation, so a late success cannot undo a newer failure;
5. the peer remains permitted by the current topology and any explicit active/inactive state.

No positive confirmation: retain exclusion. Probe does not forward a scientific message and must not be counted as a dissemination forward, delivery, duplicate, or Q reward. Successful probe changes only local availability; normal mode-specific eligible target selection decides later forwarding. A rejoin event, pod Ready status, or structural `sync_peer` alone must not clear the exclusion.

**Trigger and bounds proposed for separate approval:** event-triggered on an authoritative rejoin/availability notification, one in-flight probe per (source,target), finite timeout and limited retries, no background unbounded polling, deterministic test clock. Exact timeout/retry settings are **UNFROZEN** and require review against the churn timing. To recover from missed notifications, a separate explicitly bounded periodic fallback may be evaluated later; not included in this minimal proposal.

## 3. Alternatives reviewed

| Candidate | Assessment |
|---|---|
| Existing `GetStatus` RPC | **SELECTED FOR PROPOSAL**: app-level readiness, alive, ID; no proto change |
| New dedicated health RPC | Not necessary yet; introduces protobuf/client/server compatibility burden |
| Kubernetes pod Ready or maintenance `rejoin` only | Rejected as sole proof: neither guarantees successful application RPC |
| Probe via `Forward` | Rejected: alters message dissemination/metrics and can cause unintended duplicate delivery |
| Clear exclusion immediately on `sync_peer` | Rejected: structural update is not reachability evidence |

## 4. Contract, safety and compatibility controls

- **Scientific invariants:** canonical AHBN observations/EWMA/score/mode/S5 fanout unchanged; Q-AHBN2 81x5 state/action/reward/learning unchanged; DC-SoC topology repair algorithm unchanged; `k_real <= min(k_request, |N_e|)`.
- **RPC compatibility:** existing `GetStatus` and `StatusReply` fields; no protobuf schema edit planned. Client must handle `UNAVAILABLE`, `DEADLINE_EXCEEDED`, malformed/mismatched identity, `ready=false`, `alive=false`.
- **Ordering:** lock local unavailable state, track failure epoch/generation; a stale positive result cannot override a newer failure; one leave/join observation per actual state transition.
- **Security boundary:** current plaintext/insecure gRPC is acceptable only as an existing *test-environment assumption*, not an authenticated general-production recovery guarantee. Any claim of authenticated peer identity requires a separate security design.
- **Failure visibility:** log probe trigger, start/end, target, result, peer ID, readiness/aliveness, timeout/error, epoch, before/after availability, and next actual forwarding outcome.
- **Rollback:** feature disabled by default until tests/approval; rollback must restore original forwarding eligibility behavior and frozen parity; no change to original evidence.

## 5. Offline verification before any GKE consideration

Execute P3E T01–T12 with fake gRPC and deterministic clocks, adding:
- **T13:** positive response with wrong `peer_id` is rejected;
- **T14:** `ready=false` or `alive=false` is rejected;
- **T15:** timeout, `UNAVAILABLE`, `DEADLINE_EXCEEDED` keep exclusion;
- **T16:** recovery probe emits no `Forward` RPC and changes no delivery/duplicate/forward/reward metric;
- **T17:** concurrent recovery probe and new failure respects generation ordering;
- **T18:** disabled feature preserves deployed baseline semantics and controller parity.

Retain source commit, command output, exact local test logs, and SHA256. **No implementation or tests authorized under P3F.**

## 6. Controlled decision

- Existing protocol/interface audit: **PASS**.
- Mechanism selection: **P3F-M1 RECOMMENDED / APPROVAL PENDING**.
- Security and transport assumptions: **LIMITED to existing nonproduction test environment**.
- Timeout, retry count, trigger authority and epoch semantics: **DESIGN DETAILS PENDING**.
- Implementation: **HOLD**.
- Recovery runtime root cause: **HOLD**.
- Formal D7-F: **0/25 HOLD**; D8: **HOLD**.
- GKE spending: **NOT AUTHORIZED**.

The manuscript is under peer review at *Journal of Cloud Computing*, unpublished, no DOI.
