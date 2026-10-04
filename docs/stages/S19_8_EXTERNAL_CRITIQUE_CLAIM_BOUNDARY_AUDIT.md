# S19-8 — External-Critique Reconciliation and Final Claim-Boundary Audit

**Status:** PASS / CLOSED — fresh compile, visual proof, source/PDF consistency, and control readback completed  
**Date:** 2026-10-04  
**Scientific repository:** `wwiras/q-ahbn2`  
**Manuscript repository:** `wwiras/QAHBN2-Manuscript`  
**Pinned science baseline:** `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`

## 1. Objective

Reconcile five external criticisms through bounded manuscript wording corrections only. No experiment, parameter, algorithm, frozen result, statistic, confidence interval, table value, figure value, or evidence role may change.

## 2. Reconciled authority state

Latest `main` in both repositories was reconciled before editing. The active publication source remains:

- `versions/v0.0/main.tex`
- bibliography: `versions/v0.0/references.bib`

The primary paired ControlSim evidence, single-condition five-method benchmark, and corrected Kubernetes operational evidence remain distinct and non-pooled.

## 3. Criticism → evidence → disposition → manuscript change

| Criticism | Existing evidence / boundary | Disposition | Bounded manuscript correction |
|---|---|---|---|
| Consensus/fork implication | Consensus/fork outcomes were not measured in S11/S12/S17 evidence | ACCEPT | Abstract now ends with demonstrated dissemination outcomes only; no downstream consensus/fork implication |
| Trade-off interpretation | Primary ControlSim shows higher delivery/lower delay with higher duplicate/forward activity; no omnibus optimization test | ACCEPT | Clarified metric-specific condition-dependent operating-point shift; explicitly excludes Pareto dominance, optimality, and demonstrated bandwidth efficiency |
| Discretization rationale | Frozen design uses 4 variables × 3 bins = 81 states; no bin-count/boundary sensitivity study | ACCEPT | States compact-representation rationale; explicitly says alternative bin counts/boundaries were not tested and thirds are not proven optimal/robust |
| Scale boundary | 405 Q-values is a per-learner logical table size; evaluated networks are ControlSim N=100 and Kubernetes N=20 | ACCEPT | Separates fixed per-learner table size from empirical network-size scalability, total network overhead, or larger-N performance |
| Other RL approaches | Study tests bounded tabular refinement over frozen AHBN; no DQN/DDPG/deep/continuous-state comparison | ACCEPT | Defines narrower research question; richer state/deep/continuous-state comparisons are future work; no superiority or formal-safety claim |

## 4. Source/PDF discrepancy

The researcher-supplied Drive artifact identified as `main03Oct2026_1919.pdf` was fetched directly and inspected. Its abstract ends with:

> “ultimately supporting faster consensus and reduced fork rates in blockchain networks.”

Current GitHub source immediately before S19-8 instead ended with the softer but still unsupported wording:

> “supporting dissemination conditions associated with timely blockchain consensus and lower fork risk.”

Therefore the 19:19 PDF and the pre-S19-8 GitHub source are not an exact source/PDF pair. The historical S19-7 closure record is preserved unchanged; S19-8 records this discrepancy prospectively rather than silently rewriting history.

## 5. Applied manuscript edits

Commit: `f51cb4164d12a5dfe304061b3af3757769b32d33`

Bounded edits were applied to the abstract, Related Work positioning, state-discretization rationale, tabular-learning rationale, Discussion interpretation, Limitations, and Conclusion. Relevant captions/results were audited; no numerical or semantic evidence changes were required.

## 6. Invariants checked

The edits do not authorize or introduce:

- DQN/DDPG or other new RL experiments;
- threshold/bin sensitivity experiments;
- Pareto experiments;
- network-size experiments;
- new statistics or confidence intervals;
- new metric families;
- changed AHBN/Q-AHBN algorithms or parameters;
- pooling of ControlSim, Exp13, or Kubernetes evidence.

## 7. Fresh compile and visual/source proof

Researcher-supplied fresh build: `main04Oct2026_0834.pdf`.

Verified manuscript-Drive identity:
- Drive ID: `1Sa_BKh-tVWP5zkTj2HIgmPdEtW0H7e3o`
- size: 511,544 bytes
- pages: 28
- local binary SHA-256: `fc542a58f195842e0ec66ca2b2d7f12b851ba2fd7447e9c59749ffcdcc11f4c3`

The fresh PDF was checked against the active S19-8 source and the five criticism boundaries. The abstract ends on the demonstrated condition-dependent dissemination result and contains no consensus/fork implication. The trade-off, discretization, per-learner-table/scale, and alternative-RL boundaries are rendered in the compiled artifact. A 28-page visual proof found no new clipping, overflow, broken pagination, citation placeholder, or figure/table/algorithm regression. Figure 1's two feedback paths remain legible; Figures 2--5, Tables 1--5, Algorithm 1, and references remain intact.

No numerical result, confidence interval, table/figure value, experiment, parameter, algorithm, or evidence role changed.

## 8. Closure verification

All S19-8 closure requirements are satisfied:

1. fresh authorized compile supplied and independently identified in the manuscript Drive archive;
2. compiled PDF visually inspected across all 28 pages;
3. abstract and all five claim boundaries match the reviewed source;
4. scientific master, manuscript master, and provenance updated with the final PDF identity;
5. changed GitHub records are subject to mandatory post-write re-fetch/readback before the external status declaration.

**S19-8 = PASS / CLOSED.**
