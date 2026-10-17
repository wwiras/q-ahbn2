# JCC-R1A-C3-D7-SM-CANARY — Evidence archive and final safety review (2026-10-17)

## Source and scientific boundary
Source HEAD inspected: `fb51abe16557cdc3f93087178a0de3c7fe66f1f4`.
The local regression tested exact operational source `fb264810a545ce26114bbd4608f24bef93deb89e`; the operational runner/launcher blobs remain unchanged in the current HEAD (`c58af41e551ca138bd3cf234d95f4f8bc1c248b4`, `5e9d7611f6118bf4b6484db919b0dce44ea2f891`). The canonical AHBN scientific controller, Q-AHBN2 learning formulation, frozen D7 experimental design, and manuscript claims remain unchanged.

## Step 1 — Canonical Google Drive evidence archive: PASS
Canonical project Drive: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5
Archive folder: https://drive.google.com/drive/folders/1hN6CCIR0qB0eEP9uBmB4UO9gPS3nXKED (within `output/evidence`).
The archive already existed in Drive; no duplicate copy was needed or claimed. Confirmed 19/19 exact byte-for-byte matches from Drive read-back versus the locally verified reference set: `verification_summary.json`, `SHA256SUMS`, `regression.json`, `launcher_negative_tests.json`, `topology_contract_tests.json`, `test_d7_sm_v1_regression.py`, and 13 topology/negative-contract artifacts. The local SHA256 manifest verified, and its unchanged contents match the Drive version. The separate local ZIP `D7-SM-V1-exact-commit-evidence.zip` has SHA256 `561e2a8ba826ce18b2ab8f45bfe83be1865dbf0b668ff45861a380d757521eaa`; its **ZIP object itself was not verified as separately archived on Drive**, but the full extracted evidence set is verified.

## Step 2 — Safety controls inspected
- One-method canary switch: PASS; launcher rejects five-method mode.
- Explicit researcher authorization flag: present, with human consent on record for one NONFORMAL Gossip seed 42 run only.
- Image pinned to docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466.
- Expected kubectl context: `gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster`.
- Dedicated namespace: `qahbn2-d7-smoke-gossip`; preexistence protection is present.
- Namespace UID/owner checks, fail-closed cleanup mismatch behavior, independent experiment/cleanup exit statuses and post-run namespace checks: present; local fault-injection tests passed.
- Workload remains N=20 BA(m=2), seed 42, 240 messages at 0.4 s intervals, four leave offsets 1/26/51/76 s. NONFORMAL classification.

## Outstanding release checks
1. The smoke launcher checks clean Git working tree, but **does not enforce local HEAD parity with remote `origin/main` or a separately approved commit**. Operator must verify exact revision and remote status at point of execution, or introduce a small guard and repeat regression. Do not treat the earlier source read-back as a fresh point-in-time check.
2. The GKE read-only admission PASS was point-in-time on 2026-10-17; **current** cluster context, namespace absence, RBAC, nodes/capacity and billing exposure have not been freshly rechecked at execution. A new read-only preflight is required before cloud mutation.
3. Existing 27/27 local tests cover the runner, rejection paths and topology contract but **do not include a fully successful end-to-end mocked smoke-launcher sequence**. This is a coverage limitation, not a failed test. Live scheduling, image pull and actual cleanup remain unproven.
4. If namespace creation partially succeeds but UID is unavailable, the runner deliberately refuses deletion and requires manual review. SIGKILL/network partition also cannot guarantee cleanup. Researcher must inspect the target namespace and halt on any anomalous/remaining resource.
5. The run must remain classified NONFORMAL, 0/1 until independent post-run evidence/cleanup review. No automatic release of additional smoke or D7-F/D8.

## Controlled gate decision
**Drive evidence archival: PASS. Final safety review: COMPLETE WITH CONDITIONS / LIVE EXECUTION HOLD.** The single Gossip seed-42 canary is **NOT RELEASED** at this point. Next action: researcher performs a fresh READ-ONLY point-of-execution admission and exact GitHub revision reconciliation; independent review must explicitly release exactly one NONFORMAL Gossip canary. Assistant did not contact GKE or incur charges.

Gate states: D7-SM-V1 LOCAL PASS; D7-SM-CANARY HOLD (0/1); remaining smoke HOLD (0/4); D7-F HOLD (0/25); D8 HOLD. The Q-AHBN manuscript is under peer review at *Journal of Cloud Computing*, not published, no DOI.


## P1 — Exact GitHub revision and fresh GKE read-only admission (2026-10-17)

**Read-only GitHub verification:** `wwiras/q-ahbn2` main was checked at `8856c7158768250ae240b20d48aee9086057a3d1`. The pinned launcher Git blob remains `5e9d7611f6118bf4b6484db919b0dce44ea2f891`; it limits execution to a single seed-42 Gossip canary, verifies pinned image and expected context, and requires a clean working tree. A clean worktree **does not** establish parity with GitHub remote HEAD. The current launcher does not itself enforce local HEAD = remote `origin/main`; preserve this limitation and require explicit operator read-only check.

**GKE admission:** No live GKE connectivity from the assistant. Prior seven-Ready-node / 11-permission / namespace-absent record is historical, and **must not be counted as fresh**. Fresh kubectl context, cluster nodes, capacity, namespace absence, and effective RBAC are **NOT VERIFIED**. The researcher must execute read-only checks on their own GKE-authenticated machine and save their unedited outputs and SHA256 evidence to the canonical `q-ahbn2/output/evidence` corpus. Do not use `SMOKE_AUTHORIZED=YES` during this step.

**Decision:** `JCC-R1A-C3-D7-SM-CANARY-P1` remains **HOLD / awaiting operator read-only evidence**. Gossip 0/1 HOLD, other smoke 0/4 HOLD, D7-F 0/25 HOLD, D8 HOLD. No GKE deployment or billing action was performed by assistant. Frozen scientific design unchanged; Q-AHBN manuscript under peer review at *Journal of Cloud Computing*, unpublished and no DOI.
