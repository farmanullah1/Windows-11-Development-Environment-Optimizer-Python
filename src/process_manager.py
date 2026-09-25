"""Process information and diagnostics without aggressive termination."""

import os
from typing import List, Dict, Any
from src.subprocess_utils import run_safe_subprocess


def list_active_dev_processes() -> List[Dict[str, Any]]:
    """Inspects running Node.js / Python developer processes via tasklist."""
    code, stdout, _ = run_safe_subprocess(["tasklist", "/FO", "CSV", "/NH"])
    if code != 0:
        return []

    dev_names = {
        "node.exe",
        "python.exe",
        "dotnet.exe",
        "brave.exe",
        "docker desktop.exe",
        "postman.exe",
        "code.exe",
        "sqlservr.exe",
    }
    found = []

    for line in stdout.splitlines():
        line = line.strip()
        if not line or not line.startswith('"'):
            continue
        parts = [p.strip('"') for p in line.split('","')]
        if len(parts) >= 2:
            proc_name = parts[0].lower()
            if proc_name in dev_names:
                found.append({
                    "name": parts[0],
                    "pid": parts[1],
                    "mem_usage": parts[4] if len(parts) > 4 else "N/A",
                })
    return found
