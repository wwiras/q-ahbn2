# P3G-CAP5-A8 — Read-only mTLS design approval and Kubernetes authority reconciliation (2026-10-18)

**Decision: DESIGN ARCHITECTURE ENDORSED / MANIFEST REVIEW COMPLETED / FORMAL FREEZE HOLD / IMPLEMENTATION HOLD.** This approval is for review-level architecture only. No Helm, runtime, protobuf, security infrastructure, tests or GKE actions are authorized or claimed as completed.

## Authority and evidence
- CAP5-A7 design: `docs/stages/JCC_R1A_C3_D7_P3G_CAP5_A7_AUTH_GENERATION_ACK_CONTRACT_20261018.md`, commit `30462663ac1a85dac61b17be10e5499da01eb8e0`.
- Source review: `gke/helm/ahbn/values.yaml`, `gke/helm/ahbn/templates/job-controller.yaml`, `rbac.yaml`, `service.yaml`, `statefulset.yaml`; code baselines `gke/app/controller_shared.py`, `peer.py`, `peer.proto`, `recovery_availability.py`.
- Read-only Drive discovery: RO4 experiment corpus `https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`, output/evidence `https://drive.google.com/drive/folders/1bONTh6_TvcZ1oNL13zT_ktKw1h1rzCa0` (CAP5 diagnostic folder `https://drive.google.com/drive/folders/1rxpmLphHdW00NmfxlVInbCj6R1Vuq0qX`). No new empirical recovery results claimed. GitHub remains control/text authority; Drive remains evidence store.

## Actual Helm manifest state (source inspected)

| Source | Verified current configuration | Gap against A7 |
|---|---|---|
| values.yaml | `recovery.enabled: "0"`, `grpcPort: 50051`; controller disabled by default | No separate secure recovery port, trust configuration or fencing flag |
| job-controller.yaml | Controller Job using `serviceAccountName: ahbn-controller`, `restartPolicy: Never`, `backoffLimit: 0` | Controller-only mTLS credential provisioning/mount, verified process/run epoch and restart policy not specified |
| rbac.yaml | `ahbn-controller` ServiceAccount; namespace Role pods `get,list,delete`; RoleBinding | Does not authenticate gRPC; least-privilege scope and controller credential access policy incomplete |
| service.yaml | Headless Service on existing peer gRPC port | No distinct recovery control port or NetworkPolicy isolation |
| statefulset.yaml | Peer container exposes existing gRPC port, recovery env OFF, topology config | No secured server port, receiver server cert/CA/trust mounts or explicit recovery authority readiness gate |
| peer.py / controller_shared.py | Existing insecure gRPC channels; legacy `NotifyRecoveryRejoin` with `Ack.ok` counter | No cryptographic controller identity, generation-proof payload, mTLS boundary or typed accepted-vs-recovered response |

These are checks of **repository source templates**, not a cluster deployment inspection or rendered Helm verification. Absence from reviewed templates does not prove that no external policy exists in an actual cluster; no external policy was verified in this gate.

## A8 architecture assessment — approve direction, do not claim completed implementation

1. **Dedicated mTLS endpoint:** Endorse distinct `RecoveryControlService` with a controller-only client certificate, trusted receiver server certificate and server-side authenticated SAN/authorization check. Legacy plaintext recovery handler must fail closed if enhanced recovery is enabled. Existing dissemination and peer GetStatus are not made generally secure by this targeted change.
2. **Controller identity:** Endorse run-scoped controller principal `spiffe://ahbn.local/run/<run_id>/controller/churn` as a proposed SAN syntax only, **not evidence that SPIFFE is installed**. The actual issuer, CA bundle, signed controller certificate binding to ServiceAccount/workload, server cert DNS verification, rotation/revocation and safe distribution need a manifest- and threat-model-level design before freeze.
3. **Pod UID evidence:** Endorse Kubernetes API `metadata.uid` old/new mismatch plus readiness and target GetStatus. Current controller Role pods get/list/delete provides candidate API authority, but the precise observer trust of a controller-produced UID/lease attestation and its freshness remains unproved. Avoid calling a UID itself authentication.
4. **Independent restart fencing:** Endorse fail-closed on restart as a requirement. **Critical unresolved requirement:** A crashed controller cannot notify peers, so a process-local counter, ordinary mTLS certificate and `restartPolicy: Never` do NOT independently revoke old markers. Define one implementable issuer and validation design for a run-scoped controller epoch/lease, with expiry, trust roots, fencing and receiver checks before marker admission and any recovery commit. If none is selected/testable, feature MUST remain disabled.
5. **Ack semantics:** Endorse a versioned typed response where `ACCEPTED` only means valid marker stored, `DUPLICATE_NOOP` cannot extend TTL or probe allowance, negative outcome and RPC failure are separate, and only independent peer GetStatus + atomic exclusion removal yields `neighbors_reenabled`. Preserve historic CAP5 `acknowledged` without retroactive relabeling.

