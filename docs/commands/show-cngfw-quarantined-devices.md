---
command: "show cngfw quarantined-devices"
description: "List quarantined devices"
category: cloudngfw
scope: global
---

# show cngfw quarantined-devices

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List quarantined devices

## Usage

```
show cngfw quarantined-devices [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw quarantined-devices
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw quarantined-devices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw quarantined-devices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
