# S19-1 — Terminology, Nomenclature and Unit Consistency Remediation

**Status:** PASS / CLOSED — 2026-10-03

## Objective
Implement only the three S19-0 terminology/nomenclature corrections released for S19-1:
- MI-01 — standardize ControlSim propagation-delay reporting to **rounds** while retaining Kubernetes delay in **seconds**;
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
Replaced generic publication-facing ControlSim delay wording:
- “units”

with:
- **rounds**

for the corresponding ControlSim quantities.

Explicit ControlSim delay labels were added where needed, including:
- gamma-sensitivity propagation-delay y-axis → **Delay (rounds)**;
- primary paired-result delay and CI columns → **rounds**;
- Exp13-Q ControlSim table delay column → **Delay (rounds)**.

Kubernetes delay remains explicitly:
- **Delay (s)**

No numerical delay value changed.

## Verification
Post-write full-source readback confirmed:
- `Adaptive Hybrid Blockchain Networking`: **0 occurrences**;
- authoritative `Adaptive Hybrid Broadcast Network`: present;
- publication-facing token `S5`: **0 occurrences**;
- generic token `units`: **0 occurrences**;
- ControlSim `rounds` labels are present;
- Kubernetes `Delay (s)` remains present;
- corrected Kubernetes value `0.038385 s` remains unchanged.

Scientific numbers, confidence intervals, experiment names, reward/state/action/transition semantics, AHBN fanout thresholds/mapping, Q-AHBN action contract, and S18 evidence roles were not changed.

## Manuscript commits
- `1c391860200c1b1f9243df435f595b730b6f92af` — AHBN nomenclature, S5 terminology and primary ControlSim unit normalization.
- `3b0a03460abac71365d44f580d036b23aa538ee4` — explicit primary paired-table ControlSim delay/CI labels in rounds.

## Result
**S19-1 = PASS / CLOSED.**

## Next permitted task
**S19-2 — RO2 → AHBN → Q-AHBN Progression Clarification** is the next and only released action.

S19-2 is restricted to MI-03. It may improve reader-facing explanation of the frozen research progression but may not introduce new evidence, a new literature claim, a thesis-style expansion, or any stronger performance/novelty claim than the S18 contract permits.
