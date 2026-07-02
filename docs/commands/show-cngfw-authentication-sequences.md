---
command: "show cngfw authentication-sequences"
description: "List authentication sequences"
category: cloudngfw
scope: global
---

# show cngfw authentication-sequences

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List authentication sequences

## Usage

```
show cngfw authentication-sequences [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-sequences
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-sequences --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-sequences
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
