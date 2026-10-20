# D7-F — Seed 43 Formal GKE Execution (2026-10-20)

**Status:** EXECUTION PASS (5/5 for seed 43); basic output validation PASS; full independent evidence integrity and runtime-image audit OPEN. **Cumulative formal execution: 10/25 coordinates (seeds 42 and 43).**

## Evidence
- Researcher-supplied terminal log ends `K5-Q FORMAL SEED BATCH PASS seed=43` after `K7 RESULT VALIDATION PASS` for each of Gossip, Structured, DC-SoC, AHBN and Q-AHBN2.
- Drive-synced evidence root: `output/evidence/20261020T035637Z-K5Q-formal/`. This is a **new folder** separate from the completed seed42 root `20261020T032934Z-K5Q-formal`; generation of 25 configuration files does not imply 25 executed runs.
- Runtime reported 20 ready pods per coordinate and controller job completion. Namespace cleanup and archived per-run manifests/exit statuses have **not** been independently inspected for seed43 in this record.
- The approved frozen K4-Q protocol remains 5 methods × 5 seeds 42–46, N=20, BA(m=2), 240 messages, interval 0.4 s, four churn offsets +1/+26/+51/+76 s. User invoked `FORMAL_SEED=43`, `P3G_RECOVERY_ENABLED=0`.

## Reported seed43 results
| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards | K7 validator |
|---|---:|---:|---:|---:|---|
| Gossip | 0.885242474916388 | 0.06879696150620779 | 4322 | 4011 | PASS |
| Structured | 0.08179142136248949 | 0.004161168138186137 | 0 | 152 | PASS |
| DC-SoC | 0.886744966442953 | 0.2718620300292969 | 0 | 4004 | PASS |
| AHBN | 0.1389121338912134 | 0.009296939770380656 | 200 | 432 | PASS |
| Q-AHBN2 | 0.1311715481171548 | 0.009773279229799906 | 232 | 391 | PASS |

Q-AHBN2 minus AHBN delivery = **-0.0077405857740586** (about **-0.774 percentage points**) on seed43. Seed42 showed a positive difference; no across-seed inference is justified yet. DC-SoC seed43 delivery is substantially higher than seed42; do not suppress this variation. Performance does not determine run validity.

## Recovery evidence
- All four recovery events were censored at 18 s for Gossip, DC-SoC, AHBN and Q-AHBN2, with no recovered event observed under the logged recovery definition.
- Structured recorded one recovered event (event 1, 0.1921 s), with three censored events.
- Infrastructure readiness times were recorded; readiness alone is not equivalent to dissemination recovery. No causal claim is established solely from these fields.

## Remaining verification
1. Inspect seed43 archived per-method `run_manifest.json`, `metrics.json`, cleanup and exit status; confirm no namespace remains.
2. Verify per-pod deployed image digest and Git provenance, plus SHA256 integrity and required evidence completeness.
3. Audit churn, actual workload injection, method-specific maintenance and Q learning traces under the frozen validity rules.
4. Complete seeds 44–46 under the unchanged protocol and conduct paired K6/D8 statistical analysis before performance claims.

**Decision:** D7-F seed43 execution PASS; **10/25** completed execution coordinates, full evidence audit OPEN. No algorithm or experiment redesign authorized.

**Publication boundary:** Q-AHBN2 manuscript submitted to *Journal of Cloud Computing* and **under peer review**; no DOI and not published. This execution record does not change publication status.
