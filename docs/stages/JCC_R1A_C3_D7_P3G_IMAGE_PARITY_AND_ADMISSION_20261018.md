# P3G-ADM — offline deployment image parity and read-only admission boundary (18 October 2026)

**Decision: HELM TEMPLATE IMAGE PARITY PASS (conditional) / LIVE GKE READ-ONLY ADMISSION NOT EXECUTED / CANARY HOLD.**

## Exact candidate image and Drive receipt
- Source: `884f874c634a2e4a854a8f61b94354a06547c93e`.
- Registry: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`.
- Canonical Drive receipt: https://drive.google.com/drive/folders/1ooo2SVnCDwJgfsEjnL7hfg2y9qfv67EI
- Existing Drive receipt reports tag and immutable read-back to the same manifest digest; `imports.txt` PASS; `SHA256SUMS` exists. Full individual-file byte-level checksum recomputation has **not yet been completed**.

## Deployment template source audit
- `gke/helm/ahbn/templates/statefulset.yaml` peer image: `{{ .Values.image }}`.
- `gke/helm/ahbn/templates/job-controller.yaml` controller image: `{{ .Values.image }}`.
- `gke/helm/ahbn/values.yaml` `image: ""` by default; it **must** be supplied as the validated immutable digest.
- `gke/scripts/run_k7_experiment.sh` uses `helm install ... --set image="${IMAGE}"` and subsequently `helm upgrade --reuse-values --set controller.enabled=true`, so in the examined script both components inherit the same value **provided** `IMAGE` is the candidate digest.
- `gke/scripts/run_d7_smoke.sh` remains **historically pinned to sha256:8a47cedb...` and restricted to Gossip. It cannot be used unchanged for the new AHBN/Q-AHBN2 recovery canary. `d7_p3_verify.sh` is also historical and creates a pod, so it is NOT read-only.

## Critical feature-flag observation
Neither peer StatefulSet nor controller Job Helm template explicitly contains the `P3G_RECOVERY_ENABLED` environment variable. Container-level activation therefore **must be verified and added via a separately controlled, approved change before any recovery-enabled canary**. Do not infer that sharing an image digest activates recovery.

## GKE read-only admission pending
Existing `gke/scripts/d7_sm_canary_readonly_admission.sh` is a read-only inspector but is pinned to historical Gossip namespace/image. A new, strictly read-only P3G admission should check exact context, node architecture/readiness and 20-peer capacity, namespace nonexistence, quotas, permission checks, intended AHBN or Q-AHBN2 strategy, owner/cleanup contract, manifest render matching both containers and correct explicit recovery configuration; record UTC, git SHA and SHA256 evidence. This was **not executed**: GitHub/Drive connectors do not expose live kubectl GKE access.

**No GKE write; no canary; no formal run; D7-F/D8 HOLD; frozen algorithms unchanged.** Manuscript under review at Journal of Cloud Computing; no DOI.
