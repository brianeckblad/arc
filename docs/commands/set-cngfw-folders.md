---
command: "set cngfw folders"
description: "Create a folder"
category: cloudngfw
scope: global
---

# set cngfw folders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a folder

## Usage

```
set cngfw folders [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw folders
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw folders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw folders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
