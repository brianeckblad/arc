---
command: "update sase remote-networks"
description: "Update a remote network"
category: sase
scope: global
---

# update sase remote-networks

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a remote network

## Usage

```
update sase remote-networks [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase remote-networks
```

Run directly on device via SSH:
```
arc:fw-01 > update sase remote-networks --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase remote-networks
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
