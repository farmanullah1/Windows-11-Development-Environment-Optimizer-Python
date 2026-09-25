"""Unit test suite for CLI parsing and flag rules."""

import io
import unittest
from unittest.mock import patch
from src.cli import parse_arguments


class TestCLI(unittest.TestCase):
    def test_default_args(self):
        args, valid = parse_arguments([])
        self.assertTrue(valid)
        self.assertFalse(args.apply)
        self.assertFalse(args.dry_run)

    def test_mutually_exclusive_flags(self):
        with patch("sys.stderr", new_callable=io.StringIO):
            args, valid = parse_arguments(["--dry-run", "--apply"])
            self.assertFalse(valid)

    def test_status_flag(self):
        args, valid = parse_arguments(["--status"])
        self.assertTrue(valid)
        self.assertTrue(args.status)

    def test_doctor_flag(self):
        args, valid = parse_arguments(["--doctor"])
        self.assertTrue(valid)
        self.assertTrue(args.doctor)

    def test_rollback_flag(self):
        args, valid = parse_arguments(["--rollback", "RUN-20260925T120000Z"])
        self.assertTrue(valid)
        self.assertEqual(args.rollback, "RUN-20260925T120000Z")


if __name__ == "__main__":
    unittest.main()
