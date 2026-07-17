# Set up ARC — macOS

All commands below run in your terminal (Terminal.app / iTerm), **before** you
launch the ARC shell.

## Quick start

Pick one of two ways to hold credentials:

```bash
# 1. Install ARC (see "Install ARC" below).

# 2a. Session-only environment variables (no keychain — gone on reboot):
arc setup scm            # prints the export commands, then offers a wizard
#     one step: eval "$(arc setup scm --export)"

# 2b. — or — store them in the macOS Keychain (persistent, secure):
arc setup scm keystore   # same wizard as: arc auth configure

# 3. Confirm everything is set (secrets masked)
arc auth show
```

## Install ARC

```bash
# Recommended: uv (fast, isolated)
uv tool install .

# Alternative: pip inside a venv
python3 -m venv ~/.venv/arc
source ~/.venv/arc/bin/activate
pip install -e .
```

## Store credentials (macOS Keychain)

Run the keychain wizard — secrets are written directly to **macOS Keychain**,
not to disk:

```bash
arc setup scm keystore   # same as: arc auth configure
```

ARC stores four items in the keychain under the service name `arc`:

| Keychain Account field | What it holds |
|------------------------|---------------|
| `arc.bearer.token`    | SCM pre-issued bearer token |
| `arc.bearer.password` | SCM OAuth client secret (generates bearer tokens) |
| `arc.shell.username`  | SSH username for device connections |
| `arc.shell.password`  | SSH password for device connections |

Non-sensitive values (`client_id`, `tsg_id`, SSH key path, port) are written to
the ARC config file with mode `0600`.

In **macOS Keychain Access** (`⌘ Space` → "Keychain Access"), search for `arc` to see all four entries.
Each entry shows:
- **Name**: `arc` (the service)
- **Account**: `arc.bearer.token`, `arc.bearer.password`, etc.
- **Password**: the secret (click "Show password" to reveal)

Run `arc auth show` to see all four keychain key names alongside the current values (masked).

### Migrate from older ARC versions

If you configured ARC before 2026-06, your credentials are stored under old key names
(`scm.bearer_token`, `scm.client_secret`, `ssh.password`).  Migrate in one command:

```bash
arc auth migrate          # read old entries → write new ones → clear old ones
arc auth migrate --dry-run # preview only, no changes
```

After migrating, verify with `arc auth show`.

### Manage Keychain entries with the `security` CLI

The macOS `security` command lets you read, write, and delete Keychain entries
without opening the graphical Keychain Access app.

```bash
# --- Add / update entries manually ---
security add-generic-password -U -s arc -a arc.bearer.token    -w "YOUR_BEARER_TOKEN"
security add-generic-password -U -s arc -a arc.bearer.password -w "YOUR_CLIENT_SECRET"
security add-generic-password -U -s arc -a arc.shell.username  -w "admin"
security add-generic-password -U -s arc -a arc.shell.password  -w "YOUR_SSH_PASSWORD"
# -U = update if the entry already exists

# --- Read (print) a stored value ---
security find-generic-password -s arc -a arc.bearer.token    -w
security find-generic-password -s arc -a arc.bearer.password -w
security find-generic-password -s arc -a arc.shell.username  -w
security find-generic-password -s arc -a arc.shell.password  -w

# --- Show full metadata (no -w = prints the entry, not the secret) ---
security find-generic-password -s arc -a arc.bearer.token

# --- Delete entries ---
security delete-generic-password -s arc -a arc.bearer.token
security delete-generic-password -s arc -a arc.bearer.password
security delete-generic-password -s arc -a arc.shell.username
security delete-generic-password -s arc -a arc.shell.password

# --- List all items for service "arc" ---
security find-generic-password -s arc
```

> **Note:** `-U` (update) is required when re-running `add-generic-password`
> for an entry that already exists — without it the command fails with a
> "duplicate item" error.

### Verify what is stored

```bash
arc auth show    # display current config (secrets masked, keychain entries listed)
arc auth clear   # remove all ARC entries from Keychain
```

Open **Keychain Access** (`⌘ Space` → "Keychain Access"), search for `arc`,
to see the entries visually.

### Touch ID / Apple Watch auto-unlock

macOS Keychain is unlocked by your login password and, on supported hardware,
by Touch ID or Apple Watch. ARC reads credentials silently once the session
is unlocked — no password prompt on every `arc` invocation.

## Environment variables (session-only, no keychain)

Environment variables override keychain and config values and live only in the
current terminal — they vanish when you close it or reboot. This is the "no
keychain" path. Let ARC build them for you:

```bash
arc setup scm            # prints the export commands, then offers a wizard
arc setup scm wizard     # go straight to the wizard
eval "$(arc setup scm --export)"   # run the wizard and set them in one step
```

The wizard offers a static bearer token or a "log in now" that mints a
short-lived token — it only ever sets `SCM_BEARER_TOKEN`, never your client
secret. Do **not** put long-lived secrets in `~/.zshrc` or `~/.zprofile`; those
files are plaintext and often backed up or synced. To set the variables by hand:

```bash
# SCM — bearer token takes precedence over OAuth credentials
export SCM_BEARER_TOKEN=your-bearer-token

# SCM — OAuth client credentials (used when no bearer token is set)
export SCM_CLIENT_ID=your-client-id
export SCM_CLIENT_SECRET=your-client-secret
export SCM_TSG_ID=your-tsg-id

# SSH defaults
export ARC_SSH_USER=admin
export ARC_SSH_KEY=~/.ssh/panos_key
# export ARC_SSH_PASS=your-ssh-password  # prefer key auth

# Debug (verbose tracebacks)
# export ARC_DEBUG=1
```

When you close the terminal, these temporary values are gone. If you only set
non-secret values such as `ARC_SSH_USER` or `ARC_SSH_KEY` in a profile, reload
your shell with:

```bash
source ~/.zshrc
```

## Config file location

```
<arc_project>/config/<your_username>/config.json    (non-sensitive values, mode 0600)
```

Run `arc auth show` to see the exact path on your system.

## Shell history

ARC persists command history to:

```
~/Library/Application Support/arc/history
```

## Recommended SSH setup

Use a key instead of a password — no Keychain entry needed and more secure:

```bash
# Generate a dedicated key for PAN-OS devices
ssh-keygen -t ed25519 -f ~/.ssh/panos_key -C "arc-panos"

# Set it in ARC
arc auth configure --ssh-key ~/.ssh/panos_key
```

## See Also

- `arc setup win`           — Windows setup
- `arc setup linux`         — Linux setup
- `arc help configuration`  — full configuration reference
