# Windows 11 Development Environment Optimizer

## Security-First, Allowlist-Based, Phased Implementation

Create a **security-first Windows 11 development-environment maintenance and optimization utility** in Python 3.

The utility is intended for a Windows 11 development laptop used with:

* Node.js / npm
* React
* .NET / C#
* Microsoft SQL Server / SSMS
* Postman
* Brave Browser
* Google Antigravity
* Git
* Docker Desktop
* Python / pip
* Visual Studio Code or similar IDEs

The goal is to perform **conservative, measurable, user-approved maintenance** that may recover disk space or reduce unnecessary temporary resource usage without disrupting development work.

The utility must **never promise a guaranteed performance improvement**.

The priority order is:

1. User data safety
2. System stability
3. Development-work safety
4. Security
5. Reversibility
6. Transparency
7. Performance optimization

---

## CRITICAL AI BEHAVIOR RULES

## 0. DO NOT MAKE UNSUPPORTED SAFETY CLAIMS

Do NOT describe this prompt, the generated code, or the generated utility as:

* guaranteed safe
* guaranteed harmless
* impossible to break the system
* guaranteed not to affect the laptop
* guaranteed reversible
* production-safe without testing
* risk-free

Do not say:

> "This cannot damage the system."

Do not say:

> "This will not break your development environment."

Do not say:

> "This is completely safe to run."

Instead, distinguish between:

### Prompt safety

Whether the instructions themselves contain reasonable safeguards.

### Code safety

Whether the generated source code passes the required static review and tests.

### Runtime safety

Whether the program has been tested in an isolated environment and then carefully dry-run on the target machine.

A successful static review does NOT prove that runtime behavior is risk-free.

Always state relevant limitations and residual risks.

---

## CRITICAL IMPLEMENTATION RULE

## DO NOT WRITE THE FINAL CODE IMMEDIATELY

The project must be developed in three phases.

### Phase 1 — Design and Safety Review

Produce ONLY:

* threat model
* trust boundaries
* security assumptions
* exact cleanup allowlist
* exact protected-path list
* exact allowed commands
* forbidden commands
* CLI contract
* configuration schema
* rollback design
* quarantine design
* logging/redaction design
* privilege model
* failure modes
* residual risks
* test plan
* proposed project structure
* safety review checklist

Then:

**STOP.**

Do not generate implementation code.

Do not create files.

Do not install packages.

Do not execute commands.

Do not execute PowerShell.

Do not execute Python.

Do not execute cleanup operations.

Do not modify the user's machine.

Wait for explicit user approval before Phase 2.

---

## PHASE APPROVAL RULE

The following user instructions are considered explicit approval:

> Proceed with Phase 2.

or:

> I approve Phase 1. Generate the implementation.

Do not infer approval from:

* "looks good"
* "okay"
* "continue"
* "yes" unless it clearly means approval to proceed to Phase 2

If approval is ambiguous, ask for confirmation.

---

## PHASE 2 — IMPLEMENTATION

Only after explicit Phase 2 approval:

Generate the Python implementation according to the approved Phase 1 design.

The implementation must be:

* modular
* readable
* type-hinted
* documented
* tested
* conservative
* fail-closed
* allowlist-based

Do not add functionality that was not approved during Phase 1.

If implementation reveals a new safety concern, STOP and report it instead of silently expanding scope.

---

## PHASE 3 — STATIC SAFETY REVIEW

After implementation, perform a separate security review.

Inspect the generated source code for:

* dangerous deletion
* unsafe path handling
* command injection
* shell invocation
* privilege escalation
* unsafe subprocess usage
* accidental persistence
* excessive permissions
* sensitive logging
* protected-path violations
* rollback errors
* race conditions where relevant
* symlink/junction/reparse-point traversal
* configuration bypasses
* unsafe defaults
* unexpected network access
* hidden external dependencies
* unsafe exception handling

Produce the required final safety-review table.

---

## 1. MANUAL EXECUTION ONLY

The laptop must behave normally when the optimizer is not running.

The utility must NOT:

* install itself as a Windows service
* create a scheduled task
* add itself to startup
* create registry persistence
* run continuously in the background
* install a daemon
* monitor Windows after exiting
* create hidden processes
* create hidden accounts
* modify login behavior

The program must operate only when manually started by the user.

No persistence is allowed.

---

## 2. GOOGLE ANTIGRAVITY MUST NOT EXECUTE THE UTILITY

Google Antigravity must treat the generated program as **untrusted system-modification code until manually reviewed by the user**.

Antigravity must NOT:

* execute the generated optimizer
* execute `--apply`	ext
* execute `--purge-quarantine`	ext
* execute rollback commands
* run destructive tests against the host
* install dependencies automatically
* run cleanup commands independently
* modify Windows settings
* stop services
* terminate processes
* delete or quarantine files on the user's real machine

Antigravity may generate code and documentation.

Any execution must be explicitly initiated by the user outside the AI generation step.

---

## 3. WINDOWS 11 ONLY

The program must verify that it is actually running on Windows 11.

If Windows 11 cannot be confidently detected:

* perform no modifications
* display `[ERROR] Windows 11 was not detected.`	ext
* exit safely

Do not attempt to guess the operating system.

Do not execute Linux-only commands.

If Bash compatibility is discussed, clearly distinguish:

* Git Bash
* WSL

The primary implementation must remain Python for native Windows.

---

## 4. FAIL-CLOSED DESIGN

When anything is uncertain, the program must choose the safer behavior.

Examples:

* unknown path → skip
* unknown process → skip
* unknown command → skip
* invalid configuration → safe defaults
* insufficient permissions → skip restricted operation
* ambiguous Windows version → no modification
* inaccessible file → skip
* locked file → skip
* unexpected command output → skip
* unexpected path resolution → skip
* malformed argument → no modification

Never "try something anyway."

---

## 5. NO AUTOMATIC ADMIN ELEVATION

The program must NEVER automatically elevate itself.

Do not:

* automatically trigger UAC
* relaunch itself as administrator
* bypass UAC
* modify UAC settings

If an operation requires administrator privileges:

1. Explain exactly why.
2. Explain what the operation would change.
3. Skip the operation if the program is not elevated.
4. Continue with safe user-level operations.
5. Print the exact command the user could manually execute with administrator privileges if appropriate.

Administrator privileges must never be required for the entire program unless absolutely necessary.

Prefer normal-user operations.

---

## 6. DEFAULT MODE

Running:

```	ext
python optimizer.py
```

must perform **status / dry-run analysis only**.

It must make no system modifications.

The user must explicitly request modification mode.

---

## 7. STRICT CLI CONTRACT

Implement:

```	ext
python optimizer.py

python optimizer.py --dry-run

python optimizer.py --apply

python optimizer.py --apply --yes

python optimizer.py --plan --json

python optimizer.py --rollback <run-id>

python optimizer.py --status

python optimizer.py --doctor

python optimizer.py --version

python optimizer.py --help

python optimizer.py --purge-quarantine
```

Rules:

* no arguments = status/dry-run
* `--dry-run` and `--apply` are mutually exclusive
* malformed arguments = no modifications
* destructive operations require `--apply`	ext
* `--yes` does NOT bypass high-risk typed confirmations
* high-risk operations require separate typed confirmation
* rollback requires an explicit run ID
* purge-quarantine requires a separate typed confirmation
* unknown flags must never be interpreted as permission to modify the system

`--apply --yes` means the user has requested the approved low-risk action set, but it does NOT authorize:

* permanent deletion
* service changes
* process termination
* SQL Server changes
* Docker destructive cleanup
* Windows system changes
* other high-risk operations

Those require their own explicit opt-in.

---

## 8. DRY-RUN

Dry-run must:

* inspect
* calculate sizes
* identify eligible files
* identify skipped files
* identify protected paths
* show proposed commands
* show proposed changes
* show reversible vs irreversible operations
* show required privileges

It must NOT:

* delete files
* move files
* quarantine files
* stop processes
* stop services
* change settings
* change power plans
* modify configuration

Dry-run must not create or modify system state.

If a log file is required, explain that writing the log is the only expected filesystem write.

---

## 9. ALLOWLIST-BASED CLEANUP

Use an **allowlist**, not a denylist, for cleanup.

Never search arbitrary directories for names such as:

* `cache`	ext
* `temp`	ext
* `tmp`	ext
* `old`	ext
* `logs`

and assume they are safe.

Each cleanup target must be either:

1. an exact known safe path, or
2. an exact known official tool command approved during Phase 1.

Do not recursively scan arbitrary user directories.

Do not infer cleanup locations dynamically from vague names.

The Phase 1 design must list every cleanup target explicitly.

---

## 10. QUARANTINE INSTEAD OF PERMANENT DELETE

Permanent deletion must NOT be the default.

For file-based cleanup, use:

```	ext
%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<run-id>\
```

as the quarantine directory.

