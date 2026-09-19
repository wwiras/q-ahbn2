import json
import os
from datetime import datetime
from pathlib import Path


def main():
    repo_root = Path(__file__).resolve().parent.parent
    output_base = repo_root / "output"
    output_base.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    run_dir_name = f"q-ahbn-{timestamp}-workflow-smoke"
    run_dir = output_base / run_dir_name
    run_dir.mkdir(parents=True, exist_ok=True)

    manifest_data = {
        "project": "Q-AHBN2",
        "event": "workflow-smoke",
        "status": "PASS",
        "timestamp": timestamp,
    }

    manifest_path = run_dir / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    run_md_path = run_dir / "RUN.md"
    run_md_content = f"""# Q-AHBN2 Workflow Smoke Test Run

- Project: {manifest_data["project"]}
- Event: {manifest_data["event"]}
- Status: {manifest_data["status"]}
- Timestamp: {timestamp}
- Directory: {run_dir_name}
"""
    with open(run_md_path, "w", encoding="utf-8") as f:
        f.write(run_md_content)

    print(str(run_dir))


if __name__ == "__main__":
    main()
