---
command: "show cngfw local-users"
description: "List local users"
category: cloudngfw
scope: global
---

# show cngfw local-users

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List local users

## Usage

```
show cngfw local-users [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw local-users
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw local-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw local-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
