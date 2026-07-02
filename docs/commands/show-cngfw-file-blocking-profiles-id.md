---
command: "show cngfw file-blocking-profiles id"
description: "Get a file blocking profile"
category: cloudngfw
scope: global
---

# show cngfw file-blocking-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a file blocking profile

## Usage

```
show cngfw file-blocking-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw file-blocking-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw file-blocking-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw file-blocking-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
