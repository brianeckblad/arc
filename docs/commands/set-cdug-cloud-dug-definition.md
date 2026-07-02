---
command: "set cdug cloud-dug-definition"
description: "Create Cloud Dynamic User Groups"
category: cdug
scope: global
---

# set cdug cloud-dug-definition

**Category:** cdug
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Cloud Dynamic User Groups

## Usage

```
set cdug cloud-dug-definition [--remote]
```

## Examples

Run via SCM API:
```
arc > set cdug cloud-dug-definition
```

Run directly on device via SSH:
```
arc:fw-01 > set cdug cloud-dug-definition --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cdug cloud-dug-definition
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
