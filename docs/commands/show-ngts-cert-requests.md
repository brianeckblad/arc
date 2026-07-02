---
command: "show ngts cert-requests"
description: "Get the details of all certificate"
category: ngts
scope: global
---

# show ngts cert-requests

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of all certificate

## Usage

```
show ngts cert-requests [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-requests
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-requests --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-requests
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
