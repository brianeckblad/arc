---
command: "show system resources"
description: "Show live CPU / memory — use --remote for live device data"
feature_flag: show_system_resources
category: operations
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show system resources"
description: "Show live CPU / memory — use --remote for live device data"
feature_flag: show_system_resources
category: operations
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show system resources"
description: "Show live CPU / memory — use --remote for live device data"
feature_flag: show_system_resources
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# show system resources

Show system CPU / memory resources

## Category

system

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show system resources
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
