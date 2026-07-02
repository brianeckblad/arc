---
command: "show cngfw address-groups"
description: "List address groups"
category: cloudngfw
scope: global
---

# show cngfw address-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List address groups

## Usage

```
show cngfw address-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw address-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw address-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw address-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
