# S13 — Q-AHBN2 Manuscript

**Status:** ACTIVE — S13-1 PASS / CLOSED; S13-2 PASS / CLOSED; S13-3 PASS / CLOSED; S13-4 PASS / CLOSED; S13-5 PASS / CLOSED — 2026-09-30

## Objective
Draft the standalone Q-AHBN2 manuscript only from verified claims and registered evidence.

## Authoritative claim boundary
All manuscript statements must remain within the frozen S12A authorization in:
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`.

S13 does not reopen experiments, parameters, algorithms, metrics, statistical procedures, evidence, or scientific interpretation.

## S13-1 — Manuscript Structure / Evidence-to-Section Mapping

**Result:** PASS / CLOSED — 2026-09-29

### Working paper scope
A standalone paper on Q-AHBN2 as a bounded Q-learning meta-controller that refines immutable canonical AHBN, evaluated using primary paired ControlSim experiments under failure, churn and heterogeneity, one bounded five-method external-reference benchmark, and complementary Kubernetes operational-realization evidence.

### Working title boundary
The title must describe bounded learning/adaptive dissemination without implying optimality, universal superiority, convergence, or Kubernetes performance replication.

**Working title:**  
**Q-AHBN2: Bounded Q-Learning Refinement of Adaptive Hybrid Blockchain Dissemination under Dynamic Network Conditions**

This is a working manuscript title, not a scientific claim expansion.

## Frozen manuscript architecture

| Section | Scientific purpose | Authorized S12A claims | Primary evidence / authority | Required boundary |
|---|---|---|---|---|
| Abstract | Compact problem, method, primary result, trade-off, external positioning and deployment-realization summary | C01, C06, C07, C08, C10, C12, C13 | Design freeze; S11-A; S11-B; K6; S12 | Must state communication-overhead trade-off; no convergence/optimality/universal-superiority wording |
| 1. Introduction | Motivate dynamic dissemination problem; position AHBN as frozen adaptive baseline; state Q-AHBN2 gap and paper contributions | C01, C12, C13, C15 | Canonical AHBN contract; design freeze; reviewer lessons; S12A | Contribution language must use refinement, not replacement/redesign; no “best/state-of-the-art superiority” |
| 2. Related Work | Situate Gossip, Structured, hybrid/adaptive dissemination and RL-based adaptation; identify the bounded gap addressed by Q-AHBN2 | C01, C12, C15 as boundaries | Existing literature to be cited during drafting; canonical AHBN lineage | Literature synthesis must not manufacture empirical claims about Q-AHBN2 |
| 3. Q-AHBN2 Method | Define immutable AHBN proposal, state abstraction, bounded actions, reward attribution, Q update and post-AHBN refinement architecture | C01, C02 | Canonical AHBN contract; Q-AHBN2 design freeze; frozen learning contract | Mechanism description may show active learning design; must not imply convergence or optimality |
| 4. Experimental Methodology | Define ControlSim primary experiments, paired design, metrics/statistics, Exp13-Q bounded reference role and Kubernetes protocol/evidence role | C03–C10, C13 | Experiment contract; statistical contract; S11; K6 | Preserve n=5; same-seed pairing; Exp13 separate; K8s non-pooled and non-replication |
| 5. Results | Report learning evidence, Exp10-Q, Exp11-Q, Exp12-Q, cross-condition synthesis, Exp13-Q and Kubernetes results without changing evidence roles | C02–C10, C13, C14 | S11-A; S11-B; K6; S12 | Report delivery/delay gains together with duplicate/forwarding cost; K8s uncertainty explicit |
| 5.1 Learning behaviour | Demonstrate active Q updates, interventions and condition-dependent state/action behaviour | C02 | Frozen learning traces; S12 | Active refinement only; no convergence/policy-optimality claim |
| 5.2 Failure — Exp10-Q | Report AHBN vs Q-AHBN2 under frozen one-peer failure condition | C03 | S11-A/S12 Exp10-Q | Higher delivery/lower delay with higher duplicates/forwards; condition-specific |
| 5.3 Churn — Exp11-Q | Report three frozen churn levels and attenuation of delivery gain | C04 | S11-A/S12 Exp11-Q | Descriptive attenuation only; no dose-response proof or “churn-proof” claim |
| 5.4 Heterogeneity — Exp12-Q | Report balanced/moderate/weak-heavy profiles | C05 | S11-A/S12 Exp12-Q | Improvement under tested profiles with overhead trade-off; no general solution claim |
| 5.5 Cross-condition ControlSim synthesis | Synthesize the eight primary conditions | C06 | S11-A/S12 | No pooled overall effect; improvement is delivery–latency with communication-overhead trade-off |
| 5.6 Exp13-Q external-reference benchmark | Position Q-AHBN2 against Gossip, Structured, DC-SoC and AHBN at churn=0.40 | C07 | S11-B/S12 | Bounded external positioning only; no omnibus ranking/winner |
| 5.7 Kubernetes operational realization | Report executable cloud-native realization and paired uncertainty | C08, C09 | K6/S12 | Deployment credibility, not independent performance confirmation |
| 6. Discussion | Explain what bounded learning refinement changes, condition dependence, overhead trade-off, relation of primary/external/deployment evidence | C01, C02, C06–C10, C12–C15 | S12 interpretation + S12A contract | ControlSim and K8s complementary, not pooled/equivalent; no generic lightweight claim |
| 7. Limitations | Make evidentiary and generalization limits explicit | C13, C14, C15 | Statistical contract; S12; S12A | n=5; condition-specific; no convergence/optimality; no omnibus ranking; no cross-environment equivalence |
| 8. Conclusion | Answer paper objective with strongest evidence-bounded synthesis | C01, C06–C10, C12–C15 | Entire frozen evidence chain | Conclude refinement and tested trade-off improvement only; retain overhead and scope qualification |

## Claim-placement rules

### Paper-level contribution authority
C12 is the authoritative paper contribution synthesis. C11 is thesis RO4/RQ4 wording and is reserved for S13-T / Chapter 6 mapping; it must not be presented as an additional standalone-paper empirical claim.

### Manuscript-wide safeguards
C13–C15 apply across the complete manuscript, not only Section 7:
- C13 requires visible scope and uncertainty limitations wherever quantitative claims are summarized.
- C14 prohibits converting “bounded” architecture into a generic low-overhead/lightweight performance claim.
- C15 prohibits convergence, policy optimality, best-method, dominance and universal-superiority wording.

### Evidence-role separation
- Primary performance evidence: Exp10-Q / Exp11-Q / Exp12-Q only.
- Learning/mechanistic evidence: learning traces only.
- External positioning: Exp13-Q at churn=0.40 only.
- Operational realization: Kubernetes only.
- Cross-environment interpretation: complementary evidence; no statistical pooling, equivalence claim or literal replication.

## Planned manuscript result flow
1. Learning behaviour / mechanism evidence.
2. Exp10-Q failure.
3. Exp11-Q churn.
4. Exp12-Q heterogeneity.
5. Eight-condition ControlSim synthesis.
6. Exp13-Q bounded external positioning.
7. Kubernetes operational realization.
8. Discussion integrating the evidence roles without pooling them.

This ordering prevents the external benchmark or Kubernetes evidence from being mistaken for the primary RO4 causal evidence.

## S13-1 verification
The structure covers the requested Abstract, Introduction, Related Work, Q-AHBN2 Method, Experimental Methodology, Results, Discussion, Limitations and Conclusion. Every empirical/synthesis section is mapped to frozen S12A claim IDs and evidence roles. No new experiment, metric, statistical test, hypothesis, parameter or scientific interpretation has been introduced.

**S13-1 = PASS / CLOSED.**

---

# S13-2 — Manuscript Drafting Plan / Source-and-Evidence Pack

**Result:** PASS / CLOSED — 2026-09-30

## S13-2A — Publication workspace architecture

The publication workspace is frozen as a dual-repository model inside the researcher’s Google Drive-synchronized local workspace:

```text
Google Drive synchronized workspace
├── q-ahbn2/                 # scientific/code/control repository
│   ├── Git-tracked code/docs/contracts
│   └── output/              # Git-ignored, Drive-synchronized working/evidence area
└── QAHBN2-Manuscript/       # separate manuscript repository
    ├── Git-tracked LaTeX/publication/control files
    └── output/              # Git-ignored, Drive-synchronized manuscript working/evidence area
