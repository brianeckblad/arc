# Configuration

ARC stores configuration in two files under `config/<your-username>/` (both mode
`0600`), plus environment overrides:

- **`config.json`** — NON-secret, sectioned and human-readable:
  - `preferences` — terminal / aliases / GUI theme
  - `auth` — `preferred_method` (service|bearer), `storage` (keychain|file), `active_profile`
  - `gui` — `features` / `arc` console ports + enabled
  - `profiles` — per-profile `default_folder`
- **`auth.json`** — ALL auth info per profile: `scm` {client_id, tsg_id, real `token_expiry`} and `ssh` {user, key_path, port}. Plaintext **secrets** (client_secret, bearer_token, SSH password) appear here **only** in `file` storage mode.
- **Environment variables** — override everything (CI / temporary sessions).

## Secret storage modes

| Mode | Where secrets live | When |
|------|--------------------|------|
| `keychain` (default) | OS keychain (macOS Keychain / libsecret / Windows Credential Manager) | secure, recommended |
| `file` | plaintext `auth.json` (0600) | opt-in only, with warnings — anyone who can read the file gets your credentials |

Set the mode in **`arc gui-configure` → Credentials & Keychain** (inside the ARC
shell), or via the `ARC_AUTH_STORAGE` env var / `auth.storage` in config.json.
Real token expiry from the SCM `access_token` response is recorded in `auth.json`;
expired tokens are purged at startup.

> **Platform-specific setup guides** (run from your terminal):
> - `arc setup osx` — macOS (Keychain, zshrc, Touch ID)
> - `arc setup win` — Windows (Credential Manager, PowerShell)
> - `arc setup linux` — Linux (Secret Service, bashrc, headless/CI)

## SCM service account field mapping

When you create a service account in the Palo Alto SCM portal, it gives you:

| Portal label | ARC field | Storage |
|---|---|---|
| **Client ID** | `scm.client_id` | `auth.json` (non-secret identifier) |
| **Client Secret** | `scm.client_secret` | OS keychain (or `auth.json` in file mode) |
| **TSG ID** | `scm.tsg_id` | `auth.json` (non-secret identifier) |

`bearer_token` is only needed if you have a pre-issued token rather than a service
account. For the standard service account flow, leave `bearer_token` blank and supply
`client_id`, `client_secret`, and `tsg_id`.

## Credential setup

```bash
arc setup scm       # interactive credential wizard (recommended)
arc auth configure  # the same wizard, invoked directly
arc auth show       # display current config (secrets masked)
arc auth clear      # remove ARC secrets from the OS keychain
```

`arc setup scm` / `arc auth configure` route secrets to the keychain by default
(macOS Keychain, Linux Secret Service, or Windows Credential Manager) and
writes only non-sensitive values to the config file.

## Environment variables (always override keychain + config file)

Use environment variables for temporary shells, CI, or headless systems where
no OS keychain is available. Do **not** put long-lived secrets such as
`SCM_BEARER_TOKEN`, `SCM_CLIENT_SECRET`, or `ARC_SSH_PASS` in shell profile
files (`~/.zshrc`, `~/.bashrc`, PowerShell profile). Shell profiles are
plaintext and easy to leak through backups, screen sharing, or dotfile sync.

| Variable | Description |
|----------|-------------|
| `SCM_BEARER_TOKEN` | Pre-issued SCM bearer token (not typically needed for service accounts) |
| `SCM_CLIENT_ID` | SCM service account Client ID |
| `SCM_CLIENT_SECRET` | SCM service account Client Secret |
| `SCM_TSG_ID` | Tenant Services Group ID |
| `ARC_SSH_USER` | Default SSH username (default: `admin`) |
| `ARC_SSH_KEY` | Path to SSH private key |
| `ARC_SSH_PASS` | SSH password fallback |
| `ARC_DEBUG` | Set to `1` for verbose error output |

## What is stored where

| Value | `keychain` mode (default) | `file` mode (insecure) |
|-------|---------------------------|------------------------|
| `client_secret` | OS keychain | `auth.json` (plaintext) |
| `bearer_token` | OS keychain | `auth.json` (plaintext) |
| `ssh.password` | OS keychain | `auth.json` (plaintext) |
| `client_id`, `tsg_id` | `auth.json` (non-secret) | `auth.json` (non-secret) |
| `token_expiry` (real) | `auth.json` (non-secret) | `auth.json` (non-secret) |
| `ssh.user`, `key_path`, `port` | `auth.json` (non-secret) | `auth.json` (non-secret) |
| `preferred_method`, `storage`, `active_profile` | `config.json` → `auth` | `config.json` → `auth` |
| preferences, GUI ports, `default_folder` | `config.json` | `config.json` |

Both files live in `config/<your-username>/` at mode `0600`. ARC never writes
secrets to `config.json`.

## CI / headless environments

If the OS keychain is unavailable (e.g., a headless server or Docker), use
environment variables (below) from your CI secret store or runtime secret
manager — they override every stored value. `arc auth show` warns when keychain
access is unavailable. Alternatively, opt into `file` storage mode to keep
credentials in `auth.json` (plaintext, `0600`).

## Migration from an older config.json

The first `save_config` (via `arc setup scm`, `arc auth configure`, `login`, or the
GUI) migrates an older single- or multi-profile `config.json` automatically:
top-level `scm`/`ssh` blocks become the `default` profile in `auth.json`,
`features_gui`/`arc_gui` move under `config.json` → `gui`, and `active_profile`
moves under `config.json` → `auth`. Legacy keychain entries (`scm.bearer_token`,
`scm.client_secret`, `ssh.password`) and any plaintext secrets left in an old
`config.json` are read once and re-stored per the current storage mode.
