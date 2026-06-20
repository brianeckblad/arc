---
command: "show authentication-rules"
description: "Show authentication rules in the active folder"
feature_flag: authentication
category: identity
scope: folder
api: "GET /config/identity/v1/authentication-rules"
---

# show authentication-rules

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show authentication-rule`

## Description

Show authentication rules in the active folder

## Usage

```
show authentication-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show authentication-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show authentication-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show authentication-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
