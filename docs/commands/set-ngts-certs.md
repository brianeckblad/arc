---
command: "set ngts certs"
description: "Import a set of raw certificates"
category: ngts
scope: global
---

# set ngts certs

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Import a set of raw certificates

## Usage

```
set ngts certs [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certs
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
