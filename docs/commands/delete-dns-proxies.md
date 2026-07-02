---
command: "delete dns-proxies"
description: "Delete a DNS proxy"
category: network
scope: global
---

# delete dns-proxies

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a DNS proxy

## Usage

```
delete dns-proxies [--remote]
```

## Examples

Run via SCM API:
```
arc > delete dns-proxies
```

Run directly on device via SSH:
```
arc:fw-01 > delete dns-proxies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete dns-proxies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
