---
command: "show cdug cloud-dug-definition category"
description: "Retrieve Dynamic Group Categories"
category: cdug
scope: global
---

# show cdug cloud-dug-definition category

**Category:** cdug
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Dynamic Group Categories

## Usage

```
show cdug cloud-dug-definition category [--remote]
```

## Examples

Run via SCM API:
```
arc > show cdug cloud-dug-definition category
```

Run directly on device via SSH:
```
arc:fw-01 > show cdug cloud-dug-definition category --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cdug cloud-dug-definition category
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
