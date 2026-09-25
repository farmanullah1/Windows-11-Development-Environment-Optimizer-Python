"""Diagnostics and resource inspection (Read-Only)."""

import os
import shutil
from typing import Dict, Any
from src.safety import verify_windows_11, is_elevated


def get_system_diagnostics() -> Dict[str, Any]:
    """Collects non-invasive system resource metrics."""
    diag: Dict[str, Any] = {}

    is_win11, win_msg = verify_windows_11()
    diag["windows_detected"] = win_msg
    diag["is_windows_11"] = is_win11
    diag["is_elevated"] = is_elevated()

    # Disk space on system drive
    system_drive = os.environ.get("SystemDrive", "C:")
    try:
        usage = shutil.disk_usage(system_drive)
        diag["disk_total_gb"] = round(usage.total / (1024**3), 2)
        diag["disk_free_gb"] = round(usage.free / (1024**3), 2)
        diag["disk_used_percent"] = round((usage.used / usage.total) * 100, 1)
    except Exception:
        diag["disk_total_gb"] = 0
        diag["disk_free_gb"] = 0
        diag["disk_used_percent"] = 0

    return diag
