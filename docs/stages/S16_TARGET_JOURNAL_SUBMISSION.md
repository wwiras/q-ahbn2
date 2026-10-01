# S16 — Target Journal Selection + Submission Production

**Programme status:** ACTIVE  
**Opened:** 2026-10-01  
**Entry condition:** S15 PASS / CLOSED  
**Scientific baseline:** `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`

## Programme contract

S16 converts the scientifically closed Q-AHBN manuscript into a target-journal submission package. S16 is a publication-production programme, not an experimental programme.

Frozen throughout S16 unless a genuine scientific defect is discovered:
- canonical AHBN and Q-AHBN algorithms;
- parameters and experiment matrices;
- S12/S12A interpretation and claim boundaries;
- S15 analytical strengthening;
- evidence roles and statistical contract.

No journal template migration is permitted before S16-0 closes.

## S16-0 — Q1 Target-Journal Fit and Requirements Reconciliation

**Status:** PASS / CLOSED — 2026-10-01

### Current candidate set
Four technically plausible Q1 candidates were reconciled against the manuscript's actual contribution:
1. Journal of Network and Computer Applications (JNCA)
2. Future Generation Computer Systems (FGCS)
3. IEEE Transactions on Network and Service Management (TNSM)
4. Cluster Computing

Current 2025 SCImago information identifies all four as Q1 in relevant computing/network categories. Quartile is time/category dependent and must be rechecked at actual submission.

### Scope-fit reconciliation

**JNCA**
- Publisher scope explicitly welcomes research in computer networks and applications, including new design techniques, cloud computing, network protocols, IoT, and network/security applications.
- Q-AHBN's strongest fit axis: adaptive P2P dissemination/network protocol + distributed/cloud-native evaluation.
- Main preparation risk: manuscript must foreground network-protocol contribution and experimental evidence rather than blockchain application narrative alone.

**FGCS**
- Publisher scope explicitly covers distributed systems, clouds, IoT, dynamic resource management, protocols, algorithm design, large-scale communication/computation, scaling and performance.
- Q-AHBN's strongest fit axis: adaptive distributed dissemination + cloud-native/Kubernetes realization + learning-based control.
- Main preparation risk: Kubernetes evidence is operational rather than independent performance confirmation, so cloud/distributed-systems framing must remain evidence-bounded.

**IEEE TNSM**
- Official scope covers management of networks/systems/services, architectures/frameworks, reliability/quality assurance, management functions, enabling/emerging technologies, performance evaluation, scalability and optimization.
- Q-AHBN has a plausible fit through adaptive network control/management and ML-enabled operation.
- Main preparation risk: current manuscript is framed primarily as blockchain dissemination rather than network/service management; IEEE format also imposes a materially tighter page-production constraint (10 pages free; excess-page charges, maximum 16 under current policy).

**Cluster Computing**
- Recent publication record demonstrates active coverage of cloud/edge orchestration, distributed systems, blockchain and ML topics.
- Q-AHBN has natural continuity with its cloud-native distributed-computing evaluation.
- Main preparation risk: broader scope makes fit straightforward but provides less incentive than JNCA/FGCS to sharpen the manuscript toward its strongest network/distributed-systems contribution.

### Autonomous target decision

**Primary target for S16 production: Journal of Network and Computer Applications (JNCA).**

Reason: among the reconciled candidates, the manuscript's frozen scientific centre is a new adaptive dissemination mechanism for a dynamic P2P network, evaluated through protocol-level delivery/delay/communication metrics and complemented by cloud-native realization. This maps most directly to JNCA's explicit computer-network/new-design/network-protocol scope without requiring a scientific reframing or new experiment.

**Fallback 1:** Future Generation Computer Systems (FGCS).  
Use if JNCA fit/editorial outcome is unfavorable. The distributed/cloud-native/Kubernetes dimension is strong enough for FGCS, but the paper would need a somewhat stronger e-infrastructure/distributed-systems framing.

**Fallback 2:** IEEE Transactions on Network and Service Management (TNSM).  
Technically credible, but would require the largest framing and page-format adaptation toward network-management language.

**Fallback 3:** Cluster Computing.  
Strong scope compatibility and Q1 status, retained as a lower-friction fallback.

This ordering is a publication-strategy decision, not a scientific-quality ranking of the journals.

### S16-0 closure decision
No manuscript template was changed during journal selection. No scientific claim, parameter, evidence family or experiment was altered.

**S16-0 = PASS / CLOSED.**

## Next controlled gate

**S16-1 — JNCA Author-Guideline + Submission-Artifact Contract**

S16-1 must retrieve and freeze the current official JNCA requirements before any source-format migration. It must reconcile:
- article type and scope;
- manuscript structure/format;
- word/page constraints if any;
- abstract/highlights/keywords;
- figures/tables;
- references;
- declarations and author statements;
- data/code availability;
- supplementary material;
- anonymization/review model if applicable;
- submission files and editable-source requirements;
- cover letter;
- AI-use disclosure requirements if applicable;
- open-access/APC choices;
- submission portal requirements.

Only after S16-1 closes may S16-2 alter `versions/v0.0/main.tex` or create a target-journal version.
