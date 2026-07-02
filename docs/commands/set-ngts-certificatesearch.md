---
command: "set ngts certificatesearch"
description: "Retrieve certificate data matching search criteria"
category: ngts
scope: global
---

# set ngts certificatesearch

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve certificate data matching search criteria

## Usage

```
set ngts certificatesearch [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certificatesearch
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certificatesearch --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certificatesearch
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
