"""Unit test suite for configuration loading, fallbacks, and safety bounds."""

import json
import tempfile
import unittest
from pathlib import Path
from src.config import load_config, DEFAULT_CONFIG


class TestConfig(unittest.TestCase):
    def test_missing_config_returns_defaults(self):
        cfg = load_config(Path("C:/non_existent_config.json"))
        self.assertEqual(cfg, DEFAULT_CONFIG)

    def test_corrupted_config_returns_defaults(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write("{ invalid json")
            f_path = Path(f.name)
        cfg = load_config(f_path)
        self.assertEqual(cfg, DEFAULT_CONFIG)

    def test_minimum_age_days_safety_floor(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            json.dump({"minimum_age_days": 1}, f)
            f_path = Path(f.name)
        cfg = load_config(f_path)
        # Cannot be set below safety baseline of 7 days
        self.assertEqual(cfg["minimum_age_days"], 7)


if __name__ == "__main__":
    unittest.main()
