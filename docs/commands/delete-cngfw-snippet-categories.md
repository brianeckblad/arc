---
command: "delete cngfw snippet-categories"
description: "Delete a snippet category"
category: cloudngfw
scope: global
---

# delete cngfw snippet-categories

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a snippet category

## Usage

```
delete cngfw snippet-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw snippet-categories
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw snippet-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw snippet-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
