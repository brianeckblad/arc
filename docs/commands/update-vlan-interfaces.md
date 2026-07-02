---
command: "update vlan-interfaces"
description: "Update a VLAN interface"
category: network
scope: global
---

# update vlan-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a VLAN interface

## Usage

```
update vlan-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > update vlan-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > update vlan-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update vlan-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
