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

    # System Memory (RAM) via Win32 ctypes
    try:
        import ctypes

        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            diag["ram_total_gb"] = round(stat.ullTotalPhys / (1024**3), 2)
            diag["ram_free_gb"] = round(stat.ullAvailPhys / (1024**3), 2)
            diag["ram_used_percent"] = stat.dwMemoryLoad
        else:
            diag["ram_total_gb"] = 0
            diag["ram_free_gb"] = 0
            diag["ram_used_percent"] = 0
    except Exception:
        diag["ram_total_gb"] = 0
        diag["ram_free_gb"] = 0
        diag["ram_used_percent"] = 0

    return diag
