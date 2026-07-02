---
command: "show cngfw security-rules id"
description: "Get a security rule"
category: cloudngfw
scope: global
---

# show cngfw security-rules id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a security rule

## Usage

```
show cngfw security-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw security-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw security-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw security-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
