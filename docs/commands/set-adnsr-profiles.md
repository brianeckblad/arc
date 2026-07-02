---
command: "set adnsr profiles"
description: "Create a profile"
category: adnsr
scope: global
---

# set adnsr profiles

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a profile

## Usage

```
set adnsr profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
