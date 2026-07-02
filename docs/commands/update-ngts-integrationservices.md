---
command: "update ngts integrationservices"
description: "Update Service properties"
category: ngts
scope: global
---

# update ngts integrationservices

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Service properties

## Usage

```
update ngts integrationservices [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts integrationservices
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts integrationservices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts integrationservices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
