---
command: "update cngfw data-filtering-profiles"
description: "Update Data Filtering Profile by ID"
category: cloudngfw
scope: global
---

# update cngfw data-filtering-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Data Filtering Profile by ID

## Usage

```
update cngfw data-filtering-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw data-filtering-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw data-filtering-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw data-filtering-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
