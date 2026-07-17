# Set up ARC — Linux / WSL

All commands below run in your terminal, **before** you launch the ARC shell.

## Quick start

Pick one of two ways to hold credentials:

```bash
# 1. Install ARC (see "Install ARC" below).

# 2a. Session-only environment variables (no keychain — gone on reboot):
arc setup scm            # prints the export commands, then offers a wizard
#     one step: eval "$(arc setup scm --export)"

# 2b. — or — store them in the Secret Service (persistent, encrypted):
arc setup scm keystore   # same wizard as: arc auth configure

# 3. Confirm everything is set (secrets masked)
arc auth show
```

## Install ARC

```bash
# Recommended: uv (fast, isolated)
pip install uv           # or: curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install .

# Alternative: pip inside a venv
python3 -m venv ~/.venv/arc
source ~/.venv/arc/bin/activate
pip install -e .
```

## Store credentials (Secret Service)

Run the keychain wizard — on a desktop Linux system with GNOME Keyring or
KWallet running, secrets are stored in the **Secret Service** (encrypted wallet),
not as plaintext on disk:

```bash
arc setup scm keystore   # same as: arc auth configure
```

ARC stores three entries under the service name `arc`:

| Secret Service entry | What it holds |
|----------------------|---------------|
| `service=arc  username=scm.bearer_token`  | SCM bearer token |
| `service=arc  username=scm.client_secret` | SCM OAuth client secret |
| `service=arc  username=ssh.password`      | SSH password (if used) |

Non-sensitive values (`client_id`, `tsg_id`, SSH user/key/port) are written to
`~/.config/arc/config.json` with mode `0600`.

### Manage Secret Service entries with `secret-tool`

`secret-tool` is the standard CLI for Secret Service (libsecret).
Install it if missing:

```bash
sudo apt install libsecret-tools    # Debian / Ubuntu
sudo dnf install libsecret          # Fedora / RHEL
```

```bash
# --- Add / update entries manually ---
secret-tool store --label="ARC SCM Bearer Token"   service arc username scm.bearer_token
# (prompts for the secret value interactively — keeps it out of shell history)

secret-tool store --label="ARC SCM Client Secret"  service arc username scm.client_secret
secret-tool store --label="ARC SSH Password"        service arc username ssh.password

# --- Non-interactive add (pipe the secret in — useful in scripts) ---
echo -n "YOUR_BEARER_TOKEN" | secret-tool store --label="ARC SCM Bearer Token" \
    service arc username scm.bearer_token

# --- Read a stored value ---
secret-tool lookup service arc username scm.bearer_token
secret-tool lookup service arc username scm.client_secret
secret-tool lookup service arc username ssh.password

# --- Delete entries ---
secret-tool clear service arc username scm.bearer_token
secret-tool clear service arc username scm.client_secret
secret-tool clear service arc username ssh.password

# --- Search for all ARC entries ---
secret-tool search service arc
```

### Verify with Seahorse (GUI)

```bash
seahorse &   # open GNOME Keyring manager, search for "arc"
```

### Verify with ARC commands

```bash
arc auth show    # display current config (secrets masked, keychain status shown)
arc auth clear   # remove all ARC entries from Secret Service
```

### No Secret Service available (headless / server)

If you are running ARC on a server or in a Docker container where no keychain
daemon is running:

1. `arc auth configure` will warn you that the keychain is unavailable.
2. Use **environment variables** instead (see below).
3. The config file is still written with mode `0600`, but secrets are not
   written there.

```bash
# Required Secret Service package (desktop only — skip on servers)
sudo apt install gnome-keyring libsecret-tools   # Debian/Ubuntu
sudo dnf install gnome-keyring libsecret         # Fedora/RHEL
```

## Environment variables (session-only, no keychain)

Environment variables override keychain and config values and live only in the
current terminal — they vanish when you close it or reboot. This is the "no
keychain" path (also ideal for headless / CI). Let ARC build them for you:

```bash
arc setup scm            # prints the export commands, then offers a wizard
arc setup scm wizard     # go straight to the wizard
eval "$(arc setup scm --export)"   # run the wizard and set them in one step
```

The wizard offers a static bearer token or a "log in now" that mints a
short-lived token — it only ever sets `SCM_BEARER_TOKEN`, never your client
secret. Do **not** put long-lived secrets in `~/.bashrc`, `~/.zshrc`, or
`~/.profile`; those files are plaintext and often backed up or synced. To set
the variables by hand:

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

If you only set non-secret values such as `ARC_SSH_USER` or `ARC_SSH_KEY` in a
profile, reload your shell with:

```bash
source ~/.bashrc
```

### Headless / CI — env-var only pattern

On servers where no secret store is available, export credentials from a
secrets manager before launching ARC:

```bash
# Example: HashiCorp Vault
export SCM_BEARER_TOKEN=$(vault kv get -field=token secret/arc/scm)
arc
```

## Config file location

```
~/.config/arc/config.json    (non-sensitive values, mode 0600)
```

If `$XDG_CONFIG_HOME` is set, the config dir follows that path.
Run `arc auth show` to confirm the exact location.

## Shell history

ARC persists command history to:

```
~/.local/share/arc/history
```

## Recommended SSH setup

Key authentication is more secure than a stored password:

```bash
# Generate a dedicated key for PAN-OS devices
ssh-keygen -t ed25519 -f ~/.ssh/panos_key -C "arc-panos"

# Register it in ARC
arc auth configure --ssh-key ~/.ssh/panos_key
```

Ensure the key has correct permissions:

```bash
chmod 600 ~/.ssh/panos_key
chmod 644 ~/.ssh/panos_key.pub
```

## See Also

- `arc setup osx`           — macOS setup
- `arc setup win`           — Windows setup
- `arc help configuration`  — full configuration reference
