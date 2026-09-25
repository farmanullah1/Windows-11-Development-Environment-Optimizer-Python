# Rollback & Quarantine Documentation

## Quarantine Location
Quarantined files are staged into:
`%LOCALAPPDATA%\Win11DevOptimizer\quarantine\<run-id>\`

Each directory contains:
- `manifest.json`: Stores original paths, quarantine targets, file sizes, modification timestamps, and SHA-256 hashes.
- Quarantined file payloads named using collision-safe hashes (`<stem>_<hash8><suffix>`).

## Rollback Procedure
To restore files from a specific run:
```powershell
python optimizer.py --rollback <RUN_ID>
```

Before restoration, the rollback engine verifies:
1. That the quarantined file exists and matches its recorded SHA-256 checksum.
2. That the original target directory exists or can be safely recreated.
3. That the original path does not already contain a newer file created by the user (skipping overwrite if detected).

## Quarantine Purge
To permanently clear the quarantine store:
```powershell
python optimizer.py --purge-quarantine
```
Requires manually typing `PURGE QUARANTINE` when prompted.
