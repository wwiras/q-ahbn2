#!/usr/bin/env bash
# Four-method D7-SM continuation: NONFORMAL only. No cloud action without explicit authorization.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
[[ "${SMOKE_REMAINING_AUTHORIZED:-}" == YES ]] || { echo "HOLD: four-method authorization missing" >&2; exit 1; }
[[ "${SMOKE_AUTHORIZED:-}" != YES ]] || { echo "HOLD: legacy canary authorization is not used here" >&2; exit 1; }
PYTHON="${PYTHON:-python3}"
EXPECTED_CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"
EXPECTED_IMAGE="docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE#*@}"
[[ "${IMAGE:-$EXPECTED_IMAGE}" == "${EXPECTED_IMAGE}" ]] || { echo "HOLD: image changed" >&2; exit 1; }
for tool in kubectl helm git "${PYTHON}"; do command -v "${tool}" >/dev/null || { echo "HOLD: missing ${tool}" >&2; exit 1; }; done
[[ "$(kubectl config current-context)" == "${EXPECTED_CONTEXT}" ]] || { echo "HOLD: unexpected GKE context" >&2; exit 1; }
[[ -z "$(git status --porcelain)" ]] || { echo "HOLD: dirty Git checkout" >&2; exit 1; }
HEAD="$(git rev-parse HEAD)"
REMOTE="$(git ls-remote origin refs/heads/main | awk '{print $1}')"
[[ -n "${REMOTE}" && "${HEAD}" == "${REMOTE}" ]] || { echo "HOLD: local HEAD is not remote main" >&2; exit 1; }
METHODS=(structured dcsoc ahbn qahbn2)
for method in "${METHODS[@]}"; do
  ns="qahbn2-d7-smoke-${method}"
  [[ -z "$(kubectl get namespace "${ns}" --ignore-not-found -o name)" ]] || { echo "HOLD: namespace exists: ${ns}" >&2; exit 1; }
done
OUT="${RESULT_ROOT:-${ROOT}/output/evidence/$(date -u +%Y%m%dT%H%M%SZ)-D7-SM-remaining}"
[[ "${OUT}" == "${ROOT}/output/evidence/"* ]] || { echo "HOLD: RESULT_ROOT outside repository output/evidence" >&2; exit 1; }
case "${OUT#${ROOT}/output/evidence/}" in
  ""|/*|../*|*/../*|*/..|./*|*/./*|*/.|*//*)
    echo "HOLD: unsafe evidence path" >&2; exit 1;;
esac
probe="${ROOT}/output"
while [[ "${probe}" != "${OUT}" ]]; do
  [[ ! -L "${probe}" ]] || { echo "HOLD: symlink in evidence path" >&2; exit 1; }
  remaining="${OUT#${probe}/}"
  [[ "${remaining}" != "${OUT}" ]] || { echo "HOLD: invalid evidence path" >&2; exit 1; }
  probe="${probe}/${remaining%%/*}"
done
[[ ! -L "${OUT}" ]] || { echo "HOLD: symlink evidence path" >&2; exit 1; }
[[ ! -e "${OUT}" ]] || { echo "HOLD: evidence path exists" >&2; exit 1; }
mkdir -p "${OUT}"/{configs,generated,runs,raw}
cp gke/helm/ahbn/topology.json "${OUT}/raw/topology_before.json"
CURRENT_METHOD=""
cleanup_outer() {
  local rc=$?
  trap - EXIT INT TERM
  cp "${OUT}/raw/topology_before.json" gke/helm/ahbn/topology.json || rc=1
  printf '%s\n' "${rc}" > "${OUT}/smoke_exit_status.txt"
  (cd "${OUT}" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 shasum -a 256 > SHA256SUMS) || rc=1
  exit "${rc}"
}
trap cleanup_outer EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
printf '%s\n' "${HEAD}" > "${OUT}/git_commit.txt"
printf '%s\n' "${EXPECTED_IMAGE}" > "${OUT}/image.txt"
printf '%s\n' "NONFORMAL D7-SM remaining four methods; seed 42; 240 messages x 0.4 seconds" > "${OUT}/evidence_class.txt"
PYTHONPATH="${ROOT}" "${PYTHON}" gke/scripts/k5_q_prep_audit.py > "${OUT}/prep_audit.json"
for method in "${METHODS[@]}"; do
  cfg="${OUT}/configs/${method}_seed42.yaml"
  topo="${OUT}/generated/${method}_seed42.json"
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py config --base gke/experiments/k5_q_formal.yaml --out "${cfg}" --algorithm "${method}" --seed 42
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_gen_topology.py --config "${cfg}" --out "${topo}"
done
PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py contract --remaining-four-seed42 "${OUT}"/generated/{structured,dcsoc,ahbn,qahbn2}_seed42.json > "${OUT}/topology_contract.txt"
for method in "${METHODS[@]}"; do
  CURRENT_METHOD="${method}"
  run="${OUT}/runs/${method}"
  mkdir -p "${run}"
  cfg="${OUT}/configs/${method}_seed42.yaml"
  rel="${cfg#${ROOT}/}"
  ns="qahbn2-d7-smoke-${method}"
  printf '%s\n' "D7-SM NONFORMAL seed=42 method=${method}" > "${run}/classification.txt"
  OUTDIR="${run}" NAMESPACE="${ns}" RELEASE=qahbn2 IMAGE="${EXPECTED_IMAGE}" EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST}" EXPECTED_CONTEXT="${EXPECTED_CONTEXT}" PYTHON="${PYTHON}" bash gke/scripts/run_k7_experiment.sh "${rel}"
  [[ -z "$(kubectl get namespace "${ns}" --ignore-not-found -o name)" ]] || { echo "HOLD: namespace remains: ${ns}" >&2; exit 1; }
  [[ "$(cat "${run}/cleanup_status.txt")" == PASS ]] || { echo "HOLD: cleanup not PASS for ${method}" >&2; exit 1; }
  cp "${OUT}/generated/${method}_seed42.json" "${run}/topology_role_mapping.json"
  PYTHONPATH=gke/app "${PYTHON}" gke/app/k7_exp11_tools.py run --run-dir "${run}" > "${run}/validation.txt"
  (cd "${run}" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 shasum -a 256 > SHA256SUMS)
  printf '%s\n' "NONFORMAL ${method} validation PASS"
done
printf '%s\n' "FOUR NONFORMAL METHODS COMPLETED; independent post-run audit required" > "${OUT}/status.txt"
echo "D7-SM remaining evidence: ${OUT}"
