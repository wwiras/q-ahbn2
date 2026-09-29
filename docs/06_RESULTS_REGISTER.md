# Q-AHBN2 Results Register

**Status:** ACTIVE — K5-Q-FORMAL-PREFLIGHT PASS; 25-RUN EXECUTION RELEASED
**Created:** 2026-09-23 under DOC-SYNC-1

## Registered bounded evidence

### AR-1.4.2 / AR-1.4.3 / AR-1.4.4 — Gamma sensitivity
- Environment: ControlSim Learning Validation
- Candidate gamma: {0.70, 0.80, 0.90}
- Seeds: {42,43,44,45,46}
- Runs: 15/15
- Evidence integrity: PASS
- Scientific comparison: PASS
- Researcher-approved parameter decision: **gamma=0.70 FROZEN**
- Scope limitation: bounded stationary Learning Validation only; not convergence, policy-optimality, or universal-performance evidence.

### Exp10-Q — Failure
- Environment: ControlSim Formal Failure
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Conditions: control and one deterministic non-source peer failure before message 501
- Seeds: {42, 43, 44, 45, 46}
- Methods: AHBN, Q-AHBN2
- Runs: 20/20 completed (0 exclusions, 0 reruns)
- Raw formal directory: `output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal/`
- Analysis directory: `output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal-analysis/`
- Evidence integrity & claim boundary: PASS / CLOSED (S08-CLOSE)
- Scope / claim boundary: condition-specific delivery/delay improvement versus duplicate/forwarding overhead trade-off under one-peer failure; no universal superiority or composite adaptation claims.

### Exp11-Q — Churn
- Environment: ControlSim Formal Churn
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Churn levels: {0.00, 0.20, 0.40} target fractions
- Churn cycles: 4 leave/rejoin cycles (leave before 201, 401, 601, 801; rejoin before 251, 451, 651, 851)
- Seeds: {42, 43, 44, 45, 46}
- Methods: AHBN, Q-AHBN2
- Runs: 30/30 completed (0 exclusions, 0 reruns)
- Raw formal directory: `output/evidence/q-ahbn-28092026203251-exp11q-formal/`
- Closure audit directory: `output/evidence/q-ahbn-28092026212332-exp11q-close-audit/`
- Evidence integrity: PASS / CLOSED (S09-CLOSE)
- Scope limitation: formal evidence completed and frozen under deliberate closure audit; comparative scientific conclusions, statistical aggregation, and inferential claims are deferred beyond this gate.

### Exp12-Q — Heterogeneity
- Environment: ControlSim Formal Heterogeneity
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Resource profiles: balanced, moderate_heterogeneity, weak_heavy
- Seeds: {42, 43, 44, 45, 46}
- Methods: AHBN, Q-AHBN2
- Runs: 30/30 completed (0 exclusions, 0 reruns)
- Frozen formal directory: `output/evidence/Exp12-Q/q-ahbn-28092026215008-exp12q-formal/`
- Evidence integrity: PASS / CLOSED (S10.5)
- Evidence promotion/freeze: PASS / CLOSED (S10.6)
- Scope limitation: formal evidence completed, integrity-verified, promoted and frozen; comparative scientific conclusions and statistical interpretation remain governed by the frozen statistical contract and are not claimed by S10 closure.


### Exp13-Q — Reference Benchmark
- Environment: ControlSim Formal Reference Benchmark
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Scenario: churn = 0.40 with four leave/rejoin cycles
- Seeds: {42, 43, 44, 45, 46}
- Methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2
- Expected runs: 25
- Frozen formal directory: `output/evidence/Exp13-Q/q-ahbn-29092026081836-exp13q-formal/`
- Producing Q-AHBN2 commit: `2b11b4e95ef98c86458e02c494d6b6ea232a6d7a`
- Evidence integrity/completeness: **PASS / CLOSED (S10A-INTEGRITY)**
- Integrity accounting: 25/25 unique formal cells; 5 Q-AHBN2 trace groups; 410,852 structurally validated decision records; 0 exclusions; 0 reruns
- Evidence freeze/promotion: **PASS / CLOSED (S10A-FREEZE)**
- Scope limitation: formal evidence completed, integrity-verified, promoted and frozen; comparative scientific conclusions, aggregation and interpretation remain governed by the frozen statistical contract and are not claimed by S10A closure.

