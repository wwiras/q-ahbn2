#!/usr/bin/env bash
set -Eeuo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"; cd "${ROOT_DIR}"
PYTHON="${PYTHON:-python3}"
IMAGE="${IMAGE:-}"
EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST:-}"
EXPECTED_CONTEXT="${EXPECTED_CONTEXT:-gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster}"
NAMESPACE="${NAMESPACE:-qahbn2-s17-remediation}"
RELEASE="${RELEASE:-qahbn2}"
STAMP="$(date +%d%m%Y%H%M%S)"
RESULT_ROOT="${RESULT_ROOT:-${ROOT_DIR}/output/evidence/q-ahbn-gke-${STAMP}-s17-qahbn2-remediation}"
fail(){ echo "ERROR: $*" >&2; exit 1; }

METHOD="qahbn2"
SEEDS=(42 43 44 45 46)

[ -n "${IMAGE}" ] || fail "IMAGE is required"
[[ "${EXPECTED_IMAGE_DIGEST}" =~ ^sha256:[[:xdigit:]]{64}$ ]] || fail "EXPECTED_IMAGE_DIGEST must be an exact sha256 digest"
for x in kubectl helm shasum; do command -v "${x}" >/dev/null || fail "missing command: ${x}"; done
[ "$(kubectl config current-context)" = "${EXPECTED_CONTEXT}" ] || fail "unexpected kubectl context"
[ ! -e "${RESULT_ROOT}" ] || fail "new remediation output directory required: ${RESULT_ROOT}"

PRE_STATUS="$(git status --porcelain)"
[ -z "${PRE_STATUS}" ] || { printf '%s\n' "${PRE_STATUS}" >&2; fail "working tree must be clean before remediation evidence creation"; }
FORMAL_GIT_SHA="$(git rev-parse HEAD)"
PYTHONPATH="${ROOT_DIR}" "${PYTHON}" gke/scripts/s17_5_prep_audit.py >/dev/null
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
  cfg="${RESULT_ROOT}/configs/qahbn2_seed${seed}.yaml"
  topo="${RESULT_ROOT}/generated/qahbn2_seed${seed}.json"
  PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_exp11_tools.py config --base gke/experiments/k5_q_formal.yaml --out "${cfg}" --algorithm qahbn2 --seed "${seed}"
  PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_gen_topology.py --config "${cfg}" --out "${topo}"
done

PYTHONPATH="${ROOT_DIR}" "${PYTHON}" - "${RESULT_ROOT}" <<'PY'
import json,sys,yaml
from pathlib import Path
from gke.app.k5_q_formal_contract import SEEDS,NUM_NODES,BA_M,MESSAGE_COUNT,MESSAGE_INTERVAL_S,CHURN_OFFSETS_S
root=Path(sys.argv[1]); rows=[]
for seed in SEEDS:
    cfg=root/"configs"/f"qahbn2_seed{seed}.yaml"
    topo=root/"generated"/f"qahbn2_seed{seed}.json"
    c=yaml.safe_load(cfg.read_text())
    assert c["k7_exp11"]["algorithm"]=="qahbn2"
    assert int(c["k7_exp11"]["seed"])==seed
    assert int(c["numNodes"])==NUM_NODES
    assert int(c["topology"]["baM"])==BA_M
    assert int(c["workload"]["messageCount"])==MESSAGE_COUNT
    assert float(c["workload"]["messageInterval"])==MESSAGE_INTERVAL_S
    assert tuple(float(x) for x in c["k7_exp11"]["plannedLeaveOffsetsSec"])==CHURN_OFFSETS_S
    rows.append({"seed":seed,"method":"qahbn2","config":str(cfg.relative_to(root)),"topology":str(topo.relative_to(root))})
(root/"s17_protocol_manifest.json").write_text(json.dumps({"status":"FROZEN","coordinates":rows},indent=2)+"\n")
PY

TOPOLOGY_BACKUP="${RESULT_ROOT}/raw/helm_topology_before.json"
cp gke/helm/ahbn/topology.json "${TOPOLOGY_BACKUP}"
restore(){ cp "${TOPOLOGY_BACKUP}" gke/helm/ahbn/topology.json; }
trap restore EXIT

for seed in "${SEEDS[@]}"; do
  run="${RESULT_ROOT}/runs/seed${seed}/qahbn2"
  cfg="${RESULT_ROOT}/configs/qahbn2_seed${seed}.yaml"
  rel="${cfg#${ROOT_DIR}/}"
  echo "S17 FORMAL REMEDIATION RUN seed=${seed} method=qahbn2"
  OUTDIR="${run}" NAMESPACE="${NAMESPACE}" RELEASE="${RELEASE}" IMAGE="${IMAGE}" EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST}" PYTHON="${PYTHON}" bash gke/scripts/run_k7_experiment.sh "${rel}"
  cp "${RESULT_ROOT}/generated/qahbn2_seed${seed}.json" "${run}/topology_role_mapping.json"
  PYTHONPATH="gke/app" "${PYTHON}" gke/app/k7_exp11_tools.py run --run-dir "${run}"
done

PYTHONPATH="${ROOT_DIR}" "${PYTHON}" - "${RESULT_ROOT}" "${IMAGE}" "${EXPECTED_IMAGE_DIGEST}" <<'PY'
import json,sys
from pathlib import Path
from gke.app.k5_q_formal_contract import SEEDS
root=Path(sys.argv[1]); image=sys.argv[2]; digest=sys.argv[3]
git_sha=(root/"git_commit.txt").read_text().strip(); runs=[]
for seed in SEEDS:
    d=root/"runs"/f"seed{seed}"/"qahbn2"
    metrics=json.loads((d/"metrics.json").read_text())
    manifest=json.loads((d/"run_manifest.json").read_text())
    assert metrics["F_success"] <= metrics["F_attempt"]
    runs.append({"seed":seed,"method":"qahbn2","git_sha":git_sha,"image":image,"image_digest":digest,"status":"VALIDATED","metrics":metrics,"metrics_file":str((d/"metrics.json").relative_to(root)),"run_manifest":manifest})
(root/"remediation_manifest.json").write_text(json.dumps({"status":"COMPLETE","runs":runs},indent=2)+"\n")
PY

date -u +%FT%TZ >"${RESULT_ROOT}/completed_utc.txt"
kubectl delete namespace "${NAMESPACE}" --wait=true >/dev/null 2>&1 || true
trap - EXIT; restore
echo "S17 Q-AHBN2 FORMAL REMEDIATION 5/5 PASS"
echo "Evidence: ${RESULT_ROOT}"