Eligible files should first be moved into quarantine where technically safe.

The quarantine manifest must record:

* original path
* quarantine path
* file size
* modified time
* SHA-256 hash where practical
* run ID
* operation timestamp

Never claim a file can be restored unless it actually exists in quarantine.

Permanent purge requires:

```	ext
--purge-quarantine
```

and the typed confirmation:

```	ext
PURGE QUARANTINE
```

---

## 11. QUARANTINE SAFETY

The quarantine directory itself must be protected from accidental recursive cleanup.

The optimizer must NEVER:

* recursively quarantine its own quarantine directory
* treat quarantine files as normal cache files
* automatically purge quarantine
* overwrite an existing quarantine run without explicit handling

Each run must use a unique run ID.

Before moving a file:

1. verify source
2. verify destination
3. ensure destination remains inside the quarantine root
4. prevent path traversal
5. preserve collision-safe filenames
6. verify sufficient free disk space on the quarantine drive before moving files
7. create/update the manifest safely

---

## 12. QUARANTINE LIMITATIONS

Some application cache systems may not be safely movable.

For example, an official cache command may permanently remove data.

Such operations must be classified as:

```	ext
NON-REVERSIBLE
```

They require explicit opt-in.

Do not falsely wrap an irreversible command in a rollback feature.

If quarantine is technically impossible, the operation must remain disabled unless separately approved.

---

## 13. FILE AGE SAFETY RULES

Default cleanup eligibility:

* file must be at least 7 days old
* file must not be locked/in use
* file must not be a symbolic link
* file must not be a junction
* file must not be a reparse point
* path must be inside an approved allowlist
* file must pass every safety check

Example:

```	ext
minimum_age_days = 7
```

Do not allow configuration to reduce the minimum below the approved safety floor.

The safety floor must be defined during Phase 1.

---

## 14. LOCKED / ACTIVE FILES

Never forcibly delete or move an active/locked file.

If a file appears to be in use:

```	ext
[SKIPPED] File is currently in use.
```

Do not terminate the process merely to unlock the file.

Do not use forceful unlock techniques.

---

## 15. REPARSE POINT / SYMLINK SAFETY

Do not follow:

* symbolic links
* directory junctions
* mount points
* unexpected reparse points

during recursive cleanup or analysis.

All paths must be resolved to their canonical target (using strict Win32 final-path resolution / `os.path.realpath`) and verified to ensure that the canonical target remains strictly within the approved allowlist directory root.

If the target is a junction, symlink, or cannot be confidently validated:

```	ext
[SKIPPED] Unsafe path resolution or reparse point detected.
```

---

## 16. EXACT SAFE TOOL OPERATIONS

Only commands explicitly approved in Phase 1 may be implemented.

## npm

Preferred reporting:

```	ext
npm cache verify
```

Do not automatically run:

```	ext
npm cache clean --force
```

`npm cache clean --force` is destructive and requires explicit opt-in.

Never delete:

* `node_modules`	ext
* `package.json`	ext
* `package-lock.json`	ext
* `yarn.lock`	ext
* `pnpm-lock.yaml`	ext
* project source code

---

## pip

Reporting may use:

```	ext
python -m pip cache info
```

Permanent cache removal:

```	ext
python -m pip cache purge
```

requires explicit opt-in.

---

## NuGet

A narrowly scoped official command may be considered:

```	ext
dotnet nuget locals http-cache --clear
```

Other NuGet cache locations must be treated separately.

Do not automatically delete the global package cache.

---

## Docker

Default operation:

```	ext
docker system df
```

is reporting only.

Do NOT automatically execute:

```	ext
docker system prune

docker system prune -a

docker volume prune
```

Do not delete:

* Docker volumes
* active containers
* images
* Docker Desktop configuration

unless explicitly approved and separately gated.

---

## SQL Server

SQL Server is protected infrastructure.

Do not automatically:

* stop SQL Server
* restart SQL Server
* modify SQL Server services
* delete MDF files
* delete NDF files
* delete LDF files
* shrink databases
* delete transaction logs
* change SQL Server memory settings
* modify SQL Server configuration

SQL Server may only be inspected for status/resource information unless the user explicitly approves another operation.

---

## 17. BRAVE BROWSER

Never delete:

* passwords
* cookies
* browsing history
* bookmarks
* extensions
* sessions
* browser databases
* browser profiles

Do not close Brave automatically.

Browser cache cleanup must be separately opt-in and must use an exact approved cache path.

If Brave is running:

```	ext
[SKIPPED] Brave is currently running.
```

---

## 18. GOOGLE ANTIGRAVITY / IDEs

Never automatically terminate:

* Google Antigravity
* VS Code
* Visual Studio
* terminals
* development servers
* IDEs

Never modify:

* workspace storage
* extensions
* settings
* project files

Protect VS Code:

```	ext
workspaceStorage
```

and equivalent IDE state.

---

## 19. NODE.JS DEVELOPMENT SERVERS

Detecting Node.js processes is allowed.

Automatically terminating them is disabled.

If process management is implemented later:

1. display PID
2. display safe process information
3. require explicit process selection
4. attempt graceful termination
5. never terminate arbitrary Node.js processes
6. never force-kill without separate high-risk confirmation

---

## 20. PROTECTED PATHS

Protect the following by default.

## Windows

```	ext
C:\Windows
C:\Windows\System32
C:\Windows\WinSxS
C:\Windows\Installer
C:\Windows\Prefetch
C:\Windows\SoftwareDistribution
```

`C:\Windows\Temp` is protected by default.

---

## Program Files

```	ext
C:\Program Files
C:\Program Files (x86)
C:\ProgramData
```

---

## User Profile

Protect:

```	ext
%USERPROFILE%
```

as a whole.

Never recursively clean it.

Protect:

* Desktop
* Documents
* Downloads
* Pictures
* Videos
* OneDrive
* cloud-sync folders

---

## Development

Protect:

* `.git`	ext
* `.github`	ext
* `.env`	ext
* source code
* project configuration
* package manifests
* lock files
* database files

---

## SQL Server

Protect:

* MDF
* NDF
* LDF
* backup directories
* SQL Server installation directories

---

## Docker

Protect:

* Docker Desktop data
* Docker volumes
* Docker virtual disks
* Docker Desktop configuration

---

## WSL

Protect:

* WSL virtual disks
* `.vhdx`	ext
* WSL distributions
* WSL configuration

Do not automatically execute:

```	ext
wsl --shutdown
```

---

## IDEs

Protect:

* VS Code workspace storage
* IDE configuration
* extensions
* project metadata

---

## Browser

Protect browser profiles and persistent browser databases.

---

## 21. EXPLICITLY FORBIDDEN OPERATIONS

The default utility must NOT:

* modify registry settings
* modify Windows services
* terminate arbitrary processes
* delete Windows Temp recursively
* modify WinSxS
* modify Windows Installer
* modify Prefetch
* modify SoftwareDistribution
* modify Defender
* modify UAC
* modify Secure Boot
* modify firewall
* modify DNS
* modify proxy
* modify hosts file
* modify environment variables
* modify Windows Update
* modify pagefile
* modify hibernation
* disable indexing
* disable SysMain
* modify browser policies
* modify browser extensions
* delete cookies
* delete sessions
* empty Recycle Bin
* shut down WSL
* modify Docker Desktop settings
* modify BIOS/UEFI
* modify drivers
* overclock
* undervolt
* disable thermal protection
* disable security software
* bypass Windows security controls

---

## 22. POWER PLAN

Power-plan changes are optional.

Supported:

* Balanced
* High Performance

Before modification:

1. detect current plan
2. record its identifier
3. display proposed change
4. require confirmation
5. apply change
6. store previous state in rollback manifest

Power-plan modification must be reversible.

Do not change advanced power settings automatically.

---

## 23. ROLLBACK MANIFEST

Each modification run must receive a unique run ID.

Store:

* run ID
* timestamp
* changes
* previous values
* new values
* quarantined files
* commands executed
* results
* errors

Rollback must verify the current state before reverting.

If the user changed the system after the optimizer modified it:

```	ext
[WARNING] Current state differs from the recorded state. Skipping automatic rollback.
```

Never overwrite a newer user change.

File deletion is only considered rollback-capable when the file exists in quarantine and the manifest is valid.

---

## 24. SUBPROCESS SECURITY

All subprocess execution must follow strict rules.

Use:

```	ext
subprocess.run([...], shell=False, ...)
```

Never use:

```	ext
shell=True
```

unless a specific operation has been formally reviewed and approved in Phase 1.

Prefer:

```	ext
["npm", "cache", "verify"]
```

instead of command strings. For Python-based tools, always use `[sys.executable, "-m", ...]` instead of bare `"python"` to ensure execution with the running interpreter and prevent Windows App Execution Alias hijacking.

Every subprocess must have:

