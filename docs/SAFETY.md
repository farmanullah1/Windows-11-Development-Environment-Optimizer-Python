# Safety Architecture & Threat Model

## 1. Safety Principles
1. **Manual Execution Only:** The utility executes only while explicitly run by the user. No daemons, background services, scheduled tasks, or startup registry entries.
2. **Fail-Closed Design:** Ambiguity in path resolution, file lock status, or platform support triggers immediate safe skipping.
3. **Allowlist-Only Cleanup:** Searches strictly within designated developer caches (`npm`, `pip`, scoped `Temp`), requiring modification age >= 7 days.
4. **Quarantine & Rollback:** Deletions are never permanent by default. Files are safely staged into `%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<run-id>\` with recorded SHA-256 hashes and manifests.
5. **Zero Auto-Elevation:** Operates as a standard user process. Tasks requiring administrator elevation are reported for manual execution.
6. **Subprocess Isolation:** Commands are executed strictly using Python argument lists (`shell=False`) with timeout guards.
