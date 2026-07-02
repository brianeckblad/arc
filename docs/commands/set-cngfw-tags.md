---
command: "set cngfw tags"
description: "Create a tag"
category: cloudngfw
scope: global
---

# set cngfw tags

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a tag

## Usage

```
set cngfw tags [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw tags
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
