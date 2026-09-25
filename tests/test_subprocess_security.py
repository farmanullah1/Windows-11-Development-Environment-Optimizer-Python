"""Unit test suite for safe subprocess execution and shell=False enforcement."""

import sys
import unittest
from unittest.mock import patch, MagicMock
import subprocess
from src.subprocess_utils import run_safe_subprocess


class TestSubprocessSecurity(unittest.TestCase):
    def test_empty_command_fails_gracefully(self):
        code, out, err = run_safe_subprocess([])
        self.assertEqual(code, 1)
        self.assertIn("No command", err)

    def test_non_existent_command_returns_127(self):
        code, out, err = run_safe_subprocess(["non_existent_binary_xyz_12345"])
        self.assertEqual(code, 127)
        self.assertIn("not installed", err)

    def test_python_executable_resolution(self):
        with patch("shutil.which", return_value=sys.executable), patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="Python 3.x", stderr="")
            code, out, err = run_safe_subprocess(["python", "--version"])
            self.assertEqual(code, 0)
            mock_run.assert_called_once()
            called_args = mock_run.call_args[0][0]
            self.assertEqual(called_args[0], sys.executable)
            # Verify shell=False is enforced
            self.assertFalse(mock_run.call_args[1].get("shell", True))

    def test_timeout_handling(self):
        with patch("shutil.which", return_value="/bin/sleep"), patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd=["sleep"], timeout=1)):
            code, out, err = run_safe_subprocess(["sleep", "10"], timeout_seconds=1)
            self.assertEqual(code, 124)
            self.assertIn("timed out", err)


if __name__ == "__main__":
    unittest.main()
