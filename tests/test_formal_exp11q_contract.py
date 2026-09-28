import unittest

from qahbn2.formal_exp11q import (
    CHURN_LEVELS,
    CYCLE_ONSETS,
    EXPECTED_RUNS,
    METHODS,
    REJOIN_BEFORE_MESSAGES,
    SEEDS,
    churn_schedule_for_seed,
    validate_matrix,
)


class TestFormalExp11QContract(unittest.TestCase):
    def test_exact_frozen_matrix(self):
        self.assertEqual(len(EXPECTED_RUNS), 30)
        self.assertEqual(CHURN_LEVELS, (0.00, 0.20, 0.40))
        self.assertEqual(METHODS, ("ahbn", "qahbn2"))
        self.assertEqual(SEEDS, (42, 43, 44, 45, 46))
        self.assertEqual(CYCLE_ONSETS, (201, 401, 601, 801))
        self.assertEqual(REJOIN_BEFORE_MESSAGES, (251, 451, 651, 851))
        validate_matrix(CHURN_LEVELS, METHODS, SEEDS)

    def test_matrix_expansion_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_matrix((0.00, 0.20, 0.40, 0.50), METHODS, SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(CHURN_LEVELS, ("ahbn", "qahbn2", "gossip"), SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(CHURN_LEVELS, METHODS, (*SEEDS, 47))

    def test_schedule_is_deterministic_paired_and_excludes_source(self):
        for seed in SEEDS:
            for level, expected_count in ((0.00, 0), (0.20, 20), (0.40, 40)):
                first = churn_schedule_for_seed(seed, level)
                second = churn_schedule_for_seed(seed, level)
                self.assertEqual(first, second)
                self.assertEqual(len(first), 4)
                for cycle_targets in first:
                    self.assertEqual(len(cycle_targets), expected_count)
                    self.assertEqual(len(set(cycle_targets)), expected_count)
                    self.assertNotIn(0, cycle_targets)


if __name__ == "__main__":
    unittest.main()
