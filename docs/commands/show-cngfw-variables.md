---
command: "show cngfw variables"
description: "List variables"
category: cloudngfw
scope: global
---

# show cngfw variables

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List variables

## Usage

```
show cngfw variables [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw variables
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw variables --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw variables
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
