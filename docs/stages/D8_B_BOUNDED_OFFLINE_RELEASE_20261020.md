# D8 — Scientific gate decision and bounded D8-B release (20 October 2026)

**Decision:** D8-I1 **CLOSED for current-state file completeness only**; D8-A **PARTIAL**; D8-B **AUTHORIZED FOR BOUNDED OFFLINE VERIFICATION**, not scientifically passed.

## Evidence basis and limitations

Codex execution transcript supplied by the operator reports the following local results; its generated local completion report `docs/stages/D8_I1_D8_A_COMPLETION_20261020.md` was not present on the remote GitHub default branch when this decision was recorded, and its full text was not directly reviewed here. Treat these as *operator-supplied local audit results*, not a fresh independent remote run.

- Revised D8-I1 scanner: 920/920 readable/hashable research files (600 primary + 320 supporting), no missing/read errors/extra research files; 3 Finder `.DS_Store` metadata files excluded. Previously dataless seed44/AHBN `pod_readiness_evidence.txt` was reported hydrated.
- No trusted execution-time checksum baseline exists. Current-state hashes and three matching same-day Google Drive fingerprints do NOT establish unchanged-since-execution historical integrity.
- D8-A local analyzer reportedly reconciled all 25 formal seed-method coordinates, without a primary-metric contradiction. Focused unit tests reported 14/14 passing. Preserve the 25 observations, including unfavourable delivery ratios. Independent scientific closure remains pending.
- Actual controller injection timing reportedly had 0 s planned-grid error and maximum observed injection lateness 7.536 ms. These observations do not demonstrate that peer availability or neighbouring-state timing caused low delivery.
- Recovery accounting remains ambiguous: reportedly 10/100 recovered event observations, including seed44/Gossip observed recovery of 27.44 s despite an 18 s censor horizon, with message anchor reuse. These facts are not inherently proof of an invalid run; verify anchors and event-window definitions before drawing conclusions.
- The latest earlier 919/920 output was not retained before rerunning the audit; historical differences between local scan outputs cannot be exhaustively reconstructed from the preserved summaries.
- Local commits `57511049a` and `5cb688058` were reported reviewed, but were not pushed. `stash@{0}` reportedly remained untouched. This remote decision does not merge, approve or replace any local artifacts.

## Bounded D8-B scope — offline only

1. Reconstruct the exact frozen experiment timing definitions from GitHub source and each archived formal run's manifest, controller events and peer logs: planned/actual injection grid, leave/rejoin times, recovery anchors and censoring rules.
2. Verify the 18 s horizon meaning and how any recovery observation can exceed that threshold (especially seed44/Gossip 27.44 s), checking for cross-event message reuse, measurement lag, incorrect anchors or distinct definitions. Distinguish a metric-definition ambiguity from a scientific protocol violation.
3. Separate Kubernetes pod readiness, gRPC reachability, membership/neighbor-state updates, forwarding opportunity and actual message delivery. Build a timestamp-grounded event sequence for representative low- and high-delivery runs and identify what is observed versus what is inferred.
4. Recheck frozen configuration invariants per seed and method, including method, workload (240 messages at a planned 0.4-second interval), topology and churn offsets [1,26,51,76] seconds, target selection hashes and runtime image identifiers where archived evidence permits verification.
5. Produce a per-run protocol/timing matrix, anomaly and uncertainty register, reproducible offline checks and test logs. Do not silently reinterpret recovery/censor records or change original metrics.
6. Recommend D8-B PASS/PARTIAL/HOLD with explicit evidence paths and residual limitations. Do not close D8-A or promote manuscript claims until material discrepancies are dispositioned.

**Prohibitions:** No GKE operations or reruns; no algorithm/control changes; no alteration or exclusion of original evidence; no automatic Git push of unreviewed local commits; preserve `stash@{0}`; do not overstate causal claims or defend weak claims.

## Repositories and corpus authority
- Thesis control/text: https://github.com/wwiras/MUM_FIT_ThesisWira ; corpus https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR
- RO4 experiment authoritative code: https://github.com/wwiras/q-ahbn2 ; archived results `output/evidence` under https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5
- RO4 manuscript GitHub: https://github.com/wwiras/QAHBN2-Manuscript ; Drive https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj ; PDF https://drive.google.com/file/d/1NZKcOHtP4qW0AImbdvQgl8pqINe04qJ4/view
- Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is under peer review at *Journal of Cloud Computing* (https://link.springer.com/journal/13677). No DOI, acceptance, or publication claimed.

**Next:** local Codex scientific audit D8-B; separately review and stage local completion report, scripts, unit tests and audit outputs before committing/pushing. No manuscript edit authorized.
