# P3G-CAP5 — AHBN seed-42 nonformal recovery canary execution boundary (2026-10-18)

## Intent and decision
Researcher named next controlled action: **one nonformal recovery-enabled AHBN churn canary**, BA(m=2), 20 peers, seed 42; test whether a GetStatus-confirmed returning neighbor becomes eligible for later forwarding. **Execution remains HOLD until explicit run authorization**, consistent with CAP4. No deployment can be performed by GitHub connector.

## Frozen provenance
- CAP4: `docs/stages/JCC_R1A_C3_D7_P3G_CAP4_CANARY_ADMISSION_20261018.md` (commit `d842c61039baf3b24c32ff0c784465e1765227fd`).
- Runtime: `gke/scripts/run_k7_experiment.sh`; read-only admission: `gke/scripts/p3g_recovery_admission_readonly.sh`.
- Approved candidate image: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`.
- Recovery opt-in: `P3G_RECOVERY_ENABLED=1`; namespace `qahbn2-d7-smoke-p3g-ahbn`. Historical default remains 0.
- Generate AHBN seed42 config with `gke/app/k7_exp11_tools.py config --base gke/experiments/k5_q_formal.yaml --out <evidence>/configs/ahbn_seed42.yaml --algorithm ahbn --seed 42`; contract expects 240 messages at interval 0.4 s and four churn events. Verify resulting config, topology and target coordinates before deployment; distinguish nonformal canary from frozen formal data.

## Canary sequence (only on separate explicit authorization)
1. Confirm current source SHA, clean tracked state, exact digest and GKE context. Run read-only admission; require receipt PASS and empty target namespace.
2. Preserve original `gke/helm/ahbn/topology.json` and SHA256, generate config/topology outside tracked sources, and prepare deterministic restoration.
3. Run one authorized AHBN recovery-enabled launcher invocation with `P3G_RECOVERY_ENABLED=1`, image/digest pin, target namespace and evidence paths. Do not reuse Gossip-only `run_d7_smoke.sh`.
4. Before controller workload, assert 20 peer pods, runtime `imageID` parity, actual StatefulSet recovery flag. Require controller Job pod runtime imageID and ready/complete event.
5. Collect raw peer/controller logs, `p3g_rejoin_notification`, `peer_availability`, `recovery_probe`, `churn_triggered`, `churn_recovered`, forwarding/message receipts, unavailable neighbor state, and metrics.
6. Verify exactly-once per epoch/target recovery, affirmative GetStatus `recovered=true`, subsequent forwarding to recovered peer, and whether there is sufficient post-rejoin message opportunity. Record failures/inconclusive results, never infer positive recovery from notification or `churn_recovered` alone.
7. Require experiment/cleanup statuses, namespace UID and owner-label provenance, postcleanup absence, restored topology, validated SHA256SUMS, and independent read-only evidence audit before a GKE recovery claim.
8. Upload raw evidence under canonical RO4 Drive `output/evidence` (https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5); preserve exact source-to-image provenance and link receipt from GitHub.

## Boundaries
The current generic runner provides ownership protection but has no external researcher approval guard; never interpret CAP5 documentation as a deployment instruction. Early failed namespace-UID acquisition can leave unowned namespace requiring manual verified remediation, not automatic deletion. This stage does not amend the frozen AHBN/Q-AHBN2 algorithms and is not formal D7-F or D8 evidence. Cost and capacity remain the researcher's responsibility. Manuscript submitted to Journal of Cloud Computing, under peer review, unpublished, no DOI.

**Status:** CAP5 EXECUTION READY FOR AUTHORIZATION / NOT RUN. D7-F and D8 HOLD.
