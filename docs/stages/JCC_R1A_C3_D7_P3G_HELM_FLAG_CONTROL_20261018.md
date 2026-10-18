# P3G-ADM — Recovery feature-flag control and admission readiness (18 October 2026)

**Decision: HELM RECOVERY CONTROL IMPLEMENTED AND SOURCE-STATIC CHECKS PASS; RENDERED HELM/GKE READ-ONLY ADMISSION NOT YET EXECUTED; D7-F AND D8 HOLD.**

## Change scope

- `gke/helm/ahbn/values.yaml`: new `recovery.enabled: "0"` default; original configurations remain recovery-disabled.
- `gke/helm/ahbn/templates/statefulset.yaml`: peer container receives `P3G_RECOVERY_ENABLED` from `{{ .Values.recovery.enabled | quote }}`. No change to AHBN/Q-AHBN2 algorithm or controller template.
- `gke/scripts/p3g_recovery_admission_readonly.sh`: invokes Helm with `--set-string recovery.enabled=1` **for local rendering only**. Script checks identical immutable peer/controller digest, N=20, explicit peer recovery flag before attempting read-only kubectl queries. No Kubernetes create/apply/install/upgrade/delete operations are present in the admission script.
- Historical Gossip-only launcher remains unchanged and must not be used to authorize a P3G recovery run.

## Verified

Source-static assertions (5 checks plus peer runtime baseline): default zero, correct env injection, shared peer/controller `.Values.image`, explicit read-only rendering flag, and peer runtime `os.environ.get("P3G_RECOVERY_ENABLED","0") == "1"`. **PASS**.

Candidate registry image remains `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f` with Google Drive evidence https://drive.google.com/drive/folders/1ooo2SVnCDwJgfsEjnL7hfg2y9qfv67EI. Image contents not changed by these Helm source changes; do not republish image merely for external Helm configuration.

## Incomplete conditions

Real `helm template` rendering was **not executed** in this tool runtime (Helm executable unavailable); no live GKE `kubectl` read-only admission executed here (GKE credentials not accessible). Mark both **NOT RUN / HOLD**, not PASS. Real cluster admission must review quota/capacity for 20 peers, RBAC, empty dedicated namespace, and reconcile cleanup ownership before any canary. New read-only script reports only preliminary readiness; runtime pod `imageID` remains unverified.

## Researcher local commands (no cluster write)

```bash
git switch main
git pull --ff-only origin main
helm lint gke/helm/ahbn
P3G_STRATEGY=ahbn bash gke/scripts/p3g_recovery_admission_readonly.sh
```

The researcher must review output under `output/evidence/*-P3G-ahbn-READONLY-ADMISSION`. A PASS does **not** authorize an experiment, deployment or canary.

D7-F/D8 remain HOLD. Manuscript under peer review at Journal of Cloud Computing, no DOI, not published. No Drive writes performed at this gate.
