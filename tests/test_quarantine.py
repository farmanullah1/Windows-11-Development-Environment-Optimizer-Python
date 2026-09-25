"""Unit test suite for quarantine isolation and SHA-256 calculation."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.quarantine import QuarantineManager, calculate_sha256


class TestQuarantine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "test_cache.tmp"
        self.test_file.write_text("dummy cache contents", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_calculate_sha256(self):
        file_hash = calculate_sha256(self.test_file)
        self.assertEqual(len(file_hash), 64)

    def test_quarantine_manifest_generation(self):
        qm = QuarantineManager(run_id="TEST-RUN-001")
        self.assertEqual(qm.run_id, "TEST-RUN-001")
        self.assertEqual(qm.manifest["status"], "in_progress")

    def test_quarantine_file_move_and_manifest(self):
        quar_base = Path(self.temp_dir.name) / "quarantine_root"
        with patch("src.quarantine.get_quarantine_root", return_value=quar_base):
            qm = QuarantineManager(run_id="TEST-RUN-MOVE")
            ok, dest_path = qm.quarantine_file(self.test_file)
            self.assertTrue(ok)
            self.assertFalse(self.test_file.exists())
            self.assertTrue(Path(dest_path).exists())
            self.assertEqual(len(qm.manifest["files"]), 1)
            entry = qm.manifest["files"][0]
            self.assertEqual(entry["original_path"], str(self.test_file.resolve()))
            self.assertEqual(entry["size_bytes"], len("dummy cache contents"))
            self.assertGreater(entry["mtime"], 0)
            qm.finalize()
            self.assertEqual(qm.manifest["status"], "completed")


if __name__ == "__main__":
    unittest.main()