### S11-A — Primary RO4 deterministic aggregation
- Scope: Exp10-Q Failure + Exp11-Q Churn + Exp12-Q Heterogeneity only; Exp13-Q excluded and reserved for S11-B.
- Aggregation evidence: `output/evidence/q-ahbn-29092026111238-s11a-aggregation-formal/`
- Producing aggregation commit: `59ef254099fb3edb617f323dd864324c320d9a85`
- Runs ingested: 80/80; same-seed AHBN/Q-AHBN2 paired comparisons: 40/40.
- Output hashes: aggregation JSON `bec818623c97ae2d9918617694694e90448a2727d703ce72a8923557c48ac337`; summary CSV `9b2d21a103c9cd115acc56a003eb8bab60a49db92bc82af3a8da004d03b33833`.
- Input provenance: Drive raw-byte readback = current local frozen CSV = S11-A manifest for Exp10-Q `c51392ce83435bb15691d60b42cfb5c91971687f05b51c1bd21a2f69444edcf7`, Exp11-Q `d869f4c76cd139b2dd554de5e5a8bf61d8403e8b223106f7809200676347f00c`, Exp12-Q `dd5504109cae59b1494dc409308585906676f69c79e0c41d3845856e6762bc66`.
- PREP hash discrepancy: earlier PREP-recorded hashes differ and are retained as a provenance-record discrepancy; authoritative Drive/local/manifest evidence is mutually identical and no formal evidence was rewritten.
- Google Drive preservation: folder `q-ahbn-29092026111238-s11a-aggregation-formal`, ID `1XMWn5FWKwJV78YeTGakJb1bVJ6XKfrLH`; four expected artifacts confirmed by readback.
- Evidence freeze/closure: **PASS / CLOSED (S11-A-1)**.
- Claim boundary: aggregation/provenance closure only; comparative scientific interpretation remains deferred. S11-B must analyze Exp13-Q separately as bounded external reference evidence.


## S11-B — Exp13-Q External Benchmark Aggregation
- Status: **S11-B-1 PASS / CLOSED** (2026-09-29).
- Scope: bounded Exp13-Q external reference benchmark only; 25/25 frozen runs at churn=0.40 across Gossip, Structured, DC-SoC, AHBN and Q-AHBN2.
- Formal aggregation evidence: `output/evidence/q-ahbn-29092026121201-s11b-aggregation-formal/`.
- Source CSV SHA-256: `5b9f09c8403e7e287d631986fb76727542264eca5f07227b57d3e19b868c4708`.
- Aggregation JSON SHA-256: `37ba7c1d77c93af21d3c2581d3f95b6752858afd5f461d1231850d625d6ec223`.
- Summary CSV SHA-256: `e48c0d2a4479a05ed5826fe83c627dceef71f2629f316e303924d7adb16d0aa3`.
- Google Drive frozen evidence folder ID: `1frfPsofGtbvpRFCxFMjGi_EZUuv8tNxx`.
- Statistical boundary: descriptive summaries plus predeclared same-seed Q-AHBN2-minus-reference contrasts; no p-values, omnibus score, ranking, winner claim, or interpretation.
- Exp13-Q remains separate from the primary S11-A RO4 aggregation.


