# S19-5 — Figure 1 Presentation Redesign Specification

**Status:** PASS / CLOSED — 2026-10-03

## Objective
Freeze the presentation-only redesign specification and semantic-parity contract for manuscript Figure 1 (`fig:qahbn-cycle`) before implementation.

S19-5 is specification/control only. It does not modify the active Figure 1 TikZ source, Algorithm 1, Q-AHBN/AHBN semantics, experiments, evidence, statistics, or claims.

## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md`
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`
- `docs/stages/S19_4_CITATION_DENSITY_INTEGRATION.md`
- frozen canonical AHBN and Q-AHBN2 design contracts
- active manuscript `versions/v0.0/main.tex`
- Algorithm 1 `alg:qahbn`
- active Figure 1 `fig:qahbn-cycle`
- manuscript `docs/MANUSCRIPT_MASTER.md`
- manuscript `docs/PROVENANCE.md`

Pinned manuscript science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Reconciliation
The current active Figure 1 is native TikZ and contains six large equal-weight boxes arranged as a two-row clockwise pipeline:
1. Canonical local observations;
2. Immutable canonical AHBN;
3. Bounded Q-AHBN refinement;
4. Eligible-target realization;
5. Direct attributable outcomes;
6. Reward closure and learning feedback.

It also contains:
- a solid primary execution path;
- a dashed state-reuse path from canonical observations to Q-AHBN;
- a dashed learning-feedback return path;
- equations and implementation-level details inside several boxes.

The figure is scientifically correct but visually dense. It duplicates details already stated immediately below the figure and formalized exactly in Algorithm 1. The redesign should therefore improve hierarchy and readability by showing the architecture/cycle rather than reproducing the method specification inside the figure.

## Frozen semantic message
The redesigned Figure 1 must communicate exactly this conceptual cycle:

```text
LOCAL OBSERVATIONS
      ↓
IMMUTABLE AHBN
      ↓
BOUNDED Q-AHBN REFINEMENT
      ↓
ELIGIBLE-TARGET REALIZATION
      ↓
DIRECT OUTCOMES
      ↓
REWARD / LEARNING
      └──────────────↺ future Q-AHBN decisions
```

with the additional semantic fact that Q-AHBN discretizes/reuses the same canonical AHBN EWMA snapshot.

## Mandatory semantic invariants
S19-6 implementation must preserve all of the following:

### P1 — AHBN-first ordering
Canonical AHBN completes before Q-AHBN can refine anything.

### P2 — Immutable AHBN boundary
The figure must visibly identify AHBN as canonical/immutable. It must not imply that Q-learning modifies AHBN sensing, normalization, EWMA, score, sigmoid, mode rule, or canonical fanout actuator.

### P3 — Preserved AHBN proposal
The AHBN output `(mode_AHBN, k_AHBN)` must remain conceptually distinguishable from the post-learning proposal.

### P4 — Bounded post-AHBN action
Q-AHBN acts only after the AHBN proposal and performs one bounded refinement. It is not a replacement controller and does not choose before AHBN.

### P5 — Same canonical state
The learner's Q state comes from discretizing the same four canonical EWMA dimensions `d,l,u,c`; no privileged event/failure label is introduced.

### P6 — Requested versus realized forwarding
The refined/requested Q-AHBN proposal remains distinct from eligible-target realization. The figure must not imply that requested fanout equals realized forwarding.

### P7 — Outcome ownership
Learning evidence is based on directly attributable `NEW | DUPLICATE | FAILED` outcomes from initiated forwarding attempts.

### P8 — No synthetic failure
Nothing in the visual may imply that unrealized target slots become FAILED outcomes.

### P9 — Reward closure
Reward/learning occurs from the attributable outcome record. `F=0` remains no numerical reward/update; this exact edge case may move out of the visual because Algorithm 1 is authoritative, but the visual must not contradict it.

### P10 — Temporal transition
Learning returns to a future Q-AHBN decision; the next state is the same peer's next Q-AHBN state. The figure must not depict an immediate synchronous self-loop that implies same-event next state.

### P11 — Algorithm authority
Algorithm 1 remains the exact update-order/edge-case specification. Figure 1 is architectural, not a second pseudocode representation.

### P12 — No new scientific semantics
No new state, action, reward term, threshold, parameter, policy, feedback signal, controller link, or optimization objective may be introduced.

## Approved presentation redesign

### 1. Replace six equal-weight technical boxes with three visual layers
The preferred architecture is a clean left-to-right main flow with three visually distinct groups:

**A. Canonical adaptation**
- Local observations / canonical EWMA
- Immutable AHBN
- output: preserved AHBN proposal

**B. Bounded learning refinement**
- Q-state discretization from the same canonical EWMA
- five-action bounded Q-AHBN refinement
- output: refined requested proposal

**C. Execution and learning evidence**
- eligible-target realization / forwarding
- NEW | DUPLICATE | FAILED
- reward evidence
- feedback arrow to future Q-AHBN decisions

This grouping changes only visual hierarchy. It does not merge scientific stages semantically.

### 2. Reduce equations inside boxes
The figure should retain only compact identifiers needed to understand architecture.

Recommended retained text:
- observations: `d, l, u, c → canonical EWMA`;
- AHBN: `z=-d+l+u+c`, mode + canonical fanout, or an even shorter `canonical mode + fanout proposal` if equation is kept in surrounding prose;
- Q state: `3^4 = 81 states`;
- Q action: `KEEP | FANOUT ±1 | SET mode`;
- realization: `k_real ≤ min(k_Q, |N_e|)`;
- outcomes: `NEW | DUPLICATE | FAILED`;
- reward/learning: compact `R_t → Q update`.

The full reward equation, exact `F_t=0` edge case, exact epsilon-greedy wording, and same-peer transition sentence should remain in the method prose/Algorithm 1 rather than crowding Figure 1.

### 3. Use visual hierarchy instead of repeated prose
Approved visual conventions:
- one restrained style for canonical AHBN;
- one distinct but compatible style for the Q-AHBN learning layer;
- neutral execution/evidence style;
- solid arrows for forward execution;
- dashed arrow for same-EWMA state reuse;
- dashed/curved return arrow for future learning feedback.

Do not encode scientific meaning solely by color; labels/arrows must remain interpretable in grayscale.

### 4. Make the intervention boundary unmistakable
The central visual emphasis should be:

```text
AHBN proposal
      ↓
