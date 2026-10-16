#!/usr/bin/env bash
# D7-SM controlled smoke launcher. NEVER executed by D7-P4 validation.
# One seed-42 run for each of five frozen algorithms; full 240-message workload
# so the frozen churn/timing/metric validators remain meaningful.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
[ "${SMOKE_AUTHORIZED:-}" = "YES" ] || {
  echo "HOLD: researcher must separately authorize smoke runs (SMOKE_AUTHORIZED=YES)" >&2; exit 1;
}
PYTHON="${PYTHON:-python3}"
IMAGE="${IMAGE:-docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466}"
EXPECTED_IMAGE_DIGEST="sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
EXPECTED_CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"
METHODS=(gossip structured dcsoc ahbn qahbn2)
SEED=42
[ "${IMAGE}" = "docker.io/wwiras/q-ahbn2@${EXPECTED_IMAGE_DIGEST}" ] || {
  echo "HOLD: wrong image" >&2; exit 1;
}
for tool in kubectl helm git "${PYTHON}"; do
  command -v "${tool}" >/dev/null || { echo "missing ${tool}" >&2; exit 1; }
done
[ "$(kubectl config current-context)" = "${EXPECTED_CONTEXT}" ] || {
  echo "HOLD: wrong cluster context" >&2; exit 1;
}
[ -z "$(git status --porcelain)" ] || {
  echo "HOLD: git worktree must be clean" >&2; exit 1;
}
ROOT_OUT="${RESULT_ROOT:-${ROOT}/output/evidence/$(date -u +%Y%m%dT%H%M%SZ)-D7-SM-five-method}"
[ ! -e "${ROOT_OUT}" ] || { echo "HOLD: evidence directory exists" >&2; exit 1; }
mkdir -p "${ROOT_OUT}"/{configs,generated,runs,raw}
cp gke/helm/ahbn/topology.json "${ROOT_OUT}/raw/topology_before.json"
restore() { cp "${ROOT_OUT}/raw/topology_before.json" gke/helm/ahbn/topology.json; }
trap restore EXIT
printf '%s\n' "$(git rev-parse HEAD)" > "${ROOT_OUT}/git_commit.txt"
printf '%s\n' "${IMAGE}" > "${ROOT_OUT}/image.txt"
printf '%s\n' "D7-SM NONFORMAL; SEED=42; FULL WORKLOAD 240x0.4s" > "${ROOT_OUT}/evidence_class.txt"
PYTHONPATH="${ROOT}" "${PYTHON}" gke/scripts/k5_q_prep_audit.py > "${ROOT_OUT}/prep_audit.json"
for method in "${METHODS[@]}"; do
  cfg="${ROOT_OUT}/configs/${method}_seed42.yaml"
  topo="${ROOT_OUT}/generated/${method}_seed42.json"
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py config \
    --base gke/experiments/k5_q_formal.yaml --out "${cfg}" \
    --algorithm "${method}" --seed "${SEED}"
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_gen_topology.py \
    --config "${cfg}" --out "${topo}"
done
topos=()
for method in "${METHODS[@]}"; do
  topos+=("${ROOT_OUT}/generated/${method}_seed42.json")
done
PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py contract "${topos[@]}" > "${ROOT_OUT}/topology_contract.txt"
# Each method uses an independently created and deleted namespace.
for method in "${METHODS[@]}"; do
  run="${ROOT_OUT}/runs/${method}"
  mkdir -p "${run}"
  cfg="${ROOT_OUT}/configs/${method}_seed42.yaml"
  rel="${cfg#${ROOT}/}"
  ns="qahbn2-d7-smoke-${method}"
  printf '%s\n' "D7-SM seed=42 method=${method} NONFORMAL" > "${run}/classification.txt"
  OUTDIR="${run}" NAMESPACE="${ns}" RELEASE=qahbn2 \
    IMAGE="${IMAGE}" EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST}" \
    EXPECTED_CONTEXT="${EXPECTED_CONTEXT}" PYTHON="${PYTHON}" \
    bash gke/scripts/run_k7_experiment.sh "${rel}"
  cp "${ROOT_OUT}/generated/${method}_seed42.json" "${run}/topology_role_mapping.json"
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py run --run-dir "${run}" \
    > "${run}/validation.txt"
  echo "D7-SM validation PASS: ${method}"
done
printf '%s\n' "FIVE NONFORMAL SMOKE RUNS COMPLETED; awaiting independent evidence review" > "${ROOT_OUT}/status.txt"
echo "D7-SM results: ${ROOT_OUT}"
