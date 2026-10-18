# JCC-R1A-C3-D7-SM-POSTRUN-CAUSAL-P3 — Design / Implementation / Evidence Audit

**Date:** 2026-10-17  
**Classification:** NONFORMAL / READ-ONLY / RESEARCHER-AUTHORIZED  
**Status:** INITIAL SOURCE-TRACE AUDIT PARTIAL PASS; MESSAGE-LEVEL CAUSAL COMPLETENESS HOLD  
**Formal experiment:** D7-F 0/25 HOLD; D8 HOLD

## Question and falsifiable hypotheses
Why did dissemination remain low despite 20 ready pods? Explicitly test three competing explanations: (H-I) implementation/recovery behavior deviates from documented design; (H-D) the implemented algorithm follows its specification but has an intrinsic dissemination limitation under the specified churn/topology; (H-B) both contribute. No hypothesis is a default answer. Classify UNKNOWN whenever the current evidence cannot discriminate.

## Sources inspected
- Normative AHBN: `docs/01_CANONICAL_AHBN_CONTRACT.md`; bounded learner: `docs/02_QAHBN2_DESIGN_FREEZE.md`; main project master: `docs/00_QAHBN2_MASTER.md`.
- Actual implementation reviewed on current GitHub main: `gke/app/peer.py`, `gke/app/dcsoc_maintenance.py`, `gke/app/qahbn2_runtime.py`; prior P2 diagnostics: `gke/scripts/audit_d7_sm_causal_p2_readonly.py`.
- Original deployed runtime identity is the pinned digest `docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`, from test checkout `68aa0830873b9d8cb231d9a27bff1bbc19477128`. **Current main source inspection alone does not prove every inspected line was included in deployed bytes.** Before upgrading a finding, compare exact pinned execution checkout and corresponding image provenance.
- Evidence: canonical Google Drive `output/evidence/20261017T133327Z-D7-SM-remaining`, https://drive.google.com/drive/folders/1ol3d0N5lOg1k_KFyvPI93qm5-7o2hM_s ; original seed42 four-method peer event records and P1 checksum audit 108/108 PASS. Researcher P2 terminal event aggregate is recorded in `docs/stages/JCC_R1A_C3_D7_SM_POSTRUN_CAUSAL_P2_20261017.md`. P2 output is not yet separately archived/hashed.

## Code-level observations: observed path, not inferred intent
1. `peer.py` `forward_to_peer()`: on gRPC success or duplicate ACK it removes a peer from `unavailable_neighbors`; on exception or rejection it adds that peer. `cluster_targets()` and `target_peers()` omit unavailable head/parent targets. A peer excluded from all target lists cannot receive an outgoing probe through this path; Kubernetes pod readiness alone does not clear that application's set. This supports a **code-level reachability trap**. Whether retry/refresh is required by the frozen algorithm specification is still to be reconciled and must not be silently assumed.
2. Structured source1: P2 log m9 to peer0 `UNAVAILABLE`; no source attempts for m10–m240; 232/240 source-only. This supports operational gateway exclusion, but an **implementation defect vs design omission** classification needs normative retry/rejoin requirement and exact deployed checkout review.
3. DC-SoC source1: `target_peers()` skips unavailable DAG parent; `DCSOCMaintenance` maintains its own active and structure state, with `sync_peer()` copying repaired role/parent fields to peer state. The code includes real maintenance transitions, but separately tracked `unavailable_neighbors` and maintenance.active must be correlated; no conclusion that maintenance never occurred. P2 m11–m18 deadline errors, 230/240 source-only.
4. AHBN: `target_peers()` computes adaptive mode and realizes either structured head/gateway or gossip from neighbors after unavailable filtering; `ahbn_forwarding_decision` can expose eligible and selected peers. P2 shows source 173 attempts, 172 forward events, 178/240 source-only. Per-message mode, eligible and downstream evidence required; low reach alone does not prove controller design failure.
5. Q-AHBN2: `gke/app/qahbn2_runtime.py` calls canonical AHBN first and `realize_inherited_targets` after a bounded Q action, using `cluster_targets` for structured and filtered gossip eligibility for gossip. P2 confirms 62 empty source realized target sets, all in structured mode, among 240 decisions; 63/240 source-only opportunities. These counts are not interchangeable. Determine for each empty decision whether it followed a frozen prescribed constraint, stale application availability or structural limitation; compare AHBN base proposal to Q-refined mode. Missing `forward_failed` is not proof of complete success; reconcile attempts, ACK outcomes, duplicates and downstream reach.