```

The existing Q-AHBN2 master rule is preserved: generated artifacts remain under repository-local `output/`; no new root-level `evidence/`, `outputs/`, or `q-ahbn-*/` evidence trees are introduced.

Git and Google Drive are overlapping local workspaces:
- `.gitignore` controls what Git/GitHub tracks;
- Google Drive Desktop may still synchronize ignored local content to the cloud;
- incidental Drive synchronization does not by itself promote working output to authoritative scientific evidence.

The designated Q-AHBN2 Drive evidence hierarchy remains the experimental evidence authority.

## S13-2B — Repository-role separation

### `wwiras/q-ahbn2`
Authoritative for:
- implementation;
- canonical/design contracts;
- experiment definitions;
- statistical contract;
- analysis code;
- gate records;
- results register;
- S12 scientific interpretation;
- S12A claim authorization;
- provenance of frozen experimental evidence.

### `wwiras/QAHBN2-Manuscript`
Authoritative for:
- the active versioned LaTeX manuscript source under `versions/vX.Y/main.tex`;
- manuscript control/provenance records;
- response-to-reviewers material when applicable;
- researcher-supplied Zotero/BibTeX files placed manually inside the applicable version directory;
- controlled manuscript version transitions.

Repository architecture is intentionally lean:
- no root `main.tex`;
- no `sections/`, `figures/`, `tables/`, or dedicated `bibliography/` directories;
- all manuscript sections plus LaTeX/TikZ figures/diagrams and tables are maintained directly in the active versioned `main.tex`.

It must not become a second authority for experiment design, parameters, statistics, or scientific interpretation.

### Google Drive
The local/cloud filesystem contains both repositories and their Git-ignored `output/` trees. Large or working artifacts may be physically present beside Git-tracked files without entering GitHub.

For the manuscript repository, `output/` is reserved for working/publication evidence such as copied manifests, source-table extracts, validation exports and submission working packages. Publication figures/diagrams and tables are authored directly in LaTeX/TikZ within the active versioned `main.tex`; no dedicated tracked figure/table directories are used.

## S13-2C — Cross-repository provenance contract

The two repositories are linked by provenance, not by automatic copying of scientific state.

The minimum traceability tuple is:

```text
Q-AHBN2 science commit SHA
+ Google Drive folder ID
+ manifest/file hash where available
+ S12A claim ID
+ manuscript artifact/section identifier
```

The manuscript repository must carry a Git-tracked provenance/control record identifying:
- the authoritative `wwiras/q-ahbn2` repository;
- the exact Q-AHBN2 scientific baseline commit used by the manuscript;
- the S12A claim/evidence authority;
- Drive folder IDs for promoted evidence families;
- manuscript figure/table/source-artifact mappings.

The Q-AHBN2 master/stage record should point back to the manuscript repository once that repository exists.

A change on `q-ahbn2/main` does not silently change the manuscript scientific baseline. Any baseline advance must be a controlled reconciliation with a recorded reason.

## S13-2D — GitHub / Overleaf boundary

Overleaf must connect only to the manuscript repository, not to `q-ahbn2`.

The intended publication sync path is:

```text
local QAHBN2-Manuscript
        ⇅