* explicit executable or fully resolved binary path
* argument list
* timeout
* controlled environment where practical
* captured output where appropriate
* error handling
* expected exit-code validation

Never construct commands from untrusted user input.

Never concatenate arbitrary strings into commands.

---

## 25. FORBIDDEN EXECUTION TECHNIQUES

Never use:

* `eval`	ext
* `exec`	ext
* arbitrary dynamic code execution
* remote code execution
* downloaded scripts
* downloaded executables
* obfuscated code
* PowerShell `-EncodedCommand`	ext
* hidden PowerShell payloads
* concealed base64 commands
* arbitrary URL execution
* remote installers

The program must not download anything automatically.

---

## 26. NETWORK SAFETY

The utility must not contact external servers by default.

No:

* telemetry
* analytics
* remote reporting
* automatic updates
* external APIs
* cloud uploads

Package installation must not happen automatically.

If dependencies are required, provide installation instructions separately.

---

## 27. CONFIGURATION VALIDATION

Use a configuration file such as:

```	ext
config.json
```

Destructive operations must default to:

```	ext
false
```

If configuration is:

* missing
* malformed
* invalid
* partially corrupted

use safe defaults.

Do not perform destructive actions because configuration parsing failed.

Unknown configuration keys should produce:

```	ext
[WARNING] Unknown configuration option ignored.
```

---

## 28. SAFE CONFIGURATION DEFAULTS

Example:

```	ext
{
  "dry_run": true,
  "require_confirmation": true,
  "minimum_age_days": 7,
  "quarantine_enabled": true,
  "permanent_delete": false,
  "process_termination": false,
  "service_changes": false,
  "docker_cleanup": false,
  "sql_server_changes": false,
  "browser_cache_cleanup": false,
  "power_plan_change": false,
  "registry_changes": false,
  "network_changes": false,
  "external_network_access": false,
  "log_level": "normal"
}
```

The exact schema must be finalized during Phase 1.

---

## 29. LOGGING AND REDACTION

Create rotating local logs.

Logs may contain:

* timestamp
* run ID
* operation
* result
* reason for skipping
* error information
* command category
* rollback information

Never log:

* passwords
* API keys
* access tokens
* cookies
* database credentials
* `.env` contents
* authentication headers
* private file contents

Redact user-specific paths.

For example:

```	ext
C:\Users\Farmanullah\...
```

should appear as:

```	ext
%USERPROFILE%\...
```

where practical.

Use log rotation and maximum file-size limits.

---

## 30. TEMPORARY FILE SAFETY

Do not perform generic recursive deletion of:

```	ext
C:\Windows\Temp
```

or:

```	ext
%TEMP%
```

unless the exact operation has been separately reviewed and explicitly approved.

Prefer narrowly defined application-specific cache directories.

Every deletion target must pass:

1. allowlist validation
2. path normalization
3. protected-path check
4. symlink/junction check
5. age check
6. lock/in-use check
7. file-type check
8. quarantine check

---

## 31. FILE DELETION SAFETY

Before moving anything:

* verify exact path
* verify expected parent
* normalize path
* verify it is under an approved allowlist root
* verify it is not protected
* verify it is not a symlink/junction/reparse point
* verify age
* verify it is not locked
* verify it is a regular file or explicitly approved directory
* verify the operation is enabled
* verify quarantine destination
* verify sufficient free space for quarantine
* verify manifest can be written

If any check fails:

```	ext
[SKIPPED]
```

Never continue automatically.

---

## 32. NO "PERFORMANCE HACKS"

Do not implement:

* RAM cleaners
* registry cleaners
* DLL injection
* memory manipulation
* kernel drivers
* process injection
* undocumented Windows hacks
* global CPU priority manipulation
* disabling security features
* forced pagefile manipulation
* disabling Windows services for arbitrary performance gains

The utility should perform conservative maintenance rather than manipulate Windows internals.

---

## 33. TESTING BEFORE CODE COMPLETION

The project must include automated tests using:

* `unittest`, or
* `pytest`

Tests must use temporary directories, mocks, and simulated environments.

Do NOT run destructive tests against the real laptop.

Required tests include:

### Platform

* Windows 11 detection
* unsupported OS handling

### CLI

* default dry-run
* `--dry-run`	ext
* `--apply`	ext
* `--yes`	ext
* invalid arguments
* mutually exclusive flags
* typed confirmation requirements

### Files

* safe path accepted
* dangerous path rejected
* protected path rejected
* symlink rejected
* junction rejected
* reparse point rejected
* locked file skipped
* young file skipped
* old eligible file accepted

### Quarantine

* file moved correctly
* manifest generated
* path traversal rejected
* collision handled safely
* rollback restores quarantined file
* purge requires typed confirmation

### Configuration

* valid configuration
* invalid configuration
* missing configuration
* unknown configuration keys
* destructive options default to false

### Security

* shell injection resistance
* `shell=False`	ext
* command argument validation
* timeout handling
* sensitive log redaction
* no automatic elevation
* no persistence

### Rollback

* previous power plan restored
* changed state detected
* rollback safely skipped when state differs

### Dry-run

Verify that dry-run performs zero system modifications.

---

## 34. DO NOT TEST DESTRUCTIVELY ON THE HOST

Never test deletion, service changes, process termination, or rollback against the user's actual development environment.

Use:

* temporary directories
* mocks
* isolated test environments
* disposable virtual machines where appropriate

The generated documentation must recommend testing in a VM or disposable environment before applying changes to the real laptop.

---

## 35. AI EXECUTION SAFETY

Google Antigravity must ONLY generate and review the code.

It must NOT execute generated system-maintenance code automatically.

Recommended workflow:

1. Review Phase 1.
2. Explicitly approve Phase 1.
3. Generate Phase 2.
4. Review source code.
5. Run automated tests.
6. Perform static safety review.
7. Test in a VM/disposable environment.
8. Run `--dry-run` manually on the real laptop.
9. Review the dry-run plan.
10. Manually choose whether to run `--apply`.

Never allow an AI agent to automatically apply system modifications to the real laptop.

---

## 36. EXACT TERMINAL OUTPUT FORMAT

Use:

```	ext
[CHECK]
[SAFE]
[WARNING]
[SKIPPED]
[ACTION]
[SUCCESS]
[ERROR]
```

Before every potentially destructive operation show:

* exact operation
* exact target
* estimated size
* age threshold
* whether it is reversible
* whether quarantine is available
* whether administrator privileges are required

Example:

```	ext
[WARNING]
Operation: Quarantine npm cache files
Target: <approved exact path>
Eligible data: 842 MB
Age threshold: 7 days
Reversible: Yes, if quarantine succeeds
Administrator: No

Continue? [y/N]
```

Default answer:

```	ext
N
```

---

## 37. STATUS REPORT

After execution provide:

```	ext
System Status
-------------
Windows version:
Administrator:
CPU:
RAM:
Free disk space:
Active power plan:

Maintenance
-----------
Files analyzed:
Files skipped:
Files quarantined:
Cache commands executed:
Disk space recovered:

Protected
---------
SQL Server:
Docker:
Brave:
Google Antigravity:
IDEs:
Development servers:

Rollback
--------
Run ID:
Rollback available:
Non-reversible actions:
```

Do not invent performance improvements.

---

## 38. FINAL SAFETY REVIEW TABLE

Before declaring implementation complete, produce a table containing EVERY:

| Category               | Required information                 |
| ---------------------- | ------------------------------------ |
| File deletion          | Exact path and reason                |
| File movement          | Source and quarantine destination    |
| Process stop           | Exact process and why                |
| Service change         | Service and previous/new state       |
| Windows setting        | Exact setting and previous/new value |
| Power-plan change      | Previous/new plan                    |
| Admin operation        | Why elevation is required            |
| Irreversible operation | Exact operation and warning          |
| External command       | Executable + argument list           |
| Python dependency      | Package + purpose                    |
| Modifiable location    | Exact path                           |
| Protected location     | Protection reason                    |
| Network access         | Destination/purpose, if any          |
| Logging                | Data collected + redaction           |
| Rollback               | What can/cannot be restored          |
| Persistence            | Confirmation that none exists        |
| Auto-elevation         | Confirmation that none exists        |

If there are zero entries in a category, explicitly state:

```	ext
None.
```

No hidden system modification should remain outside this table.

---

## 39. FINAL "DO NOT DO" AUDIT

Before final output, explicitly verify that the implementation does NOT:

