---
command: "delete cngfw adv-device-objs id"
description: "Delete an advanced device object"
category: cloudngfw
scope: global
---

# delete cngfw adv-device-objs id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an advanced device object

## Usage

```
delete cngfw adv-device-objs id [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw adv-device-objs id
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw adv-device-objs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw adv-device-objs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
