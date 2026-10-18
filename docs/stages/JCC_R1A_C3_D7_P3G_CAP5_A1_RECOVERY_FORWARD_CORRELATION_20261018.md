# P3G-CAP5-A1 — Historical recovery-to-forwarding correlation audit (2026-10-18)

## Decision

**NONFORMAL GKE EXECUTION / CLEANUP PASS; RECOVERY-CORRECTION CAUSAL VERIFICATION NOT ESTABLISHED — HOLD.** Do not use this canary as formal D7-F/D8 evidence or proof of corrected dissemination. This is an evidence audit, not a new run.

## Frozen evidence source and scope

Canonical raw data: [CAP5 Drive folder](https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX) / `run/`, 20261018T135743Z-P3G-CAP5-ahbn-seed42. Audited `controller.log`, `peer_stream.jsonl`, `final_snapshot.jsonl`, and `logs.jsonl`. Run: AHBN, seed 42, N=20, churn targets 0/5/10/15, 240 injections, approved image digest `sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`. Controller pod archive confirms spec image, actual runtime `imageID`, zero restarts and exit 0. The observed cleanup status was PASS, experiment and cleanup exit code 0, namespace deletion receipt recorded. Local worktree restoration and post-run independent namespace query were not audited here.

**Parsing rule:** `peer_stream.jsonl` contained 4,156 individually parsed JSON records with 128 non-JSON/fragments (due to merged log output); `final_snapshot.jsonl` 3,593 parsed, 90 unparsed, `logs.jsonl` 8,015 parsed, 220 unparsed. These three sources overlap: NEVER sum their counts as independent message events. `peer_stream.jsonl` is the basis for the raw counts below. `logs.jsonl` used only as a presence/absence cross-check. A zero count is "not observed in collected logs", not proof that runtime never emitted an event.

## Rejoin-to-forwarding matrix (rejoin reference = controller notification timestamp)

| Returned target | Notification ACKs | Valid `recovery_probe` in collected logs | Post-notification successful forwards to target (peer_stream) | Subsequent failure evidence | Scientific classification |
|---|---:|---:|---:|---|---|
| 0 | 13/13 | 0 | 1 (peer1, message m8, +0.11 s) | first forward failure +0.50 s, later 10 distinct availability exclusions | **Partial forwarding only; recovery not confirmed** |
| 5 | 3/4 | 0 | 2 (peer8, messages m206 and m227; +51.1/+59.5 s) | no recorded forwarding failures to target in this stream; missing notification to peer0 (`_InactiveRpcError`) | **Successful ordinary forwarding demonstrated, not restoration of an excluded link** |
| 10 | 2/2 | 0 | 0 | peer8 forwarding failed +3.76 s; availability exclusion recorded | **Recovered-neighbor forwarding not demonstrated** |
| 15 | 2/2 | 0 | 0 | four post-notification forward failures; peer1 excluded target +5.24 s | **Recovered-neighbor forwarding not demonstrated** |

Notifications: 20 accepted / 21 attempted in controller log, but accepted notification is NOT successful GetStatus confirmation. Four `churn_rejoined` controller entries denote infrastructure rejoin, not transport state restoration.

**Critical causal limitation:** The first recorded `forward_failed` exclusions for targets 0, 10 and 15 occur **AFTER** their rejoin notifications. At notification time no corresponding successful rollback of earlier observed exclusions is recorded. On a receiver for which the target was not yet marked unavailable, the P3G probe's precondition (`target in unavailable_neighbors`) can prevent probing. For those receivers, later forwarding failures can place the target in unavailable state with no further rejoin notification. This is a plausible event-ordering explanation supported by observed timing and the code's guard, not an experimentally proven unique root cause.

## Exactly-once and scientific metrics boundaries

- `recovery_probe` event: **0** observed in all three overlapping saved peer-log artifacts (`peer_stream`, `final_snapshot`, `logs`). There is no observed `recovery_probe.recovered=true` or epoch/target evidence for exactly-once recovery.
- `peer_availability` in the primary `peer_stream`: 447 events; changed=True occurs **12 times, all `forward_failed` exclusions**, with no changed=True join in the collected stream. Ordinary `forward_ack` entries (411, changed=False) are not recovery transitions.
- `k7_forward_attempt` (416) and `forward` (306) in primary stream are not complete broadcast-level outcome metrics; duplicate/partial log capture must be accounted for. Do not equate post-notification ordinary forwarding with successful re-enablement after an exclusion.
- No independent reproducibility check, per-message delivery-ratio result, or source/pod log completeness guarantee was established in this audit. No performance gain claim.
- Preserve raw files immutably; do not modify approved image or frozen AHBN/Q-AHBN2 parameter contracts.

## Follow-on review / HOLD boundary

The current code logs `p3g_rejoin_notification` at the controller and only triggers `recovery_probe` where target is currently marked unavailable. A read-only P3G-CAP5-A2 should audit timing of failed-forward exclusions relative to controller rejoin notifications, reason about transient deadline failures, and determine whether a narrowly scoped **future** trigger/late-failure verification mechanism is necessary. This record **does not authorize any new GKE run or runtime patch**. Offline design review and tests first; obtain separate approval for any live retest.

**Gate:** P3G-CAP5-A1 evidence review PARTIAL / recovery-effectiveness HOLD; D7-F HOLD; D8 HOLD.

Manuscript status: *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* submitted to Journal of Cloud Computing, under peer review, unpublished, no DOI.
