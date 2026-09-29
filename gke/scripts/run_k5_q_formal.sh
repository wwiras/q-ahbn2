#!/usr/bin/env bash
set -Eeuo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"; cd "${ROOT_DIR}"
PYTHON="${PYTHON:-python3}"
IMAGE="${IMAGE:-}"
EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST:-}"
EXPECTED_CONTEXT="${EXPECTED_CONTEXT:-gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster}"
NAMESPACE="${NAMESPACE:-qahbn2-k5-formal}"
RELEASE="${RELEASE:-qahbn2}"
STAMP="$(date +%d%m%Y%H%M%S)"
RESULT_ROOT="${RESULT_ROOT:-${ROOT_DIR}/output/evidence/q-ahbn-gke-${STAMP}-k5q-formal}"
METHODS=(gossip structured dcsoc ahbn qahbn2)
SEEDS=(42 43 44 45 46)
fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required"
[[ "${EXPECTED_IMAGE_DIGEST}" =~ ^sha256:[[:xdigit:]]{64}$ ]] || fail "EXPECTED_IMAGE_DIGEST must be an exact sha256 digest"
for x in kubectl helm shasum; do command -v "${x}" >/dev/null || fail "missing command: ${x}"; done
[ "$(kubectl config current-context)" = "${EXPECTED_CONTEXT}" ] || fail "unexpected kubectl context"
[ ! -e "${RESULT_ROOT}" ] || fail "new output directory required: ${RESULT_ROOT}"
PRE_STATUS="$(git status --porcelain)"
[ -z "${PRE_STATUS}" ] || { printf '%s\n' "${PRE_STATUS}" >&2; fail "working tree must be clean before formal evidence creation"; }
FORMAL_GIT_SHA="$(git rev-parse HEAD)"
PYTHONPATH="${ROOT_DIR}" "${PYTHON}" gke/scripts/k5_q_prep_audit.py >/dev/null
IMAGE="${IMAGE}" EXPECTED_PLATFORM=linux/amd64 bash gke/scripts/verify_k3_q_image.sh >/dev/null

mkdir -p "${RESULT_ROOT}"/{configs,generated,runs,target-selection,raw}
exec > >(tee -a "${RESULT_ROOT}/terminal.log") 2>&1
printf '%s\n' "${FORMAL_GIT_SHA}" >"${RESULT_ROOT}/git_commit.txt"
printf '%s\n' "${PRE_STATUS}" >"${RESULT_ROOT}/git_status.txt"
printf '%s\n' "${IMAGE}" >"${RESULT_ROOT}/image.txt"
printf '%s\n' "${EXPECTED_IMAGE_DIGEST}" >"${RESULT_ROOT}/expected_image_digest.txt"
date -u +%FT%TZ >"${RESULT_ROOT}/started_utc.txt"
cp docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md "${RESULT_ROOT}/K4_Q_K8S_VALIDATION_FREEZE.md"
cp gke/app/k5_q_formal_contract.py "${RESULT_ROOT}/k5_q_formal_contract.py"

for seed in "${SEEDS[@]}"; do
  artifact="${RESULT_ROOT}/target-selection/seed${seed}.json"
  PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_exp11_tools.py target-selection --base gke/experiments/k5_q_formal.yaml --out "${artifact}" --seed "${seed}" >/dev/null
  generated=()
  for method in "${METHODS[@]}"; do
    cfg="${RESULT_ROOT}/configs/${method}_seed${seed}.yaml"
    topo="${RESULT_ROOT}/generated/${method}_seed${seed}.json"
    PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_exp11_tools.py config --base gke/experiments/k5_q_formal.yaml --out "${cfg}" --algorithm "${method}" --seed "${seed}"
    PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_gen_topology.py --config "${cfg}" --out "${topo}"
    generated+=("${topo}")
  done
  PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_exp11_tools.py contract "${generated[@]}"
done

TOPOLOGY_BACKUP="${RESULT_ROOT}/raw/helm_topology_before.json"
cp gke/helm/ahbn/topology.json "${TOPOLOGY_BACKUP}"
restore(){ cp "${TOPOLOGY_BACKUP}" gke/helm/ahbn/topology.json; }
trap restore EXIT

for seed in "${SEEDS[@]}"; do
  for method in "${METHODS[@]}"; do
    run="${RESULT_ROOT}/runs/seed${seed}/${method}"
    cfg="${RESULT_ROOT}/configs/${method}_seed${seed}.yaml"
    rel="${cfg#${ROOT_DIR}/}"
    echo "K5-Q FORMAL RUN seed=${seed} method=${method}"
    OUTDIR="${run}" NAMESPACE="${NAMESPACE}" RELEASE="${RELEASE}" IMAGE="${IMAGE}" EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST}" PYTHON="${PYTHON}" bash gke/scripts/run_k7_experiment.sh "${rel}"
    cp "${RESULT_ROOT}/generated/${method}_seed${seed}.json" "${run}/topology_role_mapping.json"
    PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_exp11_tools.py run --run-dir "${run}"
  done
done

PYTHONPATH="${ROOT_DIR}" "${PYTHON}" - "${RESULT_ROOT}" "${IMAGE}" "${EXPECTED_IMAGE_DIGEST}" <<'PY'
import json,sys
from pathlib import Path
from gke.app.k5_q_formal_contract import METHODS,SEEDS
root=Path(sys.argv[1]); image=sys.argv[2]; digest=sys.argv[3]
git_sha=(root/"git_commit.txt").read_text().strip()
runs=[]
for seed in SEEDS:
    for method in METHODS:
        d=root/"runs"/f"seed{seed}"/method
        metrics=json.loads((d/"metrics.json").read_text())
        manifest=json.loads((d/"run_manifest.json").read_text())
        topo=d/"topology.json"
        runs.append({"seed":seed,"method":method,"git_sha":git_sha,"image":image,
                     "image_digest":digest,"topology":str(topo.relative_to(root)),
                     "status":"VALIDATED","metrics_file":str((d/"metrics.json").relative_to(root)),
                     "run_manifest":manifest,"metrics":metrics})
(root/"matrix_manifest.json").write_text(json.dumps({"status":"COMPLETE","runs":runs},indent=2)+"\n")
PY

PYTHONPATH="${ROOT_DIR}" "${PYTHON}" gke/scripts/validate_k5_q_artifacts.py "${RESULT_ROOT}"
date -u +%FT%TZ >"${RESULT_ROOT}/completed_utc.txt"
kubectl delete namespace "${NAMESPACE}" --wait=true >/dev/null 2>&1 || true
trap - EXIT; restore
echo "K5-Q FORMAL 25/25 PASS"
echo "Evidence: ${RESULT_ROOT}"