* persist itself
* auto-elevate
* disable security
* modify Defender
* modify UAC
* modify firewall
* modify DNS
* modify proxy
* modify hosts
* modify Secure Boot
* modify BIOS/UEFI
* modify drivers
* modify registry by default
* stop SQL Server
* delete SQL Server database files
* delete Docker volumes
* shut down WSL
* delete browser profiles
* delete cookies
* delete passwords
* delete bookmarks
* delete `.env`	ext
* delete Git repositories
* delete project source
* delete lock files
* clean OneDrive automatically
* empty Recycle Bin
* modify Windows Update
* modify WinSxS
* modify Windows Installer
* modify Prefetch
* modify SoftwareDistribution
* disable indexing
* disable SysMain
* manipulate pagefile
* manipulate hibernation
* overclock hardware
* undervolt hardware
* disable thermal protections
* execute downloaded code
* use encoded PowerShell payloads
* use `eval`	ext
* use `exec`	ext
* use unsafe `shell=True`	ext
* execute arbitrary user-supplied commands

If any prohibited behavior appears, stop and report it instead of silently continuing.

---

## 40. REQUIRED DELIVERABLES

After Phase 1 approval and implementation, provide:

1. `optimizer.py`	ext
2. automated tests
3. `config.json.example`	ext
4. `requirements.txt` only if genuinely necessary
5. README
6. CLI documentation
7. rollback documentation
8. quarantine documentation
9. threat model
10. security assumptions
11. residual-risk assessment
12. test results
13. final safety-review table
14. protected-path list
15. allowed cleanup-path list
16. allowed-command list
17. forbidden-command list
18. administrator-permission requirements
19. known limitations

---

## 41. FINAL PRINCIPLE

When choosing between:

```	ext
More automation
vs.
More safety
```

choose safety.

When choosing between:

```	ext
Permanent deletion
vs.
Quarantine
```

choose quarantine.

When choosing between:

```	ext
Guessing
vs.
Skipping
```

choose skipping.

When choosing between:

```	ext
Automatic elevation
vs.
User-controlled elevation
```

choose user-controlled elevation.

When choosing between:

```	ext
Aggressive optimization
vs.
Conservative maintenance
```

choose conservative maintenance.

The utility must behave like a **careful system-maintenance tool**, not an aggressive "PC booster."

The user must remain in control of every meaningful system change.

Most importantly:

**Do not claim that the prompt, generated code, or utility is guaranteed safe. Demonstrate safety through design, testing, review, and controlled execution instead.**

## PHASE 2 — IMPLEMENT THE WINDOWS 11 DEVELOPMENT OPTIMIZER

You have completed Phase 1: architecture, threat model, safety requirements, allowlists, protected paths, CLI design, rollback strategy, testing strategy, and failure-mode analysis.

I am now explicitly approving **Phase 2 implementation**.

## CRITICAL EXECUTION RULE

**CREATE THE APPLICATION/PRODUCT, BUT DO NOT RUN, EXECUTE, TEST-EXECUTE, INSTALL, OR APPLY IT TO MY WINDOWS LAPTOP.**

Your job in this phase is to **write the complete project files and source code only**.

Do NOT execute the generated optimizer after creating it.

Do NOT run:

* `python optimizer.py`	ext
* `py optimizer.py`	ext
* `optimizer.py --apply`	ext
* `optimizer.py --apply --yes`	ext
* `optimizer.py --purge-quarantine`	ext
* rollback commands
* cleanup commands
* PowerShell commands that modify the system
* registry commands
* service commands
* process termination commands
* package-manager cleanup commands
* Docker cleanup commands
* WSL commands
* power-plan modification commands
* any generated system-modifying command

Do NOT automatically install Python packages or dependencies.

Do NOT automatically create a scheduled task, startup entry, Windows service, registry entry, background process, or persistence mechanism.

Do NOT request administrator privileges.

Do NOT launch the application automatically after generating it.

The application must remain completely inactive until **I manually choose to run it later**.

---

## 1. IMPLEMENT THE PRODUCT

Create the complete production-quality Windows 11 Development Optimizer according to the approved Phase 1 design.

The product should be a **manual-run Windows 11 optimization utility for development machines**.

Primary environment:

* Windows 11
* Python 3
* Node.js/npm
* Python/pip
* .NET/NuGet
* Docker/Docker Desktop
* WSL
* SQL Server
* Postman
* Brave Browser
* Google Antigravity / IDEs

The application must be designed specifically for a developer workstation.

---

## 2. MANUAL EXECUTION ONLY

This is extremely important.

The application must NOT run continuously.

It must NOT:

* run in the background
* start with Windows
* create a scheduled task
* create a Windows service
* add itself to Startup
* create a registry Run key
* install a daemon
* monitor the computer continuously
* automatically perform cleanup
* automatically change power settings
* automatically kill processes
* automatically modify Windows configuration

The application should perform actions **only while I have manually launched it**.

When the application exits, it must stop completely.

After reboot, nothing from this application should automatically restart.

---

## 3. DO NOT EXECUTE THE APPLICATION

After generating the project:

1. Save all source files.
2. Save configuration files.
3. Save tests.
4. Save documentation.
5. Perform static code inspection only.
6. Do NOT execute the application.
7. Do NOT execute the test suite.
8. Do NOT install dependencies.
9. Do NOT perform a dry-run.
10. Do NOT perform an actual cleanup.
11. Do NOT modify my Windows system.

At the end, show me:

* project structure
* files created
* dependencies required
* installation commands that I can manually run later
* commands for dry-run that I can manually run later
* commands for applying changes that I can manually run later
* commands for rollback
* commands for quarantine management
* how to review the generated code before running it

But **do not execute those commands yourself**.

---

## 4. SAFE DEFAULT BEHAVIOR

The application must default to:

**DRY-RUN / PLAN MODE**

If I manually execute the program with no arguments, it should NOT perform system modifications.

For example:

```text
python optimizer.py
```

must only show status/help/safety information or generate a non-destructive plan.

It must NOT:

* delete files
* move files
* terminate processes
* change power plans
* clear caches
* modify services
* modify registry
* change network settings
* modify browser settings
* modify Docker settings
* modify WSL settings

---

## 5. APPLY MODE

Actual changes must require explicit command-line intent.

For example:

```text
python optimizer.py --apply
```

must NOT be sufficient by itself.

Require the appropriate confirmation mechanism defined in Phase 1.

For destructive operations, require:

```text
--apply
--yes
```

AND the required typed confirmation where Phase 1 specifies one.

`--yes` must never bypass high-risk typed confirmation.

Never interpret an accidental or ambiguous argument as permission to perform destructive operations.

---

## 6. QUARANTINE INSTEAD OF DELETE

The optimizer must not permanently delete eligible files by default.

Use quarantine:

```text
%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<run-id>\
```

Before moving anything:

* verify source path
* verify destination path
* verify source is on the approved allowlist
* verify source is not protected
* verify age requirement
* verify it is not locked/in use
* verify it is not a symlink/junction/reparse point
* verify destination does not create a path collision
* verify sufficient free space
* record the operation in the manifest

Permanent deletion must require a separate explicit:

```text
--purge-quarantine
```

and a strong typed confirmation.

---

## 7. FILE AGE SAFETY

Default cleanup eligibility:

**Only files/directories with modification time >= 7 days old.**

Never clean recently modified files by default.

Make the threshold configurable only within the safety limits established in Phase 1.

Do not allow a configuration mistake to silently reduce the safety threshold.

---

## 8. EXACT ALLOWLIST

Use an **allowlist**, not a broad denylist.

Only clean paths/categories explicitly approved by the implementation.

Never perform generic recursive cleanup of:

```text
C:\
C:\Users\
C:\Windows\
C:\Program Files\
C:\ProgramData\
```

Never attempt "find all temporary files on the computer."

Every cleanup target must be explicitly defined.

---

## 9. PROTECTED PATHS

Implement all protected paths from Phase 1.

At minimum protect:

```text
C:\Windows
C:\Program Files
C:\Program Files (x86)
C:\ProgramData
%USERPROFILE%
%USERPROFILE%\Desktop
%USERPROFILE%\Documents
%USERPROFILE%\Downloads
%USERPROFILE%\OneDrive
.git
.env
SQL Server data directories
Docker Desktop data
WSL VHDX files
browser profiles
VS Code workspaceStorage
Windows Installer
WinSxS
Prefetch
SoftwareDistribution
Microsoft Defender data
```

Also ensure child paths and equivalent resolved paths are protected.

Do not rely solely on string matching.

Use normalized/resolved path validation.

---

## 10. SYMLINK / JUNCTION / REPARSE-POINT SAFETY

Never recursively follow arbitrary:

* symbolic links
* junctions
* mount points
* Windows reparse points

Do not allow a cleanup path to escape its approved root.

Implement explicit path containment checks.

The resolved destination must remain inside the approved cleanup root.

---

## 11. LOCKED / ACTIVE FILES

If a file or directory is:

* locked
* currently being used
* inaccessible
* permission denied
* changing during inspection

skip it safely.

Do not force-close handles.

Do not take ownership.

Do not disable security mechanisms.

Do not terminate the process merely to delete the file.

Report it as:

```text
[SKIPPED]
```

---

## 12. TOOL-SPECIFIC OPERATIONS

Use only the safe commands approved in Phase 1.

