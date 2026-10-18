# P3G-CAP3 — Recovery-enabled launcher verification (2026-10-18)

## Decision: OFFLINE PASS; LIVE RECOVERY CANARY NOT AUTHORIZED
Exact verification commit: `baeabd3d2a8d328192b036a250d3d22a1480aba5`.
GitHub Actions run: https://github.com/wwiras/q-ahbn2/actions/runs/39131675989 (**SUCCESS**, completed).
Logs show 39 integrated P3G tests PASS, 11 CAP3 launcher tests PASS, and 22 frozen-controller regression tests PASS (72 tests total), plus Bash syntax verification. This is offline verification; no GKE resources were mutated.

## Requirements verified
1. **Recovery explicit and opt-in.** Helm `recovery.enabled` defaults to `"0"`. `run_k7_experiment.sh` reads `P3G_RECOVERY_ENABLED` (default 0; must be 0/1), supplies the value to Helm install and upgrade, and verifies the observed StatefulSet peer container environment before rollout.
2. **Exact immutable image and twenty peers.** In recovery mode the runner requires the approved image `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`, with matching supplied digest. Recovery mode requires `num_nodes=20` before namespace creation. After rollout, the launcher checks 20 peers and each peer's requested image and runtime imageID; it also checks the controller Job's image. It does **not** yet check a controller pod's runtime imageID, so that remains a canary evidence item.
3. **Ownership and cleanup safeguards.** Existing-namespace refusal, permitted naming, exact kubectl context, run ownership label and namespace UID, refusal to delete on ownership mismatch, and separate experiment/cleanup exit statuses were retained. These were exercised by static assertions and early negative-guard subprocesses; no real namespace cleanup occurred.
4. **No algorithm change.** Peer recovery controller, scoring, fanout, Q-learning, and learning parameters were untouched. Historical runs default OFF; no resource sizing or spending decisions were introduced.

## Source changes
- `gke/scripts/run_k7_experiment.sh`: recovery flag, dedicated P3G namespace, immutable digest, precreate N20 guard, actual StatefulSet flag check and controller Job image check (commits `828a7048`, `39c4c2a0`).
- `tests/test_p3g_cap3_launcher.py`: 11 offline negative and static guards (commit `eb4aedcb`).
- `.github/workflows/p3g-offline.yml`: run CAP3 checks on launcher and chart changes (commit `baeabd3d`).

## Important limitations and next gate
The completed CI suite proves offline contract consistency and rejects specific invalid inputs. It does not prove live namespace lifecycle, actual peer forwarding under recovery, canary outcomes, or running controller pod imageID parity. A separately reviewed and explicitly user-authorized recovery canary is required for those claims. Preserve GKE logs, epoch/rejoin event evidence, runtime imageID, outcome and cleanup receipts, and SHA256 checksums in canonical Drive evidence on execution. Do not label CAP3 as live PASS.

**Next gate:** P3G-CAP4 — controlled recovery canary plan/admission; **no deployment authorization in this record**. D7-F and D8 remain HOLD. User controls GKE costs and capacity independently.

Manuscript status: *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* submitted to Journal of Cloud Computing; under peer review, not published, no DOI.
