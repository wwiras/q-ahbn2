import unittest

from qahbn2.formal_exp10q import (
    CONDITIONS,
    EXPECTED_RUNS,
    FAILURE_BEFORE_MESSAGE,
    METHODS,
    SEEDS,
    failed_peer_for_seed,
    validate_matrix,
)


class TestFormalExp10QContract(unittest.TestCase):
    def test_exact_frozen_matrix(self):
        self.assertEqual(len(EXPECTED_RUNS), 20)
        self.assertEqual(CONDITIONS, ("control", "failure"))
        self.assertEqual(METHODS, ("ahbn", "qahbn2"))
        self.assertEqual(SEEDS, (42, 43, 44, 45, 46))
        self.assertEqual(FAILURE_BEFORE_MESSAGE, 501)
        validate_matrix(CONDITIONS, METHODS, SEEDS)

    def test_matrix_expansion_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_matrix(("control", "failure", "extra"), METHODS, SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(CONDITIONS, ("ahbn", "qahbn2", "gossip"), SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(CONDITIONS, METHODS, (*SEEDS, 47))

    def test_failed_peer_is_deterministic_and_never_source(self):
        for seed in SEEDS:
            first = failed_peer_for_seed(seed)
            second = failed_peer_for_seed(seed)
            self.assertEqual(first, second)
            self.assertNotEqual(first, 0)
            self.assertGreaterEqual(first, 0)
            self.assertLess(first, 100)


if __name__ == "__main__":
    unittest.main()
