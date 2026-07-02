---
command: "show cngfw device-contexts id"
description: "Get a device context segment"
category: cloudngfw
scope: global
---

# show cngfw device-contexts id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a device context segment

## Usage

```
show cngfw device-contexts id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw device-contexts id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw device-contexts id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw device-contexts id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
