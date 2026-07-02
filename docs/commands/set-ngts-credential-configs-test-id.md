---
command: "set ngts credential-configs test id"
description: "Test the connection to an external"
category: ngts
scope: global
---

# set ngts credential-configs test id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Test the connection to an external

## Usage

```
set ngts credential-configs test id [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts credential-configs test id
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts credential-configs test id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts credential-configs test id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
