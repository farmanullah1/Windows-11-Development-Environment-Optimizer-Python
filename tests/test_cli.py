"""Unit test suite for CLI parsing and flag rules."""

import unittest
from unittest.mock import patch
from src.cli import parse_arguments


class TestCLI(unittest.TestCase):
    def test_default_args(self):
        with patch("sys.argv", ["optimizer.py"]):
            args, valid = parse_arguments()
            self.assertTrue(valid)
            self.assertFalse(args.apply)
            self.assertFalse(args.dry_run)

    def test_mutually_exclusive_flags(self):
        with patch("sys.argv", ["optimizer.py", "--dry-run", "--apply"]):
            args, valid = parse_arguments()
            self.assertFalse(valid)

    def test_status_flag(self):
        with patch("sys.argv", ["optimizer.py", "--status"]):
            args, valid = parse_arguments()
            self.assertTrue(valid)
            self.assertTrue(args.status)


if __name__ == "__main__":
    unittest.main()
