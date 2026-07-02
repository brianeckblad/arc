---
command: "show cngfw labels id"
description: "Get a label"
category: cloudngfw
scope: global
---

# show cngfw labels id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a label

## Usage

```
show cngfw labels id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw labels id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw labels id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw labels id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
