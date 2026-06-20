---
command: "show system info"
description: "Show device info from SCM (model, serial, SW version, IP, status…)"
feature_flag: show_system_info
category: operations
scope: device
api: "GET /config/setup/v1/devices/{id}"
---

# show system info

Show system information (hostname, model, SW version, uptime...)

## Category

system

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show system info
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
