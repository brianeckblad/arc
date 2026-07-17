---
command: "show address-group"
description: "Show address groups in the active folder"
usage: "show address-group [<name>]"
feature_flag: show_address_group
category: objects
scope: folder
api: "GET /config/objects/v1/address-groups"
---

---
command: "show address-group"
description: "Show address groups in the active folder"
usage: "show address-group [<name>]"
feature_flag: show_address_group
category: objects
scope: folder
api: "GET /config/objects/v1/address-groups"
---

---
command: "show address-group"
description: "Show address groups in the active folder"
feature_flag: show_address_group
category: objects
scope: folder
api: "GET /config/objects/v1/address-groups"
---

# show address-group

Show address groups

## Category

policy

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

API only; `--remote` falls back to API with a warning.

## Examples

```text
show address-group
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
