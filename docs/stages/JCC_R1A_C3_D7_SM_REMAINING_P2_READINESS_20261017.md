# JCC-R1A-C3-D7-SM-REMAINING-P2 — Live Authorization Readiness Review

Status: **REVIEWED / NOT RELEASED — LIVE GKE HOLD**. This is a read-only review, not execution authorization.

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
| Cost and exposure | UNBOUNDED in available source | Explicit researcher-approved cost cap, maximum execution duration, billing/project confirmation and shutdown action |
| Cleanup | MOCK PASS; live unverified | Dedicated namespace owner UID/label verified; delete only owned namespace; cleanup PASS and namespace absence after each run |
| Failure and interruption | MOCK PASS for tested signals | Stop on any error; inspect orphaned resources manually on ownership mismatch; SIGKILL cannot guarantee cleanup |
| Evidence | P1 Drive PASS; P2 pending | Per-method run artifacts, exit statuses, namespace cleanup, runtime parity, SHA256SUMS and independent Drive readback |
| Researcher approval | NOT GIVEN | Explicit separate authorization specifying this NONFORMAL four-method run and cost/time ceiling |

## Source observations and risks
1. The launcher checks authorization `SMOKE_REMAINING_AUTHORIZED=YES`, rejects legacy `SMOKE_AUTHORIZED=YES`, requires exact context, clean Git and remote-main equality, pinned image, namespace absence, and safe output/evidence path.
2. The shared runner checks namespace ownership by UID and owner label before deletion, verifies 20 pod image specs and runtime imageIDs, and attempts cleanup on normal/handled failure. It does not provide unconditional cleanup after SIGKILL or inaccessible cluster.
3. Each method can wait up to 600 s for rollout, another 600 s for readiness, and 900 s for controller completion, excluding setup, cleanup and scheduling. Therefore do **not** infer a reliable cost or elapsed-time ceiling from 240 × 0.4 s message injection alone.
4. No verified current cluster status, billing ceiling, node count/cost, or researcher authorization was obtained in this read-only review. Do not assume the historical seven-node cluster configuration is current.
5. The runner's runtime digest check is a strong admission gate, but live runtime parity is not established by local mocks.
6. Existing Drive evidence must remain immutable; any new live output requires separate classification as NONFORMAL and independent audit.

## P2 decision
**NOT READY FOR RELEASE / LIVE GKE HOLD** until the researcher supplies an explicit cost and duration ceiling and authorizes read-only current-cluster admission checks. A subsequent review must assess those checks and obtain a separate affirmative approval **before** invoking the real launcher. Do not set `SMOKE_REMAINING_AUTHORIZED=YES` or execute `run_d7_smoke_remaining.sh` as part of this gate.

Remaining smoke **0/4 HOLD**; formal D7-F **0/25 HOLD**; D8 **HOLD**. Frozen AHBN/Q-AHBN2 scientific logic and manuscript unchanged.
