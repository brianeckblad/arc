---
command: "show cngfw folders id"
description: "Get a folder"
category: cloudngfw
scope: global
---

# show cngfw folders id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a folder

## Usage

```
show cngfw folders id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw folders id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw folders id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw folders id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
