---
command: "set cngfw security-rules"
description: "Create a security rule"
category: cloudngfw
scope: global
---

# set cngfw security-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a security rule

## Usage

```
set cngfw security-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw security-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw security-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw security-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
