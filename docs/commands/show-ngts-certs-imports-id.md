---
command: "show ngts certs imports id"
description: "Retrieve import details"
category: ngts
scope: global
---

# show ngts certs imports id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve import details

## Usage

```
show ngts certs imports id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts certs imports id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts certs imports id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts certs imports id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
