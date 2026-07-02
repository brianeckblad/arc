---
command: "set cngfw local-users"
description: "Create a local user"
category: cloudngfw
scope: global
---

# set cngfw local-users

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a local user

## Usage

```
set cngfw local-users [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw local-users
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw local-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw local-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
