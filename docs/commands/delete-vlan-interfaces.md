---
command: "delete vlan-interfaces"
description: "Delete a VLAN interface"
category: network
scope: global
---

# delete vlan-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a VLAN interface

## Usage

```
delete vlan-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete vlan-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete vlan-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete vlan-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
