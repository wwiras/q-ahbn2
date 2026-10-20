"""Tests for the frozen five-seed D8-C statistical calculations."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "gke/scripts"))
import analyze_d8_c_offline as analysis


class ConfidenceIntervalTests(unittest.TestCase):
    def test_student_t_critical_value_matches_frozen_df4_contract(self):
        summary = analysis.ci_summary([1, 2, 3, 4, 5])
        self.assertEqual(summary["df"], 4)
        self.assertEqual(summary["t_critical_two_sided_95"], 2.7764451051977987)
        self.assertAlmostEqual(summary["mean"], 3.0)
        self.assertAlmostEqual(summary["sample_sd"], 1.5811388300841898)

    def test_zero_variance_has_point_interval(self):
        summary = analysis.ci_summary([0, 0, 0, 0, 0])
        self.assertEqual(summary["sample_sd"], 0)
        self.assertEqual(summary["ci95_low"], 0)
        self.assertEqual(summary["ci95_high"], 0)

    def test_requires_five_finite_values(self):
        with self.assertRaises(ValueError):
            analysis.ci_summary([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            analysis.ci_summary([1, 2, 3, 4, float("nan")])

    def test_qahbn2_minus_ahbn_pairing_is_by_seed(self):
        dataset = []
        for seed, ahbn_value, q_value in zip(
            [42, 43, 44, 45, 46], [0.1, 0.2, 0.3, 0.4, 0.5],
            [0.2, 0.1, 0.4, 0.4, 0.8]
        ):
            dataset.extend(
                [
                    {
                        "seed": seed,
                        "method": "ahbn",
                        "delivery_ratio": ahbn_value,
                        "propagation_delay": ahbn_value,
                        "duplicates": ahbn_value,
                        "total_forwards": ahbn_value,
                    },
                    {
                        "seed": seed,
                        "method": "qahbn2",
                        "delivery_ratio": q_value,
                        "propagation_delay": q_value,
                        "duplicates": q_value,
                        "total_forwards": q_value,
                    },
                ]
            )
        paired, summaries = analysis.summarize_qahbn2_vs_ahbn(dataset)
        for row, expected in zip(paired[:5], [0.1, -0.1, 0.1, 0.0, 0.3]):
            self.assertAlmostEqual(row["Q_AHBN2_minus_AHBN"], expected)
        self.assertAlmostEqual(summaries[0]["mean_difference"], 0.08)
        self.assertEqual(summaries[0]["n"], 5)

    def test_primary_metric_comparison_accepts_rounding_within_tolerance(self):
        dataset = []
        report = []
        for seed in analysis.ROOTS:
            for method in analysis.METHODS:
                run = {"seed": seed, "method": method}
                for metric in analysis.METRICS:
                    run[metric] = 1.0
                    report.append(
                        {
                            "seed": seed,
                            "method": method,
                            "metric": metric,
                            "reported": (
                                "1.0000000004"
                                if (seed, method, metric) == (42, "gossip", "delivery_ratio")
                                else "1"
                            ),
                            "archived": 1.0,
                        }
                    )
                dataset.append(run)
        comparisons = analysis.compare_reported_metrics(dataset, report)
        self.assertEqual(len(comparisons), 100)
        delivery = next(
            row
            for row in comparisons
            if row["seed"] == 42 and row["method"] == "gossip"
            and row["metric"] == "delivery_ratio"
        )
        self.assertEqual(delivery["status"], "PASS")

    def test_primary_metric_comparison_marks_values_beyond_tolerance(self):
        dataset = []
        report = []
        for seed in analysis.ROOTS:
            for method in analysis.METHODS:
                run = {"seed": seed, "method": method}
                for metric in analysis.METRICS:
                    run[metric] = 1.0
                    report.append(
                        {
                            "seed": seed,
                            "method": method,
                            "metric": metric,
                            "reported": (
                                "1.000000001"
                                if (seed, method, metric) == (42, "gossip", "delivery_ratio")
                                else "1"
                            ),
                            "archived": 1.0,
                        }
                    )
                dataset.append(run)
        comparisons = analysis.compare_reported_metrics(dataset, report)
        delivery = next(
            row
            for row in comparisons
            if row["seed"] == 42 and row["method"] == "gossip"
            and row["metric"] == "delivery_ratio"
        )
        self.assertEqual(delivery["status"], "FAIL")

    def test_statistical_report_parser_accepts_truncation_and_unicode_minus(self):
        methods = []
        for method in analysis.METHODS:
            for metric in analysis.METRICS:
                methods.append(
                    {
                        "method": method,
                        "method_label": analysis.METHOD_LABELS[method],
                        "metric": metric,
                        "unit": analysis.METRIC_UNITS[metric],
                        "mean": 0.0,
                        "sample_sd": 0.0,
                        "ci95_low": 0.0,
                        "ci95_high": 0.0,
                    }
                )

        paired = []
        for metric in analysis.METRICS:
            for seed in analysis.ROOTS:
                difference = (
                    -0.007740585774
                    if metric == "delivery_ratio" and seed == 43
                    else 0.0
                )
                paired.append(
                    {
                        "seed": seed,
                        "metric": metric,
                        "AHBN": 0.0,
                        "Q_AHBN2": difference,
                        "Q_AHBN2_minus_AHBN": difference,
                        "delivery_difference_percentage_points": (
                            difference * 100 if metric == "delivery_ratio" else None
                        ),
                    }
                )

        paired_summaries = []
        for metric in analysis.METRICS:
            summary = {
                "metric": metric,
                "AHBN_mean": 0.0,
                "Q_AHBN2_mean": 0.0,
                "mean_difference": 0.0,
                "sample_sd_of_differences": 0.0,
                "ci95_low": 0.0,
                "ci95_high": 0.0,
            }
            if metric == "total_forwards":
                summary.update(
                    AHBN_mean=726.0,
                    Q_AHBN2_mean=1738.2,
                    mean_difference=1012.2,
                    sample_sd_of_differences=717.532369,
                    ci95_low=121.265890,
                    ci95_high=1903.13410965,
                )
            paired_summaries.append(summary)

        report = [
            "| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards |",
            "|---|---|---|---|---|",
        ]
        report.extend(
            f"| {analysis.METHOD_LABELS[method]} | 0; 0; [0, 0] | "
            "0; 0; [0, 0] | 0; 0; [0, 0] | 0; 0; [0, 0] |"
            for method in analysis.METHODS
        )
        report.extend(
            [
                "",
                "| Metric | AHBN mean | Q-AHBN2 mean | Mean paired difference | "
                "SD of paired differences | Two-sided 95% paired t CI |",
                "|---|---:|---:|---:|---:|---|",
            ]
        )
        report.extend(
            "| total_forwards | 726 | 1738.2 | +1012.2 | 717.532369 | "
            "[+121.265890, +1903.134109] |"
            if row["metric"] == "total_forwards"
            else f"| {row['metric']} | 0 | 0 | 0 | 0 | [0, 0] |"
            for row in paired_summaries
        )
        report.extend(
            [
                "",
                "| Seed | Delivery ratio | Delivery (percentage points) | "
                "Propagation delay (s) | Duplicates | Total forwards |",
                "|---:|---:|---:|---:|---:|---:|",
            ]
        )
        report.extend(
            f"| {seed} | {'−0.007741' if seed == 43 else '+0.000000'} | "
            f"{'−0.7741' if seed == 43 else '+0.0000'} | +0.000000 | +0 | +0 |"
            for seed in analysis.ROOTS
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            report_path = Path(temporary_directory) / "report.md"
            report_path.write_text("\n".join(report))
            failures = analysis.compare_statistical_report(
                report_path, methods, paired, paired_summaries
            )
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
