---
command: "update dns-proxies"
description: "Update a DNS proxy"
category: network
scope: global
---

# update dns-proxies

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a DNS proxy

## Usage

```
update dns-proxies [--remote]
```

## Examples

Run via SCM API:
```
arc > update dns-proxies
```

Run directly on device via SSH:
```
arc:fw-01 > update dns-proxies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update dns-proxies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
