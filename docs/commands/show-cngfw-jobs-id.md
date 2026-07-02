---
command: "show cngfw jobs id"
description: "Get a job"
category: cloudngfw
scope: global
---

# show cngfw jobs id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a job

## Usage

```
show cngfw jobs id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw jobs id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw jobs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw jobs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
