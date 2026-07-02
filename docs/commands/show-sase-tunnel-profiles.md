---
command: "show sase tunnel-profiles"
description: "List GlobalProtect tunnel settings"
category: sase
scope: global
---

# show sase tunnel-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect tunnel settings

## Usage

```
show sase tunnel-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase tunnel-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show sase tunnel-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase tunnel-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
