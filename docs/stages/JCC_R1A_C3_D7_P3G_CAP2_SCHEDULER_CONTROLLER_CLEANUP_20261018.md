# P3G-CAP2 — Scheduler, controller, cleanup verification (2026-10-18)

## Decision
**PARTIAL PASS / HOLD FOR CANARY.** Read-only evidence supports node request and pod-slot feasibility for 20 peers. Controller resource contract and recovery-specific launcher remain unresolved; no deployment is authorized.

## Evidence
- Existing read-only admission: https://drive.google.com/drive/folders/185Tj0oDRhSSBk2qULPOV1jMtKhVnXG9M
- New capacity evidence synced to Drive: https://drive.google.com/drive/folders/1abVQ3ic8Sqyx73t2iVZyMrVEX61tlY06
- New pod snapshot: `pods.json` (65 nonterminal pods, all scheduled), and `node_allocations.txt` from `kubectl describe nodes`.
- GitHub sources: `gke/helm/ahbn/values.yaml`, `templates/statefulset.yaml`, `templates/job-controller.yaml`, `gke/scripts/run_k7_experiment.sh`.

### CAP2-A — Pod slots PASS (snapshot)
Seven ready AMD64 nodes, each allocatable 110 pods. Current active pod counts per node by hostname suffix:
`81k9=8; 86qh=16; 9v34=9; j01j=9; npsk=8; t4bk=8; zb0n=7`.
Total = 65 existing, zero unscheduled. At least 94 slots remain on every node before additional workload. 20 peers plus one controller pod can fit the total pod-slot bound. This is request-side feasibility only, not a live scheduler/admission guarantee.

### CAP2-B — CPU and memory peer feasibility PASS (snapshot)
Each node allocatable CPU = 940m; peer requests 50m CPU and 64Mi memory. Existing CPU requests by node from recorded description, in order: 316m, 585m, 426m, 360m, 316m, 316m, 301m. Sum reserved CPU = 2620m; total allocatable 6580m; free request capacity = 3960m; 20 peers need 1000m. Most-loaded CPU node still has 355m free. Memory requests are also below allocatable and aggregate free exceeds peer needs. These numbers do not guarantee runtime performance, and limits exceed requests substantially.

### CAP2-C — Controller HOLD
`gke/helm/ahbn/templates/job-controller.yaml` defines one controller Job pod, same image as peers, but **no `resources.requests` or `resources.limits`**. Its CPU/memory scheduling allowance is therefore not explicitly bounded by the Helm chart. Controller has `serviceAccountName: ahbn-controller`, config-map topology mount and namespace field-reference. No `nodeSelector`, affinity, or tolerations in the controller template. Require explicit reviewed resource contract and fresh rendered-manifest verification before release.

### CAP2-D — Namespace ownership/cleanup STATIC PASS / runtime HOLD
`run_k7_experiment.sh` limits namespace naming; rejects existing namespace; checks pinned image and GKE context; creates namespace then stores UID and owner label; verifies owner label; prior to cleanup checks both UID and label, refuses removal on mismatch; captures logs, Helm and namespace cleanup exit statuses. **No cleanup action was executed for CAP2**, hence runtime cleanup is not verified.

**Important blocker:** generic `run_k7_experiment.sh` Helm install does not set `recovery.enabled=1`; default is `0`. Reusing generic launch without controlled correction would silently test with recovery disabled. Historical Gossip-only launcher also is not a recovery canary launcher. Do not execute either unchanged for recovery verification.

### Release conditions and provenance
1. Add/review explicit controller requests and limits, consistent with evidenced capacity, without changing AHBN/Q-AHBN2 algorithms.
2. Implement and verify an explicitly recovery-enabled canary launcher with digest pin, workload imageID parity, strict ownership and cleanup, and separately authorized execution.
3. Record local render and offline failure-injection tests, preserve logs/SHA256, refresh read-only capacity check.
4. User must separately authorize any live canary, even after these gates.

D7-F and D8 HOLD. Journal of Cloud Computing manuscript remains under peer review, not published and no DOI.
