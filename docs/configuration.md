# Configuration

ARC reads configuration from three sources in priority order (last wins):

1. **OS keychain** — secrets only (bearer token, client secret, SSH password)
2. **`~/.arc/config.json`** — non-sensitive values (client_id, tsg_id, SSH username/key/port); always written mode `0600`
3. **Environment variables** — override everything; useful for temporary sessions and CI/CD

ARC never writes secrets to `config.json`. If the OS keychain is unavailable,
`arc auth login` saves only non-sensitive values and tells you to provide
secrets through environment variables for that session.

> **Platform-specific setup guides:**
> - `help config osx` — macOS (Keychain, zshrc, Touch ID)
> - `help config win` — Windows (Credential Manager, PowerShell)
> - `help config nix` — Linux (Secret Service, bashrc, headless/CI)

## SCM service account field mapping

When you create a service account in the Palo Alto SCM portal, it gives you:

| Portal label | ARC config field | Storage |
|---|---|---|
| **Client ID** | `scm.client_id` | `config.json` (non-sensitive identifier) |
| **Client Secret** | `scm.client_secret` | OS keychain (secret — never written to disk) |
| **TSG ID** | `scm.tsg_id` | `config.json` (non-sensitive identifier) |

`bearer_token` is only needed if you have a pre-issued token rather than a service
account. For the standard service account flow, leave `bearer_token` blank and supply
`client_id`, `client_secret`, and `tsg_id`.

## Credential setup

```bash
arc auth login      # interactive wizard — stores secrets in OS keychain
arc auth show       # display current config (secrets masked)
arc auth clear      # remove ARC secrets from the OS keychain
```

`arc auth login` automatically routes sensitive values to the OS keychain
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

| Value | Storage |
|-------|---------|
| `bearer_token` | OS keychain |
| `client_secret` | OS keychain |
| `ssh.password` | OS keychain |
| `client_id` | `~/.arc/config.json` (0600) |
| `tsg_id` | `~/.arc/config.json` (0600) |
| `ssh.username`, `key_path`, `port` | `~/.arc/config.json` (0600) |

## CI / headless environments

If the OS keychain is unavailable (e.g., a headless server or Docker), ARC
does not write secrets to disk. Use environment variables from your CI secret
store or runtime secret manager. The config file remains for non-sensitive
values only. `arc auth show` warns when keychain access is unavailable.

## Migration from an existing plaintext config.json

Run `arc auth login` once on a machine with keychain access. It reads your
current config file, migrates secrets to the keychain, and rewrites the file
without them. If keychain access is unavailable, ARC removes secrets from the
rewritten config but cannot persist them; provide them via environment variables
for that session.

The SSH field was renamed from `user` to `username` in the config file to match
Palo Alto portal terminology. ARC reads both; it writes `username`.

ARC reads configuration from three sources in priority order (last wins):

1. **OS keychain** — secrets only (bearer token, client secret, SSH password)
2. **`~/.arc/config.json`** — non-sensitive values (client_id, tsg_id, SSH user/key/port); always written mode `0600`
3. **Environment variables** — override everything; useful for temporary sessions and CI/CD

ARC never writes secrets to `config.json`. If the OS keychain is unavailable,
`arc auth login` saves only non-sensitive values and tells you to provide
secrets through environment variables for that session.

> **Platform-specific setup guides:**
> - `help config osx` — macOS (Keychain, zshrc, Touch ID)
> - `help config win` — Windows (Credential Manager, PowerShell)
> - `help config nix` — Linux (Secret Service, bashrc, headless/CI)

## Credential setup

```bash
arc auth login      # interactive wizard — stores secrets in OS keychain
arc auth show       # display current config (secrets masked)
arc auth clear      # remove ARC secrets from the OS keychain
```

`arc auth login` automatically routes sensitive values to the OS keychain
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
| `SCM_BEARER_TOKEN` | Pre-issued SCM bearer token |
| `SCM_CLIENT_ID` | SCM OAuth client ID |
| `SCM_CLIENT_SECRET` | SCM OAuth client secret |
| `SCM_TSG_ID` | Tenant Services Group ID |
| `ARC_SSH_USER` | Default SSH username (default: `admin`) |
| `ARC_SSH_KEY` | Path to SSH private key |
| `ARC_SSH_PASS` | SSH password fallback |
| `ARC_DEBUG` | Set to `1` for verbose error output |

## What is stored where

| Value | Storage |
|-------|---------|
| `bearer_token` | OS keychain |
| `client_secret` | OS keychain |
| `ssh.password` | OS keychain |
| `client_id` | `~/.arc/config.json` (0600) |
| `tsg_id` | `~/.arc/config.json` (0600) |
| `ssh.user`, `key_path`, `port` | `~/.arc/config.json` (0600) |

## CI / headless environments

If the OS keychain is unavailable (e.g., a headless server or Docker), ARC
does not write secrets to disk. Use environment variables from your CI secret
store or runtime secret manager. The config file remains for non-sensitive
values only. `arc auth show` warns when keychain access is unavailable.

## Migration from an existing plaintext config.json

Run `arc auth login` once on a machine with keychain access. It reads your
current config file, migrates secrets to the keychain, and rewrites the file
without them. If keychain access is unavailable, ARC removes secrets from the
rewritten config but cannot persist them; provide them via environment variables
for that session.
