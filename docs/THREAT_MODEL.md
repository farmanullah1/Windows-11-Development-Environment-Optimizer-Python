# Threat Model & Security Boundaries

This document defines the security architecture, threat model, trust boundaries, and mitigations implemented in the **Windows 11 Development Environment Optimizer**.

---

## 1. System Assumptions and Trust Boundaries

- **Host Environment:** Windows 11 (Build ≥ 22000), 64-bit architecture.
- **Operating Context:** Single-developer laptop workstation running modern development toolchains (Node.js, Docker Desktop, Python, .NET, Brave, Visual Studio Code).
- **Execution Privilege:** Standard Non-Elevated User account (recommended). Administrator privileges are never demanded nor automatically acquired.
- **Network Access:** Zero outbound or inbound network connectivity. The utility operates in complete air-gap isolation without telemetry or telemetry egress.

---

## 2. Protected Assets

The optimizer enforces strict protections to ensure that active development assets are never traversed, moved, modified, or deleted:

| Asset Category | Protection Scope | Enforcement Mechanism |
| :--- | :--- | :--- |
| **Source Code Repositories** | `.git`, `.github`, workspace folders | Explicit block by filename and path token in `src/paths.py`. |
| **Secrets & Credentials** | `.env`, credentials, tokens | File blacklist and regex-based redaction in `src/logging_utils.py`. |
| **Dependency Locks** | `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml` | Name-based protection in `src/paths.py`. |
| **Database Data Files** | `.mdf`, `.ndf`, `.ldf` (SQL Server) | File extension filter and active process locks in `src/paths.py`. |
| **Container & VM Disks** | `.vhdx`, `.vhd` (Docker Desktop, WSL2) | Extension blacklist in `src/paths.py`. |
| **Browser User Data** | Brave, Chrome profile directories | Directory root block in `src/paths.py`. |
| **Windows System Roots** | `C:\Windows`, `C:\Program Files`, `C:\ProgramData` | Canonical parent containment check in `src/paths.py`. |
| **User Personal Folders** | `Desktop`, `Documents`, `Downloads`, etc. | Path ancestry validation in `src/paths.py`. |

---

## 3. Threat Scenarios & Countermeasures

### 3.1 Path Traversal & Out-of-Bounds Modification
- **Threat:** Malicious symlink, relative path component (`..\..`), or junction directing operations outside approved cache directories.
- **Mitigation:**
  - `is_contained_in()` resolves canonical paths (`Path.resolve()`) and ensures the target path is strictly a descendant of the approved root.
  - `is_reparse_point()` validates Win32 `FILE_ATTRIBUTE_REPARSE_POINT` (0x400) and skips junctions or symbolic links during directory walking.

### 3.2 Race Conditions & File Locking (TOCTOU)
- **Threat:** A development process opens or writes to a cache file between the discovery phase and the move operation.
- **Mitigation:**
  - `is_file_locked()` attempts exclusive read-mode access prior to selection.
  - `shutil.move()` fails atomically if an OS file lock is held by a running process.
  - Minimum age filter (≥ 7 days) ensures active working files are not considered.

### 3.3 Accidental Permanent Data Loss
- **Threat:** Files are deleted permanently without recovery option.
- **Mitigation:**
  - Permanent deletion is prohibited in standard operation.
  - Files are moved into `%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<RUN_ID>\`.
  - Manifest records canonical original path, file size, modification timestamp, and SHA-256 hash.
  - Full atomic rollback is supported via `python optimizer.py --rollback <RUN_ID>`.

### 3.4 Command Injection & Execution Hijacking
- **Threat:** External tools or binaries invoked with malicious arguments or via insecure shell interpreters.
- **Mitigation:**
  - `run_safe_subprocess()` enforces `shell=False`.
  - Arguments are passed as an explicit list (`List[str]`).
  - Python invocations resolve to `sys.executable` to prevent hijacking via Windows App Execution Aliases.
  - Hard timeouts (default 30s) prevent hung or stalled sub-processes.

---

## 4. Residual Risks

- **Stale Tool Locks:** If a background tool process crashes while holding file locks, those files are skipped until the lock is freed by the OS.
- **Multi-User Environments:** Quarantine is isolated to the executing user's `%LOCALAPPDATA%`. Other users on the same machine cannot access another user's quarantine without administrator privileges.
