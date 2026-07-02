---
command: "set cngfw address-groups"
description: "Create an address group"
category: cloudngfw
scope: global
---

# set cngfw address-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an address group

## Usage

```
set cngfw address-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw address-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw address-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw address-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
