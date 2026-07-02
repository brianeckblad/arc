---
command: "show cngfw log-forwarding-profiles"
description: "List log forwarding profiles"
category: cloudngfw
scope: global
---

# show cngfw log-forwarding-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List log forwarding profiles

## Usage

```
show cngfw log-forwarding-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw log-forwarding-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw log-forwarding-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw log-forwarding-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
