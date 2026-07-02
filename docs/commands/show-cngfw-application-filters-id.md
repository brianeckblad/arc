---
command: "show cngfw application-filters id"
description: "Get an application filter"
category: cloudngfw
scope: global
---

# show cngfw application-filters id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an application filter

## Usage

```
show cngfw application-filters id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw application-filters id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw application-filters id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw application-filters id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
