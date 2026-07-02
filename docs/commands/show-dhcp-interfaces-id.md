---
command: "show dhcp-interfaces id"
description: "Get a DHCP interface"
category: network
scope: global
---

# show dhcp-interfaces id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a DHCP interface

## Usage

```
show dhcp-interfaces id [--remote]
```

## Examples

Run via SCM API:
```
arc > show dhcp-interfaces id
```

Run directly on device via SSH:
```
arc:fw-01 > show dhcp-interfaces id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show dhcp-interfaces id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
