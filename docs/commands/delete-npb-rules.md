---
command: "delete npb-rules"
description: "Delete a Network Packet Broker Rule"
category: network
scope: global
---

# delete npb-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a Network Packet Broker Rule

## Usage

```
delete npb-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete npb-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete npb-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete npb-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
