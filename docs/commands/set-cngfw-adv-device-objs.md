---
command: "set cngfw adv-device-objs"
description: "Create an advanced device object"
category: cloudngfw
scope: global
---

# set cngfw adv-device-objs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an advanced device object

## Usage

```
set cngfw adv-device-objs [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw adv-device-objs
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw adv-device-objs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw adv-device-objs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
