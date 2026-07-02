---
command: "show vlan-interfaces id"
description: "Get a VLAN interface"
category: network
scope: global
---

# show vlan-interfaces id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a VLAN interface

## Usage

```
show vlan-interfaces id [--remote]
```

## Examples

Run via SCM API:
```
arc > show vlan-interfaces id
```

Run directly on device via SSH:
```
arc:fw-01 > show vlan-interfaces id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show vlan-interfaces id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