## P3 classification matrix (provisional; no rhetorical presumption)
| Method | Documented constraints | Implementation/observations | Classification now | Missing discriminating evidence |
|---|---|---|---|---|
| Structured | Head-gateway structural dependence | m9 head0 unavailable; source excludes subsequent forwarding | Recovery/eligibility trap SUPPORTED; design-vs-defect UNRESOLVED | Frozen contract expectation for probing/rejoin; full time sequence & pinned code |
| DC-SoC | DAG parent/core & event-driven repair | 8 source RPC deadlines; maintenance logged | BOTH POSSIBLE / UNRESOLVED | Parent reassignment before/after maintenance, availability set and topology generations |
| AHBN | Frozen deterministic mode/S5 plus eligibility | Source sometimes forwards; 178 source-only | UNRESOLVED | Per-message AHBN mode/k/eligible/selected; each hop/ACK; peer recovery |
| Q-AHBN2 | Canonical AHBN then bounded Q then eligible realization | 62 zero-target structured decisions; 490 source attempts | UNRESOLVED | Base-vs-Q action attribution, empty eligibility cause, outcomes and complete downstream reach |

## Next bounded local-only P3 verification
- Verify P2 log and checksum provenance separately; retain immutable originals. Verify the exact runtime checkout matches the inspected code path.
- Reconstruct for *each of the 240 messages* and each of the four methods: injection source; intended recipient opportunities; source mode and requested fanout; Q baseline/action/refined mode where applicable; selected/eligible/realized targets; attempt destination; ACK, duplicate, reject, timeout and failed RPC; downstream receipt/hops; delivery count; application unavailable-set change and churn leave/rejoin markers.
- For DC-SoC specifically pair `dcsoc_maintenance` action, parent before/after, structural generation and actual source target choice; state UNKNOWN if fields lack direct observations.
- Report conditional causal chains with exact message/event references. For each method label `DESIGN LIMITATION SUPPORTED`, `IMPLEMENTATION DEVIATION SUPPORTED`, `BOTH SUPPORTED` or `UNRESOLVED`; require a cited frozen normative requirement before claiming a software defect or design conformance.
- Produce a new independent report under `output/evidence/<timestamp>-D7-SM-CAUSAL-P3-readonly`, with checksums and readback, **not** by editing old evidence. Local Python read-only analysis is permitted; no GKE calls, deployment, image rebuild, parameter/controller alteration, metric reinterpretation, or formal run.
- If existing telemetry cannot support an inference, list the precise missing field or counterfactual rather than inventing a diagnosis. Do not use unpaired historical Gossip canary as matched formal baseline.

## Publication and gate safeguards
The Q-AHBN manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is **under peer review at Journal of Cloud Computing, not published, no DOI**. Do not make a publication claim or update the manuscript's efficacy interpretation from this NONFORMAL smoke.

Thesis code/text authority: https://github.com/wwiras/MUM_FIT_ThesisWira ; corpus: https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR ; manuscript: https://github.com/wwiras/QAHBN2-Manuscript ; manuscript corpus: https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj ; experiment code: https://github.com/wwiras/q-ahbn2 ; experiment corpus: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5 . Frozen AHBN and Q-AHBN2 remain unchanged. No evidence for scientific release. **D7-F 0/25 HOLD; D8 HOLD.**

## P3 detailed reconstruction script prepared — 2026-10-17
- Exact experimental checkout `68aa0830873b9d8cb231d9a27bff1bbc19477128`: fetched `gke/app/peer.py` (blob `2433404c55d0df5e1e341f6e6ffcb22660db1d74`) and `gke/app/qahbn2_runtime.py` (blob `1bc97905f59e7ed701058b08e42a07e30ef934c3`); these agree with the previously inspected current-main blobs for those paths. This verifies **those two source-file identities** at the original checkout; it does not independently extract and attest complete container bytes.
- Prepared new read-only local script: `gke/scripts/audit_d7_sm_causal_p3_readonly.py` (commit `6e69385cd71c32c54b8a476f35e95dfce10534d8`). Reads each method's existing `peer_stream.jsonl` with streaming JSON object decoding and immutable `churn_events.json`, reconstructs m1–m240 chronological event lists, joins recorded source decisions, target fields, forwarding attempts and terminal observations, attaches validated delivery opportunities, and reports maintenance events where present.
- Writes only a researcher-designated **separate, initially empty** output directory outside the source corpus with `p3_message_trace.json` and `SHA256SUMS`. Script never uses kubectl, Helm, Docker, gcloud or cloud APIs. Code prepared in GitHub; **not yet researcher-executed, tested against local raw evidence or promoted as verified scientific results**. Avoid interpreting an absent event field as zero.
- Exact researcher local invocation from clean checkout:

