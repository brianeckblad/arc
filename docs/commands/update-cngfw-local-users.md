---
command: "update cngfw local-users"
description: "Update a local user"
category: cloudngfw
scope: global
---

# update cngfw local-users

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a local user

## Usage

```
update cngfw local-users [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw local-users
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw local-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw local-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
