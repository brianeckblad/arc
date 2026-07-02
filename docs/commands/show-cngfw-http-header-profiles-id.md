---
command: "show cngfw http-header-profiles id"
description: "Get an HTTP header profile"
category: cloudngfw
scope: global
---

# show cngfw http-header-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an HTTP header profile

## Usage

```
show cngfw http-header-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw http-header-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw http-header-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw http-header-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
