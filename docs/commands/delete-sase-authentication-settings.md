---
command: "delete sase authentication-settings"
description: "Delete a GlobalProtect authentication setting"
category: sase
scope: global
---

# delete sase authentication-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect authentication setting

## Usage

```
delete sase authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
