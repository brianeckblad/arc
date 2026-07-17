---
command: "show devices"
description: "List all SCM-managed devices"
feature_flag: show_devices
category: setup
scope: global
api: "GET /config/setup/v1/devices"
---

---
command: "show devices"
description: "List all SCM-managed devices"
feature_flag: show_devices
category: setup
scope: global
api: "GET /config/setup/v1/devices"
---

---
command: "show devices"
description: "List all SCM-managed devices"
feature_flag: show_devices
category: setup
scope: global
api: "GET /config/setup/v1/devices"
---

# show devices

List all managed devices

## Category

devices

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

API only; `--remote` falls back to API with a warning.

## Examples

```text
show devices
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
