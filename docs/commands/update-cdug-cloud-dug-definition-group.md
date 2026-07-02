---
command: "update cdug cloud-dug-definition group"
description: "Update Cloud Dynamic User Groups"
category: cdug
scope: global
---

# update cdug cloud-dug-definition group

**Category:** cdug
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Cloud Dynamic User Groups

## Usage

```
update cdug cloud-dug-definition group [--remote]
```

## Examples

Run via SCM API:
```
arc > update cdug cloud-dug-definition group
```

Run directly on device via SSH:
```
arc:fw-01 > update cdug cloud-dug-definition group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cdug cloud-dug-definition group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
