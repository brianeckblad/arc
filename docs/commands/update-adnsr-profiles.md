---
command: "update adnsr profiles"
description: "Update a profile"
category: adnsr
scope: global
---

# update adnsr profiles

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a profile

## Usage

```
update adnsr profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update adnsr profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update adnsr profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update adnsr profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
