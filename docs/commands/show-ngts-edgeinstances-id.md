---
command: "show ngts edgeinstances id"
description: "Retrieve Satellite Instance By Id"
category: ngts
scope: global
---

# show ngts edgeinstances id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Satellite Instance By Id

## Usage

```
show ngts edgeinstances id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts edgeinstances id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts edgeinstances id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts edgeinstances id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
