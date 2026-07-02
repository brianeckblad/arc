---
command: "delete lldp-profiles"
description: "Delete an LLDP profile"
category: network
scope: global
---

# delete lldp-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an LLDP profile

## Usage

```
delete lldp-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete lldp-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete lldp-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete lldp-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
