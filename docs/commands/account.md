# account

**Category:** shell built-in  
**Scope:** global — works regardless of device or folder context

## Description

Lists all configured credential profiles and switches between them without
restarting ARC.  A **profile** is a complete set of SCM credentials
(client_id, client_secret, tsg_id) stored in the OS keychain under a named
slot.  Profiles let you maintain separate read-only and read-write service
accounts — or accounts for different tenants — and flip between them in
seconds.

Switching a profile:
- Reinitialises the SCM client with the new credentials.
- Clears the current device context, folder, and TSG (new account = fresh scope).
- Refreshes device/folder/TSG caches for the new account.
- Persists the new active profile to `config.json` so the next ARC launch
  uses it automatically.

## Usage

```
account                  — list all profiles with active marker
account <name>           — switch to the named profile
```

**Tab** after `account ` shows available profile names.

## Creating profiles

Create or update a named profile from your shell (outside ARC):

```bash
# Create a read-write profile
arc auth configure --profile readwrite

# Inspect a profile
arc auth show --profile readwrite

# Delete a profile (cannot delete 'default')
arc auth delete-profile readwrite
```

## Examples

List profiles:
```
arc:global > account

  Credential Profiles  (use account <name> to switch)

  default                pa-readonly@1234.iam.panserviceaccount.com   1234567890  ◀ active
  readwrite              pa-rw@1234.iam.panserviceaccount.com         1234567890
```

Switch to read-write account:
```
arc:global > account readwrite

  Loading profile 'readwrite'…
  Refreshing caches for profile 'readwrite'…
  ✓ Switched to profile readwrite  (3 device(s) — pa-rw@1234... TSG: 1234567890)
```

Switch back:
```
arc:global > account default
```

## Typical workflow

```bash
# One-time setup (outside ARC)
arc auth configure                         # configure default read-only account
arc auth configure --profile readwrite     # configure read-write account

# Inside ARC during a session
arc:global > account                   # check which account is active
arc:global > show security-policy      # safe read via default account
arc:global > account readwrite         # elevate to read-write
arc:global > commit                    # make changes
arc:global > account default           # drop back to read-only
```

## See Also

- `help tsg` — switch between Tenant Services Groups within one account
- `help pwd` — shows active profile alongside device, folder, and TSG
- `help configuration` — credential setup guide

