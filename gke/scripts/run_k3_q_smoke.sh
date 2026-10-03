#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PYTHON="${PYTHON:-python3}"
IMAGE="${IMAGE:-}"
NAMESPACE="${NAMESPACE:-qahbn2-k3-smoke}"
RELEASE="${RELEASE:-qahbn2}"
OUTDIR="${ROOT_DIR}/output/evidence/q-ahbn-gke-$(date +%d%m%Y%H%M%S)-k3q-smoke"
TOPOLOGY="${OUTDIR}/topology.json"
NUM_PEERS=4

fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required"
for x in kubectl helm docker shasum; do command -v "${x}" >/dev/null || fail "missing command: ${x}"; done
IMAGE="${IMAGE}" EXPECTED_ARCH=amd64 bash "${ROOT_DIR}/gke/scripts/verify_k3_q_image.sh"
IMAGE_INSPECT="$(docker buildx imagetools inspect "${IMAGE}")"
echo "${IMAGE_INSPECT}" > /tmp/qahbn2-k3-image-inspect.txt
mkdir -p "${OUTDIR}"

collect_artifacts(){
  kubectl -n "${NAMESPACE}" get pods -o wide >"${OUTDIR}/pods.txt" 2>/dev/null || true
  for i in 0 1 2 3; do kubectl -n "${NAMESPACE}" logs "peer-${i}" >"${OUTDIR}/peer-${i}.log" 2>/dev/null || true; done
}
trap collect_artifacts EXIT

git -C "${ROOT_DIR}" rev-parse HEAD >"${OUTDIR}/git_commit.txt"
printf "%s\n" "${IMAGE}" >"${OUTDIR}/image.txt"
cp /tmp/qahbn2-k3-image-inspect.txt "${OUTDIR}/image_manifest.txt"

"${PYTHON}" "${ROOT_DIR}/gke/app/gen_topology.py" --config "${ROOT_DIR}/gke/experiments/k3_q_smoke.yaml" --out "${TOPOLOGY}"
cp "${TOPOLOGY}" "${ROOT_DIR}/gke/helm/ahbn/topology.json"

if helm status "${RELEASE}" -n "${NAMESPACE}" >/dev/null 2>&1; then helm uninstall "${RELEASE}" -n "${NAMESPACE}" >/dev/null; fi
if kubectl get namespace "${NAMESPACE}" >/dev/null 2>&1; then kubectl delete namespace "${NAMESPACE}" --wait=true >/dev/null; fi

helm install "${RELEASE}" "${ROOT_DIR}/gke/helm/ahbn" --namespace "${NAMESPACE}" --create-namespace --set namespace="${NAMESPACE}" --set image="${IMAGE}" --set numNodes="${NUM_PEERS}" --set controller.enabled=false

kubectl -n "${NAMESPACE}" rollout status statefulset/peer --timeout=600s
kubectl -n "${NAMESPACE}" wait --for=condition=ready pod -l app=ahbn-peer --timeout=600s

kubectl -n "${NAMESPACE}" exec -i peer-0 -- python - "${NAMESPACE}" <<'PY'
import sys, time, grpc
import peer_pb2, peer_pb2_grpc
ns=sys.argv[1]
addr=f"peer-0.ahbn-peer.{ns}.svc.cluster.local:50051"
with grpc.insecure_channel(addr) as ch:
    stub=peer_pb2_grpc.PeerServiceStub(ch)
    for i in range(4):
        stub.StartRun(peer_pb2.StartRequest(run_id="k3_q_smoke",message_id=f"k3m{i}"),timeout=10)
        time.sleep(.2)
PY

sleep 5
for i in 0 1 2 3; do kubectl -n "${NAMESPACE}" logs "peer-${i}" >"${OUTDIR}/peer-${i}.log"; done

cat "${OUTDIR}"/peer-*.log | grep '"event": "qahbn2_decision"' >"${OUTDIR}/qahbn2_decisions.log" || true
cat "${OUTDIR}"/peer-*.log | grep '"event": "qahbn2_attempt_outcome"' >"${OUTDIR}/qahbn2_attempt_outcomes.log" || true
cat "${OUTDIR}"/peer-*.log | grep '"event": "qahbn2_reward_closed"' >"${OUTDIR}/qahbn2_reward_closed.log" || true

[ -s "${OUTDIR}/qahbn2_decisions.log" ] || fail "no qahbn2_decision evidence"
[ -s "${OUTDIR}/qahbn2_attempt_outcomes.log" ] || fail "no qahbn2_attempt_outcome evidence"
[ -s "${OUTDIR}/qahbn2_reward_closed.log" ] || fail "no qahbn2_reward_closed evidence"

"${PYTHON}" - "${OUTDIR}" <<'PY'
import json,sys
from pathlib import Path
root=Path(sys.argv[1])
events=[]
for p in root.glob("peer-*.log"):
    for line in p.read_text().splitlines():
        try: events.append(json.loads(line))
        except Exception: pass
dec=[e for e in events if e.get("event")=="qahbn2_decision"]
out=[e for e in events if e.get("event")=="qahbn2_attempt_outcome"]
rew=[e for e in events if e.get("event")=="qahbn2_reward_closed"]
attempt=[e for e in events if e.get("event")=="k7_forward_attempt" and e.get("strategy")=="qahbn2"]
fwd=[e for e in events if e.get("event")=="forward" and e.get("strategy")=="qahbn2"]
assert dec and out and rew and attempt
required={"decision_id","state","action","mode_ahbn","k_ahbn","mode_q","k_q","realized_targets"}
assert required <= set(dec[0])

new=[e for e in out if e.get("outcome")=="NEW"]
nonnew=[e for e in out if e.get("outcome") in {"DUPLICATE","FAILED"}]
decision_fwd=[e for e in fwd if e.get("decision_id") is not None]

def key(e):
    return (str(e.get("decision_id")), int(e.get("dst_peer")), str(e.get("message_id")))

new_keys=[key(e) for e in new]
fwd_keys=[key(e) for e in decision_fwd]
assert len(new_keys)==len(set(new_keys)), "duplicate NEW outcome key"
assert len(fwd_keys)==len(set(fwd_keys)), "duplicate generic forward key"
assert sorted(new_keys)==sorted(fwd_keys), "NEW/generic-forward mismatch"

nonnew_keys={key(e) for e in nonnew}
assert not (nonnew_keys & set(fwd_keys)), "DUPLICATE/FAILED has generic successful-forward event"
assert len(fwd) <= len(attempt), "F_success exceeds F_attempt"

summary={
    "status":"PASS",
    "decision_events":len(dec),
    "attempt_outcome_events":len(out),
    "reward_closed_events":len(rew),
    "outcomes":sorted({e.get("outcome") for e in out}),
    "F_attempt":len(attempt),
    "F_success":len(fwd),
    "decision_bound_NEW":len(new),
    "decision_bound_forward":len(decision_fwd),
    "new_forward_exact_match":sorted(new_keys)==sorted(fwd_keys),
    "nonnew_forward_overlap":len(nonnew_keys & set(fwd_keys)),
    "f_success_le_f_attempt":len(fwd)<=len(attempt),
}
(root/"k3q_smoke_summary.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
PY

kubectl delete namespace "${NAMESPACE}" --wait=true >/dev/null
trap - EXIT
echo "K3-Q SMOKE PASS"
echo "Evidence: ${OUTDIR}"