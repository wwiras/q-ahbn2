#!/usr/bin/env bash
# D7-SM read-only GKE admission. No cluster mutation; does NOT authorize canary.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
EXPECTED_CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"
NS="qahbn2-d7-smoke-gossip"
IMAGE="docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
OUT="$ROOT/output/evidence/$(date -u +%Y%m%dT%H%M%SZ)-D7-SM-canary-readonly-admission"
[ ! -e "$OUT" ] || { echo "HOLD: evidence directory already exists" >&2; exit 1; }
mkdir -p "$OUT"
STATUS="HOLD: READ-ONLY ADMISSION INCOMPLETE"
finish() {
  local rc=$?
  trap - EXIT
  printf '%s\n' "$STATUS" > "$OUT/decision.txt"
  (cd "$OUT" && find . -type f ! -name SHA256SUMS -print0 | xargs -0 shasum -a 256 > SHA256SUMS) || true
  echo "Evidence: $OUT"
  exit "$rc"
}
trap finish EXIT
for cmd in kubectl helm git shasum; do
  command -v "$cmd" >/dev/null || { echo "HOLD: missing $cmd" >&2; exit 1; }
done
printf '%s\n' "$(git rev-parse HEAD)" > "$OUT/git_commit.txt"
date -u +%FT%TZ > "$OUT/time_utc.txt"
printf '%s\n' "$IMAGE" > "$OUT/image.txt"
printf '%s\n' "Gossip; seed=42; NONFORMAL; one canary; NO MUTATION" > "$OUT/scope.txt"
git status --porcelain > "$OUT/git_status.txt"
[ ! -s "$OUT/git_status.txt" ] || { echo "HOLD: git worktree not clean" >&2; exit 1; }
context="$(kubectl config current-context)"
printf '%s\n' "$context" > "$OUT/context.txt"
[ "$context" = "$EXPECTED_CONTEXT" ] || { echo "HOLD: wrong GKE context" >&2; exit 1; }
kubectl cluster-info > "$OUT/cluster_info.txt" 2>&1 || { echo "HOLD: cluster inaccessible" >&2; exit 1; }
kubectl get nodes -o json > "$OUT/nodes.json" || { echo "HOLD: cannot inspect nodes" >&2; exit 1; }
python3 - "$OUT/nodes.json" > "$OUT/nodes_check.txt" <<'PY'
import json,sys
nodes=json.load(open(sys.argv[1])).get('items',[])
ready=[n for n in nodes if any(c.get('type')=='Ready' and c.get('status')=='True' for c in n.get('status',{}).get('conditions',[]))]
print(f'nodes={len(nodes)} ready={len(ready)}')
assert len(ready)>=1, 'no ready node'
PY
kubectl get namespace "$NS" --ignore-not-found -o name > "$OUT/namespace_check.txt" || { echo "HOLD: namespace check failed" >&2; exit 1; }
[ ! -s "$OUT/namespace_check.txt" ] || { echo "HOLD: canary namespace exists" >&2; exit 1; }
# RBAC checks are read-only SubjectAccessReview queries, not resource creation.
for entry in "create namespaces" "get namespaces" "patch namespaces" "delete namespaces" "create statefulsets.apps" "create jobs.batch" "get pods" "list pods" "get pods/log" "delete statefulsets.apps" "delete jobs.batch"; do
  set -- $entry
  resource="$2"
  verb="$1"
  if [ "$resource" = namespaces ]; then
    answer="$(kubectl auth can-i "$verb" "$resource")" || { echo "HOLD: RBAC query failed: $verb $resource" >&2; exit 1; }
  else
    answer="$(kubectl auth can-i "$verb" "$resource" -n "$NS")" || { echo "HOLD: RBAC query failed: $verb $resource" >&2; exit 1; }
  fi
  printf '%s %s: %s\n' "$verb" "$resource" "$answer" >> "$OUT/rbac.txt"
  [ "$answer" = yes ] || { echo "HOLD: missing permission $verb $resource" >&2; exit 1; }
done
kubectl get resourcequota --all-namespaces -o wide > "$OUT/resourcequotas.txt" || { echo "HOLD: quota visibility unavailable" >&2; exit 1; }
helm version --short > "$OUT/helm_version.txt"
printf '%s\n' "READ-ONLY CHECKS PASS; CANARY EXECUTION REQUIRES SEPARATE APPROVAL" > "$OUT/decision.txt"
STATUS="READ-ONLY CHECKS PASS; CANARY EXECUTION REQUIRES SEPARATE APPROVAL"
echo "$STATUS"
