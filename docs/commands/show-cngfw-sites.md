---
command: "show cngfw sites"
description: "List sites"
category: cloudngfw
scope: global
---

# show cngfw sites

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List sites

## Usage

```
show cngfw sites [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw sites
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
