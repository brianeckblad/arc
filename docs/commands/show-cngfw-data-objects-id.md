---
command: "show cngfw data-objects id"
description: "Get Data Object by ID"
category: cloudngfw
scope: global
---

# show cngfw data-objects id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Data Object by ID

## Usage

```
show cngfw data-objects id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw data-objects id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw data-objects id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw data-objects id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
