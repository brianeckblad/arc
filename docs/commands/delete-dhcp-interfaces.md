---
command: "delete dhcp-interfaces"
description: "Delete a DHCP interface"
category: network
scope: global
---

# delete dhcp-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a DHCP interface

## Usage

```
delete dhcp-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete dhcp-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete dhcp-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete dhcp-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
