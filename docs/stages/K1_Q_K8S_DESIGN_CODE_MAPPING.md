# K1-Q — Q-AHBN2 GKE Design-to-Code Mapping

**Status:** NEXT / RELEASED — MAPPING / READ-ONLY AUDIT FIRST

## Objective
Map the frozen Q-AHBN2 state, action, reward, transition, and AHBN-refinement semantics into the Kubernetes event path.

## Boundary
No learner redesign. Environment-specific observation acquisition is permitted only where already compatible with the canonical AHBN deployment contract.


## Release basis
Released after K0-Q PASS / CLOSED on 2026-09-29.

## Inheritance constraint
K1-Q must start from the pinned `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` implementation. Gossip, Structured, DC-SoC and canonical AHBN are inherited deployment baselines and are not to be recreated in `q-ahbn2`.

The purpose of K1-Q is to map the frozen Q-AHBN2 learning/refinement contract onto the existing Kubernetes event path and define the smallest safe patch surface in `q-ahbn2`. Historical `q-ahbn_gke` may be consulted for integration context only and cannot override the frozen Q-AHBN2 contract.

## Next permitted task
Perform exact design-to-code mapping only: inherited files/event boundaries, Q-AHBN2 insertion point, state construction, AHBN proposal capture, bounded action refinement, eligible-target realization, attributed NEW/DUPLICATE/FAILED outcomes, reward closure, next-state bookkeeping, learning trace/provenance, and required regression/parity tests. No implementation change until the mapping is complete and accepted.
