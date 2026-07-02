---
command: "delete cngfw auto-tag-actions"
description: "Delete an Auto-Tag action"
category: cloudngfw
scope: global
---

# delete cngfw auto-tag-actions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an Auto-Tag action

## Usage

```
delete cngfw auto-tag-actions [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw auto-tag-actions
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw auto-tag-actions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw auto-tag-actions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
