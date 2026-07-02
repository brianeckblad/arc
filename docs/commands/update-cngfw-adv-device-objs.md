---
command: "update cngfw adv-device-objs"
description: "Update an advanced device object by path"
category: cloudngfw
scope: global
---

# update cngfw adv-device-objs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an advanced device object by path

## Usage

```
update cngfw adv-device-objs [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw adv-device-objs
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw adv-device-objs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw adv-device-objs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
