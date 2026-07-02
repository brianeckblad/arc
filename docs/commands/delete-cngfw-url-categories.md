---
command: "delete cngfw url-categories"
description: "Delete a custom URL Category"
category: cloudngfw
scope: global
---

# delete cngfw url-categories

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a custom URL Category

## Usage

```
delete cngfw url-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw url-categories
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw url-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw url-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
