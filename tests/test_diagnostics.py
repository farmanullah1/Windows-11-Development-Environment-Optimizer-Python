"""Unit test suite for diagnostics and system inspection."""

import unittest
from unittest.mock import patch
from src.diagnostics import get_system_diagnostics


class TestDiagnostics(unittest.TestCase):
    def test_get_system_diagnostics_keys(self):
        diag = get_system_diagnostics()
        self.assertIsInstance(diag, dict)
        self.assertIn("windows_detected", diag)
        self.assertIn("is_windows_11", diag)
        self.assertIn("is_elevated", diag)
        self.assertIn("cpu_count", diag)
        self.assertIn("cpu_architecture", diag)
        self.assertIn("cpu_identifier", diag)
        self.assertIn("disk_total_gb", diag)
        self.assertIn("disk_free_gb", diag)
        self.assertIn("disk_used_percent", diag)
        self.assertIn("disks", diag)
        self.assertIn("ram_total_gb", diag)
        self.assertIn("ram_free_gb", diag)
        self.assertIn("ram_used_percent", diag)
        self.assertIn("commit_total_gb", diag)
        self.assertIn("commit_free_gb", diag)
        self.assertIn("commit_used_percent", diag)

    def test_cpu_metrics_valid(self):
        diag = get_system_diagnostics()
        self.assertGreaterEqual(diag["cpu_count"], 1)
        self.assertIsInstance(diag["cpu_architecture"], str)

    def test_disk_usage_fallback_on_error(self):
        with patch("shutil.disk_usage", side_effect=OSError("Drive not accessible")):
            diag = get_system_diagnostics()
            self.assertEqual(diag["disk_total_gb"], 0)
            self.assertEqual(diag["disk_free_gb"], 0)
            self.assertEqual(diag["disk_used_percent"], 0)


if __name__ == "__main__":
    unittest.main()
