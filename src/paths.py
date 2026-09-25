"""Allowlist and protected paths definitions."""

import os
from pathlib import Path
from typing import List, Set


def get_protected_paths() -> Set[Path]:
    """Returns canonical normalized paths that must NEVER be modified or traversed."""
    protected: Set[Path] = set()

    # System roots
    for env_var in ["SystemRoot", "windir"]:
        val = os.environ.get(env_var)
        if val:
            p = Path(val).resolve()
            protected.add(p)
            protected.add(p / "System32")
            protected.add(p / "WinSxS")
            protected.add(p / "Installer")
            protected.add(p / "Prefetch")
            protected.add(p / "SoftwareDistribution")
            protected.add(p / "Temp")

    # Program roots
    for env_var in ["ProgramFiles", "ProgramFiles(x86)", "ProgramData"]:
        val = os.environ.get(env_var)
        if val:
            protected.add(Path(val).resolve())

    # User Profile personal folders
    userprofile = os.environ.get("USERPROFILE")
    if userprofile:
        up = Path(userprofile).resolve()
        protected.add(up)
        for folder in ["Desktop", "Documents", "Downloads", "Pictures", "Videos", "Music", "OneDrive"]:
            protected.add(up / folder)

    # LocalAppData protected areas
    localappdata = os.environ.get("LOCALAPPDATA")
    if localappdata:
        lap = Path(localappdata).resolve()
        # Protect Brave & Chrome user profile databases
        protected.add(lap / "BraveSoftware" / "Brave-Browser" / "User Data")
        protected.add(lap / "Google" / "Chrome" / "User Data")
        # Protect IDE configurations & workspace storage
        protected.add(lap / "Programs" / "Microsoft VS Code")
        # Docker & WSL
        protected.add(lap / "Docker")

    return protected


def get_cleanup_allowlist() -> List[Path]:
    """Returns specific, pre-approved directory roots eligible for file analysis and quarantine."""
    allowlist: List[Path] = []

    localappdata = os.environ.get("LOCALAPPDATA")
    if localappdata:
        lap = Path(localappdata).resolve()
        # npm cache
        allowlist.append(lap / "npm-cache" / "_cacache")
        # pip cache
        allowlist.append(lap / "pip" / "cache")
        # Scoped user temp
        allowlist.append(lap / "Temp")

    userprofile = os.environ.get("USERPROFILE")
    if userprofile:
        up = Path(userprofile).resolve()
        # Scoped NuGet HTTP cache
        allowlist.append(up / ".nuget" / "packages" / ".tools")

    return allowlist


def is_path_protected(target: Path) -> bool:
    """Evaluates whether target path is protected or located within a protected hierarchy."""
    try:
        real_target = target.resolve()
        # Protect critical dev files and directories by name regardless of path
        name_lower = real_target.name.lower()
        if name_lower in [".git", ".github", ".env", "package.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml"]:
            return True
        if any(part.lower() in [".git", "workspacestorage"] for part in real_target.parts):
            return True
        if real_target.suffix.lower() in [".mdf", ".ndf", ".ldf", ".vhdx", ".vhd", ".sln", ".csproj"]:
            return True

        protected_set = get_protected_paths()
        for p in protected_set:
            if real_target == p or p in real_target.parents:
                return True
    except Exception:
        # Fail closed on path resolution error
        return True
    return False
