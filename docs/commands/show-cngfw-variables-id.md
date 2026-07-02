---
command: "show cngfw variables id"
description: "Get a variables"
category: cloudngfw
scope: global
---

# show cngfw variables id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a variables

## Usage

```
show cngfw variables id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw variables id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw variables id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw variables id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
