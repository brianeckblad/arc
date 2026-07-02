---
command: "show cngfw auto-tag-actions"
description: "List auto-tag actions"
category: cloudngfw
scope: global
---

# show cngfw auto-tag-actions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List auto-tag actions

## Usage

```
show cngfw auto-tag-actions [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw auto-tag-actions
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw auto-tag-actions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw auto-tag-actions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
