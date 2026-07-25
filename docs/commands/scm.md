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

With no argument, `scm login` lists your profiles and asks which one to log into
(pick by number or name; Enter keeps the active one). With a name it switches
directly. Switching reinitialises the SCM client, clears the device/folder/TSG
context, refreshes caches, and persists the new active profile for next launch.

```
arc:global > scm login

  Select a profile to log into:
  1  prod-rw          pa-rw@1234.iam.panserviceaccount.com  (active)
  2  prod-ro          pa-ro@1234.iam.panserviceaccount.com

  Enter # or name [prod-rw]: 2
  ✓ Logged in to profile prod-ro  |  TSG: 1234567890  3 device(s)
```

If no profiles exist yet, `scm login` points you to `scm setup`.

## scm setup

Runs the interactive credential wizard. When you already have profiles it first
asks whether to edit an existing one or **create a new profile** — so you never
need a `--profile` flag. It prompts for the storage mode (keychain vs file),
service-account credentials, optional bearer token, and SSH defaults, then logs
you into the profile it just saved. First-time setup names the profile after the
account automatically.

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

## account (alias)

`account` is an alias of `scm login` — `account <name>` switches profiles, and
bare `account` opens the picker.

## See Also

- `help connect` — SSH to a device in the current folder
- `help tsg` — switch Tenant Services Group within the active profile
- `arc setup scm` — set up credentials from your terminal (outside ARC)
- `arc gui-configure` — manage profiles, credentials and settings in the browser
