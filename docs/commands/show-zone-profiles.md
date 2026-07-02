---
command: "show zone-profiles"
description: "List zone protection profiles"
category: network
scope: global
---

# show zone-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List zone protection profiles

## Usage

```
show zone-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show zone-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show zone-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show zone-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
