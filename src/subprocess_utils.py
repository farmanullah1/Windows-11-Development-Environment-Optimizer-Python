"""Safe subprocess runner with shell=False, timeout gating, and sys.executable resolution."""

import sys
import shutil
import subprocess
from typing import List, Optional, Tuple


def run_safe_subprocess(
    args: List[str],
    timeout_seconds: int = 30,
) -> Tuple[int, str, str]:
    """
    Executes a subprocess safely.
    - Uses shell=False
    - Checks executable existence
    - Enforces timeout
    - Replaces bare 'python' with sys.executable
    """
    if not args:
        return 1, "", "No command arguments provided."

    cmd = list(args)

    # Protect against Windows App Execution Alias by using sys.executable
    if cmd[0].lower() in ["python", "py", "python3"]:
        cmd[0] = sys.executable

    # Ensure binary exists on PATH or is absolute
    executable = shutil.which(cmd[0])
    if not executable:
        return 127, "", f"[SKIPPED] Command '{cmd[0]}' is not installed or not in PATH."

    try:
        proc = subprocess.run(
            cmd,
            shell=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"Command '{cmd[0]}' timed out after {timeout_seconds} seconds."
    except Exception as exc:
        return 1, "", f"Failed to execute command '{cmd[0]}': {exc}"
