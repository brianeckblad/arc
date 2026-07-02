---
command: "set sase tunnel-profiles"
description: "Create a GlobalProtect tunnel setting"
category: sase
scope: global
---

# set sase tunnel-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a GlobalProtect tunnel setting

## Usage

```
set sase tunnel-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase tunnel-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set sase tunnel-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase tunnel-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
