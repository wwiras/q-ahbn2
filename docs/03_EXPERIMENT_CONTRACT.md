# Q-AHBN2 Experiment Contract

**Status:** CONTROL SKELETON — FORMAL MATRICES NOT YET FROZEN
**Created:** 2026-09-23 under DOC-SYNC-1

## Purpose
Authoritative home for the controlled experimental protocols that follow design/development/validation closure.

## Current boundary
No formal Exp10-Q, Exp11-Q, or Exp12-Q matrix is frozen by this document yet. Existing historical/planning material must be reconciled before execution.

Planned formal families:
- Exp10-Q — Failure
- Exp11-Q — Churn
- Exp12-Q — Heterogeneity
- corresponding Kubernetes validation where subsequently frozen

No experiment may be added merely to improve an observed result. Canonical AHBN remains immutable.


## Project-wide test execution and evidence standard

All Q-AHBN2 executable tests inherit the GitHub-first controlled-gate workflow and operational authority frozen in `docs/00_QAHBN2_MASTER.md` and `docs/00_SOURCE_AUTHORITY_REGISTER.md`.

This standard applies to unit, deterministic, smoke, regression, parity, Learning Validation, diagnostic, pilot, ControlSim formal, and Kubernetes formal tests.

### Execution and evidence chain

```text
latest authoritative GitHub code/config
        ↓
researcher execution from designated local workspace
        ↓
timestamped working output
        ↓
completeness + validity verification
        ↓
deliberate preservation/classification in designated Drive evidence area
        ↓
artifact readback verification
        ↓
GitHub stage/status update where warranted
        ↓
post-write GitHub readback
        ↓
next controlled gate
```

The designated local workspace is:

`/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`

The designated Google Drive evidence root is folder ID:

`1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`

Automatic synchronization of working output into Drive is not evidence promotion.

### Output naming

Simulation:

```text
q-ahbn-<DDMMYYYYHHmmss>-<experiment>-<event>/
```

Kubernetes/GKE:

```text
q-ahbn-gke-<DDMMYYYYHHmmss>-<experiment>-<event>/
```

Every preserved run must contain at minimum:

```text
RUN.md
manifest.json
```

and must record, where applicable, the Git commit SHA, configuration, experiment/event, timestamp, run directory, parameters, seeds/repetitions, execution status, and scientific classification.

### Standard test grammar

```text
TEST / GATE:
OBJECTIVE:
AUTHORITATIVE GITHUB COMMIT:
AUTHORITATIVE CONTRACT:
EXECUTION ENVIRONMENT:
RUN DIRECTORY:
EVENT TYPE:
PARAMETERS:
SEEDS / REPETITIONS:
EXPECTED OUTPUTS:
USER EXECUTION COMMAND:
EVIDENCE LOCATION:
COMPLETENESS CHECK:
VALIDITY CHECK:
RESULT:
SCIENTIFIC INTERPRETATION:
GITHUB STATUS UPDATE:
NEXT CONTROLLED GATE:
```

Applicable fields are mandatory. A genuinely non-applicable field is recorded as `N/A` rather than silently omitted.

### Synchronization rule

> **Audit every gate; edit only files whose authoritative state actually changed.**

No test PASS, stage transition, or formal evidence claim may be declared solely from assistant narration, command completion, or automatic Drive synchronization. Artifact verification and the required GitHub readback must occur first.
