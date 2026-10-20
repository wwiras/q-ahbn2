from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from gke.scripts import audit_d8_i1_sha256 as audit


class Sha256StreamTests(unittest.TestCase):
    def test_known_sha256_vectors(self) -> None:
        self.assertEqual(
            hashlib.sha256(b"").hexdigest(),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        self.assertEqual(
            hashlib.sha256(b"abc").hexdigest(),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )

    def test_empty_and_binary_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            empty = Path(temporary) / "empty.bin"
            binary = Path(temporary) / "binary.bin"
            empty.write_bytes(b"")
            binary.write_bytes(b"\x00\xff\x10\x80")
            self.assertEqual(audit.sha256_stream(empty)[0], hashlib.sha256(b"").hexdigest())
            self.assertEqual(
                audit.sha256_stream(binary)[0],
                hashlib.sha256(b"\x00\xff\x10\x80").hexdigest(),
            )

    def test_large_file_is_hashed_in_chunks(self) -> None:
        data = bytes(range(256)) * 20000
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "large.bin"
            path.write_bytes(data)
            digest, size, _ = audit.sha256_stream(path, chunk_size=4096)
        self.assertEqual(size, len(data))
        self.assertEqual(digest, hashlib.sha256(data).hexdigest())


class CampaignAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.root_name = "formal-seed42"
        self.root = self.base / self.root_name
        self.run = self.root / "runs" / "seed42" / "qahbn2"
        self.run.mkdir(parents=True)
        (self.run / "manifest.json").write_bytes(b"original")
        (self.run / "metrics.json").write_bytes(b"\x00\xff")
        self.output = self.base / "audit"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_audit(self, **kwargs: object) -> dict[str, object]:
        return audit.audit_campaign(
            {self.root_name: (self.root, 42)},
            self.output,
            methods=("qahbn2",),
            required_files=("manifest.json", "metrics.json"),
            **kwargs,
        )

    def test_expected_files_are_reconciled_and_baseline_is_not_a_match(self) -> None:
        summary = self.run_audit()
        self.assertEqual(summary["expected_primary_files"], 2)
        self.assertEqual(summary["files_discovered"], 2)
        self.assertEqual(summary["files_hashed"], 2)
        self.assertEqual(
            summary["comparison_status_counts"]["BASELINE_UNAVAILABLE"], 2
        )
        self.assertEqual(summary["decision"], "CURRENT-STATE BASELINE COMPLETE")

    def test_modified_file_mismatches_trusted_reference(self) -> None:
        relative = f"{self.root_name}/runs/seed42/qahbn2/manifest.json"
        reference = hashlib.sha256(b"before edit").hexdigest()
        summary = self.run_audit(historical_references={relative: reference})
        statuses = {
            row["relative_path"]: row["comparison_status"]
            for row in json.loads((self.output / "sha256_current.json").read_text())["files"]
        }
        self.assertEqual(statuses[relative], "MISMATCH")
        self.assertEqual(summary["decision"], "INTEGRITY DISCREPANCY")

    def test_missing_file_is_reported(self) -> None:
        (self.run / "manifest.json").unlink()
        summary = self.run_audit()
        self.assertEqual(summary["comparison_status_counts"]["MISSING"], 1)
        self.assertEqual(summary["decision"], "AUDIT INCOMPLETE")

    def test_inaccessible_file_is_reported(self) -> None:
        original = audit.sha256_stream

        def fail_for_metrics(path: Path, chunk_size: int = audit.CHUNK_SIZE):
            if path.name == "metrics.json":
                raise PermissionError("fixture denies read")
            return original(path, chunk_size)

        with mock.patch.object(audit, "sha256_stream", side_effect=fail_for_metrics):
            summary = self.run_audit()
        self.assertEqual(summary["comparison_status_counts"]["READ_ERROR"], 1)
        self.assertEqual(summary["decision"], "AUDIT INCOMPLETE")

    def test_interrupted_scan_resumes_and_revalidates_completed_records(self) -> None:
        with self.assertRaises(audit.AuditInterrupted):
            audit.audit_campaign(
                {self.root_name: (self.root, 42)},
                self.output,
                methods=("qahbn2",),
                required_files=("manifest.json", "metrics.json"),
                stop_after=1,
            )
        summary = self.run_audit()
        inventory = json.loads((self.output / "sha256_current.json").read_text())
        self.assertEqual(summary["files_hashed"], 2)
        self.assertTrue(
            any(record.get("resume_revalidated") for record in inventory["files"])
        )

    def test_extras_are_classified_and_included_in_scanned_total(self) -> None:
        extra = self.run / "notes.txt"
        extra.write_text("unexpected")
        summary = self.run_audit()
        self.assertEqual(summary["files_discovered"], 3)
        self.assertEqual(summary["files_hashed"], 3)
        self.assertEqual(summary["comparison_status_counts"]["EXTRA"], 1)

    def test_output_inside_evidence_root_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            audit.audit_campaign(
                {self.root_name: (self.root, 42)},
                self.root / "generated-audit",
                methods=("qahbn2",),
                required_files=("manifest.json",),
            )


if __name__ == "__main__":
    unittest.main()
