import json
import unittest

from qahbn2.formal_exp11q import churn_schedule_for_seed as exp11_schedule
from qahbn2.formal_exp13q import (
    CHURN_LEVEL,
    CYCLE_ONSETS,
    DCSOC_EPS,
    DCSOC_MIN_SAMPLES,
    EXPECTED_RUNS,
    METHODS,
    REJOIN_BEFORE_MESSAGES,
    SEEDS,
    churn_schedule_for_seed,
    validate_matrix,
)


class TestFormalExp13QContract(unittest.TestCase):
    def test_exact_frozen_matrix(self):
        self.assertEqual(CHURN_LEVEL, 0.40)
        self.assertEqual(
            METHODS, ("gossip", "structured", "dcsoc", "ahbn", "qahbn2")
        )
        self.assertEqual(SEEDS, (42, 43, 44, 45, 46))
        self.assertEqual(len(EXPECTED_RUNS), 25)
        self.assertEqual(CYCLE_ONSETS, (201, 401, 601, 801))
        self.assertEqual(REJOIN_BEFORE_MESSAGES, (251, 451, 651, 851))
        validate_matrix(METHODS, SEEDS)

    def test_unauthorized_matrix_change_rejected(self):
        with self.assertRaises(ValueError):
            validate_matrix(("gossip", "structured", "ahbn", "qahbn2"), SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(METHODS, (42, 43, 44))

    def test_frozen_dcsoc_parameters(self):
        self.assertEqual(DCSOC_EPS, 2.0)
        self.assertEqual(DCSOC_MIN_SAMPLES, 3)

    def test_schedule_reuses_exp11_high_churn_exactly(self):
        for seed in SEEDS:
            self.assertEqual(
                churn_schedule_for_seed(seed, CHURN_LEVEL),
                exp11_schedule(seed, 0.40),
            )
            schedule = churn_schedule_for_seed(seed, CHURN_LEVEL)
            self.assertEqual(len(schedule), 4)
            self.assertTrue(all(0 not in targets for targets in schedule))
            self.assertTrue(all(len(targets) == 40 for targets in schedule))

    def test_schedule_is_deterministic_per_seed(self):
        for seed in SEEDS:
            first = churn_schedule_for_seed(seed, CHURN_LEVEL)
            second = churn_schedule_for_seed(seed, CHURN_LEVEL)
            self.assertEqual(
                json.dumps(first, sort_keys=True),
                json.dumps(second, sort_keys=True),
            )


if __name__ == "__main__":
    unittest.main()
