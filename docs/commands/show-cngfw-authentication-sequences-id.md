---
command: "show cngfw authentication-sequences id"
description: "Get an authentication sequence"
category: cloudngfw
scope: global
---

# show cngfw authentication-sequences id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an authentication sequence

## Usage

```
show cngfw authentication-sequences id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-sequences id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-sequences id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-sequences id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
