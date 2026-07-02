---
command: "show cngfw applications"
description: "List applications"
category: cloudngfw
scope: global
---

# show cngfw applications

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List applications

## Usage

```
show cngfw applications [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw applications
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw applications --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw applications
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
