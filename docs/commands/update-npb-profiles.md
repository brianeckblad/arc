---
command: "update npb-profiles"
description: "Update Network Packet Broker Profile by ID"
category: network
scope: global
---

# update npb-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Network Packet Broker Profile by ID

## Usage

```
update npb-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update npb-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update npb-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update npb-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
