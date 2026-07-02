---
command: "delete adnsr profiles"
description: "Delete a profile"
category: adnsr
scope: global
---

# delete adnsr profiles

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a profile

## Usage

```
delete adnsr profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
