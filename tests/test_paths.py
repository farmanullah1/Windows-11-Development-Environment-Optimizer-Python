"""Unit test suite for path safety and containment."""

import unittest
from pathlib import Path
from src.safety import is_contained_in
from src.paths import is_path_protected


class TestPathSafety(unittest.TestCase):
    def test_containment_positive(self):
        parent = Path("C:/SafeRoot/Cache")
        child = Path("C:/SafeRoot/Cache/sub/file.txt")
        self.assertTrue(is_contained_in(child, parent))

    def test_containment_traversal_negative(self):
        parent = Path("C:/SafeRoot/Cache")
        child = Path("C:/SafeRoot/Cache/../../Windows/System32")
        self.assertFalse(is_contained_in(child, parent))

    def test_critical_files_protected(self):
        self.assertTrue(is_path_protected(Path("C:/MyProject/.git/config")))
        self.assertTrue(is_path_protected(Path("C:/MyProject/.env")))
        self.assertTrue(is_path_protected(Path("C:/MyProject/package-lock.json")))
        self.assertTrue(is_path_protected(Path("C:/Databases/data.mdf")))


if __name__ == "__main__":
    unittest.main()