GitHub QAHBN2-Manuscript
        ⇅
Overleaf
```

The manuscript GitHub repository should remain lean. Code, tests, GKE files, raw experimental logs and large evidence are not imported merely for Overleaf convenience.

Git-ignored `output/` content remains Drive-synchronized but invisible to GitHub/Overleaf unless a verified publication-ready derivative is deliberately promoted into a tracked manuscript directory.

## S13-2E — Exact drafting order

Substantive drafting must proceed in this order:

1. **Section 3 — Q-AHBN2 Method**
2. **Section 4 — Experimental Methodology**
3. **Section 5 — Results**
   - 5.1 Learning behaviour
   - 5.2 Exp10-Q failure
   - 5.3 Exp11-Q churn
   - 5.4 Exp12-Q heterogeneity
   - 5.5 Cross-condition ControlSim synthesis
   - 5.6 Exp13-Q bounded external-reference benchmark
   - 5.7 Kubernetes operational realization
4. **Section 6 — Discussion**
5. **Section 7 — Limitations**
6. **Section 1 — Introduction**
7. **Section 2 — Related Work**
8. **Section 8 — Conclusion**
9. **Abstract**
10. **Title/keywords finalization**

Rationale: draft first from the strongest frozen internal authorities and evidence; write literature-dependent framing only after the method/results contribution is fixed; write the Abstract and final title last to prevent claim inflation.

## S13-2F — Authoritative source-and-evidence pack

| Manuscript part | Required repository authorities | Evidence/literature authority | Authorized claims |
|---|---|---|---|
| Section 3 Method | `docs/01_CANONICAL_AHBN_CONTRACT.md`; `docs/02_QAHBN2_DESIGN_FREEZE.md`; relevant frozen implementation/tests only for consistency verification | No experimental result required | C01, C02 |
| Section 4 Methodology | `docs/03_EXPERIMENT_CONTRACT.md`; `docs/04_STATISTICAL_CONTRACT.md`; K0–K6 stage records; S10A where Exp13-Q role is defined | Frozen experiment/evidence manifests as needed | C03–C10, C13 |
| Section 5.1 Learning | S05/S12 learning-mechanism records; design freeze | Frozen learning traces/evidence only | C02 |
| Section 5.2 Exp10-Q | S08, S11-A, S12, results register | Frozen Exp10-Q formal/aggregation evidence | C03 |
| Section 5.3 Exp11-Q | S09, S11-A, S12, results register | Frozen Exp11-Q formal/aggregation evidence | C04 |
| Section 5.4 Exp12-Q | S10, S11-A, S12, results register | Frozen Exp12-Q formal/aggregation evidence | C05 |
| Section 5.5 Cross-condition | S11-A, S12, S12A, claim matrix | `s11a_primary_ro4_summary.csv` / registered frozen aggregation artifacts | C06 |
| Section 5.6 Exp13-Q | S10A, S11-B, S12, S12A | Frozen S11-B 25-run five-method benchmark only | C07 |
| Section 5.7 Kubernetes | K0–K6, S12, S12A | Frozen K8s validation/evidence family only | C08, C09, C10 |
| Section 6 Discussion | S12 interpretation; S12A; claim matrix; reviewer lessons | No new analysis; literature may contextualize but cannot strengthen frozen empirical claims | C01, C02, C06–C10, C12–C15 |
| Section 7 Limitations | statistical contract; S12; S12A; claim matrix | No new evidence required | C13–C15 |
| Section 1 Introduction | canonical AHBN authority; S12A; reviewer lessons | Peer-reviewed literature + authoritative prior AHBN publication/repository lineage | C01, C12, C13, C15 boundaries |
| Section 2 Related Work | reviewer lessons; canonical AHBN lineage | Peer-reviewed/primary literature on Gossip, structured dissemination, hybrid/adaptive dissemination and RL-based networking/blockchain dissemination | C01, C12, C15 boundaries |
| Section 8 Conclusion | S12; S12A; claim matrix | Entire frozen evidence chain | C01, C06–C10, C12–C15 |
| Abstract | S12A + final manuscript sections only | No independent new evidence | C01, C06–C10, C12, C13 |
| Title/keywords | S12A + final manuscript scope | No new scientific claim | C01/C12 scope boundary |

## Literature-source rules

For Introduction and Related Work:
1. prefer peer-reviewed primary literature and authoritative original protocol/system papers;
2. use the existing verified AHBN/thesis bibliography where relevant rather than rebuilding citations from memory;
3. verify every imported citation against its actual source before manuscript use;
4. literature may motivate, compare concepts and establish gaps, but may not expand the frozen Q-AHBN2 empirical claim boundary;
5. no citation is accepted solely because it appeared in an earlier AI-generated draft;
6. bibliography scope should be paper-specific rather than automatically copying the complete thesis bibliography.

## Quantitative-source rules

For every quantitative manuscript statement:
- trace to the frozen registered artifact/evidence family;
- preserve n=5 per condition/cell where applicable;
- preserve same-seed AHBN–Q-AHBN2 pairing;
- preserve two-sided Student-t 95% CI language exactly within the statistical contract;
- do not create a pooled overall effect across unlike conditions;
- do not introduce a new p-value family, post-hoc significance selection, metric or derived statistic.

## Figure/table provenance rule

Every publication figure/table must have a traceable mapping:

```text
manuscript artifact
→ claim ID(s)
→ registered summary/source artifact
→ Drive evidence folder ID
→ manifest/hash where available
→ q-ahbn2 science commit / generation code
```

Publication-ready figures/tables required for LaTeX may be Git-tracked in `QAHBN2-Manuscript`; large source artifacts remain in Git-ignored Drive-synchronized `output/`.

## S13-2 verification

S13-2 establishes:
- the dual-repository + embedded-Drive workspace model;
- repository authority separation;
- the `output/` Git-ignore/evidence boundary consistent with the frozen master;
- bidirectional provenance requirements;
- a lean GitHub/Overleaf manuscript boundary;
- exact section drafting order;
- exact frozen source/evidence authorities for every manuscript section;
- literature and quantitative-source rules;
- figure/table provenance rules.

No experiment, parameter, algorithm, metric, statistic, hypothesis or scientific interpretation was added or reopened.

**S13-2 = PASS / CLOSED.**

## Next permitted action

**S13-3 — Manuscript Repository Bootstrap / Provenance Initialization**

**Status:** PASS / CLOSED — 2026-09-30.

Completed:
- private repository `wwiras/QAHBN2-Manuscript` verified on `main`;
- researcher local clone verified at `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myPaper/ClusterComputing/QAHBN2-Manuscript`;
- minimal publication skeleton initialized;
- manuscript `.gitignore` established with `output/` excluded from Git;
- `docs/MANUSCRIPT_MASTER.md` and `docs/PROVENANCE.md` created;
- exact Q-AHBN2 scientific baseline pinned to `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S11-A, S11-B and Kubernetes Drive evidence IDs registered in manuscript provenance;
- GitHub/Overleaf boundary recorded;
- no substantive manuscript prose drafted.

