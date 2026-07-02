---
command: "show sase traffic-steering-rules id"
description: "Get a traffic steering rule"
category: sase
scope: global
---

# show sase traffic-steering-rules id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a traffic steering rule

## Usage

```
show sase traffic-steering-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase traffic-steering-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase traffic-steering-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase traffic-steering-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
