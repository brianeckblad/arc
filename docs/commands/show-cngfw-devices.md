---
command: "show cngfw devices"
description: "List devices"
category: cloudngfw
scope: global
---

# show cngfw devices

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List devices

## Usage

```
show cngfw devices [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw devices
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw devices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw devices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
