---
command: "scm"
description: "Manage SCM credentials & profiles (login / setup / status / delete / gui)"
usage: "scm <login|setup|status|delete|gui>"
category: shell
scope: global
---

# scm

**Category:** shell built-in
**Scope:** global — works regardless of device or folder context

## Description

`scm` is the one-stop command for logging into Strata Cloud Manager and managing
your credential **profiles** from inside ARC. A profile is a complete set of SCM
credentials (client_id, client_secret, tsg_id) stored under its own named slot in
the OS keychain (or `auth.json` in file mode).

SCM API access itself is automatic — ARC authenticates at startup from the active
profile. Use `scm` when you want to switch accounts, add a new one, or check
where you're pointed.

## Subcommands

```
scm                    show the active profile, TSG and connection status
scm status             same as bare `scm`
scm login [profile]    switch to a profile and authenticate; prompts if omitted
scm setup [profile]    create or edit a credential profile (interactive wizard)
scm delete <name>      delete a credential profile (not the active one)
scm gui                open the browser settings console (profiles, creds, …)
```

**Tab** after `scm ` completes the subcommands; after `scm login `/`scm delete `
it completes profile names.

## scm login

**No profiles configured yet** — `scm login` prompts for credentials inline.
You can connect for the session only (nothing saved) or choose to save a profile:

```
arc:global > scm login

SCM credentials  (no profiles configured yet)
  Get these from: SCM portal → Settings → Identity & Access → Service Accounts

  Client ID     (leave blank to use a bearer token): pa-api-you@1234.iam.panserviceaccount.com
  Client Secret : ****
  TSG ID        : 1234567890

  Save as a profile for future sessions? [y/N]: n
✓ SCM connected  (session only — not saved)  TSG: 1234567890
```

If you choose to save (`y`), the full credential wizard runs and stores the
credentials in the OS keychain (or file mode) — same as `scm setup`.

The prompt shows `[manual]` when you are connected via session-only credentials
as a reminder that they will not persist after you exit ARC.

**Profiles already configured** — `scm login` with no argument lists your profiles
and asks which one to log into (pick by number or name; Enter keeps the active one).
With a name it switches directly. Switching reinitialises the SCM client, clears
the device/folder/TSG context, refreshes caches, and persists the new active profile.

```
arc:global > scm login

  Select a profile to log into:
  1  prod-rw          pa-rw@1234.iam.panserviceaccount.com  (active)
  2  prod-ro          pa-ro@1234.iam.panserviceaccount.com

  Enter # or name [prod-rw]: 2
  ✓ Logged in to profile prod-ro  |  TSG: 1234567890  3 device(s)
```

## scm setup

Runs the full interactive credential wizard for creating or editing a **saved**
profile. When you already have profiles it first asks whether to edit an existing
one or create a new one — no `--profile` flag needed. It prompts for storage mode
(keychain vs file), service-account credentials (Client ID, Client Secret, TSG ID),
an optional bearer token, then logs you into the saved profile.

First-time setup auto-names the profile after your account (the `client_id` stem).

```
arc:global > scm setup
  SCM profiles  (pick one to edit, or create new)
  1  prod-rw   pa-rw@1234.iam.panserviceaccount.com (active)
  n  Create a new profile
  Edit #/name, or 'n' for new [active]: n
  New profile name (blank = derive from account): lab
  …
  ✓ Logged in to profile lab
```

The same wizard runs outside ARC via `arc setup scm keystore` / `arc auth configure`.

> **Tip:** Use `scm login` for a quick session-only connection. Use `scm setup`
> when you want credentials saved to the keychain for future launches.

## account (alias)

`account` is an alias of `scm login` — `account <name>` switches profiles, and
bare `account` opens the picker.

## See Also

- `help connect` — SSH to a device in the current folder
- `help tsg` — switch Tenant Services Group within the active profile
- `arc setup scm` — set up credentials from your terminal (outside ARC)
- `arc gui-configure` — manage profiles, credentials and settings in the browser
