---
command: "set sase traffic-steering-rules"
description: "Create a traffic steering rule"
category: sase
scope: global
---

# set sase traffic-steering-rules

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a traffic steering rule

## Usage

```
set sase traffic-steering-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase traffic-steering-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set sase traffic-steering-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase traffic-steering-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
