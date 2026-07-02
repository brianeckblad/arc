---
command: "show ngts integrationservices"
description: "Get a list of services"
category: ngts
scope: global
---

# show ngts integrationservices

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a list of services

## Usage

```
show ngts integrationservices [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts integrationservices
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts integrationservices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts integrationservices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
