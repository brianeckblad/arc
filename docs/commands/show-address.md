---
command: "show address"
description: "Show address objects in the active folder"
feature_flag: show_address
category: objects
scope: folder
api: "GET /config/objects/v1/addresses"
---

# show address

Show address objects

## Category

policy

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

API only; `--remote` falls back to API with a warning.

## Examples

```text
show address
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
