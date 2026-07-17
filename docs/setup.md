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
| I want to **log in now and confirm my identity** (uses the API) | [Log in via the API](#log-in-via-the-api-login) |

**2. How will you SSH to devices?**

| I use… | Jump to |
|--------|---------|
| An **SSH key file** | [SSH key setup](#ssh-key) |
| A **password** | [SSH password setup](#ssh-password) |

> **Tip:** Run `arc setup` in your terminal (before launching the ARC shell) for
> a guided menu that detects your OS and links the wizard and per-OS guides.

---

## One-command wizard (recommended)

`arc setup scm` runs from your terminal (outside the ARC shell) and comes in two
flavors — pick based on whether you want anything stored on the machine:

```
arc setup scm            # session-only env vars (no keychain) — set by hand or wizard
arc setup scm wizard     # the env-var wizard directly
arc setup scm keystore   # store in the OS keychain (persistent)  — = arc auth configure
```

**Env-var mode (`arc setup scm` / `arc setup scm wizard`)** — for operators who
don't want the OS keychain. Because a program can't set variables in its parent
shell, the wizard *prints* the `export` commands; you apply them by pasting, or
in one step with `eval "$(arc setup scm --export)"` (PowerShell:
`arc setup scm --export | iex`). The variables live only in that terminal session
and are gone when you close it or reboot. It offers two auth choices:

- **Static bearer token** — paste a pre-issued token → sets `SCM_BEARER_TOKEN`.
- **Log in now** — enter a service account (client ID + secret + TSG); the wizard
  mints a **short-lived token** and sets `SCM_BEARER_TOKEN` only. The client
  secret is used once and **never** written to the environment or disk. When the
  token expires, re-run the wizard.

**Keychain mode (`arc setup scm keystore`)** — the persistent path. Prompts for
your service account (client ID, secret, TSG), an optional bearer token, and SSH
defaults, then verifies with a live token request. **Secrets** go to the **OS
keychain** by default; non-secret values to `config.json` (mode 0600). To keep
secrets in a plaintext `auth.json` instead (opt-in, insecure), set
`ARC_AUTH_STORAGE=file` or `auth.storage: "file"`. For a second environment, use
a named profile: `arc auth configure --profile <name>`
(see [Profiles](#profiles-multiple-accounts)).

Any wizard: **Enter** keeps an existing value; **Ctrl-C** aborts without saving.
Once configured, run `login` inside ARC to authenticate and confirm your identity.

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

## Log in via the API (`login`)

Once your SCM credentials are configured, run `login` inside ARC to authenticate
**via the API — no browser** — and confirm your identity:

```
login
```

It mints a fresh 15-minute token from your service account and reads the userinfo
endpoint to show who you are:

```
✓ Authenticated to SCM — token valid for ~15 min.
  Signed in as ARC Service  <svc@1234.iam.panserviceaccount.com>
  TSG: 1234567890
```

Two documented SCM endpoints are used:

- `POST /auth/v1/oauth2/access_token` — mint the token (Client ID + Secret as HTTP
  Basic, `client_credentials`). [pan.dev](https://pan.dev/scm/api/auth/post-auth-v-1-oauth-2-access-token/)
- `POST /auth/v1/oauth2/userinfo` — identity claims for the token.
  [pan.dev](https://pan.dev/scm/api/auth/post-auth-v-1-oauth-2-userinfo/)

If no credentials are set yet, `login` points you at `arc setup scm`.

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

- `arc setup osx`     — macOS (Keychain, Touch ID)
- `arc setup linux`   — Linux (libsecret / Secret Service / env vars)
- `arc setup win`     — Windows (Credential Manager / PowerShell)
- `arc setup shell`   — make an unquoted `arc ?` work (zsh globs `?`; adds a one-line alias)
- `arc help configuration`  — full configuration reference

---

## Once you're connected — what else ARC can do

After `arc auth test` shows a green check, these are the high-value entry points:

| Command | What it does |
|---------|--------------|
| `arc gui-configure` | Browser settings console: authentication, credentials/keychain, theme, API sources, maintenance |
| `feature gui-configure` | Browser feature editor: turn commands on/dev/hidden/off, areas, scope, aliases, built-ins |
| `feature show` / `feature find <text>` | List/search every capability flag and the commands it gates |
| `login` | Authenticate now via the API and show your identity (no browser) |
| `show log traffic\|threat\|system` | Fleet logs from Strata Logging Service — no device context needed |
| `clone <res> <src> <new>` | Duplicate any named object into the active container |
| `cd snippet <name>` | Work inside an SCM snippet container instead of a folder |
| `configure` → `set …` → `commit` | Staged writes: validate locally, then push (`commit watch`, `commit confirmed`) |
| `?` | Cisco-style, context-aware inline help for what you can run right now |

