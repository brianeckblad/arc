---
command: "show log system"
description: "Show live system log — use --remote for live device data"
feature_flag: show_log_system
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# show log system

Show system log (last 20 entries)

## Category

logs

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show log system
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
