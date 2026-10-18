# D7-F — Original-implementation evidence decision (2026-10-18)

**Status: HISTORICAL BASE CONFIG PASS / ARCHIVE EVIDENCE REVIEW PASS / ORIGINAL FORMAL D7-F 0/25 NOT EXECUTED / FORMAL GKE RUN DECISION PENDING.**

## Researcher direction
Follow earlier AHBN2-GKE methodology; do not interpret low delivery as automatically invalid or force recovery implementation. CAP5 recovery investigation closed for interpretation only; proposed recovery changes are future work for thesis and papers. Frozen AHBN and Q-AHBN2 algorithm unchanged; no additional recovery gates or changes to existing evidence.

## Direct comparisons
RO3 `ahbn2_gke/experiments/k7_exp11.yaml` and RO4 `q-ahbn2/gke/experiments/k5_q_formal.yaml` match for N20 BA m2, 4 clusters, source 0, 18 s settling, churn event count 4, trigger 1.0, intervalSec 1.2, planned absolute offsets [1,26,51,76] s, 240 messages at 0.4 s, common epoch, target selection version and S5. Q-AHBN2 generator `gke/app/k7_exp11_tools.py` explicitly declares seeds 42–46, methods gossip/structured/dcsoc/ahbn/qahbn2, fixed targets 0,5,10,15, SHA256 canonical target-selection artifact hash and schedule grid validation. Historical RO3 K7 v2 documentation preregisters identical target identities and seed policy, with per-seed target hashes; therefore **code-level coordinate policy match**. This is not an independent regenerated per-seed hash parity check.

## Original Drive formal archives checked
- RO3 historical `ahbn2_gke/outputs/k7_exp11_formal-20260907T022419Z` (Drive folder 1PpdQYA3dOFr3pNnQbGq_QGsUpBIq6nok): contains runs/seed42–seed46, target-selection/seed42–seed46, results aggregation, image and digest, git commit and terminal log. Historical terminal starts with 125 local tests passing; this does not alone certify every formal run. Evidence physically present.
- RO4 `q-ahbn2/output/evidence/q-ahbn-gke-29092026155123-k5q-formal` (Drive folder 1O-f8Gv8RqMhWxtHKbAILcVmFHIZ0MLIM): `terminal.log` reads exactly `ERROR: working tree must be clean`; `git_commit.txt` reads `52d65988850b6e4a68e99cdecb09fe0f0e90d677`; `runs`, `raw`, `generated`, `configs` and `target-selection` are empty. This archive is an **aborted launch**, not completed D7-F experiment results. Do not count it as formal success or scientifically valid repetition.
- Later RO4 `D7-SM` multi-method seed42 and `P3G` folders are **nonformal diagnostic canaries**, not part of completed D7-F 25-run formal set; retain measured low delivery without mutation or mislabelling.
- Repository's prior P3 audit supports a neighbor-exclusion timing path but leaves exclusive causal attribution unresolved. Do not claim sole timing cause, repaired recovery or invalid algorithm.

## Exact-run distinction and decision
Base configuration and frozen target-policy parity **PASS**. Full generated-hash readback and runtime image parity **NOT COMPLETE**. In particular historical RO3 files do **not** substitute for missing RO4 actual experiments. **No evidence in the reviewed original RO4 formal archive completes D7-F**. Thus the existing archive is **INSUFFICIENT** to declare 25 formal runs complete, independent of whether its future delivery ratios prove high or low.

**Recommended subsequent action:** retain original Q-AHBN2 source and recovery feature OFF, correct the separate operational cleanliness/admission issue without algorithm changes, then run the formally preregistered five methods × five seeds **only on explicit researcher authorization** and with fresh source/image digest, exact-run manifest, target hashes, capacity and cleanup checks. Do not change churn timing, workload, target selection, denominators or thresholds post hoc. D8 waits on D7-F formal evidence. The outcome is not a demand to rerun because delivery was low: the archived formal launch never ran. No new GKE action performed by this gate.

## Research reporting
Low delivery during churn may be consistent with scheduled failure/rejoin and delayed observer eligibility; neither algorithm defect nor sole scheduling cause proven. Report measured performance candidly. Rejoin/neighbor availability improvements can be future work. Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* remains under peer review at Journal of Cloud Computing, unpublished, no DOI. Keep original evidence and GitHub control records.
