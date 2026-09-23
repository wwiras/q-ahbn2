"""AR-1.4.2 minimal gamma sensitivity runner.

This runner intentionally refuses to execute until the Q-AHBN2 ControlSim
integration supplies a real episode/run adapter.  It freezes the experimental
matrix now so that no additional gamma values or seeds can be introduced
silently.

The adapter must execute the existing Q-AHBN2 Learning Validation workload and
return the predeclared learning/network diagnostics.  Do not substitute a toy
MDP: AR-1.4.2 is a ControlSim sensitivity protocol.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, Iterable


GAMMAS = (0.70, 0.80, 0.90)
SEEDS = (42, 43, 44, 45, 46)

EXPECTED_RUNS = tuple((gamma, seed) for gamma in GAMMAS for seed in SEEDS)

REQUIRED_METRICS = (
    "mean_reward",
    "cumulative_reward",
    "stabilization",
    "q_updates",
    "state_action_coverage",
    "action_distribution",
    "delivery_ratio",
    "propagation_delay",
    "duplicates",
    "total_forwards",
)


def run_controlsim_learning_validation(*, gamma: float, seed: int) -> Dict[str, object]:
    """Execute one real canonical-ControlSim Q-AHBN2 Learning Validation run."""
    from qahbn2.learning_validation import run_learning_validation
    return run_learning_validation(gamma=gamma, seed=seed)


def validate_matrix(gammas: Iterable[float], seeds: Iterable[int]) -> None:
    matrix = tuple((float(g), int(s)) for g in gammas for s in seeds)
    if matrix != EXPECTED_RUNS:
        raise ValueError(
            "AR-1.4.2 matrix is frozen: gamma={0.70,0.80,0.90}, "
            "seeds={42,43,44,45,46}, exactly 15 runs."
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    validate_matrix(GAMMAS, SEEDS)
    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    output_dir = args.output_dir or Path(
        f"q-ahbn-{timestamp}-ar142-gamma-sensitivity-rl-validation"
    )
    if output_dir.exists():
        raise FileExistsError(f"refusing to overwrite existing run directory: {output_dir}")
    output_dir.mkdir(parents=True)
    output = output_dir / "ar_1_4_2_gamma_sensitivity.csv"

    rows = []
    for gamma, seed in EXPECTED_RUNS:
        metrics = run_controlsim_learning_validation(gamma=gamma, seed=seed)
        missing = [name for name in REQUIRED_METRICS if name not in metrics]
        if missing:
            raise RuntimeError(f"run gamma={gamma}, seed={seed} missing metrics: {missing}")
        rows.append({"gamma": gamma, "seed": seed, **metrics})

    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=("gamma", "seed", *REQUIRED_METRICS))
        writer.writeheader()
        writer.writerows(rows)

    try:
        qahbn2_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.STDOUT
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        qahbn2_commit = "UNAVAILABLE"

    manifest = {
        "environment": "ControlSim",
        "experiment": "AR-1.4.2 gamma sensitivity",
        "event": "rl-validation",
        "timestamp": timestamp,
        "run_directory": str(output_dir),
        "status": "completed",
        "scientific_classification": "bounded gamma sensitivity",
        "qahbn2_commit": qahbn2_commit,
        "canonical_ahbn_commit": "936a79480bc1252c79b6ee01f65c88c740af2844",
        "gammas": list(GAMMAS),
        "seeds": list(SEEDS),
        "expected_runs": len(EXPECTED_RUNS),
        "completed_runs": len(rows),
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "RUN.md").write_text(
        "# AR-1.4.2 Gamma Sensitivity\n\n"
        f"- Timestamp: {timestamp}\n"
        "- Environment: ControlSim\n"
        "- Event: rl-validation\n"
        f"- Q-AHBN2 commit: {qahbn2_commit}\n"
        "- Canonical AHBN commit: 936a79480bc1252c79b6ee01f65c88c740af2844\n"
        f"- Expected/completed runs: {len(EXPECTED_RUNS)}/{len(rows)}\n"
        "- Scientific status: raw sensitivity evidence; gamma not yet selected\n",
        encoding="utf-8",
    )
    print(output_dir)


if __name__ == "__main__":
    main()
