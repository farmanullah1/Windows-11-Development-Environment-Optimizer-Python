# Windows 11 Development Environment Optimizer

A security-first, allowlist-based, fail-closed development environment maintenance utility written in Python 3 for Windows 11 workstations.

---

## 1. Overview & Core Philosophy

This utility provides conservative, measurable, user-approved maintenance specifically designed for Windows 11 laptops used by developers (.NET, Node.js/React, Python, Docker Desktop, SQL Server, Brave, VS Code).

The utility **never promises a guaranteed performance improvement**. Its strict priority order is:

1. **User data safety** (Zero accidental deletion of working code or repositories)
2. **System stability** (No OS modification, registry tweaks, or thermal hacks)
3. **Development-work safety** (Docker, SQL Server databases, and active processes protected)
4. **Security** (Air-gapped, zero telemetry, `shell=False` execution, zero auto-elevation)
5. **Reversibility** (Quarantine isolation with SHA-256 rollback manifests)
6. **Transparency** (Explicit tagging, dry-run simulation, and JSON execution plans)
7. **Resource maintenance** (Conservative cleanup of stale temporary caches $\ge 7$ days old)

---

## 2. Key Safety Architecture

- **Fail-Closed Execution:** Any ambiguous path, locked file, unknown process, or malformed argument results in skipping or safe termination with zero modifications.
- **Strict Allowlist:** Never performs broad recursive scans for generic terms like `temp` or `cache`. Only explicitly approved directory roots (e.g., npm cache, pip cache, scoped user temp) are examined.
- **Quarantine over Permanent Deletion:** Eligible files are moved into `%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<RUN_ID>\` with recorded SHA-256 hashes and rollback manifests.
- **Zero Auto-Elevation:** Operates as a Standard User. Never triggers UAC prompts or self-elevation. If administrator rights are needed for a task, it skips with clear instructions.
- **Protected Paths:** Absolute protection for personal folders (`Desktop`, `Documents`, `Downloads`, `OneDrive`), source code repositories (`.git`, `.env`, lock files), database engines (SQL Server `.mdf`/`.ldf`), Docker volumes, WSL disks (`.vhdx`), and IDE workspace storage.
- **Zero Network Access:** Operates with zero outbound or inbound network calls, telemetry, or remote updates.
- **Subprocess Isolation:** Enforces `subprocess.run(..., shell=False)` with argument lists, timeout gating (30s), and `sys.executable` resolution to prevent execution hijacking.

---

## 3. Directory Structure

```text
Windows 11 Development Environment Optimizer/
│
├── optimizer.py                     # Main CLI entry point
├── config.json.example              # Reference schema for fail-closed user configuration
├── requirements.txt                 # Dependency documentation (Standard Library only)
├── README.md                        # Architecture, safety bounds, and manual usage instructions
├── LICENSE                          # MIT License
├── .gitignore                       # Git ignore rules for bytecode, caches, and local logs
│
├── config/
│   └── default_config.json          # Active default configuration (safe baseline)
│
├── src/
│   ├── __init__.py                  # Package initialization
│   ├── cli.py                       # Strict argument parser with mutually exclusive flags
│   ├── config.py                    # Fail-closed JSON config loader and safety floor validator
│   ├── safety.py                    # Platform detection, elevation check, reparse point & lock detection
│   ├── paths.py                     # Canonical allowlists, personal folder protections, and asset shields
│   ├── quarantine.py                # Pre-move disk check, SHA-256 calculation, and manifest logging
│   ├── rollback.py                  # Quarantine restore engine with hash verification & collision guards
│   ├── process_manager.py           # Read-only developer process inspector (tasklist)
│   ├── power.py                     # Read-only active power scheme query (powercfg)
│   ├── cache_manager.py             # Scoped allowlist walker and tool health inspectors
│   ├── diagnostics.py               # Non-invasive reporter (OS, CPU, RAM, Commit Charge, Disks, Dev Drives)
│   ├── logging_utils.py             # Rotating file logger with path anonymization & secret redaction
│   └── subprocess_utils.py          # Subprocess executor enforcing shell=False, timeouts, and python path
│
├── tests/
│   ├── __init__.py                  # Test package initialization
│   ├── test_cli.py                  # CLI flag validation and mutually exclusive tests
│   ├── test_safety.py               # Windows 11 version check, elevation, and path containment tests
│   ├── test_paths.py                # Protected paths, personal folder shielding, and allowlist tests
│   ├── test_quarantine.py           # File isolation, SHA-256 calculation, and manifest recording tests
│   ├── test_rollback.py             # Quarantine restoration, missing run ID, and integrity tests
│   ├── test_config.py               # Default fallbacks, malformed JSON, and safety floor tests
│   ├── test_diagnostics.py          # Diagnostic keys, CPU inspection, and disk fallbacks
│   └── test_subprocess_security.py  # shell=False enforcement, timeout gating, and binary resolution
│
└── docs/
    ├── SAFETY.md                    # Core safety philosophy and operational constraints
    ├── THREAT_MODEL.md              # Threat model, trust boundaries, asset definitions, and residual risks
    ├── OPERATIONS.md                # Operational guidelines, dry-run procedures, and failure modes
    ├── ROLLBACK.md                  # Rollback instructions and quarantine directory structure
    └── STATIC_SAFETY_REVIEW.md      # Formal static review table and "Do Not Do" verification checklist
