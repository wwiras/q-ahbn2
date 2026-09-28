import unittest

from qahbn2.formal_exp12q import (
    EXPECTED_RUNS, METHODS, PROFILE_FRACTIONS, RESOURCE_CLASSES,
    RESOURCE_PROFILES, SEEDS, resource_assignment_for_seed, validate_matrix,
)


class TestFormalExp12QContract(unittest.TestCase):
    def test_exact_frozen_matrix(self):
        self.assertEqual(len(EXPECTED_RUNS), 30)
        self.assertEqual(
            RESOURCE_PROFILES,
            ("balanced", "moderate_heterogeneity", "weak_heavy"),
        )
        self.assertEqual(METHODS, ("ahbn", "qahbn2"))
        self.assertEqual(SEEDS, (42, 43, 44, 45, 46))
        validate_matrix(RESOURCE_PROFILES, METHODS, SEEDS)

    def test_matrix_expansion_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_matrix((*RESOURCE_PROFILES, "extra"), METHODS, SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(RESOURCE_PROFILES, (*METHODS, "gossip"), SEEDS)
        with self.assertRaises(ValueError):
            validate_matrix(RESOURCE_PROFILES, METHODS, (*SEEDS, 47))

    def test_exact_resource_contract(self):
        self.assertEqual(
            RESOURCE_CLASSES,
            {
                "strong": {"processing_delay": 0.15, "capacity_score": 1.80},
                "medium": {"processing_delay": 0.50, "capacity_score": 1.00},
                "weak": {"processing_delay": 1.00, "capacity_score": 0.55},
            },
        )
        self.assertEqual(
            PROFILE_FRACTIONS,
            {
                "balanced": {"strong": 0.25, "medium": 0.50, "weak": 0.25},
                "moderate_heterogeneity": {
                    "strong": 0.20, "medium": 0.45, "weak": 0.35,
                },
                "weak_heavy": {"strong": 0.15, "medium": 0.35, "weak": 0.50},
            },
        )

    def test_assignment_is_deterministic_for_profile_and_seed(self):
        try:
            first = resource_assignment_for_seed(42, "balanced")
            second = resource_assignment_for_seed(42, "balanced")
        except (RuntimeError, ImportError):
            self.skipTest("canonical AHBN checkout not available in current environment")
        self.assertEqual(first, second)
        self.assertEqual(len(first), 100)
        counts = {"strong": 0, "medium": 0, "weak": 0}
        for _, resource_class in first:
            counts[resource_class] += 1
        self.assertEqual(counts, {"strong": 25, "medium": 50, "weak": 25})

    def test_all_profile_counts(self):
        expected = {
            "balanced": {"strong": 25, "medium": 50, "weak": 25},
            "moderate_heterogeneity": {"strong": 20, "medium": 45, "weak": 35},
            "weak_heavy": {"strong": 15, "medium": 35, "weak": 50},
        }
        try:
            assignments = {
                profile: resource_assignment_for_seed(42, profile)
                for profile in RESOURCE_PROFILES
            }
        except (RuntimeError, ImportError):
            self.skipTest("canonical AHBN checkout not available in current environment")
        for profile, assignment in assignments.items():
            counts = {"strong": 0, "medium": 0, "weak": 0}
            for _, resource_class in assignment:
                counts[resource_class] += 1
            self.assertEqual(counts, expected[profile])


if __name__ == "__main__":
    unittest.main()
