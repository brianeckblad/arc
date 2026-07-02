---
command: "set cngfw trusts"
description: "Create a trust"
category: cloudngfw
scope: global
---

# set cngfw trusts

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a trust

## Usage

```
set cngfw trusts [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw trusts
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw trusts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw trusts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
