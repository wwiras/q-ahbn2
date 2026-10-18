# CAP5-A11 — Offline deterministic recovery timing approval (2026-10-18)

**CONTROL DECISION: PASS / VALUES FROZEN FOR DETERMINISTIC OFFLINE VALIDATION ONLY. IMPLEMENTATION AND EXECUTION HOLD.**

## Authority
- Researcher expressly adopts the A10 recommendation: approve **W = 10.0 seconds**, **Δ = 0.25 seconds** for deterministic offline checks, not as optimal settings or verified performance improvement.
- Predecessor: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A10_MINIMAL_WIRE_RESTART_TEST_TIMING_REVIEW_20261018.md`, commit `b6db5fa4e3940c9e2ab8a93e379de5a9592cccdc`. A9 recovery-correctness scope reset remains controlling. A7 and A8 remain preserved as historical, superseded security-scope records.
- GitHub control/text authority; Drive evidence corpus `https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`, output/evidence. No Drive results or experiment artifacts modified by A11.

## Approved deterministic timing contract

| Control | Approved offline fixed value | Exact interpretation |
|---|---|---|
| Marker lifetime W | **10.0 s** | Receiver local monotonic clock, starting at first valid marker receipt; require `now < expires_at` |
| Late-failure settling delay Δ | **0.25 s** | One deferred check eligible from a newly observed exclusion at `failure_monotonic + 0.25` |
| GetStatus timeout | **2.0 s** | Existing single peer-local RPC deadline, no retry |
| Late checks | **1 maximum** per observer,target,replacement UID,generation | Same marker replay cannot refresh window or reserve more work |
| In-flight target probes | **1 maximum** | Existing epoch/inflight guard; no new Forward from recovery path |
| Automatic retries | **0** | Preserve finite, single-shot behavior |

**Boundary rules:** A marker at exactly `expires_at` is expired; a worker cannot start before Δ; recheck run, target, UID/generation, exclusion epoch, eligibility, feature/lifecycle and expiry immediately before probe AND under lock before any join. Reject success if expiry occurs during RPC. New failure or new generation invalidates stale workers. Normal Forward ACK may already clear exclusion; avoid duplicate join.

## Scope and evidence qualification
These numbers are **fixed engineering parameters for repeatable offline testing**, selected for coverage of an observed seconds-scale late-failure case (not a statistical estimate). They are **not calibrated/optimized**, not GKE-validated, and not evidence of increased propagation performance or delivery ratio. Real-world scheduling jitter and multi-pod timing uncertainty remain untested.

Use A10's additive existing-RPC wire proposal and recovery-correctness tests T19–T38 after a **separate implementation authorization**. Current recovery feature default remains OFF. Frozen AHBN EWMA, mode and fanout S5, Q-AHBN2 learner/reward and metric definitions unchanged. No cryptographic/security-engineering requirements are introduced.

## Release and status
- CAP5-A9 recovery-correctness scope PASS.
- CAP5-A10 minimal wire, lifecycle and offline test specification PASS.
- **CAP5-A11 deterministic offline W/Δ timing approval PASS/FROZEN (offline validation only).**
- **Implementation, protobuf edits, T19–T38 execution, additional GKE, D7-F, D8 HOLD.**
- Next gate: **CAP5-A12 — separately authorize integrated recovery implementation and deterministic offline regression testing**, with logs, source SHA, parity and SHA256 evidence; no GKE without later distinct approval.
- Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* submitted to Journal of Cloud Computing; **under peer review**, unpublished, no DOI.
