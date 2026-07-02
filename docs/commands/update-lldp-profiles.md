---
command: "update lldp-profiles"
description: "Update an LLDP profile"
category: network
scope: global
---

# update lldp-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an LLDP profile

## Usage

```
update lldp-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update lldp-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update lldp-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update lldp-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
