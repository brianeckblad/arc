---
command: "set dhcp-interfaces"
description: "Create a DHCP interface"
category: network
scope: global
---

# set dhcp-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a DHCP interface

## Usage

```
set dhcp-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set dhcp-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set dhcp-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set dhcp-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
