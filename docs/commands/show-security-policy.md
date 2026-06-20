---
command: "show security policy"
description: "Show security policy rules in the active folder"
feature_flag: show_security_policy
category: security
scope: folder
api: "GET /config/security/v1/security-rules"
---

# show security policy

Show security policy rules

## Category

policy

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

API only; `--remote` falls back to API with a warning.

## Examples

```text
show security policy
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
