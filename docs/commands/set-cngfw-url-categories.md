---
command: "set cngfw url-categories"
description: "Create a custom URL category"
category: cloudngfw
scope: global
---

# set cngfw url-categories

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a custom URL category

## Usage

```
set cngfw url-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw url-categories
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw url-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw url-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
