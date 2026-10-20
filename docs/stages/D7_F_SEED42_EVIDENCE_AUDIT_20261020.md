# D7-F — Seed 42 Evidence Audit (2026-10-20)

**Status:** EXECUTION PASS (5/5) / BOUNDED EVIDENCE AUDIT PARTIAL PASS / FULL INTEGRITY AND RUNTIME IMAGE PARITY NOT YET CLOSED.

## Scope and provenance
- Authoritative experiment code/control: `wwiras/q-ahbn2`; execution source revision verified by researcher before run: `6433f7429e0342df44c272b236423c65203a9136`.
- Experiment evidence, Drive-synced folder: `output/evidence/20261020T032934Z-K5Q-formal/` (Drive folder `1cdjagJ4S6yLYfDh9wVTO_p6QahxlWux2`).
- Approved image selected at preflight: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`. Preflight Linux/amd64 registry verification PASS. This does **not** substitute for per-pod deployed-image identity verification.
- Original P3G_RECOVERY_ENABLED=1 attempt stopped before formal execution due to namespace guard; corrected formal execution used `P3G_RECOVERY_ENABLED=0`. Preserve both attempts separately.
- Frozen experiment: 5 methods × seeds 42–46 = 25 unique coordinates; protocol unchanged.

## Seed 42 results (reported by completed run validator)
| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards | Validator |
|---|---:|---:|---:|---:|---|
| Gossip | 0.8637232010 | 0.0965761026 | 2200 | 3848 | PASS |
| Structured | 0.0811320755 | 0.0034789254 | 0 | 152 | PASS |
| DC-SoC | 0.0887909320 | 0.0124917497 | 0 | 188 | PASS |
| AHBN | 0.1328436516 | 0.0093110879 | 146 | 397 | PASS |
| Q-AHBN2 | 0.3362646566 | 0.0284162064 | 403 | 1380 | PASS |

Values are descriptive for a **single seed**. Do not infer overall superiority or use low delivery as an exclusion criterion.

## Checks supported by recorded evidence
1. Terminal execution: five methods completed; K7 result validation PASS for each; runner printed `K5-Q FORMAL SEED BATCH PASS seed=42`.
2. Drive folder inspection: five seed42 method folders contain `run_manifest.json`, `metrics.json`, topology, controller, pod, churn, and cleanup records.
3. Independent per-method archived `experiment_exit_status.txt` = `0`; `cleanup_status.txt` = `PASS`; `cleanup_exit_status.txt` = `0` (five of five).
4. Researcher's local read-only command: five `run_manifest.json` files parse as JSON; all five cleanup statuses PASS; all five experiment statuses 0; `kubectl get namespace qahbn2-k5-formal --ignore-not-found` returned no namespace. This confirms namespace absence at the time of that check.
5. Five manifest records show seed 42, correct respective method, shared target-selection hash `361af2ec37edf50d9b232ed42faf4f8b14482f95fba412d2e87305dccdb39386`, frozen targets 0/5/10/15, 240 messages, 0.4 s interval, +1/+26/+51/+76 s churn offsets and shared contract hash `5b26ed302abc57ce2816511f5257da7aca488ba7f3d6686e52483cd3f5675a7d`.

## Outstanding K6/D8 evidence checks (not a claim of defect)
- Verify per-run actual Kubernetes deployed image digests, pod/runtime identity and Git provenance against pinned image.
- Verify archive-level SHA256 checksums, complete required artifact contents and full log integrity.
- Audit actual workload/churn timing, maintenance invariants, Q decision/reward traces and method-specific validity independent of `K7 RESULT VALIDATION PASS`.
- Compare seeds 42–46 only after all coordinates complete; perform prescribed paired statistics separately.

**Decision:** D7-F seed42 execution PASS; 5/25 formal coordinates completed. Evidence archive is present and basic status/manifest checks pass, but **full scientific validity audit remains PARTIAL**. No experiment redesign, parameter retuning or unsupported scientific claim is authorized. The remaining seeds may be executed using the unchanged frozen protocol while comprehensive evidence audit is tracked; any detected defect requires prospective documentation and K6 validity treatment.

**Publication status:** The Q-AHBN2 manuscript was submitted to *Journal of Cloud Computing* (Springer) and remains **under peer review**; **no DOI / not published**. Do not describe as accepted or published. Manuscript repository: `wwiras/QAHBN2-Manuscript`. Thesis repository: `wwiras/MUM_FIT_ThesisWira`; thesis Drive corpus folder `1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR`.
