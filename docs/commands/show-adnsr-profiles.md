---
command: "show adnsr profiles"
description: "List profiles"
category: adnsr
scope: global
---

# show adnsr profiles

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List profiles

## Usage

```
show adnsr profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
