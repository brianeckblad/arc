---
command: "show cngfw tags id"
description: "Get a tag"
category: cloudngfw
scope: global
---

# show cngfw tags id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a tag

## Usage

```
show cngfw tags id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw tags id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw tags id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw tags id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
