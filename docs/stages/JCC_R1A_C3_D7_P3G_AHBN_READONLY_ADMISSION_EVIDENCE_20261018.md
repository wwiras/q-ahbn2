# P3G AHBN read-only admission — evidence audit (2026-10-18)

**Decision: LOCAL HELM LINT PASS; READ-ONLY PRELIMINARY ADMISSION PASS; FULL CAPACITY/CLEANUP/IMAGE RUNTIME PARITY NOT ESTABLISHED; CANARY HOLD.**

Authoritative Git commit of executed read-only script: `175c0acd1cb08ae7452df75809bdbc6a31364d65`.

Canonical synchronized Drive evidence folder: https://drive.google.com/drive/folders/185Tj0oDRhSSBk2qULPOV1jMtKhVnXG9M (16 files, including `SHA256SUMS`). No further Drive upload needed for this run.

Researcher's local output:
- `helm lint gke/helm/ahbn` PASS: 1 chart, 0 failures; icon recommendation informational.
- `P3G_STRATEGY=ahbn bash gke/scripts/p3g_recovery_admission_readonly.sh`: `READ-ONLY PRELIMINARY CHECKS PASS; SEPARATE CANARY APPROVAL STILL REQUIRED`.
- Three warnings `resource 'namespaces' is not namespace scoped` were observed. These result from the RBAC probe form and are not admission failures; cleanup permission must still be reviewed later.

Drive readback:
- `decision.txt`: read-only preliminary checks PASS.
- `manifest_check.txt`: peer and controller planned image match; peer recovery flag explicitly `1`.
- `image.txt`: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`.
- `kube_context.txt`: `gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster`.
- `nodes_check.txt`: 7 ready AMD64 nodes out of 7 ready nodes.
- `namespace.txt`: empty, indicating the dedicated `qahbn2-d7-smoke-ahbn` namespace was absent at inspection.
- `rbac.txt`: queried namespace create/get/delete, StatefulSet create/delete, Job create/delete, Pod get/list/log permissions all return `yes`.
- Evidence includes `nodes.json`, `quotas.json`, `limitranges.json`, rendered Helm manifest, local commit, UTC, and SHA256SUMS. Full independent file-by-file checksum recomputation for this *new* admission folder remains a subsequent optional integrity audit; presence alone is not byte-level verification.

**Remaining before proposing release:** Review actual quota and schedulable N=20 capacity (seven ready nodes alone do not demonstrate 20-pod capacity); recoverable namespace ownership/cleanup protocol; fresh read-only context/namespace checks immediately before any authorized run; runtime peer and controller pod `imageID` parity cannot be established without a separately authorized execution. The old Gossip-only launcher must not be reused.

No GKE deployment, pod creation, canary or formal experiment was performed by this read-only inspection. AHBN/Q-AHBN2 algorithms frozen. D7-F and D8 HOLD. Manuscript remains under peer review at Journal of Cloud Computing; no DOI, not published.
