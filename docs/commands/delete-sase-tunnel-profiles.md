---
command: "delete sase tunnel-profiles"
description: "Delete a GlobalProtect tunnel setting"
category: sase
scope: global
---

# delete sase tunnel-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect tunnel setting

## Usage

```
delete sase tunnel-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase tunnel-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase tunnel-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase tunnel-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
