# JCC-R1A-C3-D7-SM-REMAINING-P1-SAFETY — Exact-source local regression

## Decision
**OPEN — tests pending; LIVE RELEASE HOLD.** Existing positive topology contract 4/4 and negative contract 3/3 PASS from researcher terminal on commit `7df4a240b574ba5c495ecc07a2b6fd52ebfb865b`. Bash and Python syntax PASS; authorization rejection PASS. No four-method GKE smoke executed.

## Test provenance and method
Use the committed `gke/scripts/test_d7_p4_cleanup.py`, which copies the **actual** `gke/scripts/run_k7_experiment.sh` into a temporary sandbox and replaces `kubectl`, `helm`, and Python commands with fake executables. This prevents real cloud mutations. Five mock cases currently implemented: install failure, rollout failure, delete failure, pre-existing namespace, wrong cluster context. Record test script SHA, runner SHA, commit and `output/evidence/*-D7-P4-cleanup-mock` evidence. This is a regression of the **shared runner**, not a complete four-method launcher mock.

## P1 safety checks required before P2 release
1. Execute existing mock cleanup tests, verify 5/5, inspect JSON and SHA256SUMS.
2. Verify the new four-method launcher refuses execution when `SMOKE_REMAINING_AUTHORIZED` is unset (already PASS); confirm it never reuses the Gossip authorization.
3. Extend isolated mocks to test namespace UID mismatch and owner-label mismatch, signal INT/TERM cleanup, and stop-on-first-failure/no subsequent method. SIGKILL remains inherently uncatchable; document limitation.
4. Verify partial evidence is preserved and `smoke_exit_status.txt`/SHA256SUMS are emitted on normal nonzero exits, and that topology.json is restored. Verify cleanup `PASS` before proceeding to the next method.
5. Negative topology tests for wrong seed and wrong number of paths (3 already covered; 5 outstanding). Ensure launcher only uses four ordered seed42 topologies.
6. Confirm clean Git tree, exact remote main, pinned image, expected GKE context, and all four namespace absence checks fail closed before any namespace creation.
7. Record test evidence in canonical Drive, then separately review P2 authorization.

## Source boundary
- Frozen AHBN/Q-AHBN2 scientific logic and shared runner unchanged during this gate.
- New launcher: `gke/scripts/run_d7_smoke_remaining.sh`; subset validator: `gke/app/k7_exp11_tools.py`.
- Gossip live canary PASS 1/1: https://drive.google.com/drive/folders/1drKb5LsU9CxGAeB34r-TvZrNiu-c5CN_
- Remaining four smoke 0/4 HOLD; D7-F 0/25 HOLD; D8 HOLD.
- Q-AHBN manuscript remains **under peer review at Journal of Cloud Computing**, unpublished, no DOI. No NONFORMAL run establishes scientific comparative results.

## 2026-10-17 extended mock preparation
Researcher confirmed the corrected baseline **5/5 PASS** on commit `c8c1fd1207190f8bd4cbf288dc019930236e50e9`, with local evidence `output/evidence/20261017T121948Z-D7-P4-cleanup-mock`. Earlier 2/5 was a mock incompatibility with production `go-template` label query; production runner remained unchanged.

Prepared four additional local-only cases in `gke/scripts/test_d7_p4_cleanup.py`: UID substitution, owner-label substitution, SIGTERM and SIGINT during mocked rollout. Each run also checks essential local evidence artifacts. Mock subprocesses use temporary sandboxes and fake `kubectl`/`helm`; no cloud deployment. **These four additional tests have not yet been executed/verified by the researcher.** The new matrix is expected 9/9; this is a target, not an observed result.

The original five-case PASS remains valid independently, but the new exact-source runner/harness matrix must be rerun. Launcher-level stop-on-first-failure, topology restoration, SHA256SUMS on abnormal exit, correct placement of RESULT_ROOT, and remaining negative contract checks are still pending. P1-SAFETY remains OPEN / HOLD. No algorithm, shared production runner or manuscript results were changed.

## 2026-10-17 researcher execution — extended mock PASS
Researcher terminal after fast-forward to `f05fab6ca607c0618f3a5f9af75903404bf75852`:
- `python3 -m py_compile gke/scripts/test_d7_p4_cleanup.py` — no syntax error.
- `python3 gke/scripts/test_d7_p4_cleanup.py` — **9/9 PASS**, decision `MOCK PASS / LIVE GKE HOLD`.
- Evidence: `output/evidence/20261017T122648Z-D7-P4-cleanup-mock` (researcher local/Drive-sync path). Per-case JSON and checksum validation not independently read in this update.
- Coverage: original five shared-runner failure checks; UID and owner-label mismatch; SIGTERM and SIGINT; required evidence-file existence assertions.
- This is **shared runner mock verification**, not proof of four-method launcher stop-on-first-failure or live GKE safety.
- **Next:** exact-source four-method launcher mock: fail-stop, topology restoration, checksum integrity, no subsequent methods, authorization and environment fail-closed. Then P2 review. **P1-SAFETY remains OPEN / LIVE HOLD.**

## 2026-10-17 P1-LAUNCHER controlled preparation
The researcher-confirmed shared-runner safety suite remains **9/9 PASS** (local `output/evidence/20261017T122648Z-D7-P4-cleanup-mock`). GitHub now contains `gke/scripts/test_d7_smoke_remaining_launcher.py`, an additional **exact-source launcher** regression that copies the committed launcher into isolated temporary directories with fake kubectl, helm, git, Python and experiment runner. It tests **11 mock cases**: seven admission rejections (missing authorization, legacy authorization, context, dirty git, remote mismatch, preexisting namespace, image mismatch), three first-method failures (runner failure, cleanup HOLD, validation failure), and one four-method success path. Assertions check no unintended next method, evidence SHA256SUMS, `smoke_exit_status.txt`, and topology restoration. This new suite is **PREPARED ONLY; not yet executed or independently verified**. It does not replace the already-passed shared-runner mocks. P1-SAFETY and live GKE remain HOLD.

Next researcher command after `git fetch origin main && git merge --ff-only origin/main`: `python3 -m py_compile gke/scripts/test_d7_smoke_remaining_launcher.py && python3 gke/scripts/test_d7_smoke_remaining_launcher.py`. Inspect `output/evidence/JCC-R1A-C3-D7-SM-P1-LAUNCHER_<MYT timestamp>/launcher_mock.json`, SHA256SUMS and any failing case. Do not set `SMOKE_REMAINING_AUTHORIZED` on the real launcher. The pending full launcher audit also includes reject wrong seed/five-topology count and RESULT_ROOT restriction before release.

## 2026-10-17 P1-LAUNCHER first execution and mock correction
Researcher ran Python compile and the isolated launcher test at GitHub `bdaf495`: **7/11 PASS, MOCK FAIL / HOLD**, local evidence `output/evidence/JCC-R1A-C3-D7-SM-P1-LAUNCHER_20261017205621`. Four execution cases (`runner_failure`, `cleanup_hold`, `validation_failure`, `success_all`) all stopped at mock contract exit **86**, with no method launched; topology restoration and checksum verification were true. Inspection of committed mock revealed escaped Bash parameter expansion `\${m}` (literal) instead of `${m}` (expanded) in the fake contract validator, also affecting fake-runner variable expansions. Narrow correction applied **only** to `gke/scripts/test_d7_smoke_remaining_launcher.py` at commit `a85c04616638f3677378ab0af222f217e63aae36`. No production launcher or science changed. **Rerun pending**; do not claim 11/11. Live GKE HOLD remains.