```bash
 git fetch origin main
 git merge --ff-only origin/main
 python3 -m py_compile gke/scripts/audit_d7_sm_causal_p3_readonly.py
 python3 gke/scripts/audit_d7_sm_causal_p3_readonly.py \\
   output/evidence/20261017T133327Z-D7-SM-remaining \\
   --output-dir output/evidence/20261017-D7-SM-CAUSAL-P3-readonly
 cd output/evidence/20261017-D7-SM-CAUSAL-P3-readonly && shasum -a 256 -c SHA256SUMS
```

- **Important audit limitation:** first-pass event correlation uses `message_id`; cross-peer clock order and ambiguous action-to-ACK identity require manual validation. Maintenance events lack message IDs and are retained separately. The structured diagnostic row establishes a forwarding exclusion pathway; **no method's intrinsic design defect is yet proven**.
- Gate: P3 script PREPARED / LOCAL EXECUTION NEXT; P3 causal completeness HOLD; D7-F 0/25 HOLD; D8 HOLD. No GKE activity, algorithm parameter adjustment, original evidence modification or manuscript result change.

## P3 detailed read-only trace script availability and execution gate — 2026-10-17

A P3 local-only script already exists on main at `gke/scripts/audit_d7_sm_causal_p3_readonly.py` (readback blob `2d293bb69864804e0850e9c68c91d038e786a69d`). It reconstructs 240 message records per method, records original event-stream SHA256, includes source decisions and first-pass hop events and DC-SoC maintenance, and writes a separate `p3_message_trace.json` and `SHA256SUMS` to `--output-dir`. Script inspection PASS for absence of live GKE calls; per-message and method scientific classification remain UNVERIFIED until researcher executes and shares hashed output. Guardrails: choose a fresh output directory outside original evidence; confirm 240 records per method; validate output SHA256; distinguish intermediate terminal/event totals from reconciled ACK outcomes. Original Drive evidence hierarchy was rechecked and contains all four method `peer_stream.jsonl` and `churn_events.json` files. Direct inline Drive text fetch of large peer streams yielded no readable content, so no independent message-by-message execution or root-cause closure is claimed here.

Researcher local command:

```bash
git fetch origin main
git merge --ff-only origin/main
python3 gke/scripts/audit_d7_sm_causal_p3_readonly.py \
  output/evidence/20261017T133327Z-D7-SM-remaining \
  --output-dir output/evidence/20261017-D7-SM-CAUSAL-P3-readonly
cd output/evidence/20261017-D7-SM-CAUSAL-P3-readonly
shasum -a 256 -c SHA256SUMS
```

Stop without overwriting an existing nonempty output directory; no GKE or experimental rerun. The script's `first_pass_trace` represents an observed event sequence, not an independently proven time-ordered causal graph. **P3 detailed reconstruction execution PENDING; D7-F and D8 HOLD.**

## P3 researcher execution and independent Drive readback — 2026-10-18

**Researcher-reported run:** synced `origin/main` through `d06fdc0` and executed the existing P3 read-only script against `output/evidence/20261017T133327Z-D7-SM-remaining`. It produced `output/evidence/20261017-D7-SM-CAUSAL-P3-readonly/p3_message_trace.json`, SHA256 `5cbf0d737b60dbc9c8a0d6d449ec9b1933cd160cde7953246d9ef218e0702cf2`; local `shasum -a 256 -c SHA256SUMS` reported `p3_message_trace.json: OK`.

**Independent evidence retrieval:** The corresponding Google Drive evidence folder was located at https://drive.google.com/drive/folders/1vF-E1Ib0O3vkchGCN7gV4OQij0xOw46L ; it contains the reported report and SHA256SUMS. The full report file was fetched for local analysis and independently recomputed to have exactly the reported SHA256 digest. No original logs were edited, no cloud/GKE execution was performed by this audit. The hashed report contains 240 reconstructed message records for each of four methods (960 message records total). The report is a first-pass event reconstruction, **not** independently verified complete causal attribution.