Closure completed:
- manuscript-side Google Drive folder ID `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj` registered in manuscript provenance;
- researcher local synchronized path registered;
- manuscript repository and q-ahbn2 cross-repository authority recorded;
- final readback required after these closure writes.

**S13-3 = PASS / CLOSED.**

## Next permitted action

**S13-4 — Section 3 Q-AHBN2 Method Drafting**

S13-4 may begin substantive manuscript prose only for Section 3, using the frozen S13-2 source pack and S12A claim boundaries. Later sections remain blocked until their controlled drafting turn.

The separate thesis path remains **S13-T — Chapter 6 Mapping** and is not opened by S13-3.

## Boundary
Claim wording remains traceable through `docs/07_CLAIM_EVIDENCE_MATRIX.md`. Exp13-Q is bounded external positioning, not a universal algorithm ranking. Kubernetes is operational-realization evidence, not independent confirmation of ControlSim performance. Unfinished or unverified evidence must not be promoted into manuscript claims.


---

# S13-4 — Section 3 Q-AHBN2 Method Drafting

**Result:** PASS / CLOSED — 2026-09-30

The manuscript repository now contains `sections/03_method.tex`, included from `main.tex`.

The section was drafted against the pinned manuscript science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` and restricted to S12A claims C01/C02. It covers:
- immutable canonical-AHBN proposal and post-AHBN intervention boundary;
- canonical four-variable EWMA state and 81-state discretization;
- five-action bounded refinement contract and requested-versus-realized fanout distinction;
- direct-attempt NEW/DUPLICATE/FAILED reward contract and F=0 no-reward-bearing-update boundary;
- zero-initialized 81x5 tabular Q-learning, alpha_Q=0.25, gamma=0.70, seeded epsilon-greedy selection, epsilon_0=0.30, epsilon_min=0.03, decay=0.995;
- same-peer successor-state / delayed-reward transition lifecycle;
- explicit no-convergence/no-optimality/no-performance implication boundary.

Controlled readback verified the frozen constants, action set, reward form, fanout range, manuscript inclusion, and claim guard. No performance result, experiment interpretation, new algorithmic mechanism, new parameter, or new scientific claim was introduced.

**S13-4 = PASS / CLOSED.**

## Next permitted action

**S13-5 — Section 4 Experimental Methodology Drafting**


## S13 publication-architecture refinement — 2026-09-30

Researcher-approved administrative refinement after S13-4:

- active manuscript source: `versions/v0.0/main.tex`;
- root `main.tex` removed;
- `sections/`, `figures/`, `tables/`, and dedicated `bibliography/` structures removed;
- S13-4 Section 3 prose consolidated directly into the active versioned `main.tex`;
- Zotero/BibTeX remains researcher-managed and will be supplied manually inside the applicable version directory;
- all publication figures/diagrams and tables are to be authored directly in LaTeX/TikZ within the versioned `main.tex`;
- new manuscript versions are created only by explicit controlled transition, not per drafting gate.

This is a publication-source architecture change only. No experiment, algorithm, parameter, result, statistic, claim, S12A boundary, or S13-4 scientific content changed.

**S13-4 remains PASS / CLOSED.**
**S13-5 remains NEXT — Section 4 Experimental Methodology Drafting.**


## S13-5 — Section 4 Experimental Methodology Drafting — 2026-09-30

Section 4 was drafted directly in the publication repository at `versions/v0.0/main.tex` using the pinned manuscript science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

Source pack reconciled:
- `docs/03_EXPERIMENT_CONTRACT.md`;
- `docs/04_STATISTICAL_CONTRACT.md`;
- `docs/stages/S10A_FORMAL_EXP13Q_REFERENCE_BENCHMARK.md`;
- `docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md`;
- `docs/stages/K6_Q_K8S_EVIDENCE_FREEZE.md`;
- S12A C03--C10 and C13 boundaries.

Audit confirmed:
- primary ControlSim matrix remains 80 runs (20 failure, 30 churn, 30 heterogeneity);
- seeds 42--46, BA(100,m=3), source 0 and 1,000 sequential-message protocol preserved;
- Exp10/11/12 frozen conditions and schedules preserved;
- primary outcomes remain delivery ratio, propagation delay, duplicates and total forwards;
- same-seed AHBN versus Q-AHBN pairing and n=5 Student-t 95% CI contract preserved;
- Exp13-Q remains a separate 25-run churn=0.40 five-method reference benchmark;
- Kubernetes remains a separate 25-run operational-realization/matched-reference matrix using N=20, BA(m=2), 240 messages, 0.4 s pacing and +1/+26/+51/+76 s churn offsets;
- ControlSim and Kubernetes are explicitly non-pooled and non-replication evidence families;
- no performance results, new metric, new test, new model, or new interpretation was introduced;
- manuscript-facing algorithm name is Q-AHBN; literal q-ahbn2 repository identifiers remain provenance-only.

**S13-5 = PASS / CLOSED.**

## Next permitted action

**S13-6 — Section 5 Results Drafting**, following the frozen S13 result flow and S12A claim/evidence boundaries.
