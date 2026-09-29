"""Unit tests for deterministic S11-A aggregation script (docs/04_STATISTICAL_CONTRACT.md).

Verifies:
- Exp10-Q regression parity against frozen oracle (exp10q_formal_analysis.json)
- Expected primary metrics
- Exact same-seed AHBN/Q-AHBN2 pairing
- Duplicate pair detection
- Missing pair detection
- Deterministic seed ordering
- Sample SD (ddof=1) vs population SD (ddof=0)
- Correct Student-t CI computation (df=4, t=2.7764451051977987)
- No mutation of source CSV files
- Explicit exclusion of Exp13-Q from S11-A scope
- PREP execution boundary: no formal aggregation released during PREP
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import unittest

from scripts.aggregate_s11a_formal import (
    EXPERIMENT_SPECS,
    FROZEN_SEEDS,
    LEARNING_NUMERIC_METRICS,
    METHODS,
    PRIMARY_METRICS,
    STUDENT_T_95_DF4,
    SUMMARY_CSV_COLUMNS,
    aggregate_experiment_data,
    aggregate_experiment_from_csv,
    compute_file_sha256,
    compute_metric_summary,
    compute_paired_effects,
    generate_summary_csv_rows,
    load_csv_rows,
    validate_experiment_rows,
)

EXP10_CSV_PATH = Path(
    "output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal/exp10q_formal.csv"
)
EXP10_ORACLE_PATH = Path(
    "output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal-analysis/exp10q_formal_analysis.json"
)


class TestAggregateS11A(unittest.TestCase):
    """Test suite for deterministic S11-A aggregation implementation."""

    @classmethod
    def setUpClass(cls) -> None:
        if not EXP10_ORACLE_PATH.is_file():
            raise FileNotFoundError(f"Exp10-Q oracle missing: {EXP10_ORACLE_PATH}")
        with open(EXP10_ORACLE_PATH, "r", encoding="utf-8") as f:
            cls.oracle = json.load(f)

    def test_exp10q_regression_parity_cell_summaries(self) -> None:
        """Verify new implementation reproduces Exp10-Q cell summaries exactly."""
        agg = aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp10q")
        oracle_cells = self.oracle["cell_summaries"]

        for cond in ("control", "failure"):
            self.assertIn(cond, agg["cell_summaries"])
            for method in ("ahbn", "qahbn2"):
                self.assertIn(method, agg["cell_summaries"][cond])
                for metric in PRIMARY_METRICS:
                    calc = agg["cell_summaries"][cond][method][metric]
                    exp = oracle_cells[cond][method][metric]

                    self.assertEqual(calc["n"], exp["n"])
                    self.assertTrue(
                        math.isclose(calc["mean"], exp["mean"], rel_tol=1e-12),
                        f"Mean mismatch for {cond} {method} {metric}: {calc['mean']} vs {exp['mean']}",
                    )
                    self.assertTrue(
                        math.isclose(calc["sd"], exp["sd"], rel_tol=1e-12),
                        f"SD mismatch for {cond} {method} {metric}: {calc['sd']} vs {exp['sd']}",
                    )
                    self.assertTrue(
                        math.isclose(calc["ci95_low"], exp["ci95_low"], rel_tol=1e-12),
                        f"CI low mismatch for {cond} {method} {metric}: {calc['ci95_low']} vs {exp['ci95_low']}",
                    )
                    self.assertTrue(
                        math.isclose(calc["ci95_high"], exp["ci95_high"], rel_tol=1e-12),
                        f"CI high mismatch for {cond} {method} {metric}: {calc['ci95_high']} vs {exp['ci95_high']}",
                    )
                    for s in FROZEN_SEEDS:
                        self.assertTrue(
                            math.isclose(
                                calc["seed_values"][str(s)],
                                exp["seed_values"][str(s)],
                                rel_tol=1e-12,
                            ),
                            f"Seed value mismatch for {cond} {method} {metric} seed {s}",
                        )

    def test_exp10q_regression_parity_paired_effects(self) -> None:
        """Verify new implementation reproduces Exp10-Q paired effects exactly."""
        agg = aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp10q")
        oracle_pairs = self.oracle["paired_effects"]

        for cond in ("control", "failure"):
            self.assertIn(cond, agg["paired_effects"])
            for metric in PRIMARY_METRICS:
                calc = agg["paired_effects"][cond][metric]
                exp = oracle_pairs[cond][metric]

                self.assertEqual(calc["n"], exp["n"])
                self.assertTrue(
                    math.isclose(calc["mean"], exp["mean"], rel_tol=1e-12),
                    f"Paired mean mismatch for {cond} {metric}: {calc['mean']} vs {exp['mean']}",
                )
                self.assertTrue(
                    math.isclose(calc["sd"], exp["sd"], rel_tol=1e-12),
                    f"Paired SD mismatch for {cond} {metric}: {calc['sd']} vs {exp['sd']}",
                )
                self.assertTrue(
                    math.isclose(calc["ci95_low"], exp["ci95_low"], rel_tol=1e-12),
                    f"Paired CI low mismatch for {cond} {metric}: {calc['ci95_low']} vs {exp['ci95_low']}",
                )
                self.assertTrue(
                    math.isclose(calc["ci95_high"], exp["ci95_high"], rel_tol=1e-12),
                    f"Paired CI high mismatch for {cond} {metric}: {calc['ci95_high']} vs {exp['ci95_high']}",
                )
                for s in FROZEN_SEEDS:
                    self.assertTrue(
                        math.isclose(
                            calc["seed_differences_Q_minus_A"][str(s)],
                            exp["seed_differences_Q_minus_A"][str(s)],
                            rel_tol=1e-12,
                        ),
                        f"Seed difference mismatch for {cond} {metric} seed {s}",
                    )
                self.assertTrue(
                    math.isclose(
                        calc["relative_change_percent"],
                        exp["relative_change_percent"],
                        rel_tol=1e-12,
                    ),
                    f"Relative change mismatch for {cond} {metric}",
                )
                if metric == "delivery_ratio":
                    self.assertTrue(
                        math.isclose(
                            calc["percentage_point_difference"],
                            exp["percentage_point_difference"],
                            rel_tol=1e-12,
                        ),
                        f"PP difference mismatch for {cond} {metric}",
                    )

    def test_exp10q_regression_parity_learning(self) -> None:
        """Verify new implementation reproduces Exp10-Q learning metrics exactly."""
        agg = aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp10q")
        oracle_learning = self.oracle["qahbn2_learning"]

        for cond in ("control", "failure"):
            self.assertIn(cond, agg["qahbn2_learning"])
            for metric in LEARNING_NUMERIC_METRICS:
                calc = agg["qahbn2_learning"][cond][metric]
                exp = oracle_learning[cond][metric]

                self.assertEqual(calc["n"], exp["n"])
                self.assertTrue(math.isclose(calc["mean"], exp["mean"], rel_tol=1e-12))
                self.assertTrue(math.isclose(calc["sd"], exp["sd"], rel_tol=1e-12))
                self.assertTrue(math.isclose(calc["ci95_low"], exp["ci95_low"], rel_tol=1e-12))
                self.assertTrue(math.isclose(calc["ci95_high"], exp["ci95_high"], rel_tol=1e-12))

            calc_dist = agg["qahbn2_learning"][cond]["action_distribution"]
            exp_dist = oracle_learning[cond]["action_distribution"]

            self.assertEqual(calc_dist["aggregate_counts"], exp_dist["aggregate_counts"])
            self.assertEqual(calc_dist["per_seed"], exp_dist["per_seed"])
            for action, prop in calc_dist["aggregate_proportions"].items():
                self.assertTrue(
                    math.isclose(prop, exp_dist["aggregate_proportions"][action], rel_tol=1e-12)
                )

    def test_expected_primary_metrics(self) -> None:
        """Verify primary metrics match the frozen statistical contract."""
        expected = ("delivery_ratio", "propagation_delay", "duplicates", "total_forwards")
        self.assertEqual(PRIMARY_METRICS, expected)

        # Non-finite value in primary metric rejected
        invalid_rows = load_csv_rows(EXP10_CSV_PATH)
        invalid_rows[0]["delivery_ratio"] = "nan"
        with self.assertRaises(ValueError):
            validate_experiment_rows(
                invalid_rows,
                condition_key="condition",
                conditions=("control", "failure"),
            )

        # Out-of-bounds delivery_ratio rejected
        invalid_rows = load_csv_rows(EXP10_CSV_PATH)
        invalid_rows[0]["delivery_ratio"] = "1.05"
        with self.assertRaises(ValueError):
            validate_experiment_rows(
                invalid_rows,
                condition_key="condition",
                conditions=("control", "failure"),
            )

        # Non-positive propagation_delay rejected
        invalid_rows = load_csv_rows(EXP10_CSV_PATH)
        invalid_rows[0]["propagation_delay"] = "0.0"
        with self.assertRaises(ValueError):
            validate_experiment_rows(
                invalid_rows,
                condition_key="condition",
                conditions=("control", "failure"),
            )

    def test_exact_same_seed_ahbn_qahbn2_pairing(self) -> None:
        """Verify pairing strictly matches same seed regardless of row order."""
        rows = load_csv_rows(EXP10_CSV_PATH)
        # Reverse rows to test that ordering does not affect seed-paired calculation
        reversed_rows = list(reversed(rows))
        agg_normal = aggregate_experiment_data(
            rows, condition_key="condition", conditions=("control", "failure")
        )
        agg_reversed = aggregate_experiment_data(
            reversed_rows, condition_key="condition", conditions=("control", "failure")
        )

        for cond in ("control", "failure"):
            for metric in PRIMARY_METRICS:
                diffs_normal = agg_normal["paired_effects"][cond][metric]["seed_differences_Q_minus_A"]
                diffs_reversed = agg_reversed["paired_effects"][cond][metric]["seed_differences_Q_minus_A"]
                self.assertEqual(diffs_normal, diffs_reversed)

    def test_duplicate_pair_detection(self) -> None:
        """Verify duplicate (condition, method, seed) run detection."""
        rows = load_csv_rows(EXP10_CSV_PATH)
        # Replace last row with a duplicate of the first row
        rows[-1] = dict(rows[0])
        with self.assertRaisesRegex(ValueError, "Duplicate cell"):
            validate_experiment_rows(
                rows,
                condition_key="condition",
                conditions=("control", "failure"),
            )

    def test_missing_pair_detection(self) -> None:
        """Verify detection of missing run in the required matrix."""
        rows = load_csv_rows(EXP10_CSV_PATH)
        # Remove one row
        incomplete_rows = rows[:-1]
        with self.assertRaisesRegex(ValueError, "Expected 20 rows, but received 19 rows"):
            validate_experiment_rows(
                incomplete_rows,
                condition_key="condition",
                conditions=("control", "failure"),
            )

    def test_deterministic_seed_ordering(self) -> None:
        """Verify seed values and differences are always sorted by seed [42..46]."""
        agg = aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp10q")
        expected_keys = [str(s) for s in FROZEN_SEEDS]

        for cond in ("control", "failure"):
            for metric in PRIMARY_METRICS:
                pair = agg["paired_effects"][cond][metric]
                self.assertEqual(list(pair["seed_differences_Q_minus_A"].keys()), expected_keys)
                for method in METHODS:
                    cell = agg["cell_summaries"][cond][method][metric]
                    self.assertEqual(list(cell["seed_values"].keys()), expected_keys)

    def test_sample_sd_rather_than_population_sd(self) -> None:
        """Verify sample standard deviation (ddof=1) is strictly used over population SD."""
        # For values [10, 20, 30, 40, 50]:
        # mean = 30.0
        # population variance (div by 5) = 200.0, pop SD = sqrt(200) ~= 14.1421356
        # sample variance (div by 4) = 250.0, sample SD = sqrt(250) ~= 15.8113883
        test_values = {42: 10.0, 43: 20.0, 44: 30.0, 45: 40.0, 46: 50.0}
        summary = compute_metric_summary(test_values)

        expected_sample_sd = math.sqrt(250.0)
        population_sd = math.sqrt(200.0)

        self.assertTrue(math.isclose(summary["sd"], expected_sample_sd, rel_tol=1e-12))
        self.assertFalse(math.isclose(summary["sd"], population_sd, rel_tol=1e-12))

    def test_correct_student_t_ci_computation(self) -> None:
        """Verify Student-t critical value is exactly 2.7764451051977987 for df=4."""
        self.assertEqual(STUDENT_T_95_DF4, 2.7764451051977987)

        test_values = {42: 10.0, 43: 20.0, 44: 30.0, 45: 40.0, 46: 50.0}
        summary = compute_metric_summary(test_values)

        mean_val = 30.0
        sd_val = math.sqrt(250.0)
        expected_margin = STUDENT_T_95_DF4 * sd_val / math.sqrt(5)

        self.assertTrue(math.isclose(summary["ci95_low"], mean_val - expected_margin, rel_tol=1e-12))
        self.assertTrue(math.isclose(summary["ci95_high"], mean_val + expected_margin, rel_tol=1e-12))

        # Reject standard normal z=1.96 multiplier
        z_margin = 1.960 * sd_val / math.sqrt(5)
        self.assertFalse(math.isclose(summary["ci95_low"], mean_val - z_margin, rel_tol=1e-4))

    def test_no_mutation_of_source_csv_files(self) -> None:
        """Verify source CSV file is not mutated during aggregation."""
        hash_before = compute_file_sha256(EXP10_CSV_PATH)
        _ = aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp10q")
        hash_after = compute_file_sha256(EXP10_CSV_PATH)
        self.assertEqual(hash_before, hash_after)

    def test_exp13q_excluded_from_s11a_scope(self) -> None:
        """Verify Exp13-Q is explicitly excluded from S11-A scope."""
        self.assertNotIn("exp13q", EXPERIMENT_SPECS)
        with self.assertRaises(ValueError):
            aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp13q")

    def test_summary_csv_schema_and_generation(self) -> None:
        """Verify summary CSV table schema matches requirement."""
        agg = aggregate_experiment_from_csv(EXP10_CSV_PATH, "exp10q")
        mock_s11a = {
            "experiments": {
                "exp10q": agg,
                "exp11q": agg,  # mock for schema test
                "exp12q": agg,  # mock for schema test
            }
        }
        rows = generate_summary_csv_rows(mock_s11a)
        self.assertTrue(len(rows) > 0)
        for r in rows:
            for col in SUMMARY_CSV_COLUMNS:
                self.assertIn(col, r)

    def test_prep_boundary_no_formal_aggregation_released(self) -> None:
        """Verify PREP execution boundary: no formal S11-A aggregation directory released."""
        formal_release_dir = Path("output/evidence/s11-aggregation/s11a-primary-ro4")
        self.assertFalse(
            formal_release_dir.exists(),
            f"Formal aggregation directory {formal_release_dir} must not be created during PREP gate",
        )


if __name__ == "__main__":
    unittest.main()
