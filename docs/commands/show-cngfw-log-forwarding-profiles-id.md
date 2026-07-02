---
command: "show cngfw log-forwarding-profiles id"
description: "Get a log forwarding profile"
category: cloudngfw
scope: global
---

# show cngfw log-forwarding-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a log forwarding profile

## Usage

```
show cngfw log-forwarding-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw log-forwarding-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw log-forwarding-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw log-forwarding-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
