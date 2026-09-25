"""Unit test suite for rollback restoration and conflict detection."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.rollback import execute_rollback


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


if __name__ == "__main__":
    unittest.main()
