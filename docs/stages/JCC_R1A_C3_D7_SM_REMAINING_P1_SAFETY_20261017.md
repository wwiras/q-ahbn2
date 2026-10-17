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
