---
command: "set ngts integrationservices"
description: "Add a service"
category: ngts
scope: global
---

# set ngts integrationservices

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Add a service

## Usage

```
set ngts integrationservices [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts integrationservices
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts integrationservices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts integrationservices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
