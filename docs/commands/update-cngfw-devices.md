---
command: "update cngfw devices"
description: "Update a device"
category: cloudngfw
scope: global
---

# update cngfw devices

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a device

## Usage

```
update cngfw devices [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw devices
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw devices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw devices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
