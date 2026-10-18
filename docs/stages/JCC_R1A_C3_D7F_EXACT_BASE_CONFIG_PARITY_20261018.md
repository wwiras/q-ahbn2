# D7-F — Exact RO3 versus RO4 churn configuration comparison (2026-10-18)

**Review decision: BASE CONFIGURATION PARITY PASS / HISTORICAL METHODOLOGY CONSISTENCY SUPPORTED / FORMAL RUN ADMISSION CONDITIONAL, NO NEW RUN YET.**

## Scope and provenance
Researcher directed return to the original Q-AHBN2 implementation and historically frozen AHBN2-GKE methodology, with CAP5 recovery investigation PASS/CLOSED as *interpretation only*. Recovery implementation is deferred to thesis/paper future work. No modifications to algorithms, experimental data, recovery source or reruns authorized in this read-only review.

Actual authoritative files inspected:
- RO3: `wwiras/ahbn2_gke:experiments/k7_exp11.yaml` and `docs/K7_ahbn2gke_exp11v2.md`.
- RO4: `wwiras/q-ahbn2:gke/experiments/k5_q_formal.yaml` and `gke/experiments/k3_q_smoke.yaml`.
- RO4 historical D7 safety and canary records: `docs/stages/JCC_R1A_C3_D7_SM_CANARY_RELEASE_20261017.md`, `JCC_R1A_C3_D7_SM_POSTRUN_CAUSAL_P3_20261017.md`, `JCC_R1A_C3_D7_P3G_AHBN_READONLY_ADMISSION_EVIDENCE_20261018.md`.
- Prior stage: `docs/stages/JCC_R1A_C3_D7F_RO3_HISTORICAL_CONSISTENCY_RECOVERY_FUTURE_WORK_20261018.md`.
- RO4 canonical Drive output/evidence inspected at https://drive.google.com/drive/folders/1bONTh6_TvcZ1oNL13zT_ktKw1h1rzCa0 ; raw evidence folders retained, untouched.

## Direct configuration parity — EXACT MATCH for displayed base YAML values

| Parameter | RO3 K7 Exp11 v2 | RO4 K5 Q formal | Comparison |
|---|---|---|---|
| Network | BA N=20, m=2 | BA N=20, m=2 | MATCH |
| Clusters | 4 | 4 | MATCH |
| Message source | 0 | 0 | MATCH |
| Topology base seed | 42 | 42 | MATCH |
| Seed policy in K7 historical method | 42–46 fixed IDs | RO4 runner treatment seeds must be verified | PARTIAL |
| Settling | 18.0 s | 18.0 s | MATCH |
| Churn mode | churn | churn | MATCH |
| Trigger / events / interval / target class | 1.0 s / 4 / 1.2 s / mixed | same | MATCH |
| Workload | 240 messages, interval 0.4 s | same | MATCH |
| Bottleneck | disabled | disabled | MATCH |
| S5 treatment | selector_control / S5 | same | MATCH |
| Contract | k7-exp11-v2 | k7-exp11-v2 | MATCH |
| Schedule semantics | absolute_common_epoch (both) | same | MATCH |
| Offsets | +1, +26, +51, +76 s | same | MATCH |
| Recovery definition | first_post_rejoin_opportunity_full_delivery_to_active_ready_peers | same | MATCH |
| DU after event | true | true | MATCH |

The Q-AHBN2 `k3_q_smoke.yaml` is **not** a matched formal reference: 4 peers, 4 messages, 2 clusters, no failure and 2 s settling; it is infrastructure smoke only. Do not substitute it for K5 formal / K7 churn.

## What this does and does not establish
- **ESTABLISHED**: direct textual parity of base YAML configuration, not image/runtime or full seed-by-seed output parity.
- **NOT YET ESTABLISHED**: matching generated topologies/target-selection hashes across seeds 42–46, five-method contract inclusion, actual launch commands/overrides, exact-source and deployed image identity, runtime scheduling/cleanup equivalence, historical comparison of per-seed delivery denominators.
- Historical K7 v2 says the unchanged peer/algorithm implementation is retained and expected churn-induced RPC unavailability is logged as a valid observation. This is compatible with studying incomplete delivery; an unhandled controller/scheduler failure or malformed evidence is still an execution defect and must not be relabeled as valid churn.
- P3 read-only audit classified Q-AHBN2/other method root-cause attribution as UNRESOLVED from available evidence, despite a supported neighbor exclusion path. CAP5 closure is a research disposition, **not a scientific proof that scheduling explains all outcomes**.
- Original nonformal seed42 4-method canary, and later P3G candidate, are diagnostic only; the formal D7-F 25-run campaign has NOT been completed by this review. Preserve earlier observations and do not relabel as formal.

## Readiness decision and minimal remaining checks
**D7-F CONFIGURATION PARITY PASS / FORMAL EXECUTION STILL HOLD** until original runner is inspected for generated seed/target parity and image pin, suitable N=20 capacity/runtime admission and a fresh one-time researcher execution authorization. Do *not* require the superseded A12 recovery implementation, 10 s/0.25 s control, security extension or T19–T38. No new recovery-development gates.

Next: D7-F original-launcher and target hash reconciliation against historical K7 v2 (read-only), then choose whether preserved formal artifacts suffice or any additional formal campaign is required. D8 follows formal D7-F evidence review, not this base-config pass. Manuscript submitted to Journal of Cloud Computing remains **under peer review, unpublished, without DOI**. Future work: asynchronous neighbor-state awareness / rejoin synchronization.
