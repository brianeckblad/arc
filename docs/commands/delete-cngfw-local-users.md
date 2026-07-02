---
command: "delete cngfw local-users"
description: "Delete a local user"
category: cloudngfw
scope: global
---

# delete cngfw local-users

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a local user

## Usage

```
delete cngfw local-users [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw local-users
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw local-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw local-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
