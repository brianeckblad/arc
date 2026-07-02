---
command: "set cngfw security-rules move"
description: "Move a security rule"
category: cloudngfw
scope: global
---

# set cngfw security-rules move

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Move a security rule

## Usage

```
set cngfw security-rules move [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw security-rules move
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw security-rules move --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw security-rules move
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
