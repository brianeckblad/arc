---
command: "show ngts credentials"
description: "Retrieves credentials for a company"
category: ngts
scope: global
---

# show ngts credentials

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieves credentials for a company

## Usage

```
show ngts credentials [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts credentials
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts credentials --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts credentials
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
