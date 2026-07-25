# account

**Category:** shell built-in
**Scope:** global — works regardless of device or folder context

## Description

`account` is an **alias of [`scm login`](scm.md)** — it switches the active SCM
credential profile without restarting ARC. A **profile** is a complete set of SCM
credentials (client_id, client_secret, tsg_id) stored under a named slot in the OS
keychain (or `auth.json` in file mode).

Switching a profile reinitialises the SCM client, clears the current device /
folder / TSG context, refreshes caches for the new account, and persists the new
active profile to `config.json` for the next launch.

## Usage

```
account                  — pick a profile to log into (numbered menu)
account <name>           — switch to the named profile
```

**Tab** after `account ` completes profile names. Prefer `scm login` /
`scm status` / `scm setup` for the full profile surface; `account` is kept for
muscle memory.

## Creating profiles

Create profiles interactively — no flags needed:

```
scm setup                 # inside ARC: choose "create new profile"
arc setup scm keystore    # outside ARC: same wizard
```

Manage them with `scm delete <name>`, `arc auth show`, or the browser console
(`arc gui-configure` → Profiles).

## Examples

```
arc:global > account            # open the profile picker
arc:global > account prod-rw    # switch straight to a named profile
```

## See Also

- `help scm` — the full SCM credential/profile command (login/setup/status/delete/gui)
- `help tsg` — switch between Tenant Services Groups within one account
- `help pwd` — shows active profile alongside device, folder, and TSG
