"""Scoped cache scanning and official CLI verification commands."""

import os
import time
from pathlib import Path
from typing import Dict, List, Any
from src.paths import get_cleanup_allowlist, is_path_protected
from src.safety import is_reparse_point, is_file_locked, is_contained_in
from src.subprocess_utils import run_safe_subprocess


def inspect_developer_caches() -> Dict[str, Any]:
    """Runs official status commands for development tools (pip, npm, docker)."""
    results: Dict[str, Any] = {}

    # Pip cache status
    pip_code, pip_out, _ = run_safe_subprocess(["python", "-m", "pip", "cache", "info"])
    results["pip"] = pip_out.strip() if pip_code == 0 else "pip cache not accessible"

    # npm cache status
    npm_code, npm_out, _ = run_safe_subprocess(["npm", "cache", "verify"])
    results["npm"] = npm_out.strip() if npm_code == 0 else "npm not accessible"

    # .NET NuGet cache status
    dotnet_code, dotnet_out, _ = run_safe_subprocess(["dotnet", "nuget", "locals", "all", "--list"])
    results["dotnet_nuget"] = dotnet_out.strip() if dotnet_code == 0 else ".NET SDK not installed or not in PATH"

    # Git status verification
    git_code, git_out, _ = run_safe_subprocess(["git", "--version"])
    results["git"] = git_out.strip() if git_code == 0 else "Git not accessible"

    # Docker disk status
    docker_code, docker_out, _ = run_safe_subprocess(["docker", "system", "df"])
    results["docker"] = docker_out.strip() if docker_code == 0 else "docker not running or not accessible"

    return results


def scan_allowlisted_files(min_age_days: int = 7) -> List[Dict[str, Any]]:
    """
    Scans files under allowlisted roots matching safety requirements:
    - Path strictly inside allowlist
    - Not protected
    - Not a junction, symlink, or reparse point
    - Not currently locked
    - Modification age >= min_age_days
    """
    allowlist = get_cleanup_allowlist()
    candidates: List[Dict[str, Any]] = []
    now = time.time()
    cutoff_time = now - (min_age_days * 86400)

    for root in allowlist:
        if not root.is_dir():
            continue

        for dirpath, dirnames, filenames in os.walk(str(root)):
            curr_dir = Path(dirpath)

            # Skip symlinks/junctions in directories
            if is_reparse_point(curr_dir):
                dirnames.clear()
                continue

            for fname in filenames:
                file_path = curr_dir / fname

                if is_reparse_point(file_path):
                    continue

                if is_path_protected(file_path):
                    continue

                # Ensure containment in root
                if not is_contained_in(file_path, root):
                    continue

                try:
                    stat = file_path.stat()
                    if stat.st_mtime < cutoff_time and not is_file_locked(file_path):
                        candidates.append({
                            "path": file_path,
                            "size_bytes": stat.st_size,
                            "mtime": stat.st_mtime,
                            "allowlist_root": str(root),
                        })
                except (OSError, PermissionError):
                    continue

    return candidates
