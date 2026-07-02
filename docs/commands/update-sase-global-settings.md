---
command: "update sase global-settings"
description: "Update GlobalProtect global settings"
category: sase
scope: global
---

# update sase global-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update GlobalProtect global settings

## Usage

```
update sase global-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase global-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update sase global-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase global-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
