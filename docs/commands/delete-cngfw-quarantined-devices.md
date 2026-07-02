---
command: "delete cngfw quarantined-devices"
description: "Delete a quarantined device"
category: cloudngfw
scope: global
---

# delete cngfw quarantined-devices

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a quarantined device

## Usage

```
delete cngfw quarantined-devices [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw quarantined-devices
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw quarantined-devices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw quarantined-devices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
