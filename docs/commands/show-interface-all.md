---
command: "show interface all"
description: "Show all interfaces in the active folder"
feature_flag: show_interface
category: network
scope: folder
api: "GET /config/network/v1/ethernet-interfaces"
---

# show interface all

Show all interfaces

## Category

network

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show interface all
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
