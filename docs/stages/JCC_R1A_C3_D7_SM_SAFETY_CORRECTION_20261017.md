# JCC-R1A-C3-D7-SM — Operational correction candidate (17 October 2026)

## Authority and scope
GitHub code/control repository: wwiras/q-ahbn2. The thesis repository MUM_FIT_ThesisWira is the thesis text authority. Evidence corpus: Google Drive q-ahbn2/output/evidence. Q-AHBN manuscript is **under peer review** at *Journal of Cloud Computing*, not published and without a DOI.

## Safety-only patch
- Topology validator: explicit Gossip seed-42 single-topology canary switch. Default five-treatment order remains unchanged.
- Smoke launcher: fail closed to canary mode; preserve failure evidence and SHA256 manifest on EXIT.
- Experiment runner: track namespace-create attempt, refuse deletion on missing UID/owner, use correctly quoted label lookup; record experiment and cleanup exit statuses independently. Treat Helm uninstall failure, namespace deletion failure, namespace-query failure, and remaining namespace as HOLD.

## Validation and limitations
Before this candidate commit, a separate **local prototype** runner passed 13 isolated mock cases: wrong context, preexisting namespace, namespace-create failure, failed/empty UID, failed/mismatched owner label, failed owner read, Helm install failure, rollout failure, TERM interruption, Helm uninstall failure, and namespace deletion failure. No GKE access was used. **The 13/13 result is NOT claimed as regression verification of the final committed source**, which still requires read-back, Bash/Python syntax checks and rerunning fault injection against exact GitHub checkout. No formal, scientific, or cloud execution is authorized.

## Controlled status
JCC-R1A-C3-D7-SM: HOLD — exact-commit regression outstanding.
Gossip NONFORMAL canary: HOLD 0/1. Remaining four smoke arms: HOLD 0/4. D7-F HOLD 0/25. D8 HOLD.

## Scientific freeze
D7-P2 experimental design, canonical AHBN controller and bounded Q-AHBN2 formulation not reopened. Do not count local mocks as GKE evidence. SIGKILL, connectivity loss, and namespace creation races still require manual post-failure verification.
