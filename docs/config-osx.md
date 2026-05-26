# Configuration — macOS

## Quick start

```bash
# 1. Generate a starter config file (0600, annotated with what to fill in)
arc config generate

# 2. Edit the file — replace non-secret REPLACE_WITH_* placeholders
open "$(arc auth show 2>&1 | grep 'Config file:' | awk '{print $3}')"
# or just: open ~/Library/Application\ Support/arc/config.json

# 3. Run the wizard — migrates secrets to macOS Keychain, writes safe values to disk
arc auth login
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

Run the interactive wizard — secrets are written directly to **macOS Keychain**,
not to disk:

```bash
arc auth login
```

ARC stores three items in the keychain under the service name `arc`:

| Keychain item | What it holds |
|---------------|---------------|
| `scm.bearer_token` | SCM bearer token |
| `scm.client_secret` | SCM OAuth client secret |
| `ssh.password` | SSH password (if used) |

Non-sensitive values (`client_id`, `tsg_id`, SSH user/key/port) are written to
`~/Library/Application Support/arc/config.json` with mode `0600`.

### Manage Keychain entries with the `security` CLI

The macOS `security` command lets you read, write, and delete Keychain entries
without opening the graphical Keychain Access app.

```bash
# --- Add / update entries manually ---
security add-generic-password -U -s arc -a scm.bearer_token  -w "YOUR_BEARER_TOKEN"
security add-generic-password -U -s arc -a scm.client_secret -w "YOUR_CLIENT_SECRET"
security add-generic-password -U -s arc -a ssh.password      -w "YOUR_SSH_PASSWORD"
# -U = update if the entry already exists

# --- Read (print) a stored value ---
security find-generic-password -s arc -a scm.bearer_token  -w
security find-generic-password -s arc -a scm.client_secret -w
security find-generic-password -s arc -a ssh.password      -w

# --- Show full metadata (no -w = print the entry, not the secret) ---
security find-generic-password -s arc -a scm.bearer_token

# --- Delete entries ---
security delete-generic-password -s arc -a scm.bearer_token
security delete-generic-password -s arc -a scm.client_secret
security delete-generic-password -s arc -a ssh.password

# --- List all items for service "arc" ---
security find-generic-password -s arc
```

> **Note:** `-U` (update) is required when re-running `add-generic-password`
> for an entry that already exists — without it the command fails with a
> "duplicate item" error.

### Verify what is stored

```bash
arc auth show    # display current config (secrets masked, keychain status shown)
arc auth clear   # remove all ARC entries from Keychain
```

Open **Keychain Access** (`⌘ Space` → "Keychain Access"), search for `arc`,
to see the entries visually.

### Touch ID / Apple Watch auto-unlock

macOS Keychain is unlocked by your login password and, on supported hardware,
by Touch ID or Apple Watch. ARC reads credentials silently once the session
is unlocked — no password prompt on every `arc` invocation.

## Generate a starter config file

```bash
arc config generate          # creates config file with annotated placeholders
arc config generate --force  # overwrite an existing config file
```

The generated file has `_note` fields explaining each section.
Edit only non-secret `REPLACE_WITH_*` values, then run `arc auth login` to
enter secrets securely and store them in the Keychain.

## Environment variables (temporary override)

Environment variables override keychain and config values. Use them for a
single terminal session or automation. Do **not** put long-lived secrets in
`~/.zshrc` or `~/.zprofile`; those files are plaintext and often backed up or
synced. Prefer Keychain via `arc auth login` for local development.

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
~/Library/Application Support/arc/config.json    (non-sensitive values, mode 0600)
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
arc auth login --ssh-key ~/.ssh/panos_key
```

## See Also

- `help config`             — general configuration overview
- `help config generate`    — generate a starter config file
- `help config win`         — Windows setup
- `help config nix`         — Linux setup
- `help configuration`      — full configuration reference
