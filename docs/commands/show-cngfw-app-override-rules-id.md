---
command: "show cngfw app-override-rules id"
description: "Get an application override rule"
category: cloudngfw
scope: global
---

# show cngfw app-override-rules id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an application override rule

## Usage

```
show cngfw app-override-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw app-override-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw app-override-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw app-override-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
