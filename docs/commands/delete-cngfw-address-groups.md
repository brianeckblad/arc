---
command: "delete cngfw address-groups"
description: "Delete an address group"
category: cloudngfw
scope: global
---

# delete cngfw address-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an address group

## Usage

```
delete cngfw address-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw address-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw address-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw address-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
