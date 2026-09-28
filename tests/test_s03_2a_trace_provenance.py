"""S03.2A deterministic checks for passive ControlSim decision provenance."""

import unittest

from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter
from qahbn2.learning import QAHBN2Learner
from qahbn2.learning_validation import _AttemptTracker, _DecisionTrace


class TestS032ATraceProvenance(unittest.TestCase):
    @staticmethod
    def _fixture(trace_enabled: bool):
        learner = QAHBN2Learner(
            alpha=0.25, gamma=0.70, epsilon=0.0,
            epsilon_min=0.0, epsilon_decay=1.0, seed=42,
        )
        state = learner.discretize(0.1, 0.1, 0.1, 0.1)
        learner.q_table[state]["FANOUT_UP"] = 1.0
        adapter = ControlSimQAHBN2Adapter(learner)
        trace = _DecisionTrace(enabled=trace_enabled)
        tracker = _AttemptTracker(adapter, trace=trace)

        q = adapter.decide(
            peer_id=3, message_id="m1",
            d_hat=0.1, l_hat=0.1, u_hat=0.1, c_hat=0.1,
            mode_ahbn="gossip", k_ahbn=3,
        )
        realized = [4, 5]
        trace.register(q, realized)
        tracker.register(q.decision_id, 3, "m1", realized)
        tracker.resolve(3, 4, "m1", "NEW")
        tracker.resolve(3, 5, "m1", "DUPLICATE")
        tracker.assert_empty()

        rec = learner.transitions.get(q.decision_id)
        behavior = {
            "decision": q,
            "reward": rec.reward_t,
            "epsilon": learner.epsilon,
            "decision_count": learner.decision_count,
            "update_count": learner.update_count,
            "action_history": tuple(learner.action_history),
            "reward_history": tuple(learner.reward_history),
        }
        return behavior, trace

    def test_trace_captures_frozen_provenance_chain(self):
        behavior, trace = self._fixture(True)
        q = behavior["decision"]
        rec = trace.records[q.decision_id]
        self.assertEqual(rec["state"], ("L", "L", "L", "L"))
        self.assertEqual((rec["mode_ahbn"], rec["k_ahbn"]), ("gossip", 3))
        self.assertEqual(rec["action"], "FANOUT_UP")
        self.assertEqual((rec["mode_q"], rec["k_q"]), ("gossip", 4))
        self.assertEqual(rec["k_real"], 2)
        self.assertEqual((rec["NEW"], rec["DUPLICATE"], rec["FAILED"]), (1, 1, 0))
        self.assertEqual(behavior["reward"], 0.0)

    def test_trace_off_and_on_have_identical_learning_behavior(self):
        without_trace, off = self._fixture(False)
        with_trace, on = self._fixture(True)
        self.assertEqual(without_trace, with_trace)
        self.assertEqual(off.records, {})
        self.assertEqual(len(on.records), 1)

    def test_zero_realized_targets_are_traced_without_reward(self):
        learner = QAHBN2Learner(
            alpha=0.25, gamma=0.70, epsilon=0.0,
            epsilon_min=0.0, epsilon_decay=1.0, seed=42,
        )
        adapter = ControlSimQAHBN2Adapter(learner)
        trace = _DecisionTrace(enabled=True)
        tracker = _AttemptTracker(adapter, trace=trace)
        q = adapter.decide(
            peer_id=8, message_id="m0",
            d_hat=0.0, l_hat=0.0, u_hat=0.0, c_hat=0.0,
            mode_ahbn="structured", k_ahbn=2,
        )
        trace.register(q, [])
        tracker.register(q.decision_id, 8, "m0", [])
        rec = trace.records[q.decision_id]
        self.assertEqual(rec["k_real"], 0)
        self.assertEqual((rec["NEW"], rec["DUPLICATE"], rec["FAILED"]), (0, 0, 0))
        self.assertTrue(learner.transitions.get(q.decision_id).no_forwarding_evidence)
        self.assertIsNone(learner.transitions.get(q.decision_id).reward_t)


if __name__ == "__main__":
    unittest.main()
