---
command: "set cngfw variables"
description: "Create a variable"
category: cloudngfw
scope: global
---

# set cngfw variables

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a variable

## Usage

```
set cngfw variables [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw variables
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw variables --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw variables
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
