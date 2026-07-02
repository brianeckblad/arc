---
command: "set ngts machineidentitysearch"
description: "Get the details of machine identities"
category: ngts
scope: global
---

# set ngts machineidentitysearch

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of machine identities

## Usage

```
set ngts machineidentitysearch [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machineidentitysearch
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machineidentitysearch --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machineidentitysearch
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
