---
command: "show cngfw sites id"
description: "Get a site"
category: cloudngfw
scope: global
---

# show cngfw sites id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a site

## Usage

```
show cngfw sites id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw sites id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw sites id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw sites id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
