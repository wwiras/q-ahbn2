#!/usr/bin/env bash
# D7-P3 — one-pod, zero-experiment GKE deployed-image identity probe.
# Run from repository root: bash gke/scripts/d7_p3_verify.sh
# Requires kubectl, python3, and explicit current context match.
set -euo pipefail

EXPECTED_CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"
NAMESPACE="default"
POD="qahbn2-d7-p3-verify"
EXPECTED_DIGEST="sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
IMAGE="docker.io/wwiras/q-ahbn2@${EXPECTED_DIGEST}"
SOURCE_COMMIT="280855900e89b1db5269ace73b4aabf6c7afae88"

for tool in kubectl python3 shasum; do
  command -v "$tool" >/dev/null 2>&1 || { printf 'ERROR: missing %s\n' "$tool" >&2; exit 1; }
done

CURRENT_CONTEXT="$(kubectl config current-context)"
if [[ "$CURRENT_CONTEXT" != "$EXPECTED_CONTEXT" ]]; then
  printf 'HOLD: context %s does not match %s\n' "$CURRENT_CONTEXT" "$EXPECTED_CONTEXT" >&2
  exit 1
fi

# Fail closed if the fixed verification name already exists; never replace it.
if kubectl get pod "$POD" -n "$NAMESPACE" >/dev/null 2>&1; then
  echo "HOLD: verification pod already exists; inspect it manually, do not overwrite." >&2
  exit 1
fi

UTC="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="output/evidence/${UTC}-D7-P3-single-pod"
mkdir -p "$OUT"
printf '%s\n' "$CURRENT_CONTEXT" > "$OUT/context.txt"
printf '%s\n' "$IMAGE" > "$OUT/expected_image.txt"
printf '%s\n' "$SOURCE_COMMIT" > "$OUT/source_commit.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$OUT/inspection_utc.txt"
printf 'Evidence: %s\n' "$OUT"

POD_UID=""
cleanup() {
  local rc="$?"
  trap - EXIT INT TERM
  if [[ -n "$POD_UID" ]]; then
    # A name-only delete can erase someone else's pod. Verify UID first.
    local current_uid=""
    current_uid="$(kubectl get pod "$POD" -n "$NAMESPACE" -o jsonpath='{.metadata.uid}' 2>/dev/null || true)"
    if [[ "$current_uid" == "$POD_UID" ]]; then
      kubectl delete pod "$POD" -n "$NAMESPACE" --wait=true --timeout=120s \
        > "$OUT/delete.txt" 2>&1 || true
    else
      printf 'HOLD: UID changed or unavailable; no deletion attempted.\n' > "$OUT/delete.txt"
    fi
    if kubectl get pod "$POD" -n "$NAMESPACE" > "$OUT/cleanup_check.txt" 2>&1; then
      echo "CLEANUP NOT CONFIRMED: pod still exists. Inspect/delete only after checking UID." | tee -a "$OUT/cleanup_check.txt"
    else
      echo "Pod name absent after cleanup attempt." >> "$OUT/cleanup_check.txt"
    fi
  fi
  (cd "$OUT" && shasum -a 256 ./*.txt ./*.json ./*.yaml > SHA256SUMS 2>/dev/null) || true
  echo "Evidence directory: $OUT"
  exit "$rc"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

cat > "$OUT/pod.yaml" <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: $POD
  namespace: $NAMESPACE
  labels:
    purpose: d7-p3-image-verification
spec:
  restartPolicy: Never
  automountServiceAccountToken: false
  terminationGracePeriodSeconds: 1
  nodeSelector:
    kubernetes.io/arch: amd64
  containers:
    - name: verifier
      image: $IMAGE
      imagePullPolicy: Always
      command: ["python", "-c"]
      args: ["import platform,time; print(platform.machine(), flush=True); time.sleep(240)"]
      resources:
        requests: {cpu: 100m, memory: 128Mi}
        limits: {cpu: 250m, memory: 256Mi}
EOF

# Capture UID even if kubectl apply returns a nonzero status after creation.
kubectl create -f "$OUT/pod.yaml" > "$OUT/create.txt" 2>&1 || {
  POD_UID="$(kubectl get pod "$POD" -n "$NAMESPACE" -o jsonpath='{.metadata.uid}' 2>/dev/null || true)"
  cat "$OUT/create.txt" >&2
  exit 1
}
POD_UID="$(kubectl get pod "$POD" -n "$NAMESPACE" -o jsonpath='{.metadata.uid}' 2>/dev/null || true)"
if [[ -z "$POD_UID" ]]; then
  echo "HOLD: created pod UID unavailable; check for orphaned verification pod manually." >&2
  exit 1
fi

kubectl wait "pod/$POD" -n "$NAMESPACE" --for=condition=Ready --timeout=180s \
  > "$OUT/wait.txt" 2>&1 || true
kubectl get pod "$POD" -n "$NAMESPACE" -o json > "$OUT/pod.json"
kubectl describe pod "$POD" -n "$NAMESPACE" > "$OUT/describe.txt" 2>&1 || true
kubectl logs "$POD" -n "$NAMESPACE" > "$OUT/logs.txt" 2>&1 || true

python3 - "$OUT/pod.json" "$IMAGE" "$POD_UID" <<'PY' | tee "$OUT/decision.txt"
import json, sys
pod = json.load(open(sys.argv[1]))
expected_image, expected_uid = sys.argv[2:]
spec = pod['spec']['containers'][0]
status = next((s for s in pod.get('status', {}).get('containerStatuses', []) if s.get('name') == spec['name']), {})
uid = pod['metadata'].get('uid')
image_id = status.get('imageID', '')
ready = status.get('ready', False)
restarts = status.get('restartCount')
spec_match = spec.get('image') == expected_image
digest = expected_image.rsplit('@', 1)[-1]
runtime_match = image_id.lower().split('@')[-1] == digest.lower() if '@' in image_id else False
print('Pod UID:', uid)
print('Requested image:', spec.get('image'))
print('Runtime imageID:', image_id or 'NOT OBSERVED')
print('Ready:', ready)
print('Restarts:', restarts if restarts is not None else 'NOT OBSERVED')
print('Spec matches:', spec_match)
print('Runtime manifest digest matches:', runtime_match)
if uid == expected_uid and spec_match and runtime_match and ready and restarts == 0:
    print('D7-P3: CANDIDATE PARITY OBSERVED — REVIEW REQUIRED')
else:
    print('D7-P3: PARITY NOT ESTABLISHED / HOLD')
print('NOTE: containerd config-digest-only imageID requires further provenance cross-check.')
PY

echo "Verification complete; cleanup runs automatically."
