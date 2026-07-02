---
command: "show cngfw scep-profiles id"
description: "Get a SCEP profile"
category: cloudngfw
scope: global
---

# show cngfw scep-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a SCEP profile

## Usage

```
show cngfw scep-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw scep-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw scep-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw scep-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
