"""Windows power plan inspection and reversible switching."""

import re
from typing import Dict, Optional, Tuple
from src.subprocess_utils import run_safe_subprocess


def get_active_power_plan() -> Tuple[Optional[str], Optional[str]]:
    """Retrieves current active power scheme GUID and name."""
    code, stdout, _ = run_safe_subprocess(["powercfg", "/getactivescheme"])
    if code != 0:
        return None, None

    # Matches: Power Scheme GUID: 381b4222-f694-41f0-9685-ff5bb260df2e  (Balanced)
    match = re.search(r"GUID:\s+([a-f0-9\-]+)\s+\((.+?)\)", stdout, re.IGNORECASE)
    if match:
        return match.group(1), match.group(2)
    return None, None
