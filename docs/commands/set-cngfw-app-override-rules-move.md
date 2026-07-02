---
command: "set cngfw app-override-rules move"
description: "Move an application override rule"
category: cloudngfw
scope: global
---

# set cngfw app-override-rules move

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Move an application override rule

## Usage

```
set cngfw app-override-rules move [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw app-override-rules move
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw app-override-rules move --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw app-override-rules move
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
