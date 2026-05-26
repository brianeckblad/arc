# Configuration — Linux

## Quick start

```bash
# 1. Generate a starter config file (0600, annotated with what to fill in)
arc config generate

# 2. Edit the file — replace the REPLACE_WITH_* placeholders
${EDITOR:-nano} ~/.config/arc/config.json

# 3. Run the wizard — migrates secrets to Secret Service, writes safe values to disk
arc auth login
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

Run the interactive wizard — on a desktop Linux system with GNOME Keyring or
KWallet running, secrets are stored in the **Secret Service** (encrypted wallet),
not as plaintext on disk:

```bash
arc auth login
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

1. `arc auth login` will warn you that the keychain is unavailable.
2. Use **environment variables** instead (see below).
3. If you must use the config file, ARC still writes it with mode `0600`.

```bash
# Required Secret Service package (desktop only — skip on servers)
sudo apt install gnome-keyring libsecret-tools   # Debian/Ubuntu
sudo dnf install gnome-keyring libsecret         # Fedora/RHEL
```

## Generate a starter config file

```bash
arc config generate          # creates config file with annotated placeholders
arc config generate --force  # overwrite an existing config file
```

The generated file has `_note` fields explaining each section.
Edit the `REPLACE_WITH_*` values, then run `arc auth login` to migrate
secrets to Secret Service.

## Environment variables (override keychain + config file)

Add to `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

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

Reload your shell:

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
arc auth login --ssh-key ~/.ssh/panos_key
```

Ensure the key has correct permissions:

```bash
chmod 600 ~/.ssh/panos_key
chmod 644 ~/.ssh/panos_key.pub
```

## See Also

- `help config`             — general configuration overview
- `help config generate`    — generate a starter config file
- `help config osx`         — macOS setup
- `help config win`         — Windows setup
- `help configuration`      — full configuration reference
