---
command: "delete cngfw adv-device-objs"
description: "Delete advanced device objects by names"
category: cloudngfw
scope: global
---

# delete cngfw adv-device-objs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete advanced device objects by names

## Usage

```
delete cngfw adv-device-objs [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw adv-device-objs
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw adv-device-objs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw adv-device-objs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
