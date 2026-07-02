---
command: "set cngfw authentication-sequences"
description: "Create an authentication sequence"
category: cloudngfw
scope: global
---

# set cngfw authentication-sequences

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an authentication sequence

## Usage

```
set cngfw authentication-sequences [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw authentication-sequences
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw authentication-sequences --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw authentication-sequences
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
