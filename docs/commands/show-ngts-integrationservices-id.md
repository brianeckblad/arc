---
command: "show ngts integrationservices id"
description: "Get service details"
category: ngts
scope: global
---

# show ngts integrationservices id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get service details

## Usage

```
show ngts integrationservices id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts integrationservices id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts integrationservices id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts integrationservices id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
