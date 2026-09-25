#!/usr/bin/env python3
"""
Windows 11 Development Environment Optimizer
Entry point coordinating fail-closed execution, dry-run simulation, and quarantine operations.
"""

import sys
import json
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.cli import parse_arguments
from src.config import load_config
from src.safety import verify_windows_11, is_elevated
from src.diagnostics import get_system_diagnostics
from src.process_manager import list_active_dev_processes
from src.power import get_active_power_plan
from src.cache_manager import scan_allowlisted_files, inspect_developer_caches
from src.quarantine import QuarantineManager, get_quarantine_root
from src.rollback import execute_rollback, list_available_runs
from src.logging_utils import setup_logger


def main() -> int:
    args, is_valid = parse_arguments()
    if not is_valid:
        return 1

    config = load_config(PROJECT_ROOT / "config" / "default_config.json")
    logger = setup_logger(log_level=config.get("log_level", "normal"))

    # Strict Windows 11 platform check
    is_win11, win_msg = verify_windows_11()
    if not is_win11:
        print(f"[ERROR] {win_msg}")
        return 1

    # Status Mode
    if getattr(args, "status", False):
        print("[CHECK] System Status")
        diag = get_system_diagnostics()
        print(f"  OS: {diag['windows_detected']}")
        print(f"  Admin: {'Yes' if diag['is_elevated'] else 'No (Standard User)'}")
        print(f"  System Disk: {diag['disk_free_gb']} GB free ({diag['disk_used_percent']}% used)")
        if diag.get("ram_total_gb"):
            print(f"  System RAM: {diag['ram_free_gb']} GB free of {diag['ram_total_gb']} GB ({diag['ram_used_percent']}% used)")
        guid, name = get_active_power_plan()
        print(f"  Active Power Plan: {name or 'Unknown'} ({guid or 'N/A'})")
        procs = list_active_dev_processes()
        print(f"  Active Dev Processes: {len(procs)}")
        for p in procs[:5]:
            print(f"    - {p['name']} (PID: {p['pid']}, RAM: {p['mem_usage']})")
        return 0

    # Doctor Mode
    if getattr(args, "doctor", False):
        print("[CHECK] Workstation Health & Prerequisite Verification")
        print(f"[SAFE] Windows 11 Compatibility: OK")
        print(f"[SAFE] Elevation Status: {'Running as Administrator' if is_elevated() else 'Standard User (Recommended)'}")
        caches = inspect_developer_caches()
        for tool, status in caches.items():
            print(f"[CHECK] {tool.upper()}: {status.splitlines()[0] if status else 'Not available'}")
        return 0

    # Rollback Mode
    if getattr(args, "rollback", None):
        run_id = args.rollback
        print(f"[ACTION] Initiating rollback for run ID '{run_id}'...")
        success, messages = execute_rollback(run_id)
        for msg in messages:
            print(msg)
        return 0 if success else 1

    # Purge Quarantine Mode
    if getattr(args, "purge_quarantine", False):
        print("[WARNING] This operation will permanently delete all quarantined data.")
        print("Type 'PURGE QUARANTINE' to confirm:")
        try:
            confirmation = input("> ").strip()
            if confirmation != "PURGE QUARANTINE":
                print("[SKIPPED] Purge cancelled. Confirmation did not match.")
                return 0
            # Purge execution
            quar_root = get_quarantine_root()
            if quar_root.is_dir():
                import shutil
                shutil.rmtree(str(quar_root))
                print("[SUCCESS] Quarantine directory purged successfully.")
            else:
                print("[SAFE] Quarantine directory is already empty.")
        except EOFError:
            print("[SKIPPED] Purge cancelled.")
        return 0

    # Default / Plan / Dry-Run / Apply Mode
    is_apply = getattr(args, "apply", False)
    min_age = config.get("minimum_age_days", 7)

    if not is_apply:
        print("[SAFE] Running in DRY-RUN mode. Zero system modifications will be made.")
    else:
        print("[ACTION] Running in APPLY mode.")

    print(f"[CHECK] Scanning allowlisted caches for files unmodified for >= {min_age} days...")
    candidates = scan_allowlisted_files(min_age_days=min_age)
    total_bytes = sum(c["size_bytes"] for c in candidates)
    total_mb = round(total_bytes / (1024 * 1024), 2)

    if getattr(args, "json", False):
        output = {
            "mode": "apply" if is_apply else "dry_run",
            "total_candidates": len(candidates),
            "total_size_mb": total_mb,
            "files": [str(c["path"]) for c in candidates],
        }
        print(json.dumps(output, indent=2))
        return 0

    print(f"[SAFE] Found {len(candidates)} eligible files totaling {total_mb} MB.")

    if not is_apply:
        print("[SAFE] Dry-run complete. Run with --apply to move eligible files to quarantine.")
        return 0

    # Apply Mode confirmation
    if not getattr(args, "yes", False):
        print(f"[WARNING] You are about to quarantine {len(candidates)} files ({total_mb} MB).")
        try:
            resp = input("Proceed? [y/N]: ").strip().lower()
            if resp != "y":
                print("[SKIPPED] Operation cancelled by user.")
                return 0
        except EOFError:
            print("[SKIPPED] Operation cancelled.")
            return 0

    # Execute Quarantine Isolation
    qm = QuarantineManager()
    quarantined_count = 0
    for c in candidates:
        ok, res = qm.quarantine_file(c["path"])
        if ok:
            quarantined_count += 1
        else:
            print(f"[SKIPPED] {c['path'].name}: {res}")

    qm.finalize()
    print(f"[SUCCESS] Quarantined {quarantined_count} files into run ID '{qm.run_id}'.")
    print(f"[ACTION] To restore these files at any time, run: python optimizer.py --rollback {qm.run_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
