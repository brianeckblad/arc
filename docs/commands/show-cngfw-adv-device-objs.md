---
command: "show cngfw adv-device-objs"
description: "List advanced device objects"
category: cloudngfw
scope: global
---

# show cngfw adv-device-objs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List advanced device objects

## Usage

```
show cngfw adv-device-objs [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw adv-device-objs
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw adv-device-objs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw adv-device-objs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
