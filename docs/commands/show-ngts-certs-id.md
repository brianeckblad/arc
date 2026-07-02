---
command: "show ngts certs id"
description: "Get a certificate details"
category: ngts
scope: global
---

# show ngts certs id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a certificate details

## Usage

```
show ngts certs id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts certs id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts certs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts certs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
