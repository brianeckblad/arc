---
command: "show system disk-space"
description: "Show live disk usage — use --remote for live device data"
feature_flag: show_system_disk_space
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# show system disk-space

Show disk space usage

## Category

system

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show system disk-space
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
