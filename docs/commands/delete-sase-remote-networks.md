---
command: "delete sase remote-networks"
description: "Delete a remote network"
category: sase
scope: global
---

# delete sase remote-networks

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a remote network

## Usage

```
delete sase remote-networks [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase remote-networks
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase remote-networks --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase remote-networks
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
