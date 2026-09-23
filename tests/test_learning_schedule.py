"""Deterministic guards for the frozen Q-AHBN2 epsilon schedule and diagnostics."""

import unittest

from qahbn2.learning import ACTIONS, QAHBN2Learner


class TestLearningSchedule(unittest.TestCase):
    def test_epsilon_decays_once_per_decision_to_floor(self):
        learner = QAHBN2Learner(
            alpha=0.25, gamma=0.80, epsilon=0.30,
            epsilon_min=0.03, epsilon_decay=0.995, seed=42,
        )
        state = ("L", "L", "L", "L")
        learner.choose_action(state)
        self.assertAlmostEqual(learner.epsilon, 0.30 * 0.995)
        self.assertEqual(learner.decision_count, 1)
        self.assertEqual(len(learner.action_history), 1)

        for _ in range(5000):
            learner.choose_action(state)
        self.assertAlmostEqual(learner.epsilon, 0.03)

    def test_action_history_records_frozen_action_space(self):
        learner = QAHBN2Learner(seed=42)
        state = ("M", "L", "H", "L")
        learner.choose_action(state)
        observed_state, action = learner.action_history[-1]
        self.assertEqual(observed_state, state)
        self.assertIn(action, ACTIONS)


if __name__ == "__main__":
    unittest.main()
