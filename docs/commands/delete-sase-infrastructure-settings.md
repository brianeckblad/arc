---
command: "delete sase infrastructure-settings"
description: "Delete a GlobalProtect infrastructure setting"
category: sase
scope: global
---

# delete sase infrastructure-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect infrastructure setting

## Usage

```
delete sase infrastructure-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase infrastructure-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase infrastructure-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase infrastructure-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
