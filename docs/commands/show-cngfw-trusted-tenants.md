---
command: "show cngfw trusted-tenants"
description: "Trusted Tenants With Snippets"
category: cloudngfw
scope: global
---

# show cngfw trusted-tenants

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Trusted Tenants With Snippets

## Usage

```
show cngfw trusted-tenants [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw trusted-tenants
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw trusted-tenants --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw trusted-tenants
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
