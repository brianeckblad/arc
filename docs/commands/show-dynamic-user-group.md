---
command: "show dynamic-user-group"
description: "Show dynamic user group — device-local config (break-glass)"
usage: "show dynamic-user-group
show dynamic-user-group <name>"
feature_flag: panos_config_misc
category: panos-config
scope: device
api: "(live device state — SSH via --remote)"
---

# show dynamic-user-group

List **dynamic-user-group** objects in the active SCM folder.

## Feature flag

This command requires **`local_users`** to be enabled:

```bash
arc> feature enable local_users
```

## Syntax

```text
show dynamic-user-group
show dynamic-user-group --remote    # live device state via SSH
```

## API

```
GET /config/objects/v1/dynamic-user-groups?folder=<active-folder>
```

Notes: dynamic group of users matching a filter

## Output

Returns a table of dynamic-user-group objects with key fields.

## Example

```text
arc:global > feature enable local_users
arc:global > show dynamic-user-group
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set dynamic-user-group <name>` — create a dynamic-user-group object
- `delete dynamic-user-group <name>` — remove a dynamic-user-group object
- `help features` — manage feature flags

---
*Generated stub.*
