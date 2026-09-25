"""Unit test suite for rollback restoration and conflict detection."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.quarantine import calculate_sha256
from src.rollback import execute_rollback, list_available_runs


class TestRollback(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.quar_root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_missing_run_id_returns_error(self):
        with patch("src.rollback.get_quarantine_root", return_value=self.quar_root):
            success, messages = execute_rollback("NON_EXISTENT_RUN")
            self.assertFalse(success)
            self.assertTrue(any("not found" in m for m in messages))

    def test_successful_rollback(self):
        run_id = "TEST-RUN-ROLLBACK"
        run_dir = self.quar_root / run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        orig_dest = Path(self.temp_dir.name) / "restored_cache.tmp"
        quar_file = run_dir / "restored_cache_12345678.tmp"
        quar_file.write_text("test rollback data", encoding="utf-8")
        file_hash = calculate_sha256(quar_file)

        manifest_data = {
            "run_id": run_id,
            "status": "completed",
            "files": [
                {
                    "original_path": str(orig_dest),
                    "quarantine_path": str(quar_file),
                    "size_bytes": quar_file.stat().st_size,
                    "sha256": file_hash,
                }
            ],
        }
        (run_dir / "manifest.json").write_text(json.dumps(manifest_data), encoding="utf-8")

        with patch("src.rollback.get_quarantine_root", return_value=self.quar_root):
            runs = list_available_runs()
            self.assertIn(run_id, runs)

            success, messages = execute_rollback(run_id)
            self.assertTrue(success)
            self.assertTrue(orig_dest.exists())
            self.assertEqual(orig_dest.read_text(encoding="utf-8"), "test rollback data")
            self.assertFalse(quar_file.exists())


if __name__ == "__main__":
    unittest.main()
