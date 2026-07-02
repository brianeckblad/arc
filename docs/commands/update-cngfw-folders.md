---
command: "update cngfw folders"
description: "Update a folder"
category: cloudngfw
scope: global
---

# update cngfw folders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a folder

## Usage

```
update cngfw folders [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw folders
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw folders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw folders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
