# JCC-R1A-C3-D7-F-SM — Original implementation smoke preflight (2026-10-18)

**Decision: REPOSITORY PREFLIGHT PARTIAL PASS / LIVE GKE SEED42 SMOKE NOT EXECUTED / FORMAL D7-F 0/25 HOLD.**

Researcher directive: follow historical AHBN2-GKE methodology; use original implementation, no new recovery gates or algorithm modification; low delivery during scheduled churn is a measured observation rather than automatic smoke failure. Scientific attribution of any particular loss remains evidence dependent.

## Read-only verification
- Original RO3 K7 and RO4 K5 configuration parity reviewed in prior commit `87b650294dccd6d347f55454c793a5375bea1bbf` and original archive decision `c8d7914c56ca3bcca53cf80f1ad0242e4dcaf88d`.
- RO4 base: `gke/experiments/k5_q_formal.yaml`, N=20 BA(m=2), clusters=4, source=0, settle=18s, 240 messages with 0.4s interval, four scheduled churn events at offsets [1,26,51,76]s, target selection v1, S5; seed42 for smoke; formal seeds 42–46 and methods gossip, structured, dcsoc, ahbn, qahbn2.
- Original pinned image `docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`. Fresh live runtime imageID parity not yet verified.
- Original nonformal launchers `gke/scripts/run_d7_smoke.sh` (Gossip-only, previous canary) and `gke/scripts/run_d7_smoke_remaining.sh` (other four methods). The latter is seed42-only and requires `SMOKE_REMAINING_AUTHORIZED=YES`, an exact GKE context, clean worktree and HEAD=remote main, absent run namespaces and pinned image; preserves SHA256, logs, topology, per-method validation and namespace cleanup proof.
- Shared `gke/scripts/run_k7_experiment.sh` defaults `P3G_RECOVERY_ENABLED=0` and asserts pod image references and runtime imageIDs. **Explicitly set `P3G_RECOVERY_ENABLED=0` at execution**. No CAP5 recovery proposal is a release requirement.
- `gke/scripts/run_k5_q_formal.sh` is formal-labelled and must NOT be used for a smoke run; it loops methods/seeds and requires an independent formal release after smoke audit.
- Historical RO4 formal folder `q-ahbn-gke-29092026155123-k5q-formal` was aborted at dirty worktree; no completed original D7-F runs are documented in that archive. Older D7-SM and P3G evidence is nonformal and must not be relabelled.

## Required live operator verification
1. Confirm `git status --porcelain` empty; `git rev-parse HEAD` matches `git ls-remote origin refs/heads/main`; no uncommitted algorithm change, and the deployment image and current context match the above exact values.
2. Confirm no candidate smoke namespace exists; verify cluster capacity and intended topology/target hashes from generated seed42 artifacts.
3. Execute only the nonformal original seed42 method(s) not already accepted as smoke; use existing dedicated nonformal launcher, `P3G_RECOVERY_ENABLED=0`; retain full logs, metrics, churn schedule/targets, ready/rejoin records, pod/controller imageIDs, namespace deletion receipts and SHA256. Do not overwrite historical evidence.
4. Audit observed deployment, peer communication, four churn/rejoin events, forwarding, metrics/log integrity and cleanup. **Low delivery alone does not fail smoke**. Infrastructure/orchestration/evidence errors do.
5. Mark D7-F-SM PASS only on observed evidence; maintain D7-F formal 0/25 HOLD until separately authorized.

## Status and scientific boundary
No live GKE execution, new result, or actual local preflight was performed by this repository audit. No claim of repaired recovery, superior delivery or sole timing causation. Scientific manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* remains submitted to Journal of Cloud Computing, under peer review, unpublished and without DOI.

Evidence root: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5 ; thesis corpus: https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR.