## npm

Prefer:

```text
npm cache verify
```

Do not automatically use:

```text
npm cache clean --force
```

Make destructive cache cleaning explicit and opt-in.

## pip

Only use:

```text
pip cache purge
```

when explicitly enabled by the user.

## NuGet

Use:

```text
dotnet nuget locals http-cache --clear
```

Only when explicitly selected.

## Docker

Default behavior:

```text
docker system df
```

for inspection.

Do NOT automatically run:

```text
docker system prune
docker system prune -a
docker volume prune
docker image prune
docker container prune
```

Do not delete:

* containers
* images
* volumes
* Docker Desktop data

unless a future explicit feature is separately designed and confirmed.

## WSL

Do not automatically shut down or modify WSL.

---

## 13. PROCESS MANAGEMENT

Do NOT implement broad process killing.

Do not terminate:

* Windows system processes
* security software
* SQL Server
* Docker
* WSL
* development tools
* browsers
* IDEs

unless the exact process operation was explicitly approved in Phase 1.

Prefer informational diagnostics over termination.

If process stopping is included as an optional feature, require:

* explicit opt-in
* exact allowlist
* clear process identification
* confirmation
* logging

---

## 14. POWER PLAN

If power-plan optimization was approved in Phase 1:

* make it optional
* never apply it automatically
* record the original state
* record the new state
* provide rollback
* verify current state before rollback
* skip rollback if the user has manually changed the setting since the optimizer changed it

Never claim rollback is possible for a setting that cannot be reliably restored.

---

## 15. ROLLBACK MANIFEST

Every modifying run must generate a unique run ID.

Example:

```text
RUN-20260924-120000
```

Store a manifest containing:

* run ID
* timestamp
* application version
* operation
* source path
* quarantine destination
* previous setting
* new setting
* command executed
* result
* skipped items
* errors
* rollback information

Never claim that permanently deleted data is recoverable.

Only quarantined files can be considered rollback candidates.

Before rollback:

1. verify the manifest
2. verify the source/destination state
3. verify the user has not changed the affected state
4. skip conflicting items
5. never overwrite newer user-created data
6. log the result

---

## 16. SUBPROCESS SECURITY

All external commands must use safe subprocess execution.

Use:

```python
subprocess.run([...], shell=False, ...)
```

Do not construct shell commands from unsanitized user input.

Do not use:

```text
shell=True
eval()
exec()
os.system()
```

Do not download executable code.

Do not dynamically import arbitrary modules.

Do not use remote code execution.

Do not use PowerShell:

```text
-EncodedCommand
```

Do not hide commands from the user.

Every external command must have:

* explicit executable
* argument list
* timeout
* captured output
* controlled environment
* error handling

---

## 17. NETWORK SAFETY

The optimizer must not require Internet access.

Do not:

* download scripts
* download binaries
* install dependencies automatically
* contact remote servers
* upload logs
* upload system information
* send telemetry

If an external tool is unavailable, report:

```text
[SKIPPED]
```

rather than attempting to download/install it.

---

## 18. CONFIGURATION

Create a validated configuration system.

If configuration is:

* missing
* malformed
* invalid
* partially corrupted

fall back to safe defaults.

Unknown configuration keys should generate warnings.

Destructive options must default to:

```text
false
```

Never interpret missing configuration as permission to perform destructive actions.

---

## 19. LOGGING

Implement safe logging.

Never log:

* passwords
* API keys
* access tokens
* refresh tokens
* cookies
* session IDs
* database passwords
* `.env` contents
* authentication headers
* private credentials

Redact user paths where practical:

```text
C:\Users\<username>
```

as:

```text
%USERPROFILE%
```

Implement reasonable log rotation.

Do not create excessive logs.

---

## 20. FORBIDDEN OPERATIONS

The optimizer must NOT perform the following:

* registry cleanup
* registry optimization
* service disabling
* service reconfiguration
* Windows Defender modification
* UAC modification
* firewall modification
* DNS modification
* proxy modification
* hosts-file modification
* environment-variable modification
* Secure Boot modification
* driver modification
* BIOS modification
* UEFI modification
* overclocking
* undervolting
* thermal-limit modification
* pagefile modification
* hibernation modification
* indexing modification
* SysMain modification
* Prefetch deletion
* WinSxS cleanup
* Windows Installer cleanup
* SoftwareDistribution deletion
* Windows Update manipulation
* browser policy modification
* browser extension modification
* browser cookie deletion
* browser session deletion
* OneDrive manipulation
* cloud synchronization changes
* Recycle Bin emptying
* WSL shutdown
* Docker Desktop configuration changes
* arbitrary Windows Temp root deletion

Do not add "performance tweaks" simply because they appear on Internet optimization guides.

---

## 21. ADMINISTRATOR PRIVILEGES

Never automatically elevate.

Never use:

```text
runas
```

automatically.

Never trigger a UAC prompt automatically.

If an operation requires administrator privileges:

```text
[SKIPPED] Administrator privileges required.
```

Explain:

* why it requires elevation
* what would be changed
* the exact command the user could manually execute later

The optimizer itself must remain usable without administrator privileges wherever possible.

---

## 22. CLI

Implement the approved CLI.

At minimum support:

```text
--help
--version
--status
--doctor
--plan
--plan --json
--dry-run
--apply
--yes
--rollback <run-id>
--purge-quarantine
```

Rules:

* no arguments = safe status/help/plan behavior
* `--dry-run` and `--apply` are mutually exclusive
* invalid arguments = no changes
* destructive operations require explicit confirmation
* `--yes` must not bypass high-risk confirmation
* unknown arguments must never be ignored

---

## 23. OUTPUT

Use the exact output tags:

```text
[CHECK]
[SAFE]
[WARNING]
[SKIPPED]
[ACTION]
[SUCCESS]
[ERROR]
```

Example:

```text
[CHECK] Windows 11 detected
[SAFE] Running in dry-run mode
[CHECK] Inspecting approved npm cache paths
[SKIPPED] File is currently in use
[WARNING] Administrator privileges would be required
```

Make output understandable to a beginner.

---

## 24. TESTS

Create a complete automated test suite.

Tests must cover:

* Windows 11 detection
* unsupported OS behavior
* CLI validation
* configuration validation
* allowlist enforcement
* protected-path enforcement
* path traversal prevention
* symlink/junction/reparse-point handling
* locked-file handling
* file-age filtering
* quarantine behavior
* quarantine collision handling
* rollback logic
* manifest validation
* dry-run behavior
* destructive-operation confirmation
* subprocess argument handling
* timeout handling
* shell-injection resistance
* log redaction
* admin-required behavior
* fail-closed behavior

IMPORTANT:

**Create the tests, but DO NOT RUN THEM.**

The tests must never intentionally modify the real host system.

Use temporary directories, mocks, and isolated test environments.

---

## 25. PROJECT STRUCTURE

Use a clean production-oriented structure, for example:

```text
Win11DevOptimizer/
│
├── optimizer.py
├── requirements.txt
├── README.md
├── LICENSE
├── config/
│   └── default_config.json
│
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── safety.py
│   ├── paths.py
│   ├── quarantine.py
│   ├── rollback.py
│   ├── process_manager.py
│   ├── power.py
│   ├── cache_manager.py
│   ├── diagnostics.py
│   ├── logging_utils.py
│   └── subprocess_utils.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_safety.py
│   ├── test_paths.py
│   ├── test_quarantine.py
│   ├── test_rollback.py
│   ├── test_config.py
│   └── test_subprocess_security.py
│
└── docs/
    ├── SAFETY.md
    ├── THREAT_MODEL.md
    ├── OPERATIONS.md
    └── ROLLBACK.md
```

You may adjust the structure if Phase 1 established a better design.

---

## 26. CODE QUALITY

The implementation must be:

* readable
* modular
* typed where appropriate
* documented
* defensive
* fail-closed
* maintainable
* deterministic
* explicit rather than magical

Avoid unnecessary complexity.

Do not implement undocumented features.

Do not add features outside the approved Phase 1 scope.

If you discover a new safety issue during implementation, **STOP implementation of that part and clearly report the issue instead of silently changing the requirements.**

---

## 27. DEPENDENCIES

Minimize third-party dependencies.

Prefer Python standard library where practical.

Do not automatically install anything.

Provide:

```text
requirements.txt
```

only if dependencies are genuinely required.

Document why each dependency is required.

Do not use remote packages dynamically at runtime.

---

## 28. NO AUTOMATIC EXECUTION BY ANTIGRAVITY

This rule overrides convenience.

After generating the project, DO NOT:

* run the program
* run the tests
* run `pip install`	ext
* run `python`	ext
* run PowerShell
* run cleanup commands
* run Docker commands
* run npm commands
* modify Windows settings
* modify files outside the project
* start background processes
* create scheduled tasks
* request elevation

You may perform **static inspection of the generated source code**.

