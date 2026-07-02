---
command: "update cngfw address-groups"
description: "Update an address group"
category: cloudngfw
scope: global
---

# update cngfw address-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an address group

## Usage

```
update cngfw address-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw address-groups
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw address-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw address-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
