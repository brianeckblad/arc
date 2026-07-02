---
command: "delete cngfw local-user-groups"
description: "Delete a local user group"
category: cloudngfw
scope: global
---

# delete cngfw local-user-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a local user group

## Usage

```
delete cngfw local-user-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw local-user-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw local-user-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw local-user-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
