---
command: "set cngfw log-forwarding-profiles"
description: "Create a log forwarding profile"
category: cloudngfw
scope: global
---

# set cngfw log-forwarding-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a log forwarding profile

## Usage

```
set cngfw log-forwarding-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw log-forwarding-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw log-forwarding-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw log-forwarding-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
