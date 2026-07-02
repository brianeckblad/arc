---
command: "set cngfw quarantined-devices"
description: "Create a quarantined device"
category: cloudngfw
scope: global
---

# set cngfw quarantined-devices

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a quarantined device

## Usage

```
set cngfw quarantined-devices [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw quarantined-devices
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw quarantined-devices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw quarantined-devices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
