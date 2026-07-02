---
command: "show cdug cloud-dug-definition group"
description: "Retrieve Cloud Dynamic User Groups"
category: cdug
scope: global
---

# show cdug cloud-dug-definition group

**Category:** cdug
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Cloud Dynamic User Groups

## Usage

```
show cdug cloud-dug-definition group [--remote]
```

## Examples

Run via SCM API:
```
arc > show cdug cloud-dug-definition group
```

Run directly on device via SSH:
```
arc:fw-01 > show cdug cloud-dug-definition group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cdug cloud-dug-definition group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
