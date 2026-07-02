---
command: "show cngfw folders"
description: "List folders"
category: cloudngfw
scope: global
---

# show cngfw folders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List folders

## Usage

```
show cngfw folders [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw folders
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw folders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw folders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