[bounded Q-AHBN refinement]
      ↓
refined requested proposal
```

This is the main architectural contribution and must be readable before the lower-level details.

### 5. Keep the learning loop secondary
The feedback loop should visually return from attributable outcomes/reward to **future Q-AHBN decisions**, not to AHBN and not to observations. It should not visually dominate the AHBN-first execution path.

### 6. Caption role
The caption should remain a semantic guardrail and state, compactly:
- AHBN executes first and remains immutable;
- Q-AHBN refines only the completed AHBN proposal;
- requested and realized forwarding remain distinct;
- learning uses directly attributable forwarding outcomes;
- Algorithm 1 gives exact update ordering.

The caption must not claim convergence, optimality, superiority, or cross-environment equivalence.

## Information intentionally removed from Figure 1 visual body
The following may be removed from box interiors because they are already formalized in the surrounding method/Algorithm 1:
- full sigmoid notation;
- full five-action names if a compact action-family label is used;
- full reward fraction;
- `F_t=0` textual edge case;
- full sentence defining same-peer `s_{t+1}`;
- explanatory phrases such as “initiated forwarding attempts”.

Removal from the visual body does **not** remove these semantics from the method. Algorithm 1 and prose remain authoritative.

## Prohibited redesigns
S19-6 must not:
- collapse AHBN and Q-AHBN into one controller box;
- put Q-AHBN before or parallel to AHBN;
- draw Q-learning feedback into AHBN;
- depict global topology/network state as learner input;
- imply direct action on realized targets bypassing eligible-target realization;
- add reward components or new feedback signals;
- replace NEW/DUPLICATE/FAILED with a different outcome taxonomy;
- present Q-AHBN as choosing the whole dissemination policy independently;
- use a generic “AI/ML” black box that hides the bounded action contract;
- add performance/result values to the architecture figure;
- alter Algorithm 1 as part of presentation redesign.

## S19-6 semantic-parity checklist
Before S19-6 can close, the implemented Figure 1 must be checked item-by-item against P1–P12 above.

Additionally verify:
1. all six conceptual stages remain represented, even if grouped into three visual layers;
2. preserved AHBN proposal and refined proposal remain visually distinct;
3. same canonical EWMA reuse is visible;
4. forward execution and learning feedback arrows cannot be confused;
5. figure remains legible at manuscript two-column page width;
6. no text collision, clipping, awkward word break, or arrow crossing obscures meaning;
7. caption and surrounding text remain consistent with Algorithm 1;
8. compiled PDF is visually inspected before closure.

## Implementation authority
S19-6 is authorized to modify only the Figure 1 TikZ block and, if necessary, its caption for presentation/parity. Any change outside that bounded region requires explicit reconciliation and must not be silently bundled into S19-6.

## Result
**S19-5 = PASS / CLOSED.**

The redesign is now specified without changing the active Figure 1.

## Next permitted task
**S19-6 — Figure 1 Presentation Implementation and Semantic-Parity Audit** is the next and only released action.


## Vertical-layout amendment — 2026-10-03
The researcher approved a vertical top-to-bottom Figure 1 with a central execution spine and compact side annotations. This supersedes the earlier left-to-right presentation preference; P1-P12 are unchanged. The feedback path returns to a future Q-AHBN decision and not to AHBN.

Figure simplification follows an information-preservation rule: technical content removed from the visual must either remain explicit in the method/Algorithm 1, be moved or clarified in the companion explanatory paragraph, or be retained compactly in the figure. The companion paragraph preserves the same-EWMA 81-state discretization, AHBN-first proposal, five bounded refinements, requested-versus-realized distinction, directly attributable outcome basis, zero-attempt no-update case, and same-peer future transition. Text density is reduced before font size; modest resizing is permitted only if readability remains adequate.

**S19-5 remains PASS / CLOSED as amended.**
