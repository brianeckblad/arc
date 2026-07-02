---
command: "show cngfw devices id"
description: "Get a device"
category: cloudngfw
scope: global
---

# show cngfw devices id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a device

## Usage

```
show cngfw devices id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw devices id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw devices id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw devices id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
