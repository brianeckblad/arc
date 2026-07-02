---
command: "set cngfw device-contexts"
description: "Create a device context segment"
category: cloudngfw
scope: global
---

# set cngfw device-contexts

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a device context segment

## Usage

```
set cngfw device-contexts [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw device-contexts
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw device-contexts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw device-contexts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
