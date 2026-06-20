---
command: "ping host"
description: "Ping a host from a managed device (use --remote)"
usage: "ping host <ip>"
feature_flag: ping
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# ping host

Ping a host — ping host <ip>

## Category

tools

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
ping host 8.8.8.8
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
