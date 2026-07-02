---
command: "show ngts certs contents id"
description: "Download a certificate"
category: ngts
scope: global
---

# show ngts certs contents id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Download a certificate

## Usage

```
show ngts certs contents id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts certs contents id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts certs contents id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts certs contents id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
