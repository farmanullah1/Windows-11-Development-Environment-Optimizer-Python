"""Rollback engine to restore files from quarantine manifests."""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple
from src.quarantine import calculate_sha256, get_quarantine_root


def list_available_runs() -> List[str]:
    """Lists all available quarantine run IDs."""
    root = get_quarantine_root()
    if not root.is_dir():
        return []
    return [d.name for d in root.iterdir() if d.is_dir() and (d / "manifest.json").exists()]


def execute_rollback(run_id: str) -> Tuple[bool, List[str]]:
    """Restores files from a specific quarantine run to their original locations."""
    run_dir = get_quarantine_root() / run_id
    manifest_file = run_dir / "manifest.json"

    if not manifest_file.is_file():
        return False, [f"[ERROR] Run ID '{run_id}' not found or manifest missing."]

    try:
        with open(manifest_file, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as exc:
        return False, [f"[ERROR] Failed to read manifest: {exc}"]

    results: List[str] = []
    restored_count = 0

    for item in manifest.get("files", []):
        orig_path = Path(item["original_path"])
        quar_path = Path(item["quarantine_path"])
        expected_hash = item.get("sha256", "")

        if not quar_path.is_file():
            results.append(f"[SKIPPED] Quarantined file not found: {quar_path.name}")
            continue

        # Integrity verification
        actual_hash = calculate_sha256(quar_path)
        if expected_hash and actual_hash != expected_hash:
            results.append(f"[ERROR] Hash mismatch for {quar_path.name}. Skipping rollback.")
            continue

        # Prevent overwriting if original location now contains a newer user file
        if orig_path.exists():
            results.append(f"[WARNING] Original path already exists: {orig_path}. Skipping to prevent data loss.")
            continue

        try:
            orig_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(quar_path), str(orig_path))
            results.append(f"[SUCCESS] Restored: {orig_path}")
            restored_count += 1
        except Exception as exc:
            results.append(f"[ERROR] Failed to restore {orig_path}: {exc}")

    results.append(f"[ACTION] Rollback finished: {restored_count} files restored.")
    return True, results
