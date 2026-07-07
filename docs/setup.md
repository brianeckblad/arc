# ARC Credential Setup

ARC connects to Palo Alto Networks SCM (Strata Cloud Manager) via REST API
and optionally to managed devices via SSH.  This page guides you through
storing those credentials safely for your platform.

---

## Quick path — answer two questions

**1. What SCM credentials do you have?**

| I have… | Jump to |
|---------|---------|
| A pre-issued **bearer token** | [Bearer token setup](#bearer-token) |
| An **OAuth client ID + secret** (service account) | [OAuth setup](#oauth-client-credentials) |
| Neither — I need to create a service account | [Create a service account](#create-a-service-account) |

**2. How will you SSH to devices?**

| I use… | Jump to |
|--------|---------|
| An **SSH key file** | [SSH key setup](#ssh-key) |
| A **password** | [SSH password setup](#ssh-password) |

> **Tip:** Type `setup` inside ARC for an interactive wizard that detects your
> OS and walks through the questions above step-by-step.

---

## One-command wizard (recommended)

```
setup
```

Run `setup` at the ARC prompt.  ARC auto-detects your OS, asks two questions,
and prints the exact commands to run — nothing is written until you confirm.

---

## Bearer token

A bearer token is the simplest credential — paste it once and ARC is ready.

### macOS

```bash
# Store in macOS Keychain (no plaintext on disk)
arc auth configure
# When prompted, choose "bearer token" and paste the token.
```

Manual keychain entry (for scripting / CI):
```bash
security add-generic-password -U -s arc -a arc.bearer.token -w "YOUR_BEARER_TOKEN"
```

### Linux / WSL

```bash
arc auth configure
# Uses libsecret / Secret Service if available; falls back to config file (0600).
```

Manual entry (env var for a single session):
```bash
export SCM_BEARER_TOKEN=your-bearer-token
```

### Windows

```powershell
arc auth configure
# Uses Windows Credential Manager.
```

Manual entry (PowerShell session):
```powershell
$env:SCM_BEARER_TOKEN = "your-bearer-token"
```

---

## OAuth client credentials

OAuth credentials require a client ID, client secret, and a Tenant Services
Group (TSG) ID.  These are generated when you create a service account in
Strata Cloud Manager.

### macOS

```bash
arc auth configure
# When prompted:
#   SCM auth method: 2 (OAuth)
#   Client ID: <paste>
#   Client secret: <paste>   ← stored in Keychain, not on disk
#   TSG ID: <paste>
```

### Linux / WSL

```bash
arc auth configure
# Same prompts as macOS.  Client secret stored via libsecret / Secret Service.
```

Environment variables (temporary or CI):
```bash
export SCM_CLIENT_ID=your-client-id
export SCM_CLIENT_SECRET=your-client-secret
export SCM_TSG_ID=your-tsg-id
```

### Windows

```powershell
arc auth configure
# Same prompts.  Client secret stored in Windows Credential Manager.
```

---

## SSH key

Recommended — no password stored anywhere.

```bash
# Generate a dedicated key (all platforms)
ssh-keygen -t ed25519 -f ~/.ssh/panos_key -C "arc-panos"

# Tell ARC to use it
arc auth configure --ssh-key ~/.ssh/panos_key
```

Or set the path manually in your config file (non-secret, safe to store):
```json
{ "ssh": { "key_file": "~/.ssh/panos_key", "username": "admin" } }
```

---

## SSH password

```bash
arc auth configure
# When prompted:
#   SSH username: admin
#   SSH password: <paste>   ← stored in OS keychain, not in the config file
```

---

## Create a service account

If you do not yet have SCM credentials, create a service account in SCM:

1. Log in to [Strata Cloud Manager](https://stratacloudmanager.paloaltonetworks.com/).
2. Navigate to **Settings → Identity & Access → Service Accounts**.
3. Click **Add Service Account**, give it a name, and assign the
   **Superuser** or **Read-Only Superuser** role.
4. Copy the **Client ID** and **Client Secret** — the secret is shown only once.
5. Copy your **TSG ID** from the top-right organisation switcher.
6. Run `arc auth configure` and enter the three values when prompted.

---

## Verify your credentials

```
arc auth show    # print current config (secrets masked)
arc auth test    # make a live API call to confirm connectivity
```

Inside ARC, after restarting:
```
show devices     # should list your managed devices
```

---

## Browser docs portal (arc cliup)

ARC ships with an offline browser-based docs portal (`docs/index.html`).
Run `arc cliup` once after installing to build it:

```bash
arc cliup
```

This downloads the vendor JS/CSS files (once, then cached) and bundles all
Markdown docs into `docs/docs-bundle.js` so the portal works via `file://`
with no web server needed.

**Open the portal:**
```bash
open docs/index.html          # macOS
xdg-open docs/index.html      # Linux
start docs/index.html         # Windows
```

**When to re-run `arc cliup`:**

| Event | Action |
|-------|--------|
| First install | `arc cliup` |
| After `docs update` in the dev shell | Automatic — `catalog rebuild` runs `cliup` silently |
| After editing any `docs/commands/*.md` file | `arc cliup` |

> The full chain: `docs update` → `catalog rebuild` → `arc cliup` (silent).
> For standalone edits to Markdown files, run `arc cliup` manually.

---

## Profiles (multiple accounts)

Create a named profile so you can switch between SCM environments:

```bash
arc auth configure --profile prod
arc auth configure --profile lab
```

Switch inside ARC:
```
account prod
account lab
```

---

## Platform-specific full guides

- `help config osx`     — macOS (Keychain, Touch ID)
- `help config nix`     — Linux (libsecret / Secret Service / env vars)
- `help config win`     — Windows (Credential Manager / PowerShell)
- `help config generate` — generate a starter config file
- `help configuration`  — full configuration reference

