---
command: "show service"
description: "Show service objects in the active folder"
usage: "show service [<name>]"
feature_flag: show_service
category: objects
scope: folder
api: "GET /config/objects/v1/services"
---

---
command: "show service"
description: "Show service objects in the active folder"
usage: "show service [<name>]"
feature_flag: show_service
category: objects
scope: folder
api: "GET /config/objects/v1/services"
---

---
command: "show service"
description: "Show service objects in the active folder"
feature_flag: show_service
category: objects
scope: folder
api: "GET /config/objects/v1/services"
---

# show service

Show service objects

## Category

policy

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

API only; `--remote` falls back to API with a warning.

## Examples

```text
show service
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
