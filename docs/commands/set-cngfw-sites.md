---
command: "set cngfw sites"
description: "Create sites"
category: cloudngfw
scope: global
---

# set cngfw sites

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create sites

## Usage

```
set cngfw sites [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw sites
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
