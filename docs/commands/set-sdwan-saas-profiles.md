---
command: "set sdwan-saas-profiles"
description: "Create an SD-WAN SaaS quality profile"
category: network
scope: global
---

# set sdwan-saas-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an SD-WAN SaaS quality profile

## Usage

```
set sdwan-saas-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set sdwan-saas-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set sdwan-saas-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sdwan-saas-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
