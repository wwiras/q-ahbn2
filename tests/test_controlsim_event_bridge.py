"""Deterministic smoke/parity checks for the AR-1.4.2A.1 event bridge."""

import unittest

from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter
from qahbn2.event_bridge import ControlSimEventBridge, DirectAttemptOutcome
from qahbn2.learning import QAHBN2Learner


class TestControlSimEventBridge(unittest.TestCase):
    def make_bridge(self):
        # epsilon=0 keeps this test deterministic; explicit Q values select action.
        learner = QAHBN2Learner(alpha=0.25, gamma=0.80, epsilon=0.0, seed=42)
        return learner, ControlSimEventBridge(ControlSimQAHBN2Adapter(learner))

    def test_smoke_new_message_to_reward_to_update(self):
        learner, bridge = self.make_bridge()
        s1 = learner.discretize(0.1, 0.1, 0.1, 0.1)
        learner.q_table[s1]["FANOUT_UP"] = 1.0

        d1 = bridge.new_message_decision(
            peer_id=3, message_id="m1", d_hat=0.1, l_hat=0.1,
            u_hat=0.1, c_hat=0.1, mode_ahbn="structured", k_ahbn=3,
            eligible_targets=(4, 5, 6, 7),
        )
        self.assertEqual(d1.q.mode_ahbn, "structured")
        self.assertEqual(d1.q.k_ahbn, 3)
        self.assertEqual(d1.q.mode_q, "structured")
        self.assertEqual(d1.q.k_q, 4)
        self.assertEqual(d1.realized_targets, (4, 5, 6, 7))

        bridge.close_direct_attempts(d1.q.decision_id, (
            DirectAttemptOutcome(4, "NEW"),
            DirectAttemptOutcome(5, "NEW"),
            DirectAttemptOutcome(6, "DUPLICATE"),
            DirectAttemptOutcome(7, "FAILED"),
        ))
        # Reward is closed but no same-peer successor exists yet.
        self.assertEqual(learner.transitions.get(d1.q.decision_id).reward_t, 0.0)
        self.assertEqual(learner.update_count, 0)

        s2 = learner.discretize(0.5, 0.1, 0.1, 0.1)
        learner.q_table[s2]["KEEP"] = 2.0
        bridge.new_message_decision(
            peer_id=3, message_id="m2", d_hat=0.5, l_hat=0.1,
            u_hat=0.1, c_hat=0.1, mode_ahbn="gossip", k_ahbn=4,
            eligible_targets=(1, 2, 4, 5),
        )
        self.assertEqual(learner.update_count, 1)
        # old=1.0, R=0, gamma=.8, maxQ(s2)=2 => 1 + .25*(1.6-1)=1.15
        self.assertAlmostEqual(learner.q_table[s1]["FANOUT_UP"], 1.15)

    def test_parity_ahbn_inputs_untouched_and_realized_fanout_bounded(self):
        learner, bridge = self.make_bridge()
        s = learner.discretize(0.2, 0.2, 0.2, 0.2)
        learner.q_table[s]["FANOUT_UP"] = 1.0
        mode_ahbn, k_ahbn = "gossip", 6

        decision = bridge.new_message_decision(
            peer_id=9, message_id="m9", d_hat=0.2, l_hat=0.2,
            u_hat=0.2, c_hat=0.2, mode_ahbn=mode_ahbn, k_ahbn=k_ahbn,
            eligible_targets=(10, 11, 12),
        )
        self.assertEqual((decision.q.mode_ahbn, decision.q.k_ahbn), (mode_ahbn, k_ahbn))
        self.assertEqual(decision.q.k_q, 7)
        self.assertEqual(len(decision.realized_targets), 3)

    def test_zero_attempts_remain_no_reward_no_update(self):
        learner, bridge = self.make_bridge()
        d1 = bridge.new_message_decision(
            peer_id=1, message_id="m0", d_hat=0.0, l_hat=0.0,
            u_hat=0.0, c_hat=0.0, mode_ahbn="structured", k_ahbn=2,
            eligible_targets=(),
        )
        bridge.close_direct_attempts(d1.q.decision_id, ())
        bridge.terminal(d1.q.decision_id)
        rec = learner.transitions.get(d1.q.decision_id)
        self.assertTrue(rec.no_forwarding_evidence)
        self.assertIsNone(rec.reward_t)
        self.assertEqual(learner.update_count, 0)


if __name__ == "__main__":
    unittest.main()
