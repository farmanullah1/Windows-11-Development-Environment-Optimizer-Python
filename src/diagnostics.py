"""Diagnostics and resource inspection (Read-Only)."""

import os
import shutil
from pathlib import Path
from typing import Dict, Any, List
from src.safety import verify_windows_11, is_elevated


def get_system_diagnostics() -> Dict[str, Any]:
    """Collects non-invasive system resource metrics."""
    diag: Dict[str, Any] = {}

    is_win11, win_msg = verify_windows_11()
    diag["windows_detected"] = win_msg
    diag["is_windows_11"] = is_win11
    diag["is_elevated"] = is_elevated()

    # CPU Information
    try:
        diag["cpu_count"] = os.cpu_count() or 1
        diag["cpu_architecture"] = os.environ.get("PROCESSOR_ARCHITECTURE", "Unknown")
        diag["cpu_identifier"] = os.environ.get("PROCESSOR_IDENTIFIER", "Unknown")
    except Exception:
        diag["cpu_count"] = 1
        diag["cpu_architecture"] = "Unknown"
        diag["cpu_identifier"] = "Unknown"

    # Disk space on system drive (normalized with root anchor)
    system_drive = os.environ.get("SystemDrive", "C:")
    system_drive_root = f"{system_drive.rstrip('\\')}\\"
    try:
        usage = shutil.disk_usage(system_drive_root)
        diag["disk_total_gb"] = round(usage.total / (1024**3), 2)
        diag["disk_free_gb"] = round(usage.free / (1024**3), 2)
        diag["disk_used_percent"] = round((usage.used / usage.total) * 100, 1)
    except Exception:
        diag["disk_total_gb"] = 0
        diag["disk_free_gb"] = 0
        diag["disk_used_percent"] = 0

    # Enumerate all fixed drives and Windows 11 Dev Drives
    disks: List[Dict[str, Any]] = []
    try:
        import ctypes
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for i in range(26):
            if bitmask & (1 << i):
                drive_letter = f"{chr(65 + i)}:\\"
                drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive_letter)
                if drive_type == 3:  # DRIVE_FIXED
                    try:
                        u = shutil.disk_usage(drive_letter)
                        fs_buf = ctypes.create_unicode_buffer(1024)
                        ctypes.windll.kernel32.GetVolumeInformationW(
                            drive_letter, None, 0, None, None, None, fs_buf, 1024
                        )
                        fs_name = fs_buf.value
                        is_dev_drive = (fs_name.upper() == "REFS")
                        disks.append({
                            "drive": drive_letter,
                            "fs_type": fs_name,
                            "is_dev_drive": is_dev_drive,
                            "total_gb": round(u.total / (1024**3), 2),
                            "free_gb": round(u.free / (1024**3), 2),
                            "used_percent": round((u.used / u.total) * 100, 1),
                        })
                    except Exception:
                        continue
    except Exception:
        pass
    diag["disks"] = disks

    # System Memory (RAM) & Commit Charge via Win32 ctypes
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
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            diag["ram_total_gb"] = round(stat.ullTotalPhys / (1024**3), 2)
            diag["ram_free_gb"] = round(stat.ullAvailPhys / (1024**3), 2)
            diag["ram_used_percent"] = stat.dwMemoryLoad

            # Commit Charge (Total commit limit vs commit available)
            diag["commit_total_gb"] = round(stat.ullTotalPageFile / (1024**3), 2)
            diag["commit_free_gb"] = round(stat.ullAvailPageFile / (1024**3), 2)
            if stat.ullTotalPageFile > 0:
                commit_used = stat.ullTotalPageFile - stat.ullAvailPageFile
                diag["commit_used_percent"] = round((commit_used / stat.ullTotalPageFile) * 100, 1)
            else:
                diag["commit_used_percent"] = 0
        else:
            diag["ram_total_gb"] = 0
            diag["ram_free_gb"] = 0
            diag["ram_used_percent"] = 0
            diag["commit_total_gb"] = 0
            diag["commit_free_gb"] = 0
            diag["commit_used_percent"] = 0
    except Exception:
        diag["ram_total_gb"] = 0
        diag["ram_free_gb"] = 0
        diag["ram_used_percent"] = 0
        diag["commit_total_gb"] = 0
        diag["commit_free_gb"] = 0
        diag["commit_used_percent"] = 0

    return diag
