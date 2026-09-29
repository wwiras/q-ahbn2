# K6-Q — Kubernetes Evidence Integrity / Freeze

**Status:** PASS / CLOSED — 2026-09-29

## Objective
Audit completeness, validity and provenance of both K8s-VAL-Q and Exp13-Q-K8s evidence and deliberately preserve verified artifacts.

## Required provenance families
Manifests, image/container provenance, Git commit, topology, source, event/churn schedule, workload timing, metrics, learning traces where applicable, comparator identity, Kubernetes metadata, seed/repetition mapping, exclusions/failures and exact K4-Q protocol version.

## Evidence-role separation
- K8s-VAL-Q evidence supports bounded AHBN-versus-Q-AHBN2 deployment validation.
- Exp13-Q-K8s evidence supports a matched five-method cloud-native reference benchmark corresponding to Exp13-Q-Sim.
- Cross-environment comparison must not be labelled literal replication unless later parity/equivalence evidence supports that stronger description.

## K6-Q integrity audit — 2026-09-29

### K5 closure prerequisite
K5-Q final full-cycle reconciliation returned:
- `status = PASS`;
- `runs = 25`;
- `coordinates = complete`;
- `K5-Q FORMAL 25/25 PASS`.

The reconciliation revalidated and skipped all 25 existing coordinates; it did not rerun an experiment.

### Independent Google Drive readback
The synchronized formal evidence folder was found as:
- folder: `q-ahbn-gke-29092026155435-k5q-formal`;
- stable Drive folder ID: `15iFp5E2NCKnewFFObLp3xvVQK3IsXjeP`.

Drive hierarchy readback confirmed:
- exactly five run-seed folders: 42, 43, 44, 45, 46;
- every seed folder contains exactly Gossip, Structured, DC-SoC, AHBN and Q-AHBN2;
- therefore the preserved run hierarchy contains exactly the frozen 5 x 5 coordinate matrix.

Q-AHBN2 run-folder readback for all five seeds confirmed preservation of the expected deployment evidence families, including `metrics.json`, `run_manifest.json`, topology/role mapping, `logs.jsonl`, final snapshots, controller logs, pod-readiness evidence, Kubernetes pod metadata, peer streams and generated configuration.

### Matrix-manifest audit
Drive raw-byte readback of `matrix_manifest.json`:
- size: 89,881 bytes;
- SHA-256: `d1fbc037ef9da5c253ad0b2d3851a555bdd9165f30d499011d65653aee88d7bf`;
- manifest status: `COMPLETE`;
- runs: 25;
- unique coordinates: 25;
- run statuses: 25/25 `VALIDATED`;
- seeds: 42--46;
- methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2;
- producing Git SHA recorded uniformly: `7ad474c3a249fde58223f2abd5d54918b4bcbb9f`;
- image recorded uniformly: `wwiras/q-ahbn2:k5q-formal-v2-20260929`;
- digest recorded uniformly: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`;
- contract version recorded uniformly: `k7-exp11-v2`;
- message count: 240;
- planned interval: 0.4 s;
- churn offsets: +1/+26/+51/+76 s;
- frozen churn targets: (0,5,10,15).

Root provenance readback independently matched:
- `git_commit.txt = 7ad474c3a249fde58223f2abd5d54918b4bcbb9f`;
- `image.txt = wwiras/q-ahbn2:k5q-formal-v2-20260929`;
- `expected_image_digest.txt = sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`;
- `git_status.txt` is empty, recording a clean producing worktree.

Generated-config readback confirms the frozen deterministic common non-structural source mapping:
- seed 42 -> peer 1;
- seed 43 -> peer 1;
- seed 44 -> peer 1;
- seed 45 -> peer 2;
- seed 46 -> peer 1;
with target peers (0,5,10,15), so no source/target collision occurs.

### Deliberate evidence promotion / freeze
Automatic synchronization alone is not evidence authority under `docs/00_SOURCE_AUTHORITY_REGISTER.md`. K6 therefore deliberately classified the verified formal directory under a dedicated evidence family without copying or rewriting the artifacts.

Created evidence-family folder:
- name: `K8s-VAL-Q_Exp13-Q-K8s`;
- Drive folder ID: `1dq5s83YC9-BH2PTj-VaeP_c1VirfxcFJ`.

The existing formal folder was moved from the generic synchronized `output/evidence` parent into this dedicated evidence-family folder:
- formal folder ID remained `15iFp5E2NCKnewFFObLp3xvVQK3IsXjeP`;
- artifact identity therefore remained stable;
- no raw experimental file was rewritten by the promotion.

Post-move Drive readback confirmed the dedicated evidence-family folder contains the same formal folder and that its root still contains the manifest, provenance files, run hierarchy, raw/generated/config/target-selection evidence, K4 freeze record and terminal log.

## K6-Q result

$$\boxed{\textbf{K6-Q = PASS / CLOSED — Kubernetes evidence integrity verified and deliberately frozen}}$$

## Claim boundary
K6-Q establishes completeness, provenance and preservation only. It does not interpret comparative performance, rank methods, pool ControlSim and Kubernetes outcomes, or claim literal cross-environment replication.

The two evidence roles remain separate:
1. K8s-VAL-Q: bounded AHBN versus Q-AHBN2 deployment validation.
2. Exp13-Q-K8s: matched five-method cloud-native reference benchmark.

## Next permitted action
**S12 — Interpretation**, subject to the frozen statistical and claim boundaries and the later S12A claim-reconciliation gate.
