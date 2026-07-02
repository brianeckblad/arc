---
command: "show lldp-profiles"
description: "List LLDP profiles"
category: network
scope: global
---

# show lldp-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List LLDP profiles

## Usage

```
show lldp-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show lldp-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show lldp-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show lldp-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
