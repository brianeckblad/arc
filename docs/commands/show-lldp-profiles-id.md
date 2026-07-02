---
command: "show lldp-profiles id"
description: "Get an LLDP profile"
category: network
scope: global
---

# show lldp-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an LLDP profile

## Usage

```
show lldp-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show lldp-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show lldp-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show lldp-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
