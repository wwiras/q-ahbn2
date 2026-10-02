# S16 — Publication Artifact Engineering

**Programme status:** ACTIVE  
**Opened:** 2026-10-01  
**Entry condition:** S15 PASS / CLOSED  
**Scientific baseline:** `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`


## Authorized sources and reconciliation contract

S16 inherits the project-wide authority model from `docs/00_QAHBN2_MASTER.md` and `docs/00_SOURCE_AUTHORITY_REGISTER.md`. Every S16 gate must reconcile the latest authoritative state before artifact construction or manuscript modification.

### Scientific/code/control authority

- Repository: `wwiras/q-ahbn2`
- Pinned manuscript science baseline: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`
- Designated local synchronized scientific workspace:  
  `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`
- Authoritative preserved scientific/evidence Drive root: folder ID `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`

Operational model:

```text
GitHub science/control
        ↓
local execution / working area
        ↓
validity + completeness checks
        ↓
deliberate evidence promotion / preservation
        ↓
verified Drive evidence
```

Automatic Drive synchronization alone is not evidence promotion.

### Manuscript/publication-source authority

- Repository: `wwiras/QAHBN2-Manuscript`
- Active manuscript source: `versions/v0.0/main.tex`
- Manuscript-side Drive folder ID: `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`
- Designated local synchronized manuscript workspace:  
  `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myPaper/ClusterComputing/QAHBN2-Manuscript`

Operational model:

```text
QAHBN2-Manuscript GitHub
        ↕
local manuscript workspace
        ↕
manuscript Drive synchronization
```

The manuscript repository is the publication-source authority. Drive synchronization does not override Git-tracked manuscript provenance.

### Historical source authority used during S16

- `Q_AHBN_FirstDraft.pdf` — Drive file ID `1NahEY5sZPdwhpg2uduBxIxqyS3ikMGqj` — **Authority Level 6 historical source only**.
- Permitted during S16 for historical design lineage and prior figure/table/algorithm/presentation ideas.
- It is not current scientific authority for state/action/reward semantics, hyperparameters, convergence/optimality, quantitative results, or claim wording.
- Any conflict is resolved in favour of the current frozen Q-AHBN2 contracts, promoted evidence, S12/S12A, and the pinned science baseline.

### Mandatory gate reconciliation

Before each S16 gate:
1. fetch and reconcile latest `main` for `wwiras/q-ahbn2`;
2. reconcile `docs/00_QAHBN2_MASTER.md` and `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
3. reconcile the applicable S16 stage record and frozen S12/S12A/S15 constraints;
4. reconcile the latest `wwiras/QAHBN2-Manuscript` publication source and manuscript provenance before any manuscript artifact edit;
5. use Drive only for preserved evidence/source material according to its registered role;
6. after every GitHub write, re-fetch the affected file(s) and verify readback before declaring the transition authoritative.

Conversation memory is not authority.

## Programme-control amendment

The earlier target-journal-selection branch is **SUPERSEDED by researcher decision on 2026-10-01**. Venue selection will be made manually by the researcher and is removed from the S16 critical path.

The existing neutral LaTeX format remains authoritative during S16. No journal-template migration is authorized.

S16 is now restricted to publication-artifact engineering from frozen evidence:
- figures;
- analytical tables;
- formal algorithm/pseudocode;
- artifact/text consistency and visual production.

Frozen throughout S16:
- canonical AHBN and Q-AHBN science;
- parameters, reward, state/action space and transition semantics;
- experiment matrices and run counts;
- S12/S12A claim boundaries;
- S15 statistical/evidence-role contract.

No new experiment or new inferential family is authorized by S16.

# S16-0 — Figure, Table and Algorithm Architecture Audit

**Status:** PASS / CLOSED — 2026-10-01

## Audit question

Determine exactly which final publication artifacts are scientifically necessary, which question each artifact answers, the frozen evidence source, and whether it replaces, complements, or absorbs an existing manuscript artifact.

## Current manuscript artifact inventory

The active manuscript currently contains:
- Figure `fig:qahbn-cycle`: boxed textual Q-AHBN intervention/learning cycle.
- Table `tab:learning-mechanism`: bounded learning-trace evidence.
- Table `tab:primary-paired-results`: primary paired ControlSim results including uncertainty.
- Table `tab:primary-tradeoff-synthesis`: eight-condition effect/trade-off synthesis.
- Table `tab:exp13-results`: five-method churn=0.40 benchmark.
- Table `tab:kubernetes-accounting`: total_forwards versus F_attempt accounting caveat.
- Table `tab:kubernetes-results`: frozen Kubernetes five-method means.

No formal publication pseudocode/algorithm environment is currently present.

## Artifact architecture decision

