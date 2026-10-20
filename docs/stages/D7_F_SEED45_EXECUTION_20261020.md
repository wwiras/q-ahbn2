# D7-F — Seed 45 Formal GKE Execution (2026-10-20)

**Status:** EXECUTION PASS (5/5 seed45 methods); each K7 result validator PASS. **Cumulative: 20/25 method×seed execution coordinates** (seeds 42–45). Full archive integrity, image parity and independent scientific validity audit OPEN.

## Evidence provenance
- User-supplied terminal transcript ends `K5-Q FORMAL SEED BATCH PASS seed=45`.
- Drive-synced evidence root: `output/evidence/20261020T043745Z-K5Q-formal/`. This timestamped root is distinct from seeds42–44. The 25 generated configuration files are not 25 completed experiments.
- `FORMAL_SEED=45`, `P3G_RECOVERY_ENABLED=0`. All five methods report 20 pods ready, controller job completed and four churn events. No protocol changes were requested.

## Reported results
| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards | K7 validator |
|---|---:|---:|---:|---:|---|
| Gossip | 0.8859172586711241 | 0.1377124895652135 | 5222 | 4014 | PASS |
| Structured | 0.0812565445026178 | 0.002667588988939921 | 0 | 152 | PASS |
| DC-SoC | 0.8865828092243186 | 0.15969420472780863 | 0 | 4008 | PASS |
| AHBN | 0.18777475402972577 | 0.013391058643658955 | 249 | 666 | PASS |
| Q-AHBN2 | 0.5417451349654739 | 0.049497548739115396 | 776 | 2362 | PASS |

Seed45 Q-AHBN2 minus AHBN delivery = +0.3539703809357481 (35.40 percentage points), with greater duplicates and propagation delay. Single-seed result, not overall superiority. DC-SoC again has high delivery (88.66%), contrasting with low delivery in seeds42/44; retain all observations.

## Recovery observations
- Gossip: 2 recovered events (0.3485 s, 3.2010 s), 2 censored at 18 s.
- Structured: 1 recovered event (0.0897 s), 3 censored at 18 s.
- DC-SoC, AHBN and Q-AHBN2: 0 recovered events, all 4 censored at 18 s.
- Infrastructure readiness is not equivalent to message-delivery recovery; do not infer algorithmic recovery failure solely from censoring.

## Outstanding verification
- Independently inspect per-run manifest, exit and cleanup records and namespace absence for seed45.
- Verify per-pod runtime digest against pinned image, complete artifact checksums, controller and churn traces, frozen workload conditions, and recovery-time definition.
- Finish seed46 then conduct full K6/D8 paired statistical and validity audits, including the previously flagged seed44 recovery event longer than the 18 s censoring value.

**Decision:** D7-F seed45 execution PASS; 20/25 completed; full evidence audit OPEN. No parameter changes or method exclusions authorized. Manuscript remains under peer review at *Journal of Cloud Computing*, with no DOI or publication claim.
