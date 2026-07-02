---
command: "show cngfw data-filtering-profiles"
description: "List Data Filtering Profiles"
category: cloudngfw
scope: global
---

# show cngfw data-filtering-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Data Filtering Profiles

## Usage

```
show cngfw data-filtering-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw data-filtering-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw data-filtering-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw data-filtering-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
