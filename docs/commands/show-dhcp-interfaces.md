---
command: "show dhcp-interfaces"
description: "List DHCP interfaces"
category: network
scope: global
---

# show dhcp-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List DHCP interfaces

## Usage

```
show dhcp-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > show dhcp-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > show dhcp-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show dhcp-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
