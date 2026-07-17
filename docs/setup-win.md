# Set up ARC — Windows

All commands below run in PowerShell, **before** you launch the ARC shell.

## Quick start

Pick one of two ways to hold credentials:

```powershell
# 1. Install ARC (see "Install ARC" below).

# 2a. Session-only environment variables (no keychain — gone on reboot):
arc setup scm            # prints the $env: commands, then offers a wizard
#     one step: arc setup scm --export | iex

# 2b. — or — store them in Windows Credential Manager (persistent, secure):
arc setup scm keystore   # same wizard as: arc auth configure

# 3. Confirm everything is set (secrets masked)
arc auth show
```

## Install ARC

ARC requires Python 3.11+.  Install from [python.org](https://python.org) or
via the Microsoft Store, then:

```powershell
# Recommended: uv
pip install uv
uv tool install .

# Alternative: pip inside a venv
python -m venv $env:USERPROFILE\.venv\arc
& "$env:USERPROFILE\.venv\arc\Scripts\Activate.ps1"
pip install -e .
```

## Store credentials (Windows Credential Manager)

Run the keychain wizard — secrets are written to **Windows Credential Manager**,
not to disk as plaintext:

```powershell
arc setup scm keystore   # same as: arc auth configure
```

ARC stores entries with target `arc/<item>` in Credential Manager:

| Credential Manager target | What it holds |
|---------------------------|---------------|
| `arc/scm.bearer_token`    | SCM bearer token |
| `arc/scm.client_secret`   | SCM OAuth client secret |
| `arc/ssh.password`        | SSH password (if used) |

Non-sensitive values (`client_id`, `tsg_id`, SSH user/key/port) are written to
`%APPDATA%\arc\config.json`.

### Manage Credential Manager entries with `cmdkey`

`cmdkey` is the built-in Windows CLI for Credential Manager.

```powershell
# --- Add / update entries manually ---
cmdkey /generic:"arc/scm.bearer_token"  /user:"scm.bearer_token"  /pass:"YOUR_BEARER_TOKEN"
cmdkey /generic:"arc/scm.client_secret" /user:"scm.client_secret" /pass:"YOUR_CLIENT_SECRET"
cmdkey /generic:"arc/ssh.password"      /user:"ssh.password"      /pass:"YOUR_SSH_PASSWORD"

# --- List all stored credentials (look for entries starting with "arc/") ---
cmdkey /list

# --- Delete entries ---
cmdkey /delete:"arc/scm.bearer_token"
cmdkey /delete:"arc/scm.client_secret"
cmdkey /delete:"arc/ssh.password"
```

### Manage with PowerShell `CredentialManager` module (optional)

```powershell
# Install once (optional — cmdkey is sufficient)
Install-Module -Name CredentialManager -Scope CurrentUser

# Add
New-StoredCredential -Target "arc/scm.bearer_token"  -UserName "scm.bearer_token"  -Password "YOUR_TOKEN"   -Type Generic -Persist LocalMachine
New-StoredCredential -Target "arc/scm.client_secret" -UserName "scm.client_secret" -Password "YOUR_SECRET"  -Type Generic -Persist LocalMachine

# Read (shows password in plain — keep terminal session private)
Get-StoredCredential -Target "arc/scm.bearer_token" | Select-Object -ExpandProperty Password

# Delete
Remove-StoredCredential -Target "arc/scm.bearer_token"
Remove-StoredCredential -Target "arc/scm.client_secret"
Remove-StoredCredential -Target "arc/ssh.password"
```

### Verify what is stored

```powershell
arc auth show    # display current config (secrets masked, keychain status shown)
arc auth clear   # remove all ARC entries from Credential Manager
```

Open **Control Panel → Credential Manager → Windows Credentials** and search
for entries starting with `arc/` to verify visually.

## Environment variables (session-only, no keychain)

Environment variables override Credential Manager and config values and live
only in the current PowerShell session — they vanish when you close it or
reboot. This is the "no keychain" path. Let ARC build them for you:

```powershell
arc setup scm            # prints the $env: commands, then offers a wizard
arc setup scm wizard     # go straight to the wizard
arc setup scm --export | iex   # run the wizard and set them in one step
```

The wizard offers a static bearer token or a "log in now" that mints a
short-lived token — it only ever sets `SCM_BEARER_TOKEN`, never your client
secret. Do **not** store long-lived secrets permanently in Windows user
environment variables or PowerShell profiles; those values are plaintext from
ARC's perspective. To set the variables by hand:

```powershell
# SCM — bearer token takes precedence over OAuth credentials
$env:SCM_BEARER_TOKEN  = "your-bearer-token"

# SCM — OAuth client credentials
$env:SCM_CLIENT_ID     = "your-client-id"
$env:SCM_CLIENT_SECRET = "your-client-secret"
$env:SCM_TSG_ID        = "your-tsg-id"

# SSH defaults
$env:ARC_SSH_USER = "admin"
$env:ARC_SSH_KEY  = "$env:USERPROFILE\.ssh\panos_key"

# Debug (verbose tracebacks)
# $env:ARC_DEBUG = "1"
```

If you set non-secret values permanently from PowerShell (user scope), use:

```powershell
[Environment]::SetEnvironmentVariable("ARC_SSH_USER", "admin", "User")
```

## Config file location

```
%APPDATA%\arc\config.json    (non-sensitive values)
```

Run `arc auth show` to confirm the exact path.

## Windows Terminal / PowerShell profile

To auto-set variables on every shell open, add them to your profile:

```powershell
# Find your profile path
$PROFILE

# Edit it (creates if missing)
notepad $PROFILE
```

## Recommended SSH setup

Use a key instead of a password:

```powershell
# Generate a key (OpenSSH ships with Windows 10+)
ssh-keygen -t ed25519 -f "$env:USERPROFILE\.ssh\panos_key" -C "arc-panos"

# Register it in ARC
arc auth configure --ssh-key "$env:USERPROFILE\.ssh\panos_key"
```

## See Also

- `arc setup osx`           — macOS setup
- `arc setup linux`         — Linux setup
- `arc help configuration`  — full configuration reference
