#!/usr/bin/env bash
set -Eeuo pipefail
CONFIG="$1"; ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"; OUTDIR="${OUTDIR:?}"; NAMESPACE="${NAMESPACE:?}"; RELEASE="${RELEASE:-ahbn}"; IMAGE="${IMAGE:?}"; EXPECTED_IMAGE_DIGEST="${EXPECTED_IMAGE_DIGEST:?}"; PYTHON="${PYTHON:?}"
mkdir -p "${OUTDIR}"; LOG_FOLLOW_PID=""; OWN_NAMESPACE=0; NS_UID=""; CREATE_ATTEMPTED=0
RUN_OWNER="${RUN_OWNER:-d7-smoke-${NAMESPACE}}"
P3G_RECOVERY_ENABLED="${P3G_RECOVERY_ENABLED:-0}"
[[ "${P3G_RECOVERY_ENABLED}" == "0" || "${P3G_RECOVERY_ENABLED}" == "1" ]] || { echo "HOLD: recovery flag must be 0 or 1" >&2; exit 1; }
if [ "${P3G_RECOVERY_ENABLED}" = "1" ]; then
  [[ "${NAMESPACE}" =~ ^qahbn2-d7-smoke-p3g-[a-z0-9-]+$ ]] || { echo "HOLD: recovery requires a P3G-specific namespace" >&2; exit 1; }
fi
[[ "${RUN_OWNER}" =~ ^[a-z0-9-]+$ ]] || { echo "HOLD: invalid owner" >&2; exit 1; }
# Only an absent, dedicated namespace is allowed; never uninstall unrelated workloads.
[[ "${NAMESPACE}" =~ ^qahbn2-(k5-formal|d7-smoke-[a-z0-9-]+)$ ]] || {
  echo "HOLD: unsafe namespace ${NAMESPACE}" >&2; exit 1;
}
[[ "${IMAGE}" == *@sha256:* && "${IMAGE#*@}" == "${EXPECTED_IMAGE_DIGEST}" ]] || {
  echo "HOLD: image/digest mismatch" >&2; exit 1;
}
[ "$(kubectl config current-context)" = "${EXPECTED_CONTEXT:-gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster}" ] || {
  echo "HOLD: unexpected kubectl context" >&2; exit 1;
}
existing_ns="$(kubectl get namespace "${NAMESPACE}" --ignore-not-found -o name)"
[ -z "${existing_ns}" ] || { echo "HOLD: namespace already exists: ${NAMESPACE}" >&2; exit 1; }

