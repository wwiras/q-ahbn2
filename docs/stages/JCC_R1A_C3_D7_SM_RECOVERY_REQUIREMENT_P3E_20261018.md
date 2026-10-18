# JCC-R1A-C3-D7-SM — P3E Recovery-State Requirement and Local Regression Plan

**Date:** 2026-10-18
**Classification:** NONFORMAL / DESIGN-ONLY / APPROVAL PENDING
**Experiment context:** Exp11-style node churn, seed 42; not a formal Exp11 result.
**Authority:** GitHub text/code contracts; immutable evidence in Drive/local output.
**Source:** P3B/P3C/P3D audit in `docs/stages/JCC_R1A_C3_D7_SM_POSTRUN_CAUSAL_P3_20261017.md`; deployed source commit `68aa0830873b9d8cb231d9a27bff1bbc19477128`.
**Prohibition:** No code changes, GKE rerun, formal D7-F execution, D8 execution, or frozen algorithm changes under this gate.

## 1. Evidence and bounded diagnosis

P3B SHA256 `fa735635c7cb8655a450ad1d1cf503864528b59ea2b2a629d144373efeddf0b4` independently reconciled. P3C: DC-SoC source briefly forwarded m9/m10 to replacement core4 and later failed m11–m18 to peer0; AHBN source 240 decisions, of which 177 cluster decisions had no eligible targets, while peer0 remained in its unavailable list for m10–m240.

Pinned `peer.py`: RPC errors add destination to `unavailable_neighbors`; successful or duplicate acknowledgements remove it. Structured/cluster and DC-SoC target selection excludes unavailable peers *before* RPC. Pinned `dcsoc_maintenance.py`: `set_availability` and `sync_peer` update maintenance structural fields including parent/children but do not clear or reconcile `unavailable_neighbors`. This is a code-confirmed synchronization gap, not a proven full runtime root cause. Frozen AHBN §8 specifies bounded eligible realization, not a universal recovery probe policy.

## 2. Proposed external recovery requirement (NOT YET APPROVED)

**RR-01 — Confirmed re-eligibility.** If a peer previously excluded as unavailable is independently confirmed reachable by an explicitly authorized recovery signal, its *local forwarding availability* may transition from unavailable to available. After that transition, the existing strategy-specific eligibility and target realization are applied unchanged. A Kubernetes pod becoming Ready or a topology `rejoin` event by itself is not proof of reachable peer RPC.

**RR-02 — Verification and authority.** Define an independent, bounded, observable health-check/acknowledgement path or a demonstrably authenticated transport recovery signal; do not silently treat a structural `sync_peer` call as proof of RPC availability. An availability notification may request a check, not unconditionally clear exclusion. Specify the health-check endpoint, trust boundary, failure timeout, and maximum retry frequency before implementation.

**RR-03 — State transition discipline.** Use one synchronized state-update operation for unavailable-set add/remove and corresponding churn observation exactly once per actual transition. Ignore repeated identical signals (idempotency). Guard against a late positive check overwriting a newer negative result (generation/epoch or comparable ordering). Preserve clear source and reason in logs.

**RR-04 — Strategy neutrality.** Recovery handling is infrastructure/transport availability management, not an AHBN mode/fanout override or a Q-AHBN2 action. Do not change EWMA, score, mode threshold, S5 fanout, Q table, reward, actions, or realized-target bound. No special forwarding target may be appended beyond the eligible set or requested budget. DC-SoC structural repairs remain separate and traceable.

**RR-05 — Evidence.** Log peer ID, target ID, recovery trigger, observed health-check result, previous/new unavailable state, structural generation (where applicable), check generation, and first subsequent forwarding attempt/outcome. Never equate `rejoin`, Ready, or a cleared exclusion with successful end-to-end delivery.

## 3. Proposed minimal implementation scope (not authorization)

1. Add a small transport availability manager or equivalent helper used by `PeerState` to reconcile `unavailable_neighbors`, with a lock and ordered transitions. Keep scientific controller files untouched.
2. Add a bounded health-confirmation path for previously unavailable neighbors, outside ordinary target selection. **Design decision pending:** whether to use existing gRPC service, a dedicated lightweight RPC, or a verified external health signal; audit protobuf/API compatibility first.
3. Wire the recovery trigger into the appropriate lifecycle/maintenance adapter without conflating DC-SoC structural `set_availability` with verified RPC reachability. Ensure AHBN and Q-AHBN2 share the same neutral availability semantics.
4. Add structured recovery-state trace fields; keep existing scientific metric semantics unchanged.
5. Do not modify the deployed-commit evidence or retroactively reinterpret the original nonformal run.

## 4. Local regression test matrix (all offline, no GKE)

| ID | Scenario | Acceptance criterion |
|---|---|---|
| T01 | First RPC failure | Destination excluded once; one leave observation |
| T02 | Duplicate failure | No duplicate leave observation |
| T03 | Structural DC-SoC rejoin with failed health check | Topology may update; destination stays excluded |
| T04 | Verified recovery after exclusion | Destination removed once; one join observation |
| T05 | Repeated positive signal | Idempotent, no duplicate join |
| T06 | Late positive after newer failure | Stale signal cannot clear newer exclusion |
| T07 | AHBN cluster source, unavailable head | Zero eligible targets, no forced forwarding |
| T08 | AHBN cluster source, verified recovered head | Head becomes eligible under original mode/budget rules |
| T09 | DC-SoC parent replacement/rejoin | Selected targets follow current parent and availability, never a stale parent |
| T10 | Gossip and Q-AHBN2 eligibility | No algorithm/action changes; same recovered-set semantics |
| T11 | No health confirmation | Exclusion retained; no false recovery |
| T12 | Controller parity and deterministic seed | Existing AHBN and Q-AHBN2 frozen parity fixtures unchanged |

**Execution controls:** run `python -m py_compile`, focused unit tests with fake gRPC and deterministic clocks, preexisting frozen parity tests, and negative/failure-injection tests. Collect exact code commit, command logs, test summaries, SHA256 of generated output. No Kubernetes, network deployment, or cloud charges.

## 5. Gates and release criteria

- **P3E requirement drafting:** PASS (proposal recorded).
- **Recovery signal/protocol design:** PENDING explicit approval and API audit.
- **Implementation:** NOT AUTHORIZED.
- **Local tests:** NOT RUN; NOT AUTHORIZED as a code-change gate.
- **Root cause of observed D7-SM recovery:** HOLD.
- **Formal D7-F:** 0/25 HOLD.
- **D8:** HOLD.

Approval must specify the selected recovery confirmation mechanism, synchronization/order model, allowed implementation files, exact test acceptance criteria, and a rollback plan. Only after independent local regression and contract-parity evidence may a separate gate consider GKE; no automatic release.

**Publication guard:** Q-AHBN manuscript is under peer review at *Journal of Cloud Computing*; not published; no DOI.
