---
command: "show cngfw applications id"
description: "Get the application by id"
category: cloudngfw
scope: global
---

# show cngfw applications id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the application by id

## Usage

```
show cngfw applications id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw applications id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw applications id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw applications id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