| Method | Messages | Messages reaching only source | Exact message-level observed pattern |
|---|---:|---:|---|
| Structured | 240 | 232 | Source forwards successfully m1–m8; m9 has failed source forward; m10–m240 have no source forward success |
| DC-SoC | 240 | 230 | Source forwards successfully m1–m10; m11–m18 have failed source forward; m19–m240 do not record source forward success |
| AHBN | 240 | 178 | Source forwarding successes occur across dispersed message IDs, including m10–m19 and m235–m238; no global permanent halt proven |
| Q-AHBN2 | 240 | 63 | 62 source decisions have empty realized targets, **all in structured mode**; remaining source-only message is m9 where target peer0 was selected and recorded Q-attributed outcome `FAILED` with `StatusCode.UNAVAILABLE` |

### Q-AHBN2 specific attribution — readback supported

- Of the 63 source-only messages, **62 have empty realized target sets** and **one (m9) selected target peer0 but failed at the RPC outcome**. No zero-target decision in the report is associated with multi-peer delivery. This partition holds within the retrieved message trace; it does **not** prove what would happen under another topology, seed or rerun.
- Source Q actions paired with prior canonical mode: **145** instances `mode_ahbn=structured` and `SET_GOSSIP` lead to `mode_q=gossip`; another **22** `SET_GOSSIP` occur when `mode_ahbn=gossip`. These are observed choices, not a causal measurement of improvement due to learning.
- At m10 the source makes `SET_STRUCTURED` with `eligible_targets=[]` and `realized_targets=[]`, producing source-only delivery. At m21 `FANOUT_UP` likewise has empty eligible/realized targets; a requested fanout increase does not create eligible peers. At m63 the source makes `SET_GOSSIP` after canonical `structured`, realizes two targets and reports 11 delivered peers. These are examples from a single seed only.
- The P3 event trace explicitly records a Q `FAILED` attempt outcome for m9 even though the aggregate has no `forward_failed` event for Q-AHBN2. Thus interpreting absence of `forward_failed` as zero transport failures is **incorrect**.

### Discriminating causal conclusion and limits

**Verified operational behavior:** Under this smoke configuration, Structured and DC-SoC source paths stop propagating after head/parent RPC failures. AHBN source occasionally forwards later; Q-AHBN2 frequently realizes Gossip forwarding after canonical Structured selection, but also suffers numerous Structured zero-target decisions. These observations strengthen eligibility/recovery failure as a *possible* cause, yet do not isolate algorithmic design failure versus implementation deviation. In particular, exact successful Kubernetes recovery, re-eligibility requirements under frozen contracts, DC-SoC maintenance state, and downstream hop/ACK closure remain unproven. Poor dissemination is real and must not be defended away.

**Decision:** P3 **LOCAL EXECUTION PASS; REPORT SHA256 AND GOOGLE DRIVE READBACK PASS; INITIAL MESSAGE-LEVEL PARTIAL PASS; ROOT-CAUSE / DESIGN-vs-IMPLEMENTATION SCIENTIFIC CLOSURE HOLD.** Next subgate must reconcile normative design expectations with logged application unavailable-set transitions and DC-SoC maintenance before recommending code repair or any algorithm change. D7-F 0/25 HOLD, D8 HOLD. Q-AHBN manuscript remains under peer review at Journal of Cloud Computing, not published, no DOI.

## P3 read-only design and recovery conformance assessment — 2026-10-18

**Input authorities:** frozen `docs/01_CANONICAL_AHBN_CONTRACT.md` and `docs/02_QAHBN2_DESIGN_FREEZE.md`; deployed-checkout source `68aa0830873b9d8cb231d9a27bff1bbc19477128`: `gke/app/peer.py`, `gke/app/dcsoc_maintenance.py`, `gke/app/qahbn2_runtime.py`; original seed-42 `peer_stream.jsonl`; independently checksum-verified P3 `p3_message_trace.json` in Drive folder https://drive.google.com/drive/folders/1vF-E1Ib0O3vkchGCN7gV4OQij0xOw46L (SHA256 `5cbf0d737b60dbc9c8a0d6d449ec9b1933cd160cde7953246d9ef218e0702cf2`).

