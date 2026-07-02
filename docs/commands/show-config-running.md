---
command: "show config running"
description: "Show the running config version, or one resource as set commands"
usage: "show config running [address|address-group|service|service-group|tag|external-dynamic-list]"
feature_flag: config_view
category: operations
scope: folder
api: "GET /config/operations/v1/config-versions/running"
---

# show config running

Show the tenant's **running configuration version** — the config that was last
pushed to devices.

```
arc:Production > show config running
```

The SCM endpoint returns config **version metadata** (id, date, admin, scope),
not raw config content — ARC renders exactly what the API provides.

## Per-resource form

Add a resource to list that object type in the **active folder** as replayable
`set` commands (same format as `show config format set`):

```
arc:Production > show config running address
set address WebServer ip-netmask 10.1.2.3/32
set address DMZ-Subnet ip-netmask 10.1.0.0/24 description "DMZ network"
```

Supported resources: `address`, `address-group`, `service`, `service-group`,
`tag`, `external-dynamic-list`.

## Related

- `show config versions` — full version history
- `show config format set` — dump the whole folder as set commands
- `load config version <id>` — rollback to an earlier version
- `show config` (bare) — locally staged, uncommitted changes in this session