---

## 29. FINAL RESPONSE AFTER IMPLEMENTATION

When implementation is complete, DO NOT say:

> "The optimizer is safe."

Do not say:

> "This cannot harm your laptop."

Do not say:

> "This is guaranteed safe."

Instead report objectively:

### Files created

List every file.

### Dependencies

List required packages and why.

### Static safety checks

List the checks performed without executing the program.

### Not executed

Explicitly state:

* application was not run
* tests were not run
* dependencies were not installed
* cleanup was not performed
* Windows settings were not changed
* no administrator elevation occurred

### Manual next steps

Give me the exact commands I can manually review and execute later.

Do NOT execute those commands yourself.

---

## 30. STOP CONDITION

After creating and statically reviewing the project, STOP.

Do not continue to Phase 3 unless I explicitly request it.

Do not run anything.

Wait for my next instruction.

## FINAL REQUIREMENT

The goal of this phase is:

**BUILD THE PRODUCT → STATICALLY REVIEW THE CODE → STOP.**

Not:

**BUILD → RUN → TEST → CLEAN MY COMPUTER.**

I will personally decide when the application is executed.



# PHASE 2 — BUILD THE WINDOWS 11 DEVELOPMENT OPTIMIZER

## CREATE THE COMPLETE PRODUCT — DO NOT EXECUTE ANYTHING

You have already completed Phase 1: requirements analysis, architecture, threat model, safety model, allowlist design, protected-path design, CLI design, quarantine strategy, rollback strategy, configuration design, logging strategy, privilege model, failure-mode analysis, and testing strategy.

I am now explicitly authorizing you to proceed with **PHASE 2: IMPLEMENTATION**.

However, this approval has a very specific scope:

> **YOU ARE AUTHORIZED TO CREATE THE COMPLETE APPLICATION/PRODUCT AND ALL PROJECT FILES.**
>
> **YOU ARE NOT AUTHORIZED TO RUN, EXECUTE, INSTALL, TEST-EXECUTE, OR APPLY THE APPLICATION TO MY WINDOWS COMPUTER.**

The implementation must be complete enough that I can manually review it and later decide when to run it.

---

# 1. ABSOLUTE EXECUTION RESTRICTION

This is the most important requirement in this prompt.

During this phase, you may:

* create source-code files
* create configuration files
* create documentation
* create test files
* create project directories
* inspect the source code you generated
* perform static analysis/review of the generated code
* explain how the application should be manually installed and executed later

You may NOT:

* run the application
* execute the generated Python code
* execute the generated test suite
* install Python packages
* execute `pip install`
* execute `python`
* execute `py`
* execute PowerShell commands that modify the computer
* execute CMD commands that modify the computer
* execute npm commands
* execute Docker commands
* execute WSL commands
* execute SQL commands against my system
* modify Windows settings
* modify the registry
* modify services
* terminate processes
* change the power plan
* clean caches
* delete files
* move files into quarantine
* purge quarantine
* perform rollback
* request administrator elevation
* create scheduled tasks
* create Windows services
* create startup entries
* create registry Run entries
* create background processes
* create persistence mechanisms

### DO NOT EXECUTE THE APPLICATION AFTER GENERATING IT.

### DO NOT AUTOMATICALLY TEST-EXECUTE THE APPLICATION.

### DO NOT AUTOMATICALLY INSTALL ITS DEPENDENCIES.

### DO NOT AUTOMATICALLY "VERIFY" IT BY RUNNING IT.

Static code review is allowed.

Execution is not allowed.

---

# 2. DO NOT INTERPRET "IMPLEMENTATION COMPLETE" AS PERMISSION TO RUN

When implementation is finished, STOP.

Do not assume that:

* "build complete"
* "implementation complete"
* "project generated"
* "code generated"
* "tests created"
* "dependencies listed"
* "ready"
* "done"

means that you have permission to execute the application.

It does not.

The application must remain unexecuted until I give a separate, explicit instruction.

---

# 3. EXPLICIT APPROVAL MODEL

This is a two-step authorization model.

### Authorization 1 — Already granted

I am granting you permission to:

**CREATE THE SOFTWARE.**

### Authorization 2 — NOT granted

I am NOT granting permission to:

**EXECUTE THE SOFTWARE.**

Execution will require a separate future instruction from me.

Do not combine these two permissions.

---

# 4. PRODUCT GOAL

Build a production-oriented Windows 11 development-machine optimization utility.

The utility is intended for a developer workstation using technologies/tools such as:

* Windows 11
* Python
* Node.js
* npm
* pip
* .NET
* NuGet
* Docker
* Docker Desktop
* WSL
* SQL Server
* Postman
* Brave Browser
* Google Antigravity
* VS Code and other development tools

The goal is to provide **controlled diagnostics and optional cleanup of specifically approved development-related temporary/cache data** while minimizing the possibility of damaging the user's development environment.

This is NOT a generic Windows "speed booster."

Do not add random Internet optimization tricks.

Do not add undocumented "performance hacks."

Do not make aggressive system modifications.

---

# 5. MANUAL-RUN ONLY

The application must operate only when manually launched by the user.

It must NOT create persistence.

Never implement:

* Windows Startup registration
* Scheduled Tasks
* Windows Services
* registry Run keys
* background daemons
* startup scripts
* login hooks
* event-triggered execution
* continuous monitoring
* automatic timers
* automatic cleanup
* automatic optimization

When the application exits, it must stop completely.

After Windows restarts, the application must remain inactive unless I manually start it.

---

# 6. WINDOWS 11 ONLY

The application must verify that it is running on Windows 11.

If the operating system is unsupported:

```text
[ERROR] Unsupported operating system.
[SKIPPED] No system modifications will be performed.
```

Fail closed.

Do not attempt compatibility workarounds that could modify another operating system.

---

# 7. FAIL-CLOSED DESIGN

If anything is uncertain, unexpected, invalid, inaccessible, or unsafe:

**DO NOTHING.**

Examples:

* invalid command-line arguments
* malformed configuration
* unknown cleanup path
* unexpected filesystem structure
* insufficient permissions
* inaccessible file
* locked file
* path resolution failure
* suspicious symlink
* junction/reparse point
* missing executable
* unexpected subprocess result
* unsupported Windows version
* ambiguous configuration
* insufficient quarantine space
* manifest failure

The application should skip the operation and report the reason.

Never "try something else" that is broader or more destructive.

---

# 8. SAFE DEFAULT

The application must default to a non-destructive mode.

If the user runs:

```text
python optimizer.py
```

the application must NOT perform cleanup.

It should display status, help, diagnostics, or a safe plan.

No file deletion.

No file movement.

No process termination.

No Windows setting changes.

No registry changes.

No service changes.

No network changes.

No browser changes.

No Docker configuration changes.

No WSL changes.

---

# 9. DRY-RUN MODE

Support:

```text
python optimizer.py --dry-run
```

Dry-run means:

> Inspect and report what WOULD happen without performing the action.

Dry-run must NOT:

* delete files
* move files
* quarantine files
* purge files
* change settings
* stop processes
* modify services
* modify registry
* change power plans
* modify Docker
* modify WSL
* modify browser data

A dry-run must not accidentally perform the operation it is describing.

---

# 10. APPLY MODE

Actual modifications must require explicit user intent.

Support:

```text
python optimizer.py --apply
```

But `--apply` alone must not automatically authorize high-risk/destructive operations.

For destructive categories require:

```text
--apply --yes
```

and, where required, an additional typed confirmation.

`--yes` must NOT bypass high-risk confirmation.

Do not treat arbitrary text or accidental input as confirmation.

---

# 11. STRICT COMMAND-LINE INTERFACE

Implement:

```text
--help
--version
--status
--doctor
--plan
--plan --json
--dry-run
--apply
--yes
--rollback <run-id>
--purge-quarantine
```

Rules:

* unknown arguments = error + no changes
* invalid combinations = error + no changes
* `--dry-run` and `--apply` are mutually exclusive
* no arguments = safe status/plan behavior
* destructive actions require explicit confirmation
* purge requires separate confirmation
* rollback requires explicit run ID
* malformed run ID = no changes

---

# 12. QUARANTINE INSTEAD OF PERMANENT DELETION

The default cleanup mechanism must be quarantine, not permanent deletion.

Use:

```text
%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<run-id>\
```

Every modifying run gets a unique run ID.

Example:

```text
RUN-20260925-153000
```

Before moving an item into quarantine:

1. Verify source path.
2. Resolve the path safely.
3. Verify it belongs to an approved allowlist.
4. Verify it is not protected.
5. Verify it satisfies the age requirement.
6. Verify it is not locked/in use.
7. Verify it is not a symlink/junction/reparse point.
8. Verify destination safety.
9. Verify destination collision handling.
10. Verify sufficient free disk space.
11. Record the operation.
12. Move the item only after all checks succeed.

