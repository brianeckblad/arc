---
command: "set service-accounts reset"
description: "Reset a service account"
category: iam
scope: global
---

# set service-accounts reset

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Reset a service account

## Usage

```
set service-accounts reset [--remote]
```

## Examples

Run via SCM API:
```
arc > set service-accounts reset
```

Run directly on device via SSH:
```
arc:fw-01 > set service-accounts reset --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set service-accounts reset
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
