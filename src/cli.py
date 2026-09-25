"""Strict CLI parsing with mutually exclusive flags and safe default plan mode."""

import argparse
from typing import Tuple, Optional, List


def parse_arguments(cli_args: Optional[List[str]] = None) -> Tuple[argparse.Namespace, bool]:
    """
    Parses CLI arguments under fail-closed contract.
    Returns (args, is_valid).
    """
    parser = argparse.ArgumentParser(
        description="Windows 11 Development Environment Optimizer — Security-First Maintenance Utility",
        add_help=True,
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate and inspect eligible items without modifying files.",
    )
    group.add_argument(
        "--apply",
        action="store_true",
        help="Apply approved low-risk maintenance operations.",
    )

    parser.add_argument(
        "--yes",
        action="store_true",
        help="Acknowledge prompt for approved operations.",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Display system status and developer process diagnostics.",
    )
    parser.add_argument(
        "--doctor",
        action="store_true",
        help="Run health and prerequisite checks on the local workstation.",
    )
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Generate analysis plan of candidates.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Format output as JSON.",
    )
    parser.add_argument(
        "--rollback",
        metavar="RUN_ID",
        type=str,
        help="Restore quarantined files for specified run ID.",
    )
    parser.add_argument(
        "--purge-quarantine",
        action="store_true",
        help="Permanently delete quarantined files (requires typed confirmation).",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="Windows 11 Development Optimizer v1.0.0",
    )

    try:
        args = parser.parse_args(cli_args)
        return args, True
    except SystemExit:
        return argparse.Namespace(), False
