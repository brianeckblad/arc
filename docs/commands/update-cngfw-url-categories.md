---
command: "update cngfw url-categories"
description: "Update a custom URL category"
category: cloudngfw
scope: global
---

# update cngfw url-categories

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a custom URL category

## Usage

```
update cngfw url-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw url-categories
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw url-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw url-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
