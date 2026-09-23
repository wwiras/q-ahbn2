"""Guards for the frozen AR-1.4.2B Learning Validation contract."""

import unittest

from qahbn2.learning import ACTIONS
from qahbn2.learning_validation import (
    ALPHA_Q,
    BA_M,
    BASE_DELAY,
    EPSILON_0,
    EPSILON_DECAY,
    EPSILON_MIN,
    JITTER,
    MESSAGE_SOURCE,
    NUM_CLUSTERS,
    NUM_MESSAGES,
    NUM_NODES,
    STABILIZATION_CONSECUTIVE,
    STABILIZATION_DELTA,
    STABILIZATION_WINDOW,
    TOTAL_STATE_ACTION_PAIRS,
    stabilization_point,
)


class TestLearningValidationContract(unittest.TestCase):
    def test_fixed_workload_and_learning_constants(self):
        self.assertEqual(NUM_MESSAGES, 1000)
        self.assertEqual(NUM_NODES, 100)
        self.assertEqual(BA_M, 3)
        self.assertEqual(MESSAGE_SOURCE, 0)
        self.assertEqual(BASE_DELAY, 1.0)
        self.assertEqual(JITTER, 0.2)
        self.assertEqual(NUM_CLUSTERS, 4)
        self.assertEqual(ALPHA_Q, 0.25)
        self.assertEqual(EPSILON_0, 0.30)
        self.assertEqual(EPSILON_MIN, 0.03)
        self.assertEqual(EPSILON_DECAY, 0.995)
        self.assertEqual(TOTAL_STATE_ACTION_PAIRS, 81 * len(ACTIONS))
        self.assertEqual(TOTAL_STATE_ACTION_PAIRS, 405)

    def test_frozen_stabilization_parameters(self):
        self.assertEqual(STABILIZATION_WINDOW, 50)
        self.assertEqual(STABILIZATION_DELTA, 0.05)
        self.assertEqual(STABILIZATION_CONSECUTIVE, 3)

    def test_stabilization_constant_reward_sequence(self):
        # Four full windows are required for three consecutive comparisons.
        self.assertEqual(stabilization_point([0.25] * 200), 100)

    def test_stabilization_reports_not_stabilized_when_insufficient(self):
        self.assertEqual(stabilization_point([0.25] * 199), "NOT_STABILIZED")


if __name__ == "__main__":
    unittest.main()
