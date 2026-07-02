---
command: "delete cngfw dynamic-user-groups"
description: "Delete a Dynamic User Group"
category: cloudngfw
scope: global
---

# delete cngfw dynamic-user-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a Dynamic User Group

## Usage

```
delete cngfw dynamic-user-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw dynamic-user-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw dynamic-user-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw dynamic-user-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
