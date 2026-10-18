# P3F-M1 — Pre-implementation Design Review (2026-10-18)

**Status:** REVIEWED / PROPOSED SETTINGS / IMPLEMENTATION HOLD. No tests executed, no implementation approved by this record.

## Verified implementation facts
- `gke/app/controller_shared.py` calls `GetStatus` with 2 s timeout.
- `gke/app/peer.py` uses 3 s timeout for `Forward`; forwarding acknowledgements and errors directly mutate `unavailable_neighbors` and emit join/leave observations.
- `gke/app/dcsoc_maintenance.py` tracks `structural_generation` separately; `sync_peer` changes structural fields, not transport availability.
- Existing P3F recommends `GetStatus` but leaves timeout, trigger authority, retry and epoch rules unfrozen.

## Proposed bounded implementation contract (subject to user approval)
1. **Timeout:** configurable 2 s for recovery `GetStatus` (consistent with existing status checks), not an empirically optimized value. One attempt per authoritative event, no automatic retries, one in-flight probe per target.
2. **Trigger:** only explicit, recorded topology rejoin/availability notification from the existing authorized lifecycle pathway; notification requests a check, never itself clears exclusion. Require target currently excluded and still structurally permitted. No periodic fallback.
3. **Positive check:** successful `GetStatus`, matching numeric peer ID, ready and alive both true, current epoch unchanged, current topology permits target. Plaintext gRPC does not authenticate identity cryptographically.
4. **Synchronization:** per-neighbor monotonic availability epoch under a common lock; increment on every observed failure (including repeated failure while already unavailable), structural invalidation and feature disable. Snapshot epoch when probe starts. Apply positive transition only if epoch unchanged and target still excluded; exactly one join observation per actual unavailable-to-available transition. Leave observation only on first available-to-unavailable transition. All forwarding ACK/error mutation sites must use the same transition helper; no unsynchronized writes. Use deterministic concurrency tests.
5. **Metric isolation:** probes cannot invoke `Forward`, increment forwarding/delivery/duplicate counters or Q reward, or change AHBN/Q controller contracts. Recovery availability join/leave observations are allowed exactly once per actual transition; document their EWMA implications instead of claiming observations are unchanged.
6. **Rollback:** disabled-by-default feature flag; disable prevents new probes and invalidates in-flight probes. Restore legacy probe-free operation without reverting recorded observations or rewriting historical evidence. Revert implementation commit if needed; require parity rerun.
7. **Evidence:** test T01–T18 on actual integrated `PeerState` using fake gRPC and deterministic clocks, frozen parity, exact commit, full command logs, SHA256. No PASS until tests actually run.

## Open decision
Approve the above scope and values before modifying runtime code. GKE and formal D7/D8 remain HOLD. Journal of Cloud Computing manuscript is under peer review, not published, no DOI.
