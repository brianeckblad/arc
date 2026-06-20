---
command: "show region"
description: "Show regions (TSG-wide, no folder filter)"
feature_flag: regions
category: objects
scope: global
api: "GET /config/objects/v1/regions"
---

# show region

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show regions (TSG-wide, no folder filter)

## Usage

```
show region [--remote]
```

## Examples

Run via SCM API:
```
arc > show region
```

Run directly on device via SSH:
```
arc:fw-01 > show region --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show region
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
