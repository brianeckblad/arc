---
command: "show ngts cert-instances id"
description: "Get a certificate installation details"
category: ngts
scope: global
---

# show ngts cert-instances id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a certificate installation details

## Usage

```
show ngts cert-instances id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-instances id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-instances id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-instances id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
