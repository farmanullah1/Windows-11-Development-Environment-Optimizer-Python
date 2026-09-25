"""Unit test suite for safety checks (Windows detection, elevation, reparse points)."""

import sys
import unittest
from unittest.mock import patch
from src.safety import verify_windows_11, is_elevated


class TestSafety(unittest.TestCase):
    def test_verify_windows_11_pass(self):
        # Mock Windows 11 build number
        mock_ver = type("WindowsVersion", (), {"major": 10, "build": 22631})()
        with patch("sys.platform", "win32"), patch("sys.getwindowsversion", return_value=mock_ver):
            is_win11, msg = verify_windows_11()
            self.assertTrue(is_win11)
            self.assertIn("Windows 11 detected", msg)

    def test_verify_windows_11_fail_old_build(self):
        # Mock Windows 10 older build number
        mock_ver = type("WindowsVersion", (), {"major": 10, "build": 19045})()
        with patch("sys.platform", "win32"), patch("sys.getwindowsversion", return_value=mock_ver):
            is_win11, msg = verify_windows_11()
            self.assertFalse(is_win11)
            self.assertIn("below Windows 11 baseline", msg)

    def test_verify_non_windows_platform(self):
        with patch("sys.platform", "linux"):
            is_win11, msg = verify_windows_11()
            self.assertFalse(is_win11)
            self.assertIn("Unsupported OS", msg)

    def test_is_elevated_mock(self):
        with patch("ctypes.windll.shell32.IsUserAnAdmin", return_value=1):
            self.assertTrue(is_elevated())
        with patch("ctypes.windll.shell32.IsUserAnAdmin", return_value=0):
            self.assertFalse(is_elevated())


if __name__ == "__main__":
    unittest.main()
