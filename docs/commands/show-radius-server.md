---
command: "show radius-server"
description: "Show RADIUS server profiles in the active folder"
feature_flag: authentication
category: identity
scope: folder
api: "GET /config/identity/v1/radius-server-profiles"
---

# show radius-server

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show radius-server`

## Description

Show RADIUS server profiles in the active folder

## Usage

```
show radius-server [--remote]
```

## Examples

Run via SCM API:
```
arc > show radius-server
```

Run directly on device via SSH:
```
arc:fw-01 > show radius-server --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show radius-server
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
