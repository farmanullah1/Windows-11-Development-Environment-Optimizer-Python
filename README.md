# Windows 11 Development Environment Optimizer

A security-first, allowlist-based, fail-closed development environment maintenance utility in Python 3 for Windows 11 workstations.

## Overview
This utility provides conservative, measurable, user-approved maintenance specifically tailored for Windows 11 laptops used for development (.NET, Node.js/React, Python, Docker, SQL Server, Brave, VS Code).

The utility **never promises a guaranteed performance improvement**. Its priorities are:
1. User data safety
2. System stability
3. Development-work safety
4. Security
5. Reversibility (quarantine and rollback)
6. Transparency
7. Resource optimization

---

## Key Safety Architecture
- **Fail-Closed:** Any ambiguous path, locked file, unknown process, or malformed argument results in skipping or safe termination with zero modifications.
- **Strict Allowlist:** Never performs generic recursive scans for terms like `temp` or `cache`. Only exact, predefined paths and official tools are handled.
- **Quarantine over Permanent Deletion:** Eligible files are moved to `%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<run-id>\` with recorded SHA-256 hashes and rollback manifests.
- **Zero Auto-Elevation:** Never bypasses or prompts UAC automatically. Privileged tasks report exact instructions for manual review.
- **Protected Paths:** Complete lockdown of personal files (Desktop, Documents, Downloads, OneDrive), source repositories (`.git`, `.env`, lock files), database engines (SQL Server `.mdf`/`.ldf`), Docker volumes, and IDE configs.
- **Zero Network Access:** No telemetry, tracking, external API calls, or automatic updates.
- **Subprocess Isolation:** Enforces `subprocess.run(..., shell=False)` with argument lists, timeout gating, and `sys.executable` integrity.

---

## Directory Structure
```text
Win11DevOptimizer/
├── optimizer.py           # CLI entry point and execution coordinator
├── config/
│   └── default_config.json # Safe configuration schema and defaults
├── src/
│   ├── __init__.py
│   ├── cli.py             # Strict argument parser with mutually exclusive rules
│   ├── config.py          # Configuration loading and schema validation
│   ├── safety.py          # OS detection, reparse point & path containment validation
│   ├── paths.py           # Explicit allowlist and protected path registries
│   ├── quarantine.py      # Isolation engine, SHA-256 calculator, disk space checker
│   ├── rollback.py        # Rollback engine and manifest validator
│   ├── process_manager.py # Informational process inspector (fail-closed, no auto-kill)
│   ├── power.py           # Power scheme inspector & reversible switcher
│   ├── cache_manager.py   # Scoped cache inspectors and handlers
│   ├── diagnostics.py     # System resource reporter (CPU, RAM, Disks)
│   ├── logging_utils.py   # Local rotating logger with username & secret redaction
│   └── subprocess_utils.py # Safe subprocess runner (shell=False, argument lists)
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_config.py
│   ├── test_paths.py
│   ├── test_quarantine.py
│   ├── test_rollback.py
│   └── test_safety.py
└── docs/
    ├── SAFETY.md
    ├── THREAT_MODEL.md
    ├── OPERATIONS.md
    └── ROLLBACK.md
```

---

## Manual Next Steps (User Execution Only)
The application has been generated and statically verified. Per instructions, **it has not been executed on your machine**.

To inspect the system safely in read-only / dry-run mode:
```powershell
python optimizer.py
```
or explicitly:
```powershell
python optimizer.py --dry-run
```

To run diagnostics:
```powershell
python optimizer.py --doctor
python optimizer.py --status
```