```

---

## 4. Command-Line Interface (CLI)

The utility operates under a strict command-line contract with mutually exclusive modes.

### 4.1 Diagnostics & Health Checks (Read-Only)

```powershell
# Display workstation resource diagnostics (CPU, RAM, Commit Charge, Disks, Dev Drives, Processes)
python optimizer.py --status

# Verify local developer environment prerequisites (pip, npm, .NET NuGet, Git, Docker)
python optimizer.py --doctor
```

### 4.2 Planning & Dry-Run Simulation (Zero Modifications)

```powershell
# Default safe inspection (Dry-Run mode by default)
python optimizer.py

# Explicit dry-run
python optimizer.py --dry-run

# Formatted analysis plan
python optimizer.py --plan

# Machine-readable JSON plan for automated auditing
python optimizer.py --plan --json
```

### 4.3 Applying Maintenance (Quarantine Isolation)

Eligible cache files unmodified for at least 7 days are moved into isolated quarantine with recorded SHA-256 hashes:

```powershell
# Interactive apply mode (prompts for user confirmation [y/N])
python optimizer.py --apply

# Automated apply mode (pre-acknowledged prompt)
python optimizer.py --apply --yes
```

### 4.4 Rollback & Disaster Recovery

Any modification run can be restored to its exact original location:

```powershell
# Restore all quarantined files from a specific run ID
python optimizer.py --rollback RUN-20260925-153000
```

### 4.5 Permanent Purge

Permanently delete quarantined archives (cannot be rolled back):

```powershell
python optimizer.py --purge-quarantine
```
*Requires explicit typed confirmation (`PURGE QUARANTINE`).*

---

## 5. Protected Assets & Boundaries

The following locations and file types are strictly protected and never traversed or moved:

- **System Roots:** `C:\Windows`, `C:\Program Files`, `C:\Program Files (x86)`, `C:\ProgramData`
- **User Personal Folders:** `Desktop`, `Documents`, `Downloads`, `Pictures`, `Videos`, `Music`, `OneDrive`
- **Code Repositories:** `.git`, `.github`, workspace configurations
- **Sensitive Files:** `.env`, `.pem`, lock files (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`)
- **Databases & VM Disks:** SQL Server (`.mdf`, `.ldf`, `.ndf`), Docker/WSL (`.vhdx`, `.vhd`)
- **Browser Profiles:** Brave & Chrome User Data directories
- **Active Files:** Any file locked or open by a running process (`is_file_locked`)

---

## 6. Testing & Static Verification

The project includes a complete unit test suite requiring zero third-party dependencies:

```powershell
python -m unittest discover tests
```

Tests cover:
- Windows 11 platform checks and standard user elevation detection
- Path containment and traversal rejection
- Quarantine isolation, pre-flight disk capacity checks, and SHA-256 calculation
- Rollback restoration, conflict checks, and missing manifest handling
- Subprocess isolation, `shell=False` enforcement, and timeout gating
- Configuration safety floor (`minimum_age_days >= 7`)

---

## 7. License

Distributed under the [MIT License](file:///c:/Users/farma/Desktop/Windows%2011%20Development%20Environment%20Optimizer/LICENSE).
