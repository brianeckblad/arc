---
command: "set cngfw site-groups"
description: "Create a site group"
category: cloudngfw
scope: global
---

# set cngfw site-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a site group

## Usage

```
set cngfw site-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw site-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw site-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw site-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