Never silently overwrite an existing quarantine item.

---

# 13. PERMANENT PURGE

Permanent deletion must be a separate operation:

```text
python optimizer.py --purge-quarantine
```

This must require strong confirmation.

The application must clearly explain:

* what will be permanently deleted
* where it is located
* which run it belongs to
* that permanent deletion cannot be rolled back by the optimizer

Never claim permanent deletion is reversible.

---

# 14. FILE AGE SAFETY

Default cleanup rule:

> Only consider files/directories whose modification time is at least 7 days old.

Do not clean recently modified files by default.

Do not silently lower this threshold.

If a configurable threshold is supported, enforce a safety floor.

---

# 15. LOCKED / IN-USE FILES

If a file is:

* locked
* open
* actively being used
* inaccessible
* permission denied
* changing while inspected

skip it.

Do not:

* force-close it
* take ownership
* change permissions merely to delete it
* terminate the owning process
* reboot Windows
* bypass the lock

Report:

```text
[SKIPPED] File is currently in use.
```

---

# 16. SYMLINK / JUNCTION / REPARSE POINT SAFETY

Never blindly follow:

* symbolic links
* junctions
* mount points
* Windows reparse points

Do not allow a cleanup operation to escape its approved root.

Use normalized/resolved paths and explicit containment checks.

A path must remain inside its approved cleanup root after resolution.

---

# 17. EXACT ALLOWLIST CLEANUP

Use an explicit **allowlist**.

Do NOT use a broad strategy such as:

> "Delete temporary files everywhere."

Do NOT scan the entire drive looking for files that appear unnecessary.

Do NOT use:

```text
C:\
C:\Users\
C:\Windows\
```

as generic cleanup roots.

Every cleanup location must be explicitly defined and approved.

---

# 18. PROTECTED PATHS

Protect at minimum:

```text
C:\Windows
C:\Program Files
C:\Program Files (x86)
C:\ProgramData

%USERPROFILE%
%USERPROFILE%\Desktop
%USERPROFILE%\Documents
%USERPROFILE%\Downloads
%USERPROFILE%\OneDrive

.git
.env

SQL Server data directories
Docker Desktop data
WSL VHDX files
browser profile directories
VS Code workspaceStorage
Windows Installer
WinSxS
Prefetch
SoftwareDistribution
Microsoft Defender data
```

Also protect equivalent/resolved paths.

Do not rely only on simple string matching.

---

# 19. EXPLICITLY FORBIDDEN OPERATIONS

Do NOT implement automatic operations for:

### Windows/system

* registry cleanup
* registry optimization
* registry modification
* service disabling
* service reconfiguration
* Windows Defender modification
* UAC modification
* firewall modification
* DNS modification
* proxy modification
* hosts-file modification
* environment-variable modification
* Secure Boot modification
* driver modification
* BIOS modification
* UEFI modification
* overclocking
* undervolting
* thermal-limit modification
* pagefile modification
* hibernation modification
* indexing modification
* SysMain modification
* Prefetch deletion
* WinSxS deletion
* Windows Installer cleanup
* SoftwareDistribution deletion
* Windows Update manipulation

### Browser

Do not modify:

* browser policies
* extensions
* cookies
* sessions
* saved passwords
* profiles
* history
* bookmarks

### Cloud

Do not modify:

* OneDrive
* cloud synchronization
* cloud files

### Development environments

Do not automatically:

* delete Git repositories
* delete `.git`
* delete `.env`
* modify source code
* modify project files
* modify package manifests
* modify lock files
* modify SQL Server databases
* modify Docker Desktop configuration
* delete Docker volumes
* delete Docker containers
* delete Docker images
* shut down WSL

### Hardware

Do not modify:

* BIOS
* UEFI
* firmware
* drivers
* CPU settings
* GPU settings
* voltage
* thermal controls

---

# 20. SAFE TOOL-SPECIFIC OPERATIONS

Use only operations explicitly approved in Phase 1.

## npm

Prefer inspection:

```text
npm cache verify
```

Do not automatically run:

```text
npm cache clean --force
```

If supported, destructive npm cache cleaning must be explicitly opt-in.

---

## pip

If cache cleanup is implemented, make:

```text
pip cache purge
```

explicitly opt-in.

Do not automatically run it.

---

## NuGet

If implemented:

```text
dotnet nuget locals http-cache --clear
```

must be explicitly selected.

Do not clear other NuGet locations unless separately approved.

---

## Docker

Default operation:

```text
docker system df
```

for inspection only.

Do NOT automatically run:

```text
docker system prune
docker system prune -a
docker volume prune
docker image prune
docker container prune
```

Do not delete Docker volumes, containers, or images by default.

---

## WSL

Do not automatically shut down WSL.

Do not modify WSL distributions.

Do not touch WSL VHDX files.

---

# 21. PROCESS MANAGEMENT

Do not implement broad process termination.

Never use:

```text
taskkill /F /IM *
```

or equivalent broad termination.

Do not terminate arbitrary processes.

Do not terminate:

* Windows processes
* security software
* SQL Server
* Docker
* WSL
* browsers
* IDEs
* development tools

unless an exact process-management feature has been separately approved.

Prefer diagnostics.

---

# 22. POWER PLAN

If power-plan functionality was approved in Phase 1:

* it must be opt-in
* it must never run automatically
* record the previous state
* record the new state
* provide rollback
* verify current state before rollback
* do not overwrite a user change made after optimization

If reliable rollback cannot be guaranteed, do not implement the modification.

---

# 23. ROLLBACK

Every modifying run must have a unique run ID.

Create a rollback manifest containing:

* run ID
* timestamp
* application version
* operation
* original path
* quarantine path
* previous setting
* new setting
* command
* result
* skipped items
* errors
* rollback information

Rollback must:

1. validate the manifest
2. verify the current state
3. detect conflicts
4. avoid overwriting newer user data
5. restore only when safe
6. skip conflicting items
7. log every result

Never claim that permanently deleted files can be restored.

---

# 24. SUBPROCESS SECURITY

All subprocess execution must use safe argument lists.

Use:

```python
subprocess.run(
    [...],
    shell=False,
    timeout=...,
    ...
)
```

Never use:

```python
shell=True
```

Never use:

```python
os.system()
eval()
exec()
```

Never construct shell commands from unsanitized user input.

Every executable must be explicitly identified.

Every subprocess must have:

* timeout
* captured output
* error handling
* controlled arguments
* predictable environment

---

# 25. NO REMOTE CODE

Never:

* download executable code
* download Python scripts
* execute remote scripts
* dynamically import downloaded modules
* use remote code execution
* fetch configuration from an unknown server
* install packages automatically

Do not use PowerShell encoded commands.

Do not hide commands from the user.

---

# 26. NETWORK

The optimizer should not require Internet access.

Do not:

* send telemetry
* upload logs
* upload system information
* send diagnostics to external servers
* download dependencies automatically

If a required executable is unavailable, report:

```text
[SKIPPED]
```

Do not automatically install it.

---

# 27. ADMINISTRATOR PRIVILEGES

Never automatically elevate.

Do not automatically trigger UAC.

Do not use `runas` automatically.

If administrator access would be required:

```text
[SKIPPED] Administrator privileges are required.
```

Explain:

* why
* what would be changed
* what command the user could manually execute

The application should continue safely where possible.

---

# 28. CONFIGURATION

Implement validated configuration.

If configuration is:

* missing
* invalid
* malformed
* corrupted

use safe defaults.

Unknown keys should produce warnings.

Destructive options must default to:

```text
false
```

Never interpret missing configuration as permission to perform a destructive action.

---

# 29. LOGGING

Implement safe logging.

Never log:

* passwords
* API keys
* access tokens
* refresh tokens
* cookies
* session tokens
* database passwords
* `.env` contents
* credentials
* authentication headers

Where appropriate, redact:

```text
C:\Users\<username>
```

to:

```text
%USERPROFILE%
```

Implement log rotation.

Avoid excessive logging.

---

# 30. OUTPUT FORMAT

Use these tags:

```text
[CHECK]
[SAFE]
[WARNING]
[SKIPPED]
[ACTION]
[SUCCESS]
[ERROR]
```

Example:

```text
[CHECK] Windows 11 detected
[SAFE] Dry-run mode
[CHECK] Checking approved npm cache
[SKIPPED] File is locked
[WARNING] Administrator privileges would be required
```

Output must be understandable to a beginner.

---

# 31. DIAGNOSTICS

Implement a safe diagnostics command:

```text
python optimizer.py --doctor
```

It should inspect things such as:

* supported Windows version
* Python version
* available tools
* permissions
* configuration validity
* available disk space
* quarantine directory availability

Diagnostics must NOT modify the system.

---

# 32. STATUS

Implement:

```text
python optimizer.py --status
```

It should provide informational status only.

It must not perform optimization.

---

# 33. JSON PLAN

