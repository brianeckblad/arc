---
command: "set ngts cert-request-search"
description: "Get the details of certificate requests"
category: ngts
scope: global
---

# set ngts cert-request-search

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of certificate requests

## Usage

```
set ngts cert-request-search [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-request-search
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-request-search --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-request-search
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
