"""Unit test suite for quarantine isolation and SHA-256 calculation."""

import tempfile
import unittest
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
