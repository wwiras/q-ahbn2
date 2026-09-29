"""Pure integration helpers for the inherited ahbn2_gke runtime.

These helpers deliberately do not import Kubernetes, gRPC, canonical AHBN code,
or comparator implementations. The inherited runtime supplies the canonical
post-update AHBN state, the final S5 proposal, and eligible-target semantics.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

from qahbn2.kubernetes_adapter import KubernetesQAHBN2Adapter, KubernetesQDecision


@dataclass(frozen=True)
class RealizedQDecision:
    q: KubernetesQDecision
    eligible_targets: tuple[int, ...]
    realized_targets: tuple[int, ...]


def realize_inherited_targets(
    *,
    q: KubernetesQDecision,
    sender_id: int,
    gossip_eligible: Sequence[int],
    structured_selector: Callable[[int, int], Sequence[int]],
    rng_sample: Callable[[Sequence[int], int], Sequence[int]],
) -> RealizedQDecision:
    """Realize the Q-refined request using inherited GKE selection semantics."""
    if q.mode_q == "structured":
        eligible = tuple(dict.fromkeys(int(x) for x in gossip_eligible))
        # The caller supplies the inherited structured selector; this helper
        # neither reconstructs nor changes cluster semantics.
        targets = tuple(int(x) for x in structured_selector(sender_id, q.k_q))
        return RealizedQDecision(q=q, eligible_targets=eligible, realized_targets=targets)

    if q.mode_q != "gossip":
        raise ValueError(f"unsupported refined mode: {q.mode_q}")

    eligible = tuple(dict.fromkeys(int(x) for x in gossip_eligible))
    k = min(max(0, int(q.k_q)), len(eligible))
    targets = tuple(int(x) for x in (rng_sample(eligible, k) if k else ()))
    return RealizedQDecision(q=q, eligible_targets=eligible, realized_targets=targets)


def register_realized_targets(
    adapter: KubernetesQAHBN2Adapter, realized: RealizedQDecision
) -> None:
    adapter.register_targets(realized.q.decision_id, realized.realized_targets)
