"""Platform, reparse point, path containment, and privilege verification."""

import os
import sys
import ctypes
from pathlib import Path
from typing import Tuple


def verify_windows_11() -> Tuple[bool, str]:
    """Strictly checks if host OS is Windows 11 (Build >= 22000)."""
    if sys.platform != "win32":
        return False, f"Unsupported OS '{sys.platform}'. Native Windows required."

    try:
        win_ver = sys.getwindowsversion()
        # Windows 11 reports major version 10 with build number >= 22000
        if win_ver.major == 10 and win_ver.build >= 22000:
            return True, f"Windows 11 detected (Build {win_ver.build})"
        elif win_ver.major > 10:
            return True, f"Windows version detected (Major {win_ver.major}, Build {win_ver.build})"
        else:
            return False, f"Windows build {win_ver.build} is below Windows 11 baseline (22000)."
    except Exception as exc:
        return False, f"Failed to query Windows version: {exc}"


def is_elevated() -> bool:
    """Checks whether the current process is running with Administrator rights."""
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin() != 0)
    except Exception:
        return False


def is_reparse_point(path: Path) -> bool:
    """Detects whether a path is a symbolic link, directory junction, or reparse point."""
    try:
        if path.is_symlink():
            return True
        # Check Win32 FILE_ATTRIBUTE_REPARSE_POINT (0x400)
        attrs = ctypes.windll.kernel32.GetFileAttributesW(str(path))
        if attrs != -1 and (attrs & 0x400):
            return True
    except Exception:
        # In case of doubt, fail-closed
        return True
    return False


def is_contained_in(child: Path, parent: Path) -> bool:
    """Ensures child path is canonically strictly inside parent path, preventing traversal."""
    try:
        real_child = child.resolve()
        real_parent = parent.resolve()
        return real_child == real_parent or real_parent in real_child.parents
    except Exception:
        return False


def is_file_locked(path: Path) -> bool:
    """Checks if a file is currently open or locked by another process."""
    if not path.is_file():
        return False
    try:
        # Attempt to open file exclusively in append mode without modifying
        with open(path, "r+b"):
            return False
    except (IOError, PermissionError):
        return True
