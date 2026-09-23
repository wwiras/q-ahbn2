"""Guard tests for the frozen AR-1.4.2 experimental matrix."""

import unittest

from scripts.run_ar_1_4_2_gamma_sensitivity import (
    EXPECTED_RUNS,
    GAMMAS,
    SEEDS,
    validate_matrix,
)


class TestAR142Protocol(unittest.TestCase):
    def test_exact_frozen_matrix(self):
        self.assertEqual(GAMMAS, (0.70, 0.80, 0.90))
        self.assertEqual(SEEDS, (42, 43, 44, 45, 46))
        self.assertEqual(len(EXPECTED_RUNS), 15)
        validate_matrix(GAMMAS, SEEDS)

    def test_extra_gamma_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_matrix((0.70, 0.80, 0.90, 0.95), SEEDS)


if __name__ == "__main__":
    unittest.main()
