---
command: "show cngfw authentication-rules id"
description: "Get an authentication rule"
category: cloudngfw
scope: global
---

# show cngfw authentication-rules id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an authentication rule

## Usage

```
show cngfw authentication-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
