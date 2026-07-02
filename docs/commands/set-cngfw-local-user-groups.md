---
command: "set cngfw local-user-groups"
description: "Create a local user group"
category: cloudngfw
scope: global
---

# set cngfw local-user-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a local user group

## Usage

```
set cngfw local-user-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw local-user-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw local-user-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw local-user-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