collect(){
  if [ -n "${LOG_FOLLOW_PID}" ]; then kill "${LOG_FOLLOW_PID}" 2>/dev/null || true; wait "${LOG_FOLLOW_PID}" 2>/dev/null || true; LOG_FOLLOW_PID=""; fi
  kubectl -n "${NAMESPACE}" get pods -l app=ahbn-peer -o json >"${OUTDIR}/pods.json" 2>/dev/null || true
  kubectl -n "${NAMESPACE}" get events --sort-by=.metadata.creationTimestamp >"${OUTDIR}/pod_readiness_evidence.txt" 2>/dev/null || true
  kubectl -n "${NAMESPACE}" logs job/ahbn-controller >"${OUTDIR}/controller.log" 2>/dev/null || true
  kubectl -n "${NAMESPACE}" logs -l app=ahbn-peer --all-containers=true --max-log-requests=20 --tail=-1 >"${OUTDIR}/final_snapshot.jsonl" 2>/dev/null || true
  { [ -s "${OUTDIR}/peer_stream.jsonl" ] && cat "${OUTDIR}/peer_stream.jsonl"; cat "${OUTDIR}/final_snapshot.jsonl" 2>/dev/null || true; cat "${OUTDIR}/controller.log" 2>/dev/null || true; } >"${OUTDIR}/logs.jsonl"
}
finalize() {
  local experiment_rc=$? cleanup_rc=0
  trap - EXIT INT TERM
  printf "%s\n" "${experiment_rc}" > "${OUTDIR}/experiment_exit_status.txt"
  collect || true
  if [ "${OWN_NAMESPACE}" = 1 ]; then
    local current_uid current_owner
    current_uid="$(kubectl get namespace "${NAMESPACE}" --ignore-not-found -o jsonpath='{.metadata.uid}' 2>/dev/null)" || current_uid=""
    current_owner="$(kubectl get namespace "${NAMESPACE}" --ignore-not-found -o go-template='{{index .metadata.labels "qahbn2-run-owner"}}' 2>/dev/null)" || current_owner=""
    if [ -z "${NS_UID}" ] || [ "${current_uid}" != "${NS_UID}" ] || [ "${current_owner}" != "${RUN_OWNER}" ]; then
      echo "HOLD: namespace ownership mismatch; refusing deletion" >&2
      printf "OWNERSHIP_MISMATCH\n" > "${OUTDIR}/cleanup_status.txt"
      printf "1\n" > "${OUTDIR}/cleanup_exit_status.txt"
      if [ "${experiment_rc}" -eq 0 ]; then exit 1; else exit "${experiment_rc}"; fi
    fi
    local helm_rc=0 delete_rc=0
    helm uninstall "${RELEASE}" -n "${NAMESPACE}" >"${OUTDIR}/helm_cleanup.txt" 2>&1 || helm_rc=$?
    kubectl delete namespace "${NAMESPACE}" --wait=true --timeout=180s >"${OUTDIR}/namespace_cleanup.txt" 2>&1 || delete_rc=$?
    printf "%s\n" "${helm_rc}" > "${OUTDIR}/helm_cleanup_exit_status.txt"
    printf "%s\n" "${delete_rc}" > "${OUTDIR}/namespace_cleanup_exit_status.txt"
    if [ "${helm_rc}" -ne 0 ] || [ "${delete_rc}" -ne 0 ]; then cleanup_rc=1; fi
    local remaining
    remaining="$(kubectl get namespace "${NAMESPACE}" --ignore-not-found -o name 2>"${OUTDIR}/namespace_check_error.txt")" || {
      echo "HOLD: cannot confirm namespace cleanup" >&2; cleanup_rc=1;
    }
    if [ -n "${remaining}" ]; then
      echo "HOLD: namespace remains: ${NAMESPACE}" >&2
      cleanup_rc=1
    fi
    if [ "${cleanup_rc}" -eq 0 ]; then printf "PASS\n" > "${OUTDIR}/cleanup_status.txt"; else printf "HOLD\n" > "${OUTDIR}/cleanup_status.txt"; fi
  elif [ "${CREATE_ATTEMPTED}" = 1 ]; then
    cleanup_rc=1
    printf "OWNERSHIP_UNESTABLISHED\n" > "${OUTDIR}/cleanup_status.txt"
  else
    printf "NOT_CREATED\n" > "${OUTDIR}/cleanup_status.txt"
  fi
  printf '%s\n' "${cleanup_rc}" > "${OUTDIR}/cleanup_exit_status.txt"
  if [ "${experiment_rc}" -ne 0 ]; then exit "${experiment_rc}"; fi
  if [ "${cleanup_rc}" -ne 0 ]; then exit 1; fi
  exit 0
}
trap finalize EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
"${PYTHON}" "${ROOT_DIR}/gke/app/k7_gen_topology.py" --config "${ROOT_DIR}/${CONFIG}" --out "${OUTDIR}/topology.json"
cp "${OUTDIR}/topology.json" "${ROOT_DIR}/gke/helm/ahbn/topology.json"; cp "${ROOT_DIR}/${CONFIG}" "${OUTDIR}/generated_config.yaml"
NUM_NODES="$("${PYTHON}" -c 'import json,sys; print(json.load(open(sys.argv[1]))["num_nodes"])' "${OUTDIR}/topology.json")"
CREATE_ATTEMPTED=1
kubectl create namespace "${NAMESPACE}"
NS_UID="$(kubectl get namespace "${NAMESPACE}" -o jsonpath='{.metadata.uid}')"
[ -n "${NS_UID}" ] || { echo "HOLD: missing namespace UID" >&2; exit 1; }
OWN_NAMESPACE=1
kubectl label namespace "${NAMESPACE}" "qahbn2-run-owner=${RUN_OWNER}" --overwrite
[ "$(kubectl get namespace "${NAMESPACE}" -o go-template='{{index .metadata.labels "qahbn2-run-owner"}}')" = "${RUN_OWNER}" ] || { echo "HOLD: owner label unverified" >&2; exit 1; }
helm install "${RELEASE}" "${ROOT_DIR}/gke/helm/ahbn" --namespace "${NAMESPACE}" --set namespace="${NAMESPACE}" --set image="${IMAGE}" --set numNodes="${NUM_NODES}" --set podManagementPolicy=Parallel --set controller.enabled=false --set-string "recovery.enabled=${P3G_RECOVERY_ENABLED}"
kubectl -n "${NAMESPACE}" get statefulset peer -o json >"${OUTDIR}/statefulset.json"
"${PYTHON}" -c 'import json,sys; d=json.load(open(sys.argv[1])); c=d["spec"]["template"]["spec"]["containers"][0]; e=[x.get("value") for x in c.get("env",[]) if x["name"]=="P3G_RECOVERY_ENABLED"]; assert e==[sys.argv[2]], "recovery flag mismatch"' "${OUTDIR}/statefulset.json" "${P3G_RECOVERY_ENABLED}"
kubectl -n "${NAMESPACE}" rollout status statefulset/peer --timeout=600s
kubectl -n "${NAMESPACE}" wait --for=condition=ready pod -l app=ahbn-peer --timeout=600s
kubectl -n "${NAMESPACE}" get pods -l app=ahbn-peer -o json >"${OUTDIR}/pods.json"
"${PYTHON}" -c 'import json,sys; p=json.load(open(sys.argv[1])); image=sys.argv[2]; digest=sys.argv[3]; items=p.get("items",[]); assert len(items)==20, f"expected 20 pods, got {len(items)}"; assert all(x["spec"]["containers"][0]["image"]==image for x in items), "pod image reference mismatch"; ids=[x["status"]["containerStatuses"][0]["imageID"] for x in items]; assert all(digest in value for value in ids), f"pod image digest mismatch: {sorted(set(ids))}"' "${OUTDIR}/pods.json" "${IMAGE}" "${EXPECTED_IMAGE_DIGEST}"
sleep 5
kubectl -n "${NAMESPACE}" logs -f -l app=ahbn-peer --all-containers=true --max-log-requests=20 --tail=-1 >"${OUTDIR}/peer_stream.jsonl" 2>"${OUTDIR}/peer_stream.err" & LOG_FOLLOW_PID=$!
helm upgrade "${RELEASE}" "${ROOT_DIR}/gke/helm/ahbn" --namespace "${NAMESPACE}" --reuse-values --set controller.enabled=true --set-string "recovery.enabled=${P3G_RECOVERY_ENABLED}"
kubectl -n "${NAMESPACE}" wait --for=condition=complete job/ahbn-controller --timeout=900s
# EXIT trap preserves separate experiment/cleanup status and cleanup evidence.
