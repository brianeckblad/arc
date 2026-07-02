---
command: "delete ngts integrationservices"
description: "Remove a service"
category: ngts
scope: global
---

# delete ngts integrationservices

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Remove a service

## Usage

```
delete ngts integrationservices [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts integrationservices
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts integrationservices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts integrationservices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
