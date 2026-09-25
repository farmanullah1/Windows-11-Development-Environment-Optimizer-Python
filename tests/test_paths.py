"""Unit test suite for path safety and containment."""

import os
import unittest
from pathlib import Path
from src.safety import is_contained_in
from src.paths import is_path_protected, get_cleanup_allowlist


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

    def test_user_personal_folders_protected(self):
        userprofile = os.environ.get("USERPROFILE", "C:/Users/TestUser")
        up = Path(userprofile)
        self.assertTrue(is_path_protected(up))
        self.assertTrue(is_path_protected(up / "Desktop" / "notes.txt"))
        self.assertTrue(is_path_protected(up / "Documents" / "project" / "code.cs"))

    def test_allowlisted_cache_not_blocked_by_userprofile(self):
        localappdata = os.environ.get("LOCALAPPDATA")
        if localappdata:
            cache_file = Path(localappdata) / "npm-cache" / "_cacache" / "content-v2" / "sample.tmp"
            self.assertFalse(is_path_protected(cache_file))

    def test_sensitive_file_inside_allowlist_still_protected(self):
        localappdata = os.environ.get("LOCALAPPDATA")
        if localappdata:
            bad_file = Path(localappdata) / "npm-cache" / "_cacache" / ".env"
            self.assertTrue(is_path_protected(bad_file))


if __name__ == "__main__":
    unittest.main()
