---
command: "set cngfw config-versions load"
description: "Load config version"
category: cloudngfw
scope: global
---

# set cngfw config-versions load

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Load config version

## Usage

```
set cngfw config-versions load [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw config-versions load
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw config-versions load --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw config-versions load
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