## Current controlled stage
- **S11 complete; Kubernetes chain next.**
- S11-A primary RO4 aggregation: PASS / CLOSED.
- S11-B Exp13-Q external benchmark aggregation: PASS / CLOSED.
- K0-Q Kubernetes scope reconciliation: PASS / CLOSED.
- K1-Q Kubernetes design/code mapping: PASS / CLOSED.
- K2-Q GKE integration/parity verification: **PASS / CLOSED (2026-09-29)**.
- K2-Q local verification: focused deterministic suite **9/9 PASS**; full repository regression **78/78 PASS**; synchronized `main` clean.
- K3-Q-PREP deployable runtime assembly: **PASS (2026-09-29)**; inherited `ahbn2_gke` runtime/Helm assets assembled under `q-ahbn2/gke/` with additive Q-AHBN2-only runtime wrapper.
- K3-Q first deployment attempt: **STARTUP INVALID / diagnostic only** — container failed before Python execution with `exec /usr/local/bin/python: exec format error`; classified as image-architecture/build-provenance defect, not algorithm evidence.
- K3-Q-D1 architecture diagnostic/correction: **PASS (2026-09-29)**; build now explicitly targets `linux/amd64` and smoke preflights/records pushed image manifest.
- K3-Q-D2/D3 verifier corrections: **PASS**; registry architecture verification was hardened to a platform-constrained pull plus image-config inspection.
- K3-Q-D4 packaging correction: **PASS**; missing inherited `gen_topology.py` dependency added to the image and guarded by a local real-container import preflight.
- K3-Q bounded GKE smoke: **PASS / CLOSED (2026-09-29)**; image `wwiras/q-ahbn2:k3q-smoke-amd64-d4-20260929`, digest `sha256:dc6c6ceeec0220e51b03f76313a3cfa6448be9647c00e0a68a8a6abccbf33f52`; 4/4 pods Ready; 15 Q decisions, 17 attributed attempts, 11 reward closures; evidence `output/evidence/q-ahbn-gke-29092026140017-k3q-smoke/`.
- K4-Q Kubernetes protocol freeze: **PASS / FROZEN (2026-09-29)**. One shared 25-run matrix (5 methods x seeds 42--46) is frozen; the 10 AHBN/Q-AHBN2 cells simultaneously serve K8s-VAL-Q, avoiding duplicate execution. Kubernetes-native matched scenario: N=20, BA(m=2), source 0, 240 messages at 0.4 s, four absolute leave/rejoin events at +1/+26/+51/+76 s using the validated inherited churn lineage. This is a matched cross-environment benchmark, not literal Exp13-Q-Sim replication.
- K5-Q-PREP harness/artifact preparation: **PASS (2026-09-29)**. Added executable 25-coordinate contract, fail-closed pre-execution audit, immutable AMD64 formal-image build/preflight, formal artifact completeness validator, and regression guards. No formal GKE coordinate executed and no formal outcome inspected.
- Current gate: **K5-Q-PREEXEC — Human local regression + immutable formal-image build/preflight**; formal GKE execution remains blocked until this passes.
- S12 interpretation remains blocked until the Kubernetes chain K0-Q through K6-Q is completed and its evidence frozen.

## K5-Q-PREEXEC diagnostic — 2026-09-29
- Local K5-Q preparation tests: **4/4 PASS**.
- Standalone 25-coordinate preparation audit: **PASS**.
- First formal-image wrapper attempt: **INVALID / no build started** due solely to missing repository root on Python module search path.
- K5-Q-PREEXEC-D1 correction: **PASS**; build wrapper now injects repository root into `PYTHONPATH`.
- Current gate remains **K5-Q-PREEXEC — corrected immutable formal-image build/preflight**.

## K5-Q-PREEXEC closure — 2026-09-29
- **PASS / CLOSED**.
- Formal image: `wwiras/q-ahbn2:k5q-formal-20260929`.
- Platform: `linux/amd64` verified.
- Digest: `sha256:dc6c6ceeec0220e51b03f76313a3cfa6448be9647c00e0a68a8a6abccbf33f52`.
- Real-container import preflight: PASS.
- Git/control release HEAD: `a6cea140604a268fc0c781c8dcc2130eb1923efa`.
- Digest identity with K3 reflects unchanged container runtime content; K5 provenance must record image digest and Git/control SHA separately.
- Current gate: **K5-Q-FORMAL — exact frozen 25-coordinate GKE execution**.

## K5-Q-FORMAL-PREP — 2026-09-29
- **PASS / assembled prospectively; 0/25 formal runs executed.**
- Imported pinned K7 churn/controller/target-selection/Helm Job assets required by the broader formal matrix.
- Standalone AHBN formal path explicitly uses final S5; Q-AHBN2 remains the frozen post-AHBN refinement.
- K4-Q-A1 prospective correction: fixed source=0 replaced by inherited deterministic common non-structural source per seed because peer 0 is a frozen churn target.
- Locked formal runner: `gke/scripts/run_k5_q_formal.sh`; exact 5 methods x 5 seeds; per-run validation and final matrix manifest.
- Previous formal image is superseded for K5 execution because formal controller/runtime packaging changed before run 1/25.
- Current gate: **K5-Q-FORMAL-PREFLIGHT — local regression + rebuilt immutable formal image/preflight**.

