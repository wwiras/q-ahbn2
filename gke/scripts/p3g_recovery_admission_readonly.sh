#!/usr/bin/env bash
# P3G recovery-specific READ-ONLY admission; cannot deploy or launch experiments.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
EXPECTED_CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"
IMAGE="docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f"
STRATEGY="${P3G_STRATEGY:-ahbn}"
[[ "$STRATEGY" == ahbn || "$STRATEGY" == qahbn2 ]] || { echo 'HOLD: only AHBN or Q-AHBN2'; exit 1; }
NS="qahbn2-d7-smoke-${STRATEGY}"
for cmd in kubectl helm git python3 shasum; do command -v "$cmd" >/dev/null || { echo "HOLD: missing $cmd"; exit 1; }; done
OUT="${P3G_ADMISSION_OUT:-$ROOT/output/evidence/$(date -u +%Y%m%dT%H%M%SZ)-P3G-${STRATEGY}-READONLY-ADMISSION}"
[[ ! -e "$OUT" ]] || { echo 'HOLD: evidence folder exists'; exit 1; }
mkdir -p "$OUT"
DECISION="HOLD: NOT ALL ADMISSION CONDITIONS MET"
finish() {
  code=$?
  trap - EXIT
  printf '%s\n' "$DECISION" > "$OUT/decision.txt"
  (cd "$OUT" && find . -maxdepth 1 -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 shasum -a 256 > SHA256SUMS) || true
  echo "Evidence: $OUT"
  exit "$code"
}
trap finish EXIT
git rev-parse HEAD > "$OUT/git_commit.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$OUT/inspection_utc.txt"
printf '%s\n' "$IMAGE" > "$OUT/image.txt"
printf '%s\n' "$STRATEGY" > "$OUT/strategy.txt"
git status --porcelain --untracked-files=no > "$OUT/git_status.txt"
[[ ! -s "$OUT/git_status.txt" ]] || { echo 'HOLD: modified tracked files'; exit 1; }
# Local Helm rendering never connects to GKE. Both components must use exactly the same digest.
helm template p3g-readonly gke/helm/ahbn --namespace "$NS" --set namespace="$NS" --set image="$IMAGE" --set controller.enabled=true --set numNodes=20 > "$OUT/rendered.yaml"
python3 - "$OUT/rendered.yaml" "$IMAGE" > "$OUT/manifest_check.txt" <<'PY'
import sys
try:
    import yaml
except ImportError:
    raise SystemExit('HOLD: PyYAML unavailable')
docs=[d for d in yaml.safe_load_all(open(sys.argv[1])) if isinstance(d,dict)]
peer=next((d for d in docs if d.get('kind')=='StatefulSet' and d.get('metadata',{}).get('name')=='peer'),None)
ctrl=next((d for d in docs if d.get('kind')=='Job' and d.get('metadata',{}).get('name')=='ahbn-controller'),None)
assert peer and ctrl, 'HOLD: peer/controller workloads absent'
assert peer['spec']['replicas']==20, 'HOLD: incorrect node count'
p=peer['spec']['template']['spec']['containers']
c=ctrl['spec']['template']['spec']['containers']
assert len(p)==len(c)==1, 'HOLD: unexpected workload containers'
assert p[0]['image']==c[0]['image']==sys.argv[2], 'HOLD: immutable peer/controller image mismatch'
print('PASS: intended peer and controller image digest matches')
env={x['name']:x.get('value') for x in p[0].get('env',[])}
assert env.get('P3G_RECOVERY_ENABLED')=='1', 'HOLD: peer recovery flag is not explicitly enabled'
print('PASS: peer recovery flag is explicitly enabled')
PY
# No cluster mutations below: only get, cluster-info, auth can-i.
context="$(kubectl config current-context)"
printf '%s\n' "$context" > "$OUT/kube_context.txt"
[[ "$context" == "$EXPECTED_CONTEXT" ]] || { echo 'HOLD: wrong cluster context'; exit 1; }
kubectl cluster-info > "$OUT/cluster_info.txt" 2>&1 || { echo 'HOLD: cluster unreachable'; exit 1; }
kubectl get nodes -o json > "$OUT/nodes.json"
kubectl get namespace "$NS" --ignore-not-found -o name > "$OUT/namespace.txt"
[[ ! -s "$OUT/namespace.txt" ]] || { echo 'HOLD: namespace already exists'; exit 1; }
kubectl get resourcequota --all-namespaces -o json > "$OUT/quotas.json"
kubectl get limitrange --all-namespaces -o json > "$OUT/limitranges.json"
for spec in 'create namespaces' 'get namespaces' 'delete namespaces' 'create statefulsets.apps' 'delete statefulsets.apps' 'create jobs.batch' 'delete jobs.batch' 'get pods' 'list pods' 'get pods/log'; do
  read -r verb resource <<< "$spec"
  if [[ "$resource" == namespaces ]]; then response="$(kubectl auth can-i "$verb" "$resource")"; else response="$(kubectl auth can-i "$verb" "$resource" -n "$NS")"; fi
  printf '%s: %s\n' "$spec" "$response" >> "$OUT/rbac.txt"
  [[ "$response" == yes ]] || { echo "HOLD: missing permission: $spec"; exit 1; }
done
python3 - "$OUT/nodes.json" > "$OUT/nodes_check.txt" <<'PY'
import json,sys
nodes=json.load(open(sys.argv[1]))['items']
ready=[n for n in nodes if any(c.get('type')=='Ready' and c.get('status')=='True' for c in n.get('status',{}).get('conditions',[]))]
amd=[n for n in ready if n.get('metadata',{}).get('labels',{}).get('kubernetes.io/arch')=='amd64']
print('ready=',len(ready),'ready_amd64=',len(amd))
assert amd,'HOLD: no ready amd64 node'
print('Capacity for N=20, cleanup provenance, and runtime pod imageID still require independent verification.')
PY
DECISION='READ-ONLY PRELIMINARY CHECKS PASS; SEPARATE CANARY APPROVAL STILL REQUIRED'
echo "$DECISION"
