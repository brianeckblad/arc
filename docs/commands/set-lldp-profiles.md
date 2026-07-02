---
command: "set lldp-profiles"
description: "Create an LLDP profile"
category: network
scope: global
---

# set lldp-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an LLDP profile

## Usage

```
set lldp-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set lldp-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set lldp-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set lldp-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
