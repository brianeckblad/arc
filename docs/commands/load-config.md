---
command: "load config version"
description: "Rollback: load a config version as the candidate (preview without confirm)"
usage: "load config version <id> [confirm]"
feature_flag: config_rollback
category: operations
scope: global
api: "POST /config/operations/v1/config-versions:load"
---

# load config version

**Rollback**: load an earlier configuration version as the tenant's
**candidate** configuration.

```
arc:global # load config version 123
```

Without `confirm` this is a **preview only** — ARC fetches the version's
metadata (date, admin, description) and explains exactly what would happen.
Nothing is changed.

```
arc:global # load config version 123 confirm
```

With `confirm` the load **executes in SCM immediately** (it does not go
through ARC's local staging queue — `load` is not a staged write). It:

1. Replaces the tenant's candidate configuration with version 123 —
   including discarding any uncommitted changes made in the SCM UI.
2. Does **not** touch devices. Run `commit` to push the loaded
   configuration to the fleet.

## Workflow

```
show config versions          # find the version id to roll back to
load config version 123       # preview what will be loaded
load config version 123 confirm
commit                        # push to devices
```

## Related

- `show config versions` — version history with ids
- `show config running` — what is currently running
- `commit` — push the candidate configuration to devices
