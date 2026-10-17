# JCC-R1A-C3-D7-SM-REMAINING-P2 — Live Authorization Readiness Review

Status: **TECHNICAL READINESS REVIEW / LIVE GKE HOLD**. This is a read-only review, not execution authorization. Resource spending decisions are explicitly outside this research gate and are controlled by the researcher.

## Authority and scope
- P1 local safety gate PASS/CLOSED, Drive-readback verified: 15/15 launcher mocks, 5/5 real topology-contract tests, separate 9/9 shared-runner mocks. Final-negative source commit `9024d7df3080c195826da08a2469825df87edbca`.
- Source-of-truth scripts: `gke/scripts/run_d7_smoke_remaining.sh`, `gke/scripts/run_k7_experiment.sh`, `gke/app/k7_exp11_tools.py`.
- NONFORMAL D7-SM only: four methods `structured,dcsoc,ahbn,qahbn2`, seed 42, 240 messages at 0.4 s intervals per method, N=20 per run. Gossip canary was previously independently tested.
- Four sequential, dedicated namespaces `qahbn2-d7-smoke-<method>`; no formal D7-F or D8 authorization.
- Pinned image `docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`; expected context `gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster`.

## Readiness matrix (no live checks performed during this review)
| Criterion | Assessment | Release condition |
|---|---|---|
| Local fail-closed regression | PASS, local-only | Maintain tested exact launcher/runner/validator hashes and clean remote main |
| Four-topology contract | PASS, local-only | Generated seed-42 topologies validate on the execution checkout |
| Live GKE context/identity | UNVERIFIED | Researcher confirms project, cluster, active credentials, current context and namespace absence |
| Deployed image parity | UNVERIFIED for four methods | All 20 pod spec references and runtime imageIDs match pinned digest; fail immediately otherwise |
| Cleanup | MOCK PASS; live unverified | Dedicated namespace owner UID/label verified; delete only owned namespace; cleanup PASS and namespace absence after each run |
| Failure and interruption | MOCK PASS for tested signals | Stop on any error; inspect orphaned resources manually on ownership mismatch; SIGKILL cannot guarantee cleanup |
| Evidence | P1 Drive PASS; P2 pending | Per-method run artifacts, exit statuses, namespace cleanup, runtime parity, SHA256SUMS and independent Drive readback |
| Researcher approval | NOT GIVEN | Explicit authorization specifying the NONFORMAL four-method run only |

## Source observations and risks
1. The launcher checks authorization `SMOKE_REMAINING_AUTHORIZED=YES`, rejects legacy `SMOKE_AUTHORIZED=YES`, requires exact context, clean Git and remote-main equality, pinned image, namespace absence, and safe output/evidence path.
2. The shared runner checks namespace ownership by UID and owner label before deletion, verifies 20 pod image specs and runtime imageIDs, and attempts cleanup on normal/handled failure. It does not provide unconditional cleanup after SIGKILL or inaccessible cluster.
3. Each method can wait up to 600 s for rollout, another 600 s for readiness, and 900 s for controller completion, excluding setup and cleanup. Treat timeout handling as a technical fail-stop condition; do not conflate message-injection time with end-to-end experiment execution.
4. Current cluster status, namespace state, runtime image identity and researcher live-execution authorization have not yet been independently verified. Do not assume historical cluster state is current.
5. The runner's runtime digest check is a strong admission gate, but live runtime parity is not established by local mocks.
6. Existing Drive evidence must remain immutable; any new live output requires separate classification as NONFORMAL and independent audit.

## P2 decision
**TECHNICAL ADMISSION PENDING / LIVE GKE HOLD** until read-only current-cluster checks verify context, dedicated namespace absence, image readiness and code provenance. Following those checks, obtain explicit researcher approval for the NONFORMAL four-method smoke **before** invoking the real launcher. Cost and budget decisions belong exclusively to the researcher and are not a release criterion for this gate. Do not set `SMOKE_REMAINING_AUTHORIZED=YES` or execute `run_d7_smoke_remaining.sh` as part of this gate.

Remaining smoke **0/4 HOLD**; formal D7-F **0/25 HOLD**; D8 **HOLD**. Frozen AHBN/Q-AHBN2 scientific logic and manuscript unchanged.

## Researcher scope correction — 2026-10-17
Researcher directed that **cost must not be considered in Q-AHBN2 gate decisions**. The research workflow is restricted to smoke and formal experiment technical readiness, execution, cleanup and evidence validation, using prior Q-AHBN scripts as guidance. Any earlier cost-ceiling requirements in this review are superseded and must not block progression. No live execution has been authorized by this scope clarification alone.

