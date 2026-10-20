# D8-I1 and D8-A — Parallel validation decision (20 October 2026)

**Status: D8-I1 HOLD for administrative closure; D8-A OPEN for offline scientific reconciliation; D8-B NOT RELEASED.** This record is a reconciliation decision, not evidence that the missing local scan or 25-run content verification was executed.

## Source authority
- Authoritative experimental code and control text: https://github.com/wwiras/q-ahbn2
- Canonical experimental evidence: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5 (output/evidence)
- Thesis control/text repository: https://github.com/wwiras/MUM_FIT_ThesisWira
- Thesis corpus: https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR
- RO4 manuscript repository: https://github.com/wwiras/QAHBN2-Manuscript
- RO4 manuscript corpus: https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj

## Audit observations and unresolved differences
1. User-reported latest **local** audit: 920 inventoried research files (600 expected direct run files + 320 discovered supporting artifacts); 919 hashed (599 primary, 320 support); `MATCH=0`, `MISMATCH=0`, `BASELINE_UNAVAILABLE=919`, `MISSING=0`, `READ_ERROR=1`, `EXTRA=0`; 10 focused tests reported passing. These are reported observations, **not independently re-executed or verified by this remote record**.
2. Outstanding item: `20261020T041621Z-K5Q-formal/runs/seed44/ahbn/pod_readiness_evidence.txt`, recorded as macOS `compressed,dataless`. Hydration must be verified locally without replacing or modifying the original file. The local rerun is `venv/bin/python gke/scripts/audit_d8_i1_sha256.py` from the `q-ahbn2` repository root. Retain timestamped `output/d8_integrity/` outputs and source identifiers.
3. Existing GitHub `D8_I1_SHA256_AUDIT_REPORT_20261020.md` records an earlier operator-supplied 2026-10-20 07:10:44 UTC post-hydration scan that reportedly hashed 920/920 research files, but counted three `.DS_Store` files as `EXTRA`. The revised metadata classifier's successful full local run was **not** established in that record. The latest user report differs. Compare actual source revision, execution timestamps, summary JSON and append-only logs to determine the authoritative latest execution. Do not presume that either scan proves historical integrity.
4. No trusted execution-time per-file checksums have been identified. Current-state SHA256 hashes are not proof of unchanged bytes since formal experiment execution. The three matching same-day Drive fingerprints are supplementary only.
5. User-reported local commits `57511049a27db0034c5fefa29d5daef1e6207dc5` and `5cb6880585790915fee5c5301596f68976e9dd47` remain unpushed. A GitHub lookup of the second SHA returned no commit. Do not claim to have reviewed its diff or merged its content. Inspect and reconcile local changes and preserve `stash@{0}` before any push.

## D8-A release scope
Proceed in parallel with offline verification of 25 formal coordinates (seeds 42–46 × Gossip, Structured, DC-SoC, AHBN, Q-AHBN2): manifests, metrics, exit/cleanup/validator status, controller and peer logs, topology/target selection, workload, recorded commit and image identifiers. Produce a per-run cross-check matrix and discrepancy register. Preserve low-delivery outcomes without exclusions; distinguish file-access failure, scientific protocol violation, observation, and causal attribution. Preserve all raw evidence; no GKE reruns or algorithm changes.

D8-A PASS requires independent content-level reconciliation and resolution or explicit scientific disposition of material discrepancies. Prior inventory and validator PASS are insufficient. D8-B timing/protocol conclusions remain a separate subsequent gate.

Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is **under peer review** at *Journal of Cloud Computing*, without DOI; not described as accepted or published. No manuscript claims are changed here.
