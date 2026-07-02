---
command: "update sase tunnel-profiles"
description: "Update a GlobalProtect tunnel setting"
category: sase
scope: global
---

# update sase tunnel-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect tunnel setting

## Usage

```
update sase tunnel-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase tunnel-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update sase tunnel-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase tunnel-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
