---
command: "show cngfw site-groups"
description: "List site groups"
category: cloudngfw
scope: global
---

# show cngfw site-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List site groups

## Usage

```
show cngfw site-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw site-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw site-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw site-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
