# D7-F — Seed 44 Formal GKE Execution (2026-10-20)

**Status:** EXECUTION PASS (5/5 for seed44); K7 validators PASS. **Cumulative formal execution: 15/25 unique method×seed coordinates** (seeds 42, 43 and 44). Full independent archive-integrity and runtime-image parity audit remains OPEN.

## Provenance
- User-supplied terminal transcript ends `K5-Q FORMAL SEED BATCH PASS seed=44`; each of five methods prints `K7 RESULT VALIDATION PASS`.
- Evidence root (Drive-synced): `output/evidence/20261020T041621Z-K5Q-formal/`. The 25 `generated/*.json` configurations in this root are **not** 25 completed experiments; only five seed44 runs are demonstrated.
- Invoked `FORMAL_SEED=44` and `P3G_RECOVERY_ENABLED=0`; frozen experimental contract not modified. All five methods reported deployment and readiness of 20 pods, controller completion, and four churn events.

## Results (from terminal metrics)
| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards | K7 validation |
|---|---:|---:|---:|---:|---|
| Gossip | 0.8858695652173914 | 0.06577114164829254 | 3089 | 4014 | PASS |
| Structured | 0.08125131219819441 | 0.0048006991545359295 | 0 | 152 | PASS |
| DC-SoC | 0.08859962208692 | 0.0111682524283727 | 0 | 184 | PASS |
| AHBN | 0.31206715634837356 | 0.03050021231174469 | 531 | 1257 | PASS |
| Q-AHBN2 | 0.4701695624869165 | 0.04419563710689545 | 767 | 2020 | PASS |

Seed44 Q-AHBN2 − AHBN delivery: +0.15810240613854294 (15.81 percentage points). Q-AHBN2 has higher duplicates and propagation delay. Single-seed observation only; no across-seed statistical inference.

## Recovery measurements / audit flag
- Gossip: two recovered events (event1 recovery_time_s=27.438531398773193, message `m77`; event2 recovery_time_s=2.982052803039551, also `m77`), events3–4 censored at 18 s.
- Structured, DC-SoC, AHBN, Q-AHBN2: four events each censored at 18 s, zero recovered events.
- **Audit question:** Explain how Gossip event1 is marked recovered at 27.44 s while non-recovered events use 18 s censoring, and why events1 and 2 share message `m77`. Confirm event-time anchors and recovery-window implementation against frozen definition. This is a **measurement consistency question**, not a proven defect; do not alter or exclude the observation without evidence.
- DC-SoC delivery (8.86%) is markedly lower than seed43 (88.67%). Preserve variation and investigate only within the existing audit.

## Outstanding checks
- Inspect per-run archived manifest, image/pod identity, cleanup status, experiment exit status and namespace absence; transcript does not independently establish cleanup.
- SHA256 evidence integrity, frozen topology/target contract, workload timing and method-specific logs.
- Complete seeds 45–46, then run prescribed paired K6/D8 statistics and validity review. Do not tune the algorithm or change the frozen protocol on the basis of observed performance.

**Decision:** D7-F seed44 execution PASS; 15/25 completed. Full evidence audit OPEN. Manuscript remains **under peer review at Journal of Cloud Computing**, without DOI or publication claim.
