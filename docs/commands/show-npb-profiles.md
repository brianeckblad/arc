---
command: "show npb-profiles"
description: "List all Network Packet Broker Profiles"
category: network
scope: global
---

# show npb-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all Network Packet Broker Profiles

## Usage

```
show npb-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show npb-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show npb-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show npb-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
