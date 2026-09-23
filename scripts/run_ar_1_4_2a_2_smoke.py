"""AR-1.4.2A.2 one-seed end-to-end ControlSim smoke harness.

This is a bounded executable harness using the frozen Q-AHBN2 components.  It
models the ControlSim event boundary explicitly: a canonical AHBN proposal is
passed in unchanged, Q-AHBN2 refines it, direct attempts resolve through
receiver seen-state semantics, and the originating transition receives the
resulting NEW/DUPLICATE/FAILED counts.

It is not an experimental result and must not be used for gamma comparison.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Set

from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter
from qahbn2.event_bridge import ControlSimEventBridge, DirectAttemptOutcome
from qahbn2.learning import QAHBN2Learner


SMOKE_SEED = 42
SMOKE_GAMMA = 0.80  # fixture only; not a selected scientific value


@dataclass
class MiniControlSim:
    """Small deterministic event harness for integration proof, not evaluation."""

    seen: Dict[int, Set[str]] = field(
        default_factory=lambda: {0: set(), 1: set(), 2: set(), 3: set()}
    )

    def attempt(self, src: int, dst: int, message_id: str) -> DirectAttemptOutcome:
        if dst not in self.seen:
            return DirectAttemptOutcome(dst, "FAILED")
        if message_id in self.seen[dst]:
            return DirectAttemptOutcome(dst, "DUPLICATE")
        self.seen[dst].add(message_id)
        return DirectAttemptOutcome(dst, "NEW")


def run_smoke() -> dict:
    learner = QAHBN2Learner(
        alpha=0.25, gamma=SMOKE_GAMMA, epsilon=0.0, seed=SMOKE_SEED
    )
    bridge = ControlSimEventBridge(ControlSimQAHBN2Adapter(learner))
    sim = MiniControlSim()

    # Decision 1: force KEEP without altering the canonical AHBN proposal.
    s1 = learner.discretize(0.10, 0.10, 0.10, 0.10)
    learner.q_table[s1]["KEEP"] = 1.0
    d1 = bridge.new_message_decision(
        peer_id=0, message_id="m1",
        d_hat=0.10, l_hat=0.10, u_hat=0.10, c_hat=0.10,
        mode_ahbn="gossip", k_ahbn=3, eligible_targets=(1, 2, 3),
    )
    outcomes1 = [sim.attempt(0, t, "m1") for t in d1.realized_targets]
    bridge.close_direct_attempts(d1.q.decision_id, outcomes1)

    # Decision 2 at the same peer supplies s_(t+1), triggering exactly one update.
    s2 = learner.discretize(0.50, 0.10, 0.10, 0.10)
    learner.q_table[s2]["KEEP"] = 2.0
    d2 = bridge.new_message_decision(
        peer_id=0, message_id="m2",
        d_hat=0.50, l_hat=0.10, u_hat=0.10, c_hat=0.10,
        mode_ahbn="structured", k_ahbn=2, eligible_targets=(1, 2),
    )
    outcomes2 = [sim.attempt(0, t, "m2") for t in d2.realized_targets]
    bridge.close_direct_attempts(d2.q.decision_id, outcomes2)
    bridge.terminal(d2.q.decision_id)

    r1 = learner.transitions.get(d1.q.decision_id)
    r2 = learner.transitions.get(d2.q.decision_id)
    return {
        "seed": SMOKE_SEED,
        "gamma_fixture": SMOKE_GAMMA,
        "d1_ahbn": (d1.q.mode_ahbn, d1.q.k_ahbn),
        "d1_q": (d1.q.mode_q, d1.q.k_q),
        "d1_outcomes": tuple(o.outcome for o in outcomes1),
        "d1_reward": r1.reward_t,
        "d1_successor": r1.next_state,
        "d1_updated": r1.update_consumed,
        "d2_outcomes": tuple(o.outcome for o in outcomes2),
        "d2_reward": r2.reward_t,
        "d2_terminal": r2.terminal,
        "d2_updated": r2.update_consumed,
        "q_updates": learner.update_count,
    }


if __name__ == "__main__":
    print(run_smoke())