### Question 1 — Does frozen design require a recovered peer to become eligible again?
**Not explicitly specified in inspected canonical AHBN/Q-AHBN2 contracts.** AHBN contract §8 states that available/active peers in the environment form the eligible set, `k_real <= min(k_request, |N_e|)`; it does **not** normatively specify a universal active retry/probe timer, Kubernetes-ready-to-application-state synchronizer, or precise re-eligibility deadline. Q-AHBN2 retains the canonical realization rule and prohibits unlabelled recovery overrides or interventions before the canonical proposal. Therefore it is justified to flag a recovery coverage/specification **gap** but **not** to declare a frozen-algorithm rule violated or certify adequate recovery design. DC-SoC `dcsoc_maintenance.py` does explicitly implement event-driven `leave`/`rejoin` and explicit `du` reclustering; that is a different mechanism and must be audited against its frozen baseline separately.

### Question 2 — Does the deployed implementation restore eligibility?
**Only partially: conditional on a successful subsequent RPC or duplicate ACK.** In deployed-checkout `peer.py` `forward_to_peer`, a failed/rejected destination is placed in `unavailable_neighbors`; only a later successful forward or duplicate response removes it in the inspected base path. Meanwhile `cluster_targets` excludes an unavailable cluster head, DC-SoC `target_peers` excludes an unavailable parent and Gossip excludes unavailable neighbors. Thus when a Structured leaf has only the excluded cluster-head target it will not generate the outbound RPC that could clear the exclusion. Pod readiness alone does not repair that application-level state in this code path. A different external clearing pathway must be documented before claiming permanent impossibility across the system.

**Structured concrete smoke:** peer1 fails forwarding m9 to head0 with `UNAVAILABLE`; no source forwarding after m9 (232 source-only messages). This is direct evidence of a *persistent forwarding/eligibility blockage in the tested workflow*, not evidence of why the earlier transport error occurred, nor proof of conformance/violation of a missing retry requirement.

**DC-SoC concrete smoke:** source1 has 8 failed `DEADLINE_EXCEEDED` sends to parent0 at m11–m18; no subsequent source forwarding; 230 source-only. The P3 report retains **140 `dcsoc_maintenance` events** (source peer1 eight), but these are unscoped records captured only with `ts` and `peer_id`; it omits original action/role/parent/generation fields, so the report cannot prove whether source1's parent was changed, whether maintenance restored DAG eligibility or whether the application unavailable set was cleared. The code keeps maintenance's `active`/structural model separate from `PeerState.unavailable_neighbors`; this is a potential inconsistency pathway, **not yet an observed verified defect**. A new bounded read-only diagnostic must retrieve the full maintenance record fields from original peer stream and test source parent/availability state across the m11–m19 boundary.

**AHBN concrete smoke:** m9 peer0 failure is recorded. Unlike pure Structured, AHBN's source later selects other Gossip neighbors and forwarding succeeds on some messages, but still has 178/240 source-only. The P3 script's `source_decisions` lists are empty even when `ahbn_forwarding_decision` exists in `first_pass_trace`: the script's `compact` output omits `peer_id` on AHBN decision events because these source events may not carry that field. This is an **audit-extraction attribution limitation**, not proof that AHBN made no decisions. Reconstruct each AHBN source decision using original event schema, `run_id`, `sender_id`/log context and sequence before inferring zero target sets or exhausted eligibility.

**Q-AHBN2 concrete smoke:** P3 captures 240 source `qahbn2_decision` with explicit `peer_id=1`, 62 empty realized targets in Structured mode and one source-only RPC failure (m9). `SET_GOSSIP` after canonical Structured can find eligible Gossip peers, while a Structured choice/KEEP/fanout action with zero eligible Structural peers cannot create a forwarding destination. This behavior conforms to the **eligible-realization bound**; it does **not** by itself establish whether the bounded learning policy is optimal or whether persistent lack of eligible structural targets was caused by stale availability or intrinsic structural design. Cross-method experimental values are NONFORMAL and cannot establish causal algorithm superiority.

### Conformance matrix and decision
| Method | Frozen design/recovery requirement | Observed implementation and evidence | Status |
|---|---|---|---|
| Structured | Structural head dependence; universal recovery/retry rule **not shown** in inspected contracts | Failed head marked unavailable; forwarding ceases after m9 | Operational blockage SUPPORTED; **DESIGN VS IMPLEMENTATION UNRESOLVED** |
| DC-SoC | Event-driven maintenance exists in deployed source; precise frozen K3.4 behavior still needs separate normative read | 140 maintenance events; 8 source failures; maintenance/parent convergence unproven | **UNRESOLVED** |
| AHBN | Eligibility cap and mode switch are frozen; restoration timing not specified | m9 failure; later some Gossip dissemination; P3 source attribution incomplete | **UNRESOLVED** |
| Q-AHBN2 | Must preserve canonical base proposal and eligibility bound; Q intervention cannot manufacture eligible peers | 62 empty Structured targets, observed Gossip refinements and one failed RPC | Realization-bound conformance SUPPORTED for illustrated decisions; **OVERALL ROOT CAUSE UNRESOLVED** |

