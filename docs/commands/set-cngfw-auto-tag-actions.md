---
command: "set cngfw auto-tag-actions"
description: "Create an auto-tag action"
category: cloudngfw
scope: global
---

# set cngfw auto-tag-actions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an auto-tag action

## Usage

```
set cngfw auto-tag-actions [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw auto-tag-actions
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw auto-tag-actions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw auto-tag-actions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
