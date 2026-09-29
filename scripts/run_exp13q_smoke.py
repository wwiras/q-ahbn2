"""Bounded non-formal five-method Exp13-Q smoke.

This smoke reuses the real frozen Exp13-Q execution paths but temporarily bounds
the workload to seed 42 and messages 1..260 so that exactly the first frozen
leave/rejoin cycle is crossed. It is integration evidence only and must never
be treated as formal performance evidence.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import qahbn2.formal_exp11q as exp11
import qahbn2.formal_exp13q as exp13

SMOKE_SEED = 42
SMOKE_MESSAGES = 260
SMOKE_METHODS = exp13.METHODS
CANONICAL_AHBN_COMMIT = "936a79480bc1252c79b6ee01f65c88c740af2844"


def _git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.STDOUT
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNAVAILABLE"


def _verify_first_cycle(result: dict) -> None:
    events = json.loads(result["churn_events"])
    observed = [
        (event["event"], int(event["before_message"]))
        for event in events
        if int(event["cycle"]) == 1
    ]
    if observed != [("leave", 201), ("join", 251)]:
        raise RuntimeError(
            f"bounded Exp13-Q smoke did not cross the exact first churn cycle: {observed}"
        )
    if int(result["churn_target_count"]) != 40:
        raise RuntimeError(
            f"bounded Exp13-Q smoke expected 40 churn targets, got "
            f"{result['churn_target_count']}"
        )


def run_smoke() -> dict:
    schedule = exp13.churn_schedule_for_seed(SMOKE_SEED, exp13.CHURN_LEVEL)
    rows = []

    # Patch only the module-local loop bounds. The frozen formal constants and
    # run_exp13q_cell default behavior remain unchanged outside this context.
    with patch.object(exp13, "NUM_MESSAGES", SMOKE_MESSAGES), patch.object(
        exp11, "NUM_MESSAGES", SMOKE_MESSAGES
    ):
        for method in SMOKE_METHODS:
            result = exp13.run_exp13q_cell(
                method=method,
                seed=SMOKE_SEED,
                trace_decisions=False,
            )
            _verify_first_cycle(result)
            rows.append(
                {
                    "method": method,
                    "seed": SMOKE_SEED,
                    "runtime": "PASS",
                    "first_leave_before_message": 201,
                    "first_rejoin_before_message": 251,
                    "churn_target_count": int(result["churn_target_count"]),
                }
            )

    return {
        "scientific_classification": "non-formal bounded integration smoke",
        "seed": SMOKE_SEED,
        "messages": SMOKE_MESSAGES,
        "methods": list(SMOKE_METHODS),
        "churn_level": exp13.CHURN_LEVEL,
        "schedule": [list(targets) for targets in schedule],
        "qahbn2_commit": _git_head(),
        "canonical_ahbn_commit": CANONICAL_AHBN_COMMIT,
        "rows": rows,
        "formal_performance_evidence": False,
    }


def main() -> None:
    result = run_smoke()
    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    output_dir = (
        Path("output")
        / "evidence"
        / f"q-ahbn-{timestamp}-exp13q-smoke"
    )
    output_dir.mkdir(parents=True, exist_ok=False)
    (output_dir / "smoke.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "RUN.md").write_text(
        "# Exp13-Q Bounded Five-Method Smoke\n\n"
        "- Scientific classification: non-formal integration smoke\n"
        f"- Seed: {SMOKE_SEED}\n"
        f"- Messages: {SMOKE_MESSAGES}\n"
        f"- Methods: {', '.join(SMOKE_METHODS)}\n"
        "- Churn: 0.40\n"
        "- Verified boundary: leave before message 201; rejoin before message 251\n"
        f"- Q-AHBN2 commit: {result['qahbn2_commit']}\n"
        f"- Canonical AHBN commit: {CANONICAL_AHBN_COMMIT}\n"
        "- Formal performance evidence: NO\n",
        encoding="utf-8",
    )
    print(output_dir)
    for row in result["rows"]:
        print(
            f"{row['method']}: PASS "
            f"(leave=201, rejoin=251, churn_targets={row['churn_target_count']})"
        )
    print("EXP13Q_BOUNDED_SMOKE_PASS")


if __name__ == "__main__":
    main()
