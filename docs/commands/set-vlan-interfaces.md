---
command: "set vlan-interfaces"
description: "Create a VLAN interface"
category: network
scope: global
---

# set vlan-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a VLAN interface

## Usage

```
set vlan-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set vlan-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set vlan-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set vlan-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
