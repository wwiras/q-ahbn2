# D8 final scientific disposition — 20 October 2026

**Decision: BOUNDED SCIENTIFIC CLOSURE RECOMMENDED / accepted with explicit limitations.** This is a scientific interpretation decision for the frozen 25-run experiment, not a claim of complete historical byte-level attestation, causal recovery verification, manuscript acceptance, or universal superiority. D8-A, D8-B and D8-C retain their individual recorded PARTIAL labels; no retroactive PASS is asserted.

## Basis
- Frozen methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2; five blocked seeds 42–46, 25 method-seed coordinates, four frozen primary endpoints.
- Local Codex audit transcript supplied by operator reports 25/25 original run identities, 100/100 primary metric matches within 5e-10, 100/100 current SHA256 values matching earlier D8-A fingerprints, statistical summary and paired-interval reproduction, and resolved folder navigation. It reports local commit `cd06981efe7ef974b83e21e449c29297d1e05214`.
- **Remote verification boundary:** On 20 October 2026, the GitHub connector for `wwiras/q-ahbn2` did not find that Codex-reported commit or its final D8-C files on the default branch (latest visible commit `53d34eb5855cc46958c21cbbca9b7366175c04c9`). Accordingly the supplied local transcript is evidence *reported by local Codex*, not represented here as verified remotely merged. Preserve the local audit outputs and ensure the worktree commit is pushed/synced before citing its remote hash as repository provenance.
- Independently available remote statistical recalculation and prior D8-B decision support the statistical values and identified limitations.

## Decision for D8-A, D8-B and D8-C
- **D8-A — ACCEPT WITH DISCLOSURE, recorded status PARTIAL:** Matching current archived hashes to prior audit fingerprints supports consistency from that prior audit forward but does not establish unchanged bytes since GKE execution; no execution-time trusted hash baseline is available. This is not positive evidence of tampering or invalid results.
- **D8-B — ACCEPT PRIMARY-ENDPOINT INTERPRETATION WITH DISCLOSURE, recorded status PARTIAL:** Injection-grid consistency and 25-run protocol evidence are compatible with the frozen implementation. The 18-second settling setting is run-level, not a per-churn hard recovery deadline. Recovery observations may span intervening churn events and have unequal post-event injection opportunities. The report lacks cluster-wide neighbour convergence measurements. Recovery is secondary diagnostic evidence and does not invalidate the four primary dissemination endpoints, but must not be promoted to an isolated recovery-time or causal neighbour-state claim.
- **D8-C — ACCEPT COMPUTATIONAL REPRODUCIBILITY WITH DISCLOSURE, recorded status PARTIAL pending remote source-artifact sync:** Local Codex reports 25/25 original pairs and 100/100 source metrics reconciled, 100 prior-audit fingerprint matches, no material statistical differences. Full historical byte attestation is unavailable. Remote-independent reproduction from the secondary reconciliation dataset agrees numerically.
- **Final D8 — BOUNDED SCIENTIFIC CLOSURE:** Existing data are adequate for carefully framed, scenario-specific descriptive and prespecified paired inferences. Do not describe this disposition as complete protocol/causal/historical-integrity certification. No additional GKE experiment or algorithm modification is required merely to address these limitations.

## Permitted findings from original four endpoints
| Method | Five-seed mean delivery ratio | Propagation delay (s) | Duplicates | Total forwards |
|---|---:|---:|---:|---:|
| Gossip | 0.876779 | 0.089328 | 3479.2 | 3958.4 |
| Structured | 0.081396 | 0.003677 | 0 | 152 |
| DC-SoC | 0.407186 | 0.093072 | 0 | 1710.6 |
| AHBN | 0.200718 | 0.017040 | 341.6 | 726 |
| Q-AHBN2 | 0.411666 | 0.037168 | 608.0 | 1738.2 |

Prespecified within-seed Q-AHBN2−AHBN difference (n=5): delivery +0.210948, two-sided **unadjusted** 95% paired Student-t CI [+0.025075,+0.396821]; delay +0.020129 s [+.002483,+.037774]; duplicates +266.4 [+47.7,+485.1]; total forwards +1012.2 [+121.3,+1903.1]. Delivery improved in four seeds and declined in one. Gossip had higher average delivery (0.876779) than Q-AHBN2; DC-SoC was highly heterogeneous across seeds. No claim of overall superiority or robustness over all environments is supported.

## Mandatory scientific disclosure / claim boundaries
1. Exactly five independent blocked seeds in one frozen BA(m=2), N=20 GKE scenario, with the specified 240-message injection and four churn cycles; do not generalize beyond tested conditions.
2. Multiple outcomes/contrasts; Student-t intervals are unadjusted. Avoid blanket confirmatory significance assertions.
3. Report all four primary endpoints and all five baselines without exclusions or performance-conditioned selections; propagate adverse forwarding/delay/duplication results.
4. Propagation delay is conditioned on successfully delivered messages where defined, so comparisons can reflect different delivered subsets.
5. Unverified execution-time hash provenance and local-to-GitHub synchronization must be stated accurately; do not convert a prior-audit hash match into an execution-time authenticity claim.
6. Recovery timing/neighbor-membership convergence cannot be causally inferred from the available event metrics. Do not rewrite original recovery fields or describe 18 s as a hard per-event bound.
7. GKE results constitute implementation validation in the tested environment, **not** direct numerical replication of ControlSim results.

## Action and manuscript boundary
No new GKE execution, algorithm tuning or changes to raw evidence. Preserve the local Codex audit outputs and sync their committed decision/evidence to GitHub before treating the local hash as remotely accessible. For thesis Chapter 6 and the RO4 manuscript, incorporate these bounded results only as an explicitly authorized separate editorial action; avoid claim inflation. The paper *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is **under peer review** at *Journal of Cloud Computing*, **no DOI**, not accepted or published. No thesis or manuscript files are modified by this decision.

Source: `docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md`, `D8_B_OFFLINE_REVIEW_DECISION_20261020.md`, `D8_C_INDEPENDENT_STATISTICAL_RECALCULATION_20261020.md`, local Codex D8-C final audit transcript submitted on 20 October 2026.
