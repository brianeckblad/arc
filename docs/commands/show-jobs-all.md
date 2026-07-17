---
command: "show jobs all"
description: "Show all SCM jobs (TSG-wide)"
feature_flag: show_jobs
category: operations
scope: global
api: "GET /config/setup/v1/jobs"
---

---
command: "show jobs all"
description: "Show all SCM jobs (TSG-wide)"
feature_flag: show_jobs
category: operations
scope: global
api: "GET /config/setup/v1/jobs"
---

---
command: "show jobs all"
description: "Show all SCM jobs (TSG-wide)"
feature_flag: show_jobs
category: operations
scope: global
api: "GET /config/setup/v1/jobs"
---

# show jobs all

Show all SCM jobs for the current tenant (TSG-wide).

## Category

operations

## Scope

**Global** — no folder or device context required. Returns jobs for the entire
TSG regardless of the active folder or whether a device is selected.

## Default path

SCM REST API: `GET /config/setup/v1/jobs`

## Remote behavior

Supported — pass `--remote` or use `remote <device>` to run the PAN-OS
`show jobs all` command on a specific device instead.

## Examples

```text
show jobs all
show jobs all --remote
```

## Notes

This command queries SCM directly and works without a `cd` context. To see
jobs on a specific managed device, use `show jobs all --remote` while connected.
