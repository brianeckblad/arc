---
command: "show cngfw authentication-rules"
description: "List authentication rules"
category: cloudngfw
scope: global
---

# show cngfw authentication-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List authentication rules

## Usage

```
show cngfw authentication-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
