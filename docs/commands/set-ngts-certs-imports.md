---
command: "set ngts certs imports"
description: "Import a list of certificates and"
category: ngts
scope: global
---

# set ngts certs imports

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Import a list of certificates and

## Usage

```
set ngts certs imports [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certs imports
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certs imports --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certs imports
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
