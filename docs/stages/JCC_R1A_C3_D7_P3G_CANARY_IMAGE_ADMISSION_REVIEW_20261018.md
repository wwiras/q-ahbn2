# P3G-CANARY-PREEXEC — Exact-image identity and release-condition review (2026-10-18)

**Decision: READ-ONLY REVIEW COMPLETE / LIVE CANARY HOLD.** No GKE action, image build, registry push, namespace mutation or experiment execution is authorized by this review.

## Reviewed authorities
- RO4 code: https://github.com/wwiras/q-ahbn2 ; latest reviewed main: `b7314f92d53ad5ee8dfe9ad0780483f86875201d`.
- P3G-V3 actual verified source: `2f3d66ac7fc9ffb3653cc8005f00bd167c3232b5`; offline CI https://github.com/wwiras/q-ahbn2/actions/runs/39126351325 — 39 recovery/integration + 22 frozen-learning regression tests pass. This is **offline**, not image/deployment parity.
- `gke/app/Dockerfile.qahbn2` includes the recovery module and new peer.proto; production runtime imports qahbn2_runtime.
- Legacy `gke/scripts/run_d7_smoke.sh` pins `docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`. This was approved for the **historical Gossip seed-42 canary**, NOT demonstrated to contain P3G recovery changes. `gke/scripts/d7_p3_verify.sh` also pins legacy digest and older source SHA. Do not reuse these as P3G image-parity evidence.
- Prior safety record `docs/stages/JCC_R1A_C3_D7_SM_CANARY_RELEASE_20261017.md` flags insufficient readiness threshold and weak remote-main parity enforcement.

## Requirements before release
1. Freeze an exact new source commit containing current P3G recovery and test fixes. Record `git rev-parse HEAD` plus clean worktree, reconcile to GitHub authoritative source. Document controller and peer modules included in the image.
2. Build container from `gke/app/Dockerfile.qahbn2`, verify imports of `recovery_availability`, `peer`, `qahbn2_runtime`, generated `peer_pb2_grpc.NotifyRecoveryRejoin`; verify architecture and immutable registry digest, plus label/build provenance linking exact source. Do **not** substitute source-file SHA256 for image manifest digest.
3. Critical: image build alone is insufficient; inspect actual candidate Pod image specs and runtime imageID after deployment, including peer StatefulSet and controller job; record image digest and control Git SHA separately. Prevent mixed old/new pod versions. `P3G_RECOVERY_ENABLED` defaults false; require explicit verified activation solely for approved recovery canary and preserve rollback path.
4. Run fresh, **read-only** admission: intended kubectl context, actual Ready/schedulable nodes for 20 peers, resource quota/requests, absence of dedicated namespace, service account/namespace access, source revision and clean checkout, evidence destination, interruption and UID/owner-verified cleanup plan. Previous read-only check is stale.
5. Preserve exact nonformal seed-42 workload (N=20, BA m=2, 240 messages every 0.4 s, churn offsets 1/26/51/76 s) only if using an appropriately approved strategy. Prior one-canary authorization was Gossip only and does **not** authorize corrected AHBN or Q-AHBN2 canary; ensure chosen strategy directly tests corrected recovery path. Do not relabel Gossip validation as AHBN/Q-AHBN2 evidence.
6. Before launch require **new explicit researcher authorization** identifying strategy, exact digest, source SHA, and one nonformal run. No auto-run. On any mismatch HOLD.
7. After any later run, independently audit per-peer recovery/status logs, delivery and duplicate metrics without inflating interpretation, namespace absence and SHA256 evidence; never claim formal D7-F or D8 success from smoke.

## Scientific and editorial controls
No AHBN controller threshold/weight, S5 actuator, Q-learning state/action/reward/parameters, or historical experimental datasets are changed here. Journal of Cloud Computing manuscript is under peer review, not published, no DOI. Formal D7-F 0/25 and D8 remain HOLD.

**Gate result:** historical launcher image digest ≠ verified proof of updated runtime. New image provenance and fresh admission are outstanding. Canary NOT RELEASED.
