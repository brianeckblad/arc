---
command: "update cngfw device-contexts"
description: "Update a device context segment"
category: cloudngfw
scope: global
---

# update cngfw device-contexts

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a device context segment

## Usage

```
update cngfw device-contexts [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw device-contexts
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw device-contexts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw device-contexts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