## K5-Q-FORMAL-PREFLIGHT-S1 — 2026-09-29
- **PASS**; 0/25 formal GKE runs executed.
- Local K5 regression: 5/5 PASS.
- Preparation audit: exact 25-coordinate contract PASS.
- No-GKE full matrix generation/contract validation: PASS.
- Per-seed common sources: 42->1, 43->1, 44->1, 45->2, 46->1; no collision with frozen churn targets `(0,5,10,15)`.
- Remaining gate: rebuilt immutable v2 formal image + expanded container/controller preflight.

## K5-Q-FORMAL-PREFLIGHT-D1 — 2026-09-29
- v2 image build/push and `linux/amd64` registry verification: PASS.
- v2 digest: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`.
- Expanded import preflight: INVALID before imports due literal `\\n` wrapper syntax defect.
- Wrapper corrected and regression guard added; 0/25 formal runs executed.
- Current gate remains K5-Q-FORMAL-PREFLIGHT-S2 pending corrected container import preflight.

## K5-Q-FORMAL-PREFLIGHT-D3 — 2026-09-29
- Final local regression: 6/7 PASS; sole failure was an inverted newline regression assertion.
- Production preflight content was already correct and had previously passed real-container imports.
- Test corrected to require a genuine newline and reject literal `\\n`.
- Test-only correction; v2 image/digest unchanged; 0/25 formal runs.

## K5-Q-FORMAL-PREFLIGHT closure — 2026-09-29
- **PASS / CLOSED**.
- Final local K5 regression: **7/7 PASS**.
- Preparation audit: **PASS**, exact 25-coordinate matrix.
- Formal image: `wwiras/q-ahbn2:k5q-formal-v2-20260929`.
- Platform: `linux/amd64`.
- Pinned digest: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`.
- Real-container runtime/controller import preflight: PASS.
- Host-runner Helm paths and newline regression guards: PASS.
- Formal run count at release: **0/25**.
- Current gate: **K5-Q-FORMAL — exact frozen 25-coordinate GKE execution**.

## K5-Q-FORMAL-D4 — 2026-09-29
- First formal invocation stopped pre-coordinate on sole untracked generated file `gke/helm/ahbn/topology.json`; tracked diff was empty.
- Generated Helm topology is now explicitly ignored.
- Clean-tree provenance check moved before evidence creation/mutation and regression-guarded.
- Runtime/science/image unchanged; formal count remains **0/25**.

## K5-Q-FORMAL-D5 — 2026-09-29
- Formal campaign stopped after seed42/Q-AHBN2 controller completion in post-run validation: inherited validator rejected expected canonical AHBN/S5 traces in Q-AHBN2.
- Validator reconciled with frozen architecture: AHBN and Q-AHBN2 are both adaptive trace-bearing methods; standalone baselines remain trace-isolated.
- Q-AHBN2-specific learning-evidence checks remain unchanged.
- Raw stopped evidence preserved; no performance-triggered rerun or full-campaign restart authorized.
- Execution HOLD pending local regression and in-place seed42/Q-AHBN2 artifact revalidation.

## K5-Q-FORMAL-D5 closure — 2026-09-29
- Corrected validator regression: **9/9 PASS**.
- Preserved seed42/Q-AHBN2 coordinate revalidated in place: **K7 RESULT VALIDATION PASS**.
- No same-coordinate rerun required.
- Formal progress: **5/25 validated; 20/25 remaining**.
- Resume mode added: same evidence root, same frozen image/digest, validate-before-skip, execute missing coordinates only.

## K5-Q-FORMAL-D6 — 2026-09-29
- Resume reached seed43/Q-AHBN2 after seed43 Gossip/Structured/DC-SoC/AHBN validated.
- Seed43/Q-AHBN2 diagnostic: AHBN controller=1331; standalone S5 events=0; Q decisions=1065; outcomes=756; reward closures=480; forwarding attempts=733.
- Source audit confirms Q-AHBN2 computes frozen S5 directly and embeds AHBN/S5 proposal in Q decision; standalone S5 event belongs to standalone AHBN path only.
- Validator corrected to the frozen evidence shape; runtime/image/science unchanged.
- HOLD pending in-place seed43/Q-AHBN2 revalidation.
