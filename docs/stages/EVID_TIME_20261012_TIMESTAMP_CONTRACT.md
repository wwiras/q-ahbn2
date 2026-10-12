# EVID-TIME-20261012 — Prospective Evidence Folder Timestamp Gate

## Objective
Adopt a consistent, human-readable evidence folder timestamp for future AHBN thesis Chapters 5–7 and Q-AHBN2 actions.

## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md` §11 (operating contract).
- `docs/03_EXPERIMENT_CONTRACT.md` §9 (generated-output provenance).
- Researcher instruction 2026-10-12; pinned science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.
- Canonical Q-AHBN2 Google Drive folder ID `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`.

## Scope / decision
**Forward-only administrative naming change.** New evidence folders MUST use `YYYYMMDDHHmmss` (14 digits, local Malaysia time, MYT UTC+08:00), in the pre-existing designated evidence root. Prefixes and the existing output/evidence/ hierarchy are preserved.

Examples (illustrative, not actual artifacts):
- `output/evidence/q-ahbn-20261012205630-exp10-formal/`
- `output/evidence/q-ahbn-gke-20261012205630-exp13-formal/`
- `C05-PH4_20261012205630/` under the established Chapter 5 evidence root.

## Hard boundaries
- No retroactive renaming, deletion, movement, replacement, or re-dating of existing evidence.
- Existing registered evidence identifiers, manifests, timestamps, historical paths, and Drive IDs remain valid.
- Legacy `DDMMYYYYHHmmss` naming is historical and superseded **only for future folders**.
- No scientific code, settings, seeds, data, inference, claims, frozen experiment contract, manuscript, or pinned baseline is changed.
- S20-18 and scientific stages are not reopened.

## Gate checks for every future folder
1. Identify the originating stage/gate and designated evidence authority.
2. Derive actual folder-creation timestamp in MYT; verify exact 14-digit `YYYYMMDDHHmmss` and 24-hour time.
3. Confirm a unique directory name; do not overwrite or reuse a previous directory.
4. Preserve `RUN.md`/`manifest.json` metadata and time zone as applicable.
5. Record the exact created path/Drive ID in the stage/control record; perform normal completeness, validity, deliberate evidence preservation, and readback verification.
6. Declare naming compliance separately from scientific admissibility.

## Actions performed
- Updated Master §11 to specify forward-only timestamp contract and gate.
- Updated Experiment Contract §9 and both prospective example run paths.
- Registered this stage document as the persistent administrative gate record.
- No experiment execution or evidence-folder relocation was authorized.

## Verification
- Check latest GitHub `main` readback of Master, Experiment Contract, and this record.
- Check scientific baseline unchanged and stage progression unaffected.
- Check future-only semantics and historical evidence protection.

## Result
Administrative naming contract adopted, subject to post-write GitHub readback.

## Scientific decision
N/A; administrative control only.

## Issues / limitations
Direct researcher-local filesystem modification is not available through the connector environment. All historical names remain unchanged.

## Next permitted task
Continue the existing controlled scientific/manuscript workflow; apply this pre-creation naming gate to each future evidence folder.

## Status
PASS / ADMINISTRATIVE CONTRACT (subject to final readback)
