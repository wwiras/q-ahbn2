# JCC-R1A-C3-D7-SM-POSTRUN-CAUSAL-P2 — Method-specific causal investigation

**Date:** 2026-10-17. **Gate:** READ-ONLY DIAGNOSTIC PARTIAL PASS; CAUSAL COMPLETENESS HOLD. **No live GKE activity or scientific design changes authorized.** Formal D7-F 0/25 HOLD; D8 HOLD.

## Provenance
- Code: [q-ahbn2 GitHub](https://github.com/wwiras/q-ahbn2), `gke/app/peer.py` and `gke/app/k7_exp11_tools.py` on main; original pinned experimental deployed image `docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`.
- Evidence: [canonical Drive smoke folder](https://drive.google.com/drive/folders/1ol3d0N5lOg1k_KFyvPI93qm5-7o2hM_s); original 2026-10-17 NONFORMAL Structured / DC-SoC / AHBN / Q-AHBN2 seed42 runs.
- Previous P1 audit: `docs/stages/JCC_R1A_C3_D7_SM_POSTRUN_AUDIT_P1_20261017.md`. Full SHA256 local audit **108/108 outer entries PASS; each of four run-local manifests 23/23 PASS**. All recorded pods ready, spec/runtime image matched pinned digest and cleanup validated.
- Method scope: N=20, BA(m=2), source peer1, messages=240 at 0.4s, churn peers [0,5,10,15] at offsets [1,26,51,76]s, settle=18s.
- No conclusion from the NOFORMAL smoke is a formal scientific comparison or proof of superiority.

## Parsing qualification
The raw `peer_stream.jsonl` includes several **adjacent JSON objects with no newline separator**. A line-oriented `json.loads(line)` can fail at the concatenation. For this diagnostic audit, objects were parsed with a streaming `JSONDecoder.raw_decode`-style approach, recognizing object boundaries. This finding is a **log-serialization / formatting limitation** that needs documented parser treatment. It is not evidence of a forwarding or metric error by itself. The run metrics were independently reconstructed from validator `churn_events.json`.

## Method-specific results

| Method | Delivery ratio | Raw peer stream events | Source peer forwarding | Observed limitation |
|---|---:|---:|---|---|
| Structured | 0.081273565 | 979 | 9 attempts; 8 success; 1 failed | Source peer stops attempting after message m9 |
| DC-SoC | 0.088865546 | 2511 | 18 attempts; 10 success; 8 failed | Source parent RPC deadlines; restricted reach |
| AHBN | 0.130745016 | 4052 | 173 attempts; 172 successful; 1 failed | Intermittent source forwarding but 178/240 messages remain source-only |
| Q-AHBN2 | 0.341274817 | 12144 | 490 attempts; 486 successful; no `forward_failed`; 4 non-success outcomes to check | Stronger source forwarding than AHBN but insufficient end-to-end reach; many realized target sets empty |

**Structured (confirmed implementation/recovery interaction).** Source peer1 is a leaf pointing to cluster head0. Messages m1–m8 have full eligible-peer delivery. At m9 `forward_failed` from peer1 to head0 is logged with gRPC `StatusCode.UNAVAILABLE` / connection refused. `peer.py` records head0 in `unavailable_neighbors`; `cluster_targets()` returns no targets when cluster head is unavailable. The source subsequently produces no attempts for m10–m240. A successful outbound acknowledgement would remove an unavailable peer, but target selection already excludes head0, trapping this path. The peer's recovery at Kubernetes level is distinct from restoration of *application forwarding eligibility*. Classify: **implemented neighbor state / retry handling failure under churn**, not a proof of correct structural method irrelevance or a controller change request.

**DC-SoC (strong evidence; full state transition needs trace).** Source1 is a leaf whose DAG parent is peer0. m1–m10 delivered near-completely, m11 onward source-only. Source stream shows 8 `forward_failed` attempts towards peer0, including `StatusCode.DEADLINE_EXCEEDED`; `target_peers()` excludes unavailable parent. `dcsoc_maintenance` and multiple RPC trace types are present, so do not assert that maintenance never ran. Audit whether maintenance reassigns parent, whether expected dynamic neighbor state is synchronized, and whether remote availability transitions remain visible to peer1. This could involve both structural single-parent fragility and an implementation/maintenance re-eligibility deficiency. Root cause **not completely proven**.

**AHBN (mixed observation; not a proven algorithm defect).** Source1 sends 173 attempts, 172 successful, and records a single `forward_failed` to peer0 on m9 (`UNAVAILABLE`). Across all peers 32 failures, 515 attempts and 359 successful forwards are visible in raw peer stream; 127 received-duplicate events. 178/240 message opportunities reached only source1, yet source kept forwarding some later messages. The AHBN deterministic controller trace and standalone S5 decisions exist. Distinguish (i) deterministic mode selection, (ii) eligible set after churn, (iii) realized target list, (iv) hop-by-hop propagation failures before judging AHBN design limitations. A sole structural-gateway explanation is unsupported.

**Q-AHBN2 (confirmed bounded learning action/selection traces, adequacy unresolved).** Source1 had 240 `qahbn2_decision` events, including **KEEP 26, FANOUT_DOWN 32, FANOUT_UP 8, SET_GOSSIP 167, SET_STRUCTURED 7**. Realized source target cardinalities: **0:62, 1:8, 2:29, 3:140, 4:1**. Proposed/selected source modes: **gossip 170, structured 70**. 490 source forwarding attempts and 486 successful `forward` events, with 490 attributable outcome events, show that simply attributing low delivery to RPC failure is unsupported. Across the cluster 1,841 attempts, 1,365 successful forwards, 457 duplicate receipts, 1,070 reward-closed events and no `forward_failed` entries appear in the raw stream. m10–m12 source decisions have **empty eligible and realized sets** while in structured mode. This is a concrete local forwarding-reach limiter. Do not confuse the 62 zero-target proposals with 62 source-only messages: propagation can also depend on downstream activity. The frozen Q-learning actions are observable; whether they are scientifically suboptimal remains **undetermined** in a single-seed NONFORMAL test.

### Implementation versus algorithm distinction

**Supported implementation/recovery issue:** Structural head/parent stuck in `unavailable_neighbors`, no outbound retry after selection excludes it. Proven causally for Structured's source pathway. DC-SoC may have overlapping symptoms, but concurrent maintenance must be traced independently.

**Supported algorithmic/design constraints:** Structured relies on a head gateway and DC-SoC on directed parent/core; adaptive controller and bounded Q layer intentionally restrict mode and fanout. Such design constraints can yield limited dissemination on some topologies and stress profiles. The present evidence does *not* separate these intrinsic limitations from implementation and telemetry effects cleanly enough to claim causality for AHBN or Q-AHBN2.

**Potential telemetry limitation:** concatenated adjacent JSON events in stream file; reconstruct event identity robustly, without replacing original evidence or redefining metrics.

## Gate decision
**P2 read-only event inventory PASS; scientific root-cause closure HOLD.** The data show **real inadequate delivery** under the current GKE smoke and must not be defended away. No changes to canonical AHBN, Q-AHBN2 action/reward semantics, metric formulas, experimental outcomes or manuscript efficacy claims.

Next required controlled subgate: reconstruct source and downstream per-message `eligible_targets`, mode, Q actions, `realized_targets`, `k7_forward_attempt`, successful/failed outcomes and rejoin visibility, and review DC-SoC maintenance reassignment. A read-only script is available: `gke/scripts/audit_d7_sm_causal_p2_readonly.py`. Execution is local only; raw evidence untouched. Explicit future approval is required for any code correction, rebuild, or GKE rerun.

## Publication and corpus safeguards
Thesis: [MUM_FIT_ThesisWira](https://github.com/wwiras/MUM_FIT_ThesisWira), [Drive corpus](https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR); RO4 manuscript: [QAHBN2-Manuscript](https://github.com/wwiras/QAHBN2-Manuscript), [Drive manuscript corpus](https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj); RO4 experiment: [q-ahbn2](https://github.com/wwiras/q-ahbn2), [Drive results](https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5). Q-AHBN manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* remains **under peer review at Journal of Cloud Computing, not published, no DOI**.

## CAUSAL-P1 request reconciliation — 2026-10-17
Researcher requested read-only source transmission, eligibility, forwarding, RPC/ACK, recovery and termination investigation. Existing POSTRUN-CAUSAL-P2 already covers the principal initial causal inventory, so the request is reconciled here rather than creating a competing gate. P1 local checksum audit PASS/CLOSED; P2 diagnostic inventory PARTIAL PASS / causal completeness HOLD. Structured source gateway re-eligibility trap is supported; DC-SoC maintenance transitions, AHBN per-message hop reach, and Q-AHBN2 eligible/realized targets plus downstream outcome attribution remain open. No claim of algorithmic defect or superiority is supported. Existing `gke/scripts/audit_d7_sm_causal_p2_readonly.py` is prepared for researcher read-only execution on `output/evidence/20261017T133327Z-D7-SM-remaining`; output should be preserved separately under `output/evidence/` with a checksum and reviewed before any correction or rerun. No cloud calls or science changes authorized. D7-F 0/25 HOLD; D8 HOLD.
