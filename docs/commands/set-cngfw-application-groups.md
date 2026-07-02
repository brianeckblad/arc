---
command: "set cngfw application-groups"
description: "Create an application group"
category: cloudngfw
scope: global
---

# set cngfw application-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an application group

## Usage

```
set cngfw application-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw application-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw application-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw application-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
