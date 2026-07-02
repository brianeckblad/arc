---
command: "show cngfw service-groups id"
description: "Get the service group by id"
category: cloudngfw
scope: global
---

# show cngfw service-groups id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the service group by id

## Usage

```
show cngfw service-groups id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw service-groups id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw service-groups id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw service-groups id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
