# S19-1 — Terminology, Nomenclature and Unit Consistency Remediation

**Status:** PASS / CLOSED — 2026-10-03

## Objective
Implement only the three S19-0 terminology/nomenclature corrections released for S19-1:
- MI-01 — standardize ControlSim propagation-delay reporting to **seconds** while retaining Kubernetes delay in **seconds**;
- MI-05 — remove unexplained publication-facing **S5** terminology while preserving the frozen canonical AHBN fanout semantics;
- MI-06 — correct the AHBN expansion to **Adaptive Hybrid Broadcast Network (AHBN)**.

No experiment, parameter, statistic, algorithm, evidence, claim authorization, citation architecture, or scientific interpretation is reopened.

## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md`
- `docs/stages/S18_POST_REMEDIATION_RECLOSURE.md`
- `docs/stages/S19_0_MANUSCRIPT_IMPROVEMENT_BACKLOG_FREEZE.md`
- frozen canonical AHBN contract / design authorities
- manuscript `wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`
- manuscript control records
- Drive workspace identities registered at S19-0

Pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`

## Actions performed

### MI-06 — AHBN nomenclature correction
Replaced publication-facing occurrences of:
- **Adaptive Hybrid Blockchain Networking (AHBN)**

with:
- **Adaptive Hybrid Broadcast Network (AHBN)**

Affected active-source locations include the Abstract and Introduction.

### MI-05 — publication-facing S5 terminology normalization
Removed publication-facing `S5` jargon and replaced it with reader-facing terms that preserve the exact frozen semantics, including:
- **canonical bounded fanout actuator**
- **canonical fanout actuator**
- **canonical fanout thresholds**
- **canonical fanout proposal**
- **canonical fanout**

No threshold, mapping, supported fanout value, AHBN proposal rule, or intervention boundary changed.

### MI-01 — ControlSim delay-unit normalization
Replaced generic publication-facing ControlSim delay wording with the source-verified unit **seconds (s)**.

for the corresponding ControlSim quantities.

Explicit ControlSim delay labels were added where needed, including:
- gamma-sensitivity propagation-delay y-axis → **Delay (s)**;
- primary paired-result delay and CI columns → **seconds**;
- Exp13-Q ControlSim table delay column → **Delay (s)**.

Kubernetes delay remains explicitly:
- **Delay (s)**

No numerical delay value changed.

## Verification
Post-write full-source readback confirmed:
- `Adaptive Hybrid Blockchain Networking`: **0 occurrences**;
- authoritative `Adaptive Hybrid Broadcast Network`: present;
- publication-facing token `S5`: **0 occurrences**;
- generic token `units`: **0 occurrences**;
- ControlSim `Delay (s)` labels are present;
- Kubernetes `Delay (s)` remains present;
- corrected Kubernetes value `0.038385 s` remains unchanged.

Scientific numbers, confidence intervals, experiment names, reward/state/action/transition semantics, AHBN fanout thresholds/mapping, Q-AHBN action contract, and S18 evidence roles were not changed.

## Manuscript commits
- `1c391860200c1b1f9243df435f595b730b6f92af` — AHBN nomenclature, S5 terminology and primary ControlSim unit normalization.
- `3b0a03460abac71365d44f580d036b23aa538ee4` — historical MI-01 edit that labelled primary paired-table ControlSim delay/CI in rounds; superseded by the source-verified seconds correction.

## Result
**S19-1 = PASS / CLOSED.**

## Next permitted task
**S19-2 — RO2 → AHBN → Q-AHBN Progression Clarification** is the next and only released action.

S19-2 is restricted to MI-03. It may improve reader-facing explanation of the frozen research progression but may not introduce new evidence, a new literature claim, a thesis-style expansion, or any stronger performance/novelty claim than the S18 contract permits.


## MI-01 source-level verification and corrective re-closure — 2026-10-03
MI-01 was reopened after comparison with the previous AHBN Scientific Reports manuscript. Verification traced Q-AHBN2 ControlSim to the pinned canonical AHBN implementation `wwiras/ahbn@936a79480bc1252c79b6ee01f65c88c740af2844`. `MetricsCollector.summarize_message()` computes `propagation_delay = max(first_seen_times) - created_at`; `Simulator.inject_message()` records `created_at=self.clock`; and `Simulator.send_message()` advances event time by `base_delay + uniform(0,jitter) + extra`. The canonical regression record explicitly classifies this as simulation-time propagation delay. The AHBN Scientific Reports manuscript reports the same controlled-simulation metric in seconds (for example Exp07/Exp08(sim)/Exp09 labels use `Propagation Delay (s)`).

Decision: publication-facing ControlSim propagation delay is **seconds (s)**, not rounds. Kubernetes remains **seconds (s)**. The manuscript was corrected without changing any numerical value or scientific interpretation. MI-05 and MI-06 remain valid and unchanged. **S19-1 remains PASS / CLOSED after corrective re-verification.**


## MI-01 methodological rationale for future reference — 2026-10-03

This note preserves the researcher's earlier methodological justification and its boundary. It is supporting rationale for future manuscript/thesis explanation; it does **not** alter the completed experiments, numerical evidence, or S18/S19 claim contract.

### Why physical simulation-time units are methodologically defensible
Blockchain discrete-event simulators commonly represent network/event timing using physical time units and schedule future events by adding modeled transmission/processing delay to the current simulation time. Relevant examples identified during the earlier rationale review include SimBlock (Aoki et al.) and BlockSim, both of which use discrete-event blockchain simulation and compare simulation behaviour with real/empirical blockchain systems. The methodological implication for AHBN/Q-AHBN2 is that an event-driven ControlSim clock may legitimately be defined in a physical time unit rather than interpreted as propagation rounds.

This is consistent with the verified canonical AHBN code path:
- message creation time is the simulator clock;
- transmission reception is scheduled at `now + delay`;
- `delay = base_delay + uniform(0,jitter) + extra`;
- first-seen time is an event timestamp;
- `propagation_delay = max(first_seen_times) - created_at`.

Accordingly, the metric is elapsed **simulation time**, not a hop/round counter.

### Controlled-simulation interpretation
The controlled simulator is used primarily to compare dissemination behaviour under prescribed conditions. Its timing scale should therefore be described as a controlled timing model rather than as a claim that the configured per-hop delay reproduces a particular Internet-wide blockchain WAN.

The intended defence is:

> The simulation uses an explicitly defined physical-time scale for controlled comparative dissemination experiments. The nominal link-delay and jitter parameters define that simulation scale; they are not asserted to reproduce a specific geographical blockchain WAN. Absolute operational behaviour is evaluated separately in the Kubernetes environment.

This preserves the scientific distinction between:
- controlled event-driven simulation for relative algorithmic comparison; and
- Kubernetes for complementary cloud-native operational realization/observability.

It does not authorize pooling, equivalence, literal replication, or a claim that ControlSim predicts absolute Kubernetes latency.

### Important dimensional-consistency boundary
The earlier rationale also distinguished **choosing a physical unit** from **justifying the numerical parameter values**. Literature precedent for millisecond-based blockchain simulation does not by itself prove that `base_delay = 1.0` represents a typical WAN link.

Before any future document explicitly freezes `base_delay = 1.0 ms` and `jitter = 0.2 ms`, every time-dependent quantity that interacts with the ControlSim clock should be dimensionally reconciled, including at minimum:
- base delay and jitter;
- overload/extra-delay terms;
- processing-delay/heterogeneity terms;
- failure/churn event timing;
- recovery timing;
- latency-reference normalization; and
- any controller or experiment timing thresholds.

Only after that audit should a specific millisecond parameterization be treated as formally frozen. This note therefore supports the **methodological legitimacy** of physical-time/millisecond simulation, while deliberately not retroactively inferring units solely from the numeric constants.

### RO2 → AHBN/Q-AHBN methodological progression
For future thesis explanation, the distinction may be expressed as:
- RO2 characterization may use abstract propagation structure/round-based reasoning where appropriate;
- AHBN/Q-AHBN ControlSim uses event-driven elapsed simulation time to evaluate adaptive dissemination under controlled conditions;
- Kubernetes measures actual runtime elapsed time in the deployed cloud-native environment.

These are complementary levels of evaluation and should not be conflated. The source-verified MI-01 publication decision remains **ControlSim propagation delay = seconds (s)** for the current manuscript; any future decision to express the same simulation clock in milliseconds would be a unit rescaling only if the underlying timing contract is explicitly and consistently defined.
