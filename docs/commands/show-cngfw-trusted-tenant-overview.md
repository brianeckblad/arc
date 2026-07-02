---
command: "show cngfw trusted-tenant-overview"
description: "Trusted Tenants Overview"
category: cloudngfw
scope: global
---

# show cngfw trusted-tenant-overview

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Trusted Tenants Overview

## Usage

```
show cngfw trusted-tenant-overview [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw trusted-tenant-overview
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw trusted-tenant-overview --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw trusted-tenant-overview
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
