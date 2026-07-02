---
command: "show sase infrastructure-settings"
description: "List GlobalProtect infrastructure settings"
category: sase
scope: global
---

# show sase infrastructure-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect infrastructure settings

## Usage

```
show sase infrastructure-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase infrastructure-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show sase infrastructure-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase infrastructure-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
