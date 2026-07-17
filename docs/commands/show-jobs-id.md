---
command: "show jobs id"
description: "Show a specific job by ID — show jobs id <n>"
feature_flag: show_jobs
category: operations
scope: global
api: "GET /config/setup/v1/jobs/{id}"
---

---
command: "show jobs id"
description: "Show a specific job by ID — show jobs id <n>"
feature_flag: show_jobs
category: operations
scope: global
api: "GET /config/setup/v1/jobs/{id}"
---

---
command: "show jobs id"
description: "Show a specific SCM job by ID"
usage: "show jobs id <n>"
feature_flag: show_jobs
category: operations
scope: global
api: "GET /config/setup/v1/jobs/{id}"
---

# show jobs id

Show a specific job by ID

## Category

system

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show jobs id 42
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
