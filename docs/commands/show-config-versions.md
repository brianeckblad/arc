---
command: "show config versions"
description: "List SCM config versions (id, date, admin) or one version by id"
usage: "show config versions [<id>]"
feature_flag: config_view
category: operations
scope: global
---

---
command: "show config versions"
description: "List SCM config versions (id, date, admin) or one version by id"
usage: "show config versions [<id>]"
feature_flag: config_view
category: operations
scope: global
---

---
command: "show config versions"
description: "List SCM config versions (id, date, admin) or one version by id"
usage: "show config versions [<id>]"
feature_flag: config_view
category: operations
scope: global
api: "GET /config/operations/v1/config-versions"
---

# show config versions

List the tenant's **configuration version history** — one row per pushed
config version, with id, date, and the administrator (or service account)
that pushed it.

```
arc:global > show config versions
```

Columns come from the SCM config-version record: `id`, `version`, `date`,
`admin`, `scope`, `description`.

## Single version

```
arc:global > show config versions 123
```

Shows the full record for version 123 (`GET /config-versions/{version}`).

## Related

- `show config running` — the currently running version
- `load config version <id>` — rollback: load a version as the candidate
- `commit` — push the candidate configuration to devices
