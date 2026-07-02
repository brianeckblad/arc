---
command: "show sase global-settings"
description: "List GlobalProtect global settings"
category: sase
scope: global
---

# show sase global-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect global settings

## Usage

```
show sase global-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase global-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show sase global-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase global-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
