---
command: "update sase authentication-settings"
description: "Update a GlobalProtect authentication setting"
category: sase
scope: global
---

# update sase authentication-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect authentication setting

## Usage

```
update sase authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update sase authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