## P2 technical preflight prepared — 2026-10-17

Read-only preflight script: `gke/scripts/run_d7_smoke_p2_preflight_readonly.sh` (commit `1e88c733`). It performs no namespace create/delete, no Helm deployment, and no experiment run. It inspects installed tools, Git status and remote-main equality, GKE context and reachability, four dedicated namespace absences, pinned image identity, source hashes, and Bash/Python syntax. Evidence outputs: `technical_preflight.txt`, `preflight_status.txt`, `preflight_exit_code.txt`, and `SHA256SUMS` under `output/evidence/<UTC>-D7-SM-P2-readonly`.

Run on researcher's Mac only after syncing latest `main`: `bash gke/scripts/run_d7_smoke_p2_preflight_readonly.sh`. **PREPARED / NOT EXECUTED / LIVE FOUR-METHOD HOLD**. If preflight fails, inspect and resolve technically, do not run the launcher.

References: thesis authority `wwiras/MUM_FIT_ThesisWira`; thesis corpus `1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR`; RO4 manuscript `wwiras/QAHBN2-Manuscript`; RO4 manuscript Drive `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`; experiments `wwiras/q-ahbn2`; experiments Drive `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`. Q-AHBN manuscript submitted to Journal of Cloud Computing, **under review, not published, no DOI**. No scientific claims, manuscript or frozen controllers altered.

Current status: P1 PASS/CLOSED; P2 READ-ONLY PREFLIGHT PREPARED / NOT YET VERIFIED; NONFORMAL remaining 0/4 HOLD; formal D7-F 0/25 HOLD; D8 HOLD.

## P2 researcher read-only preflight execution — 2026-10-17
Researcher fast-forwarded to `02133b1ea0ad335db66f663a5d6bfd5ce77c3dad` (local HEAD = remote main) and executed `bash gke/scripts/run_d7_smoke_p2_preflight_readonly.sh`. Terminal reports `decision=PASS_READ_ONLY`. Correct context `gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster`; four method namespaces ABSENT; cluster-info succeeded; pinned image reference as contracted. SHA256 source fingerprints: launcher `d878ce3ba76a5d4e8863abf1132c431bb7b9d419dc3204d18746f0634f2f7407`, runner `ec0f54068ceec9e06fa8fea56f286dce4d4d8e8b91606f0e82b325131be5d132`, validator `2862f8b6dfce5ae9f43808ae05e486d0a3d8c64ab9f557df0dda32d93a5f49e7`. Local evidence `output/evidence/20261017T132927Z-D7-SM-P2-readonly`.

This is a researcher-reported terminal result; local SHA256SUMS verification and independent Drive readback of preflight files remain pending. **P2 READ-ONLY TECHNICAL PREFLIGHT REPORTED PASS / EVIDENCE AUDIT PENDING. LIVE FOUR-METHOD SMOKE HOLD**, formal D7-F and D8 HOLD. Do not treat this as deployed image parity.

## P2 independent canonical Drive evidence readback — PASS
Traversed RO4 Drive corpus `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5` to `output/evidence/20261017T132927Z-D7-SM-P2-readonly` (folder ID `1ObIFtAwmC-rY5DoHObF2Cj0Y1Tfo-bok`). Fetched all four files and compared SHA256SUMS against downloaded bytes:
- `preflight_exit_code.txt`: `0`; SHA256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` — MATCH.
- `preflight_status.txt`: `PASS_READ_ONLY`; SHA256 `f344a82801f4e2d741ec1c730476a3b3e66e9de1a0a5e645c3adae5fbd16a2da` — MATCH.
- `technical_preflight.txt`: recorded exact context, all four namespaces ABSENT, Git HEAD=remote main `02133b1ea0ad335db66f663a5d6bfd5ce77c3dad`, and expected launcher/runner/validator hashes; SHA256 `22de17e42c8d4b612f31c11876cb720ce23cecabd70106653a9166c39e07b2a1` — MATCH.

**Decision: P2 READ-ONLY TECHNICAL PREFLIGHT PASS / EVIDENCE VERIFIED.** This does not establish runtime parity or authorize the remaining live smoke. Separate explicit researcher approval is required before setting `SMOKE_REMAINING_AUTHORIZED=YES` and running the launcher. NONFORMAL 0/4 HOLD; D7-F 0/25 HOLD; D8 HOLD.
