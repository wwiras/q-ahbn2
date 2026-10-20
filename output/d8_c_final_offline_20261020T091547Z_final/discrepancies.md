# D8-C offline evidence discrepancies and limitations

- Source-to-report comparisons: 100/100 PASS using absolute tolerance 5e-10; unresolved failed comparisons: 0.
- Original evidence files read and hashed: 100; matched prior D8-A audit hashes: 100; hash mismatches or absent references: 0.
- No trusted execution-time per-file hash baseline is available. Current hashes and matching prior D8-A audit fingerprints do not establish byte identity since experiment execution.
- The local mirror's selected seed-43 root `20261020T035637Z-K5Q-formal/runs/seed43/` contains all five methods and each manifest identifies seed 43. The earlier, distinct root `20261020T023432Z-K5Q-formal` is outside the selected matrix and was not deleted, renamed, or reclassified.
- Missing/unreadable required files: none among the 25 original metrics, manifests, topologies, or logs; all were opened and parsed.
- Scientific/protocol violations: none confirmed in the selected 25-run local evidence set. Unexplained source-to-report mismatches: 0. This is a local-mirror finding; no live cluster or remote Drive operation was performed.
- D8-B recovery diagnostics remain limited: 18 seconds is the post-workload settle interval rather than an event-relative censoring window; one recovered record exceeds 18 seconds and two event observations reuse a message anchor. Recovery is secondary and not used in these four metrics.
- Statistical reports retain n=5 seeds, unadjusted two-sided Student-t intervals (df=4), no multiplicity adjustment, and no causal or overall-superiority claim.
- D8-A and D8-B remain PARTIAL. No run is excluded for low delivery, and no manuscript or thesis content is modified.
- Existing statistical report and per-seed tables match at displayed precision.
