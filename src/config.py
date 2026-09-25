"""Configuration parsing and schema validation."""

import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "dry_run": True,
    "require_confirmation": True,
    "minimum_age_days": 7,
    "quarantine_enabled": True,
    "permanent_delete": False,
    "process_termination": False,
    "service_changes": False,
    "docker_cleanup": false_if_any := False,
    "sql_server_changes": False,
    "browser_cache_cleanup": False,
    "power_plan_change": False,
    "registry_changes": False,
    "network_changes": False,
    "external_network_access": False,
    "log_level": "normal",
}


def load_config(config_path: Path) -> Dict[str, Any]:
    """Loads configuration with fail-closed defaults and strict schema checks."""
    config = DEFAULT_CONFIG.copy()

    if not config_path.is_file():
        return config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            return config

        for key, val in data.items():
            if key not in DEFAULT_CONFIG:
                # Ignore unknown keys without failing
                continue

            expected_type = type(DEFAULT_CONFIG[key])
            if isinstance(val, expected_type):
                # Safety floor check: minimum_age_days cannot be less than 7
                if key == "minimum_age_days" and val < 7:
                    config[key] = 7
                else:
                    config[key] = val

    except Exception:
        # Fallback cleanly to safe defaults on any parse error
        return DEFAULT_CONFIG.copy()

    return config
