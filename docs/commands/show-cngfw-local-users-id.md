---
command: "show cngfw local-users id"
description: "Get a local user"
category: cloudngfw
scope: global
---

# show cngfw local-users id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a local user

## Usage

```
show cngfw local-users id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw local-users id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw local-users id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw local-users id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
