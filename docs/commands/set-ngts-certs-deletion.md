---
command: "set ngts certs deletion"
description: "Delete a set of retired certificates"
category: ngts
scope: global
---

# set ngts certs deletion

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a set of retired certificates

## Usage

```
set ngts certs deletion [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certs deletion
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certs deletion --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certs deletion
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
