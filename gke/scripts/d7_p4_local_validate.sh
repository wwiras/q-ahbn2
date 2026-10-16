#!/usr/bin/env bash
# D7-P4 local-only verification; NO kubectl calls, Helm template ONLY.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
PYTHON="${PYTHON:-python3}"
OUT="${ROOT}/output/evidence/$(date -u +%Y%m%dT%H%M%SZ)-D7-P4-operations-local"
[ ! -e "${OUT}" ] || { echo "HOLD: evidence folder exists"; exit 1; }
mkdir -p "${OUT}"/{configs,topologies,rendered}
echo "$(git rev-parse HEAD)" > "${OUT}/git_commit.txt"
date -u +%FT%TZ > "${OUT}/started_utc.txt"
STATUS=HOLD
finalize() {
  local rc=$?
  trap - EXIT
  printf '%s\n' "${STATUS}" > "${OUT}/decision.txt"
  (cd "${OUT}" && find . -type f ! -name SHA256SUMS -print0 | xargs -0 shasum -a 256 > SHA256SUMS) || true
  echo "D7-P4 local evidence: ${OUT}"
  exit "${rc}"
}
trap finalize EXIT
for tool in bash helm "${PYTHON}" git shasum; do
  command -v "${tool}" >/dev/null || { echo "HOLD: missing tool ${tool}" >&2; exit 1; }
done
for f in gke/scripts/run_k7_experiment.sh gke/scripts/run_k5_q_formal.sh gke/scripts/run_d7_smoke.sh; do
  bash -n "${f}"
done
"${PYTHON}" -m py_compile gke/scripts/d7_p4_preflight.py gke/app/k7_exp11_tools.py
PYTHONPATH="${ROOT}" "${PYTHON}" gke/scripts/k5_q_prep_audit.py > "${OUT}/contract_audit.json"
METHODS=(gossip structured dcsoc ahbn qahbn2)
SEEDS=(42 43 44 45 46)
IMAGE="docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
for seed in "${SEEDS[@]}"; do
  paths=()
  for method in "${METHODS[@]}"; do
    cfg="${OUT}/configs/${method}_seed${seed}.yaml"
    topo="${OUT}/topologies/${method}_seed${seed}.json"
    PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py config \
      --base gke/experiments/k5_q_formal.yaml --out "${cfg}" \
      --algorithm "${method}" --seed "${seed}"
    PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_gen_topology.py --config "${cfg}" --out "${topo}"
    paths+=("${topo}")
  done
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py contract "${paths[@]}" \
    > "${OUT}/contract_seed${seed}.txt"
done
helm template qahbn2 gke/helm/ahbn --namespace qahbn2-d7-smoke-gossip \
  --set namespace=qahbn2-d7-smoke-gossip --set image="${IMAGE}" \
  --set numNodes=20 --set podManagementPolicy=Parallel \
  --set controller.enabled=true > "${OUT}/rendered/smoke_helm.yaml"
"${PYTHON}" - "${OUT}/rendered/smoke_helm.yaml" "${IMAGE}" <<'PY'
import sys, yaml
docs = [x for x in yaml.safe_load_all(open(sys.argv[1])) if x]
expected = sys.argv[2]
kinds = {d.get('kind') for d in docs}
assert 'StatefulSet' in kinds and 'Job' in kinds, f'missing Helm kinds: {kinds}'
state = next(d for d in docs if d.get('kind')=='StatefulSet')
job = next(d for d in docs if d.get('kind')=='Job')
assert state['spec']['replicas']==20
assert state['spec']['template']['spec']['containers'][0]['image']==expected
assert job['spec']['template']['spec']['containers'][0]['image']==expected
print('Helm chart rendered: 20-peer StatefulSet and controller Job, digest pinned')
PY
STATUS="STATIC AND HELM TEMPLATE PASS; D7-P4 LIVE OPERATIONS STILL HOLD"
echo "${STATUS}"