## Concrete manifest change inventory (FUTURE ONLY; do not edit during A8)
- values: separate `recovery.controlPort`, `recovery.auth.enabled`, `recovery.epochAuthority.enabled`, trust/secret names and feature gate; preserve default OFF and frozen 50051.
- statefulset: distinct control container port, secured server-only endpoint, peer server identity and read-only server cert/CA mounts, readiness/fail-closed behavior.
- controller Job: controller-only ServiceAccount, trusted client cert/key mount/issuer binding, server identity verification, run/epoch launch contract, no reuse of prior run authority.
- service: separate named control port, no public exposure, explicit selector/DNS target binding.
- rbac: separate minimum pod-UID observation/delete permissions from certificate issuance/secret access; ensure peer workloads cannot acquire controller key; admission isolation and token audience contract.
- NetworkPolicy: default deny control port except approved controller pods, controller egress and DNS/needed Kubernetes API access documented; labels are defense-in-depth, not sole authentication.
- external issuer/admission: CA roots and cert rotation/revocation/short-lived credentials, trust-policy manifests; no private key material in GitHub/Drive or logs.
- fencing authority: unambiguous independent lease/epoch source, issuer access and revocation/expiry semantics, replay resistance, observer-side invariant tests and startup/shutdown cleanup.
- proto/runtime: versioned secure request/typed response, reject legacy insecure method when feature ON, fake clock/lease tests, frozen controller/Q parity and no additional Forward/learner counters.

## Risks and release blockers

**R1 SECURITY:** exact CA/certificate lifecycle, SAN verification and secret isolation unverified.
**R2 FENCING:** independent controller crash/restart fencing/observer validation mechanism not yet concretely chosen; high priority.
**R3 WIRE:** A4 optional legacy-proto extension versus A7 dedicated versioned service must have one approved canonical schema and backward-compatibility test.
**R4 ENVIRONMENT:** no rendered Helm chart, deployed cluster NetworkPolicy, issuer, ingress/egress or Role rules have been verified.
**R5 ACK:** typed outcome contract needs complete compatibility/error handling test contract.
**R6 TIMING:** W=10.0s and Δ=0.25s are proposed finite offline settings, NOT frozen or empirically optimized.

## Decision and next gate

- CAP5-A8 = **READ-ONLY MANIFEST RECONCILIATION PASS / SECURITY ARCHITECTURE CONDITIONALLY ENDORSED / FINAL APPROVAL AND DESIGN FREEZE HOLD**.
- This review does not represent explicit researcher acceptance of final security details. A7 direction is supported but its concrete independent lease/fencing authority remains an open choice.
- Runtime/proto/Helm edits, T19–T38, new GKE run, D7-F, D8 = **HOLD**.
- No alteration of frozen AHBN EWMA, mode, S5 fanout, Q-AHBN2 reward/policy or simulator parity.
- Scientific caveat: CAP5 nonformal diagnostic run is not evidence of restored end-to-end forwarding or performance increase.
- Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* submitted to **Journal of Cloud Computing**, under peer review, unpublished, no DOI.

**Recommended A9:** select a precise independently verifiable controller-epoch fencing scheme; complete an explicit controller cert issuer/permission model and canonical RPC/proto decision; inspect generated Helm output and negative-test plan **offline**. After A9 only, request independent approval of numerical W and Δ before implementation.
