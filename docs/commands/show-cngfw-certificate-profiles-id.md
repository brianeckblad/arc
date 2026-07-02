---
command: "show cngfw certificate-profiles id"
description: "Get a certificate profile"
category: cloudngfw
scope: global
---

# show cngfw certificate-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a certificate profile

## Usage

```
show cngfw certificate-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw certificate-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw certificate-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw certificate-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
