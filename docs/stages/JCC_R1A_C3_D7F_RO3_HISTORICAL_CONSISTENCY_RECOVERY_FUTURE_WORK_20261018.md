# D7-F — Historical AHBN2-GKE consistency and recovery-investigation closure (18 October 2026)

**Researcher-approved disposition: CAP5 recovery investigation PASS/CLOSED for scientific interpretation; proposed recovery enhancements DEFERRED TO FUTURE WORK. D7-F historical consistency review RELEASED, not yet a formal experiment PASS.**

## Scope and scientific claim
The investigator's interpretation is that message transmission and neighbor membership/availability update windows overlap with planned leave/rejoin events. Thus a message may encounter a temporarily unavailable neighbor, leading to missing forwards and reduced delivery. This is a legitimate dynamic-network experimental observation, not automatically a protocol defect or an invalid experiment. The diagnostic timing and code evidence are consistent with this explanation, but do not isolate it as the sole cause; record alternate possible contributors. Do not claim successful enhanced recovery, universal reliability, or causal proof without additional data.

The recovery design records CAP5-A7 through CAP5-A11 are retained as provenance, *not* requirements for RO3/RO4 evaluation. Security-scope design A7/A8 superseded; proposed marker lifetime W=10 s, delay Δ=0.25 s and T19-T38 are not part of the current experiment. CAP5-A12 implementation is cancelled/deferred; no new recovery code/protobuf/behavior should be merged into the comparative method. Follow historical AHBN2-GKE behavior, not a retroactively repaired implementation. Document improved neighbor-awareness, rejoin synchronization and bounded recovery as **future work** for thesis and both relevant papers, subject to each venue's revision policies.

## Historical RO3 GKE baseline directly inspected
- Source repository: https://github.com/wwiras/ahbn2_gke
- K7 v2 contract: `docs/K7_ahbn2gke_exp11v2.md`
- K7 config: `experiments/k7_exp11.yaml`
- K6 config: `experiments/k6_exp10.yaml`
- K5 scientific interpretation: `docs/K5_exp08_final_scientific_interpretation.md`
- RO3 GKE raw outputs Drive: https://drive.google.com/drive/folders/1QsEqOnB8ltNbOwsXlHWsNTKJZZyxppJa?usp=sharing (outputs folder).

K7 v2 documented N=20 BA(m=2), seeds 42–46, fixed churn peers 0/5/10/15, shared absolute injection/churn epoch, churn offsets +1/+26/+51/+76 seconds, 240 messages per run at 0.4-second planned intervals, 4 churn events, and logging of late injection/forwarding attempts. The runner preserves unchanged AHBN controller and peers, does not add retries, larger timeouts, participant removal, recovery behavior or scheduling changes. Expected unavailable/deadline/connection failures are observations; unhandled controller errors, malformed artifacts, incomplete schedules or failed validations are actual orchestration failures. **Do not assume these exact parameters are automatically Q-AHBN2's already frozen contract; confirm seed-by-seed/treatment matching against its registered benchmark before executing or asserting equivalence.**

K5 interpretation records AHBN lower delivery (0.6435, 0.6730, 0.6250, 0.6815 across overload settings) alongside fewer forwards; report delivery sacrifice and efficiency trade-off openly, not as proof of maintained reachability. Controller/topology/runtime timing causal contributions were not independently isolated.

## Next D7-F historical comparison: mandatory evidence checklist
1. Identify original exact-commit and image-digest Q-AHBN2 evaluation, experimental family, strategy, topology N/BA(m), seeds, fixed churn targets, schedule epoch/offsets, workload/message interval, settle/grace conditions and observed delivery denominator.
2. Compare explicitly with K7 v2 and other applicable K6/K8 records (do not conflate Exp08 overload with Exp11 churn).
3. Preserve controlled experimental conditions and original result logs; document unavoidable differences as scope limitations rather than quietly altering treatment. Retain existing fixed AHBN/Q controller contracts.
4. Separate (a) scheduler/interruption/validation failure from (b) legitimate loss during a planned churn window and (c) degraded but valid delivery. Only (a) is a test invalidity on its own.
5. For each run, verify planned and observed leave/rejoin, message injection, peer state/neighbor availability updates, attempted/failed/successful forwards, readiness and delivery. State timing-consistency and alternative explanations with proportionate certainty.
6. Compare GKE runtime results only to GKE runtime baselines under matching conditions; do not substitute ControlSim simulated-time findings as wall-clock reference.
7. Do not use the proposed recovery enhancement, additional retries or post-hoc removal of lost messages to improve reported ratios.
8. Existing researcher's historical criterion of >=80% for a specific K8s acceptance context must not be silently converted into a universal scientific-validity criterion; make the relevant pre-registered gate criterion explicit.
9. Preserve code/report/source hashes and raw evidence before any formal D7-F verdict; later GKE execution requires separate authorization.

## Publication and future-work tracking
- RO3 AHBN manuscript *Adaptive Hybrid Broadcast Network for Balancing the Latency–Duplication Trade-off in Blockchain Dissemination Under Cloud-Native Infrastructure Dynamics*: **under peer review at Scientific Reports**, unpublished, no DOI. Source repo https://github.com/wwiras/SRpt . Avoid editing a submitted paper solely on the strength of a plausible explanation.
- RO4 Q-AHBN manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions*: **under peer review at Journal of Cloud Computing**, unpublished, no DOI.
- Thesis master repository: https://github.com/wwiras/MUM_FIT_ThesisWira . Proposed future-work wording (not a measured result): “The present experiments retain the configured churn and propagation timing without post hoc recovery modifications. Future work could evaluate how asynchronous neighbor-state awareness and rejoin synchronization affect delivery, while preserving a comparable disturbance schedule.”
- Control repo for this stage: https://github.com/wwiras/q-ahbn2 .

**Gate decision:** CAP5 recovery investigation PASS/CLOSED (research interpretation only); recovery implementation deferred to future work; D7-F historical-parity/readiness comparison NEXT; D8 waits on D7-F. No code changes, no new GKE run, and no experimental evidence rewritten.
