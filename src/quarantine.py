"""Quarantine manager and manifest recorder."""

import os
import json
import shutil
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def calculate_sha256(file_path: Path) -> str:
    """Calculates SHA-256 hash of a file."""
    h = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def get_quarantine_root() -> Path:
    r"""Returns %LOCALAPPDATA%\Win11DevOptimizer\quarantine."""
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    if not local_app_data:
        local_app_data = str(Path.home() / "AppData" / "Local")
    return Path(local_app_data) / "Win11DevOptimizer" / "quarantine"


def check_free_space(dest_drive_path: Path, required_bytes: int) -> bool:
    """Verifies destination drive has at least 2x the required free space."""
    try:
        usage = shutil.disk_usage(str(dest_drive_path))
        # Ensure free space is at least 2x required, minimum 50MB
        safety_margin = max(required_bytes * 2, 50 * 1024 * 1024)
        return usage.free >= safety_margin
    except Exception:
        return False


class QuarantineManager:
    """Handles file isolation and manifest creation."""

    def __init__(self, run_id: Optional[str] = None):
        if not run_id:
            now_str = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            self.run_id = f"RUN-{now_str}"
        else:
            self.run_id = run_id

        self.quarantine_dir = get_quarantine_root() / self.run_id
        self.manifest_path = self.quarantine_dir / "manifest.json"
        self.manifest: Dict = {
            "run_id": self.run_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "files": [],
            "status": "in_progress",
        }

    def quarantine_file(self, source_path: Path) -> Tuple[bool, str]:
        """Moves source file to quarantine and logs in manifest."""
        try:
            if not source_path.is_file():
                return False, "Not a regular file"

            file_stat = source_path.stat()
            file_size = file_stat.st_size
            file_mtime = file_stat.st_mtime
            resolved_orig = str(source_path.resolve())

            self.quarantine_dir.mkdir(parents=True, exist_ok=True)

            if not check_free_space(self.quarantine_dir, file_size):
                return False, "Insufficient free space on quarantine drive"

            # Compute sha256 before move
            file_hash = calculate_sha256(source_path)

            # Generate collision-safe target name in quarantine
            dest_name = f"{source_path.stem}_{file_hash[:8]}{source_path.suffix}"
            dest_path = self.quarantine_dir / dest_name

            shutil.move(str(source_path), str(dest_path))

            self.manifest["files"].append({
                "original_path": resolved_orig,
                "quarantine_path": str(dest_path.resolve()),
                "size_bytes": file_size,
                "sha256": file_hash,
                "mtime": file_mtime,
            })
            self._save_manifest()
            return True, str(dest_path)
        except Exception as exc:
            return False, str(exc)

    def _save_manifest(self) -> None:
        try:
            with open(self.manifest_path, "w", encoding="utf-8") as f:
                json.dump(self.manifest, f, indent=2)
        except Exception:
            pass

    def finalize(self) -> None:
        self.manifest["status"] = "completed"
        self._save_manifest()
