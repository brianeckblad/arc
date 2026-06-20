---
command: "show interface"
description: "Show a specific interface in the active folder"
usage: "show interface <name>"
feature_flag: show_interface
category: network
scope: folder
api: "GET /config/network/v1/ethernet-interfaces"
---

# show interface

Show a specific interface — show interface <name>

## Category

network

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show interface ethernet1/1
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
