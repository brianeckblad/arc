---
command: "show ngts cert-requests id"
description: "Get a certificate request details"
category: ngts
scope: global
---

# show ngts cert-requests id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a certificate request details

## Usage

```
show ngts cert-requests id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-requests id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-requests id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-requests id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
