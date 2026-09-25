# Operations Manual & CLI Reference

This document provides a guide for manually running and managing the Windows 11 Development Environment Optimizer.

---

## 1. Safety Principles & Execution Policy

- **Manual Launch Only**: The application operates only while running directly in a terminal. When it exits, it halts completely. No background processes, services, or registry startup keys exist.
- **Fail-Closed Default**: Running without flags performs a dry-run analysis and generates a plan with zero modifications.
- **Quarantine First**: Files are moved to an isolated quarantine location rather than permanently deleted.
- **Explicit High-Risk Confirmation**: Destructive actions (like purging quarantine) require manual typed confirmation.

---

## 2. Command Line Interface (CLI)

### Status & Inspection (Read-Only)

Inspect current workstation metrics, disk utilization, and active developer processes:

```powershell
python optimizer.py --status
```

Run health checks and verify developer tool availability (`pip`, `npm`, `docker`):

```powershell
python optimizer.py --doctor
```

---

### Dry-Run & Plan Generation (Zero Writes)

Simulate cleanup of eligible cache files (older than 7 days) and view candidate items:

```powershell
python optimizer.py --dry-run
```

Generate candidate analysis output formatted as JSON:

```powershell
python optimizer.py --plan --json
```

---

### Applying Maintenance Operations

To quarantine eligible cache files with an interactive confirmation prompt:

```powershell
python optimizer.py --apply
```

To run in automated batch mode for approved low-risk actions:

```powershell
python optimizer.py --apply --yes
```

*Note: `--yes` acknowledges low-risk quarantine moves only. It never bypasses typed confirmations for permanent deletion.*

---

### Rollback & Restoration

To restore files from a previous run to their original paths:

```powershell
python optimizer.py --rollback <RUN_ID>
```

*Example: `python optimizer.py --rollback RUN-20260925T131000Z`*

Before restoring files, the rollback engine checks:

1. File exists in quarantine and its SHA-256 matches the manifest.
2. The original target path has not been overwritten by newer user files.

---

### Purging Quarantine (Permanent Deletion)

To permanently remove all files stored in quarantine:

```powershell
python optimizer.py --purge-quarantine
```

When prompted, type:

```text
PURGE QUARANTINE
```

Any other input will cancel the operation.

---

## 3. Configuration (`config/default_config.json`)

The behavior can be customized by editing `config/default_config.json`:

- `"minimum_age_days"`: Minimum age of files before they become eligible for quarantine (default: `7`).
- `"dry_run"`: Default execution mode safety flag (default: `true`).
- `"quarantine_enabled"`: Ensure files are quarantined rather than deleted (default: `true`).
- `"log_level"`: Logging verbosity (`"normal"` or `"verbose"`).
