---
command: "show vlan-interfaces"
description: "List VLAN interfaces"
category: network
scope: global
---

# show vlan-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List VLAN interfaces

## Usage

```
show vlan-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > show vlan-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > show vlan-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show vlan-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
