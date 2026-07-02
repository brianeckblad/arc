---
command: "delete cngfw site-groups"
description: "Delete a site group"
category: cloudngfw
scope: global
---

# delete cngfw site-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a site group

## Usage

```
delete cngfw site-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw site-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw site-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw site-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