**Evidence integrity warning:** P3 first-pass reconstruction preserves event records in source-stream order and maintenance only partially; cross-peer events must be ordered by `ts` and correlated with injected message IDs before claiming exact causality. The 140 DC-SoC maintenance events are evidence that maintenance ran, **not** evidence that it successfully repaired forwarding. A Kubernetes-ready pod does not imply its application peer was re-admitted.

**Next narrow audit:** From the original immutable DC-SoC peer log, extract complete maintenance/action/parent/availability transitions around the first source timeout; separately repair only the P3 analysis attribution/report (not scientific controller or original evidence) for AHBN source decision fields. Verify exact frozen DC-SoC K3.4 spec and deployed-checkout code correspondences. Produce a new independent hashed diagnostic, compare against this P3 readback, then reconsider classification. No new GKE runs, no changes to frozen AHBN/Q-AHBN2, and no paper claims.

**Controlled decision:** **P3 DESIGN CONTRACT INTERPRETATION PARTIAL PASS; DEPLOYED-CODE ELIGIBILITY PATH PASS; RECOVERY CAUSAL CONFORMANCE HOLD; D7-F 0/25 HOLD; D8 HOLD.** Q-AHBN manuscript stays *under peer review* at Journal of Cloud Computing, **not published**, **no DOI**.

## P3B — DC-SoC maintenance and AHBN source-decision attribution (2026-10-18)

**Target:** Exp11-style churn, seed 42, NONFORMAL D7-SM; no GKE rerun. New independently generated diagnostic: `gke/scripts/audit_d7_sm_causal_p3b_readonly.py` (GitHub commit `f6f816178e816cecc9b071f788d5b056afee3901`). It reads original immutable `runs/dcsoc/peer_stream.jsonl` and `runs/ahbn/peer_stream.jsonl` using multi-object JSON decoding, extracts all maintenance fields and exact source peer1 failures/successes, and attributes AHBN decisions with the **actual `sender` field** (rather than incorrectly using `peer_id`). It does **not** modify the original P3 script or original evidence. It writes a separate JSON report and SHA256 manifest.

**Direct code-level verification:** pinned deployed `gke/app/peer.py` emits `ahbn_forwarding_decision` with `sender=self.peer_id`, `incoming_sender=sender_id`, `eligible_neighbors`, `selected_peers` and `unavailable_neighbors`; it does not emit `peer_id` on that event. P3's AHBN source_decisions extraction used `peer_id==1`; empty results are therefore an extraction issue, not proof of absent AHBN decisions. Pinned `gke/app/dcsoc_maintenance.py` emits event-driven leave/rejoin/recluster actions; the gRPC `ApplyDCSOCMaintenance` logs `maintenance.events[-1]` and cumulative counters, but `sync_peer` only copies the local peer object's structural configuration, while `PeerState.unavailable_neighbors` is a separately managed set. **Whether maintenance leads to successful forwarding remains unverified.**

Researcher local execution (from repository root, only after fast-forward updating main):
```bash
git fetch origin main
git merge --ff-only origin/main
python3 -m py_compile gke/scripts/audit_d7_sm_causal_p3b_readonly.py
python3 gke/scripts/audit_d7_sm_causal_p3b_readonly.py \
  output/evidence/20261017T133327Z-D7-SM-remaining \
  --output-dir output/evidence/20261018-D7-SM-P3B-readonly
cd output/evidence/20261018-D7-SM-P3B-readonly
shasum -a 256 -c SHA256SUMS
```

**Execution status:** script committed; local P3B trace and checksum **PENDING**. Retain all hypotheses H-I/H-D/H-B open. Do not label maintenance as successful merely because events exist, nor infer an AHBN mode failure without source attribution. Original evidence and algorithms remain untouched. **P3 root-cause HOLD, D7-F 0/25 HOLD, D8 HOLD.** Manuscript under peer review at Journal of Cloud Computing, not published, no DOI.
