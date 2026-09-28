# S04 — Regression / Parity

**Status:** PASS / CLOSED — S05 NEXT

Entry requirement satisfied: S03 Development is PASS / CLOSED.

Purpose: verify regression safety, canonical AHBN immutability, deterministic contract behavior, and required ControlSim/cross-environment logical parity before broader validation.

No formal dynamic experiment was authorized or performed in S04.

---

## S04.1 — Regression-Safety and Canonical-Immutability Audit — 2026-09-28

**Status:** PASS / COMPLETE.

Evidence:
- S03.3 frozen-contract regression verification completed without an identified contract contradiction;
- S03.2A deterministic trace/no-side-effect verification passed 3/3;
- current Q-AHBN2 learner, transition bookkeeping, adapter, event bridge, and Learning Validation contract remain aligned to the frozen S02 design;
- canonical AHBN remains an external pinned dependency at `wwiras/ahbn@936a79480bc1252c79b6ee01f65c88c740af2844`;
- no canonical-AHBN source file was modified by S03/S04 work.

Scientific decision:
- no regression-safety defect requiring redesign or parameter reopening was identified;
- no new experiment is justified by this audit.

---

## S04.2 — Deterministic Logical-Contract Parity Audit — 2026-09-28

**Status:** PASS / COMPLETE.

The source-authority register explicitly distinguishes:
- canonical AHBN cross-platform logical parity, which has already been established for equivalent normalized inputs; and
- historical Q-AHBN ControlSim↔GKE RL parity, which was **not** established and must not be inherited.

The frozen Q-AHBN2 logical learning contract is platform-independent at the design boundary:

```text
environment-specific acquisition
        ↓
canonical logical d,l,u,c
        ↓
immutable canonical AHBN
        ↓
(mode_AHBN, k_AHBN)
        ↓
Q-AHBN2 frozen state/action/refinement
        ↓
(mode_Q, k_Q)
        ↓
environment-specific eligible-target realization
        ↓
direct NEW / DUPLICATE / FAILED attribution
        ↓
frozen reward / transition / Q update
```

ControlSim currently implements this contract.

Kubernetes Q-AHBN2 empirical implementation parity is **not** claimed by S04 because a new Q-AHBN2 Kubernetes implementation has not yet been established as validated evidence. This is not a parity failure: it is an explicit scope boundary that prevents the historical GKE Q-AHBN implementation from being misrepresented as Q-AHBN2.

Therefore S04 parity means:
1. canonical AHBN parity remains inherited from its frozen reconciled authorities;
2. Q-AHBN2's logical state/action/reward/transition contract is fixed independently of environment-specific sensor and transport plumbing;
3. empirical Q-AHBN2 Kubernetes parity remains a later implementation/validation obligation and cannot be fabricated from historical Q-AHBN evidence.

**Scientific classification:** PASS for required logical-contract parity and scope control; no claim of empirical ControlSim↔Kubernetes Q-AHBN2 runtime parity.

---

## S04 Closure Decision — 2026-09-28

**Result:** PASS / CLOSED.

Closure basis:
- S03 entry condition satisfied;
- regression-safety audit: PASS;
- canonical-AHBN immutability: PASS;
- deterministic frozen-contract behavior: PASS;
- logical cross-environment contract reconciliation: PASS;
- historical RL parity is explicitly excluded rather than silently inherited;
- no formal experiment performed.

**Limitation retained:** empirical Kubernetes Q-AHBN2 implementation/runtime parity remains unestablished and must be validated when the Kubernetes Q-AHBN2 implementation exists. This limitation does not invalidate the ControlSim Learning Validation evidence or require reopening S02/S03.

**Next permitted stage:** `S05 — RL Validation`.