| ID | Final artifact | Scientific question answered | Frozen evidence / contract | Relationship to current manuscript | Priority |
|---|---|---|---|---|---|
| F1 | Q-AHBN architecture and learning-cycle figure | Where does Q-AHBN act relative to immutable AHBN, and how does information/reward flow? | Frozen AHBN boundary; Q-AHBN state/action/reward/transition contract; S12 C01-C02 | **REPLACE/UPGRADE** current boxed `fig:qahbn-cycle` | ESSENTIAL |
| A1 | Formal Q-AHBN bounded-refinement pseudocode | What exact ordered procedure is executed at each decision and update? | 81-state, five-action, epsilon-greedy, direct-attempt reward closure, next-same-peer update, frozen Q update | **NEW; COMPLEMENTS F1**. Must not duplicate explanatory prose line-for-line | ESSENTIAL |
| F2 | Primary eight-condition paired trade-off figure | Are delivery/delay improvements accompanied by communication cost across the primary conditions? | S11-A 40 paired comparisons; authorized paired CIs; S12 C03-C06 | **COMPLEMENTS/ABSORBS visual role of** `tab:primary-tradeoff-synthesis`; exact uncertainty remains in `tab:primary-paired-results` | ESSENTIAL |
| F3 | Dynamic-stress response figure | How does the AHBN→Q-AHBN effect vary across failure, churn and heterogeneity conditions? | Same S11-A frozen effects; descriptive churn attenuation; S12/S15 | **COMPLEMENTS F2**, not a second copy of all four metrics. Focus on stress-family interpretation | HIGH |
| F4 | Exp13 bounded comparator figure | Where does Q-AHBN sit relative to Gossip, Structured, DC-SoC and AHBN at the single frozen churn=0.40 benchmark? | S11-B / Exp13-Q 25 runs; S12 C07 | **COMPLEMENTS** `tab:exp13-results`; must remain metric-wise, descriptive, non-ranking | HIGH |
| T1 | Learning-mechanism evidence table | Is learning demonstrably active without claiming convergence? | Frozen learning traces; q_updates, coverage, interventions/action use; S12 C02/C13/C15 | **RETAIN AND RATIONALIZE** `tab:learning-mechanism` | HIGH |
| T2 | Primary paired statistical table | What are the exact primary paired estimates/uncertainty supporting the main claims? | S11-A paired contract | **RETAIN** `tab:primary-paired-results` as numerical/statistical authority | ESSENTIAL |
| T3 | Kubernetes evidence + accounting table | What does Kubernetes establish, and why must total_forwards be interpreted with F_attempt? | 25/25 Kubernetes coordinates; paired intervals; runtime accounting; S12 C08-C10/C14-C15 | **MERGE/RATIONALIZE** `tab:kubernetes-accounting` with the relevant AHBN/Q-AHBN portion of `tab:kubernetes-results` where clarity permits; five-method operational context may remain separately if needed | HIGH |
| T4 | Gamma sensitivity table/callout | Why was gamma=0.70 selected, and what is the bounded scope of that evidence? | 15-run gamma sensitivity, gamma={0.70,0.80,0.90}, seeds 42-46 | **NEW compact artifact** only if exact frozen values are publication-ready; otherwise concise methods text is sufficient | MEDIUM |
| T5 | Exp13 exact-values table | What exact five-method values underlie F4? | Frozen Exp13 means | **RETAIN** `tab:exp13-results`, potentially compacted after F4 | HIGH |

## Redundancy decisions

1. **F1 versus A1:** both are required but answer different questions. F1 is architecture/information flow; A1 is executable logical sequence.
2. **F2 versus primary tables:** F2 carries the pattern/trade-off message. T2 remains the exact statistical authority. The current `tab:primary-tradeoff-synthesis` becomes redundant once F2 exists unless it contains exact values unavailable in T2; default disposition is **ABSORB/REMOVE after verification**.
3. **F2 versus F3:** F2 gives the complete eight-condition four-metric overview; F3 must therefore emphasize stress-family response, especially churn attenuation and heterogeneity/failure context, rather than redraw the same four panels.
4. **F4 versus T5:** F4 supports visual comparison; T5 preserves exact benchmark values. Neither may imply an omnibus score, ranking or winner.
5. **Kubernetes:** do **not** create a superiority figure. A table/callout is scientifically safer because the key message is evidence role and accounting semantics, not a stable performance direction.
6. **Gamma:** do **not** create a large robustness figure. The evidence covers gamma only over three predeclared values and does not justify broad sensitivity/robustness presentation.

## Minimum final artifact set

The minimum publication-complete package is therefore:
- **4 figures:** F1 architecture, F2 primary trade-off, F3 dynamic stress, F4 Exp13 positioning;
- **1 formal algorithm:** A1 Q-AHBN pseudocode;
- **4 core tables:** T1 learning evidence, T2 paired statistical results, T3 Kubernetes/accounting, T5 Exp13 exact values;
- **optional compact T4 gamma table/callout**, subject to exact-value/provenance readback.

This is a maximum useful architecture, not a requirement to inflate artifact count. During implementation, an artifact may be merged only when the scientific question remains immediately readable.

## Construction principles

- Every artifact must answer one explicit scientific/reviewer question.
- Exact numerical values must originate from frozen registered evidence or existing authorized manuscript values.
- No chart may imply ranking, convergence, universal superiority, global optimality, generic low overhead or cross-environment equivalence.
- ControlSim and Kubernetes remain visually and statistically separate.
- Use consistent condition/method naming across figure, table and prose.
- Captions must state evidence scope and interpretation boundaries where misreading is plausible.
- Publication artifacts should be source-controlled and reproducible; no decorative graphics are authorized.
- Existing neutral LaTeX format remains unchanged.

## Gate decision

The current evidence is sufficient to construct the artifact package. No new experiment, rerun, parameter change or new inferential test is required.

**S16-0 = PASS / CLOSED.**

## Next controlled gate

**S16-1 — Q-AHBN Architecture Figure + Formal Algorithm Specification**

S16-1 should first replace the boxed mechanism placeholder with a publication-quality architecture/learning-cycle figure and introduce formal pseudocode derived exactly from the frozen algorithm contract. It must complete a figure↔algorithm↔Methods consistency audit before proceeding to empirical figures.
