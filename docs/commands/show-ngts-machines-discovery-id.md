---
command: "show ngts machines discovery id"
description: "Get the discovery results for a"
category: ngts
scope: global
---

# show ngts machines discovery id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the discovery results for a

## Usage

```
show ngts machines discovery id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts machines discovery id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts machines discovery id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts machines discovery id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
