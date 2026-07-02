---
command: "set ngts credentials test"
description: "Test the access to shared credential"
category: ngts
scope: global
---

# set ngts credentials test

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Test the access to shared credential

## Usage

```
set ngts credentials test [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts credentials test
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts credentials test --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts credentials test
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