Implement:

```text
python optimizer.py --plan --json
```

The JSON output should describe:

* detected environment
* eligible cleanup categories
* candidate items
* skipped items
* reasons
* required privileges
* proposed actions
* warnings

It must not execute the actions.

---

# 34. TEST SUITE

Create tests for:

* Windows 11 detection
* unsupported OS
* CLI validation
* configuration validation
* allowlist enforcement
* protected-path enforcement
* path traversal protection
* symlink handling
* junction handling
* reparse-point handling
* locked files
* file-age filtering
* quarantine
* quarantine collisions
* rollback
* manifest validation
* dry-run
* confirmation logic
* subprocess safety
* shell-injection resistance
* timeout handling
* log redaction
* admin-required behavior
* fail-closed behavior

Use:

* temporary directories
* mocks
* fixtures
* isolated test data

Never write tests that intentionally modify the real Windows installation.

---

# 35. IMPORTANT — DO NOT RUN THE TESTS

Create the tests.

Do NOT execute the tests.

Do NOT run:

```text
pytest
python -m pytest
python -m unittest
```

Do not run any test command.

Static inspection of test code is allowed.

---

# 36. PROJECT STRUCTURE

Create a clean production-oriented structure.

Use this as the baseline:

```text
Win11DevOptimizer/
│
├── optimizer.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── config/
│   └── default_config.json
│
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── safety.py
│   ├── paths.py
│   ├── quarantine.py
│   ├── rollback.py
│   ├── process_manager.py
│   ├── power.py
│   ├── cache_manager.py
│   ├── diagnostics.py
│   ├── logging_utils.py
│   └── subprocess_utils.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_safety.py
│   ├── test_paths.py
│   ├── test_quarantine.py
│   ├── test_rollback.py
│   ├── test_config.py
│   └── test_subprocess_security.py
│
└── docs/
    ├── SAFETY.md
    ├── THREAT_MODEL.md
    ├── OPERATIONS.md
    └── ROLLBACK.md
```

You may improve the structure if there is a clear technical reason.

Do not add unnecessary components.

---

# 37. CODE QUALITY

The implementation must be:

* production-oriented
* modular
* readable
* maintainable
* defensive
* fail-closed
* documented
* explicit
* deterministic

Use type hints where appropriate.

Use clear error handling.

Do not hide failures.

Do not silently continue after a safety validation failure.

---

# 38. DEPENDENCIES

Minimize dependencies.

Prefer the Python standard library where practical.

If external dependencies are required:

1. list them in `requirements.txt`
2. explain why each is required
3. document installation instructions

Do NOT install them.

Do NOT run pip.

---

# 39. NO AUTO-MODIFICATION OUTSIDE THE PROJECT

During implementation, only create/modify files belonging to the project you are building.

Do not modify:

* Windows system files
* user documents
* browser data
* developer projects
* SQL Server data
* Docker data
* WSL data
* registry
* services
* environment variables
* firewall
* network configuration
* system settings

The optimizer itself must also enforce these boundaries when eventually executed.

---

# 40. NO HIDDEN FEATURES

Do not secretly add:

* telemetry
* analytics
* remote connections
* automatic updates
* background services
* scheduled tasks
* startup behavior
* system monitoring
* keylogging
* credential collection
* browser data collection
* environment-variable collection
* network scanning

The product must do exactly what is documented.

---

# 41. SECURITY REVIEW BEFORE STOPPING

Before you finish Phase 2, perform a **STATIC REVIEW ONLY**.

Do not execute anything.

Review the generated code for:

### Filesystem

* unsafe deletion
* unsafe movement
* path traversal
* protected-path bypass
* symlink traversal
* junction traversal
* reparse-point traversal
* quarantine collision
* insufficient free space

### Processes

* broad process termination
* unsafe process matching
* forced termination

### Commands

* `shell=True`
* `os.system`
* `eval`
* `exec`
* encoded PowerShell
* hidden commands
* dynamic command construction

### Privileges

* automatic elevation
* UAC triggers
* `runas`
* service creation

### Persistence

* scheduled tasks
* startup entries
* registry Run keys
* services
* background processes

### Network

* downloads
* telemetry
* remote code
* unexpected HTTP requests

### Secrets

* passwords
* tokens
* cookies
* API keys
* `.env` contents
* database credentials

### Rollback

* incorrect assumptions
* overwriting newer files
* restoring stale settings

### Configuration

* unsafe defaults
* destructive defaults
* unknown configuration behavior

If you discover a serious safety issue:

**DO NOT silently work around it.**

Clearly report the issue and stop the affected implementation.

---

# 42. STATIC SAFETY REVIEW TABLE

Before finishing, produce a table like:

| Area                     | Implementation | Risk | Mitigation | Static Review Result |
| ------------------------ | -------------- | ---- | ---------- | -------------------- |
| File cleanup             | ...            | ...  | ...        | ...                  |
| Quarantine               | ...            | ...  | ...        | ...                  |
| Process management       | ...            | ...  | ...        | ...                  |
| Power plan               | ...            | ...  | ...        | ...                  |
| Administrator privileges | ...            | ...  | ...        | ...                  |
| Subprocesses             | ...            | ...  | ...        | ...                  |
| Configuration            | ...            | ...  | ...        | ...                  |
| Logging                  | ...            | ...  | ...        | ...                  |
| Rollback                 | ...            | ...  | ...        | ...                  |
| Persistence              | ...            | ...  | ...        | ...                  |
| Network                  | ...            | ...  | ...        | ...                  |

Do not claim that the product is guaranteed safe.

Report what was actually inspected.

---

# 43. DO NOT MAKE UNSUPPORTED SAFETY CLAIMS

Never state:

> "This application is guaranteed safe."

Never state:

> "This cannot harm your laptop."

Never state:

> "This will definitely not break Windows."

Never state:

> "The optimizer is risk-free."

Never state:

> "The code is guaranteed harmless."

Instead use factual statements such as:

> "The implementation includes the specified safety controls."

> "The application was not executed."

> "The test suite was created but not executed."

> "Static review identified the following..."

Safety must be demonstrated through design, validation, testing, and controlled execution—not guaranteed by wording.

---

# 44. FINAL RESPONSE REQUIREMENTS

After creating the project, provide:

## A. Project structure

Show the complete structure.

## B. Files created

List every file.

## C. Dependencies

List every dependency and explain why it exists.

## D. Static safety review

Explain what was inspected.

## E. Known limitations

Clearly identify anything that has not been verified because execution was prohibited.

## F. Manual installation instructions

Give commands that I can manually review and run later.

## G. Manual dry-run instructions

Give commands that I can manually execute later.

## H. Manual apply instructions

Give commands that I can manually execute later.

## I. Manual rollback instructions

Give commands that I can manually execute later.

## J. Manual quarantine purge instructions

Give commands that I can manually execute later.

---

# 45. REQUIRED "NOT EXECUTED" STATEMENT

Your final response must explicitly state:

```text
[SAFE]
Application execution was not performed.

[SAFE]
Automated tests were not executed.

[SAFE]
Dependencies were not automatically installed.

[SAFE]
No Windows system settings were modified.

[SAFE]
No registry changes were made.

[SAFE]
No services were modified.

[SAFE]
No processes were terminated.

[SAFE]
No cleanup operation was performed.

[SAFE]
No quarantine purge was performed.

[SAFE]
No rollback operation was performed.

[SAFE]
No administrator elevation was requested.

[SAFE]
No persistence mechanism was created by the optimizer.
```

Only state these things if they are actually true.

---

# 46. STOP CONDITION

After:

1. creating the complete project
2. creating the source code
3. creating configuration
4. creating documentation
5. creating tests
6. performing static code review
7. reporting the results

**STOP.**

Do not:

* run the application
* run tests
* install dependencies
* perform dry-run
* perform cleanup
* modify Windows
* request administrator access

Wait for my next instruction.

---

# 47. FUTURE EXECUTION AUTHORIZATION

A future instruction from me may separately authorize execution.

Until I explicitly provide that future instruction:

> **EXECUTION IS NOT AUTHORIZED.**

Do not infer execution permission from any other instruction.

---

# FINAL OBJECTIVE

The required workflow is:

```text
PHASE 1
Design + Threat Model + Safety Architecture
        ↓
USER APPROVAL
        ↓
PHASE 2
CREATE COMPLETE PRODUCT
        ↓
STATIC CODE REVIEW
        ↓
STOP
        ↓
USER INSPECTION
        ↓
USER EXPLICITLY AUTHORIZES EXECUTION
        ↓
ONLY THEN MAY EXECUTION BE CONSIDERED
```

The goal of this phase is therefore:

**BUILD → REVIEW → STOP**

NOT:

**BUILD → RUN → TEST → CLEAN → MODIFY MY COMPUTER**

Do not execute anything unless I separately and explicitly authorize execution in a future message.
