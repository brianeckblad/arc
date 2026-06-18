# show dns-security-profile

List **dns-security-profile** objects in the active SCM folder.

## Feature flag

This command requires **`security_profiles`** to be enabled:

```bash
arc> feature enable security_profiles
```

## Syntax

```text
show dns-security-profile
show dns-security-profile --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/dns-security-profiles?folder=<active-folder>
```

Notes: DNS sinkholing and threat prevention

## Output

Returns a table of dns-security-profile objects with key fields.

## Example

```text
arc:global > feature enable security_profiles
arc:global > show dns-security-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set dns-security-profile <name>` — create a dns-security-profile object
- `delete dns-security-profile <name>` — remove a dns-security-profile object
- `help features` — manage feature flags

---
*Generated stub.*
