---
command: "show cngfw device-contexts"
description: "List device context segments"
category: cloudngfw
scope: global
---

# show cngfw device-contexts

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List device context segments

## Usage

```
show cngfw device-contexts [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw device-contexts
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw device-contexts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw device-contexts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
