# P3G — Implementation and Verification Status (2026-10-18)

**Status: IMPLEMENTED CANDIDATE / VERIFICATION HOLD / NOT PASS.**

User approved P3F-M1 design review at `ba11dc1d5037b4a88fa3b38f1d2697d2d17ca274`.

## Changes committed
- `gke/app/recovery_availability.py`: bounded GetStatus transport recovery, per-neighbor epoch/lock, one in-flight probe, exactly-once transition observations, feature disabled by default.
- `gke/app/peer.py`: replaces direct unavailable-set mutations with helper and connects DC-SoC rejoin notification to a recovery probe; 2-second status timeout.
- `tests/test_p3g_recovery.py`: T01–T18 scenario-labelled offline tests (initial helper-level coverage; some cases are proxy checks, not full integrated PeerState assertions).

Latest code/test commit: `c9d7c0256b4823b34071842622fc09d1f5752d1b`.

## Mandatory unresolved verification
1. Tests were **not executed**: remote GitHub checkout from this environment failed due to DNS/network restriction. No fabricated PASS counts, logs, or SHA256.
2. T01–T18 are currently **helper-focused**, not yet complete integrated `PeerState` + fake gRPC assertions. Particularly T07–T10, T12, T16 and T18 need integrated metric/controller/forwarding fixtures.
3. Rejoin trigger currently wired through DC-SoC maintenance; applicability to AHBN and Q-AHBN2 rejoin pathways requires integration audit. Do not claim cross-strategy recovery.
4. Review lock order, duplicate ACK/failure races, late response ordering, and feature-flag rollback under actual runtime.
5. Run `python -m py_compile`, `PYTHONPATH=gke/app python -m unittest tests.test_p3g_recovery -v`, existing frozen-controller parity tests, capture full logs and SHA256 at pinned commit.

**Decision:** P3G HOLD, D7-P3 onward HOLD. No GKE or formal runs released. Q-AHBN manuscript remains under peer review at Journal of Cloud Computing; not published, no DOI.
