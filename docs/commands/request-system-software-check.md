---
command: "request system software check"
description: "Check available software updates — use --remote for live data"
usage: "request system software check"
feature_flag: request_system_software
category: operations
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "request system software check"
description: "Check available software updates — use --remote for live data"
usage: "request system software check"
feature_flag: request_system_software
category: operations
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "request system software check"
description: "Check available software updates (use --remote for live data)"
usage: "request system software check"
feature_flag: request_system_software
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# request system software check

Check for available software updates

## Category

system

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
request system software check
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
