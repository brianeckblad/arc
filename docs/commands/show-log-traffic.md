---
command: "show log traffic"
description: "Show live traffic log — use --remote for live device data"
feature_flag: show_log_traffic
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# show log traffic

Show traffic log (last 20 entries)

## Category

logs

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show log traffic
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
