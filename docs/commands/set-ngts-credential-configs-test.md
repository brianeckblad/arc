---
command: "set ngts credential-configs test"
description: "Test the connection to a privileged"
category: ngts
scope: global
---

# set ngts credential-configs test

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Test the connection to a privileged

## Usage

```
set ngts credential-configs test [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts credential-configs test
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts credential-configs test --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts credential-configs test
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
