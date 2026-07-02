---
command: "show dns-proxies id"
description: "Get a DNS proxy"
category: network
scope: global
---

# show dns-proxies id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a DNS proxy

## Usage

```
show dns-proxies id [--remote]
```

## Examples

Run via SCM API:
```
arc > show dns-proxies id
```

Run directly on device via SSH:
```
arc:fw-01 > show dns-proxies id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show dns-proxies id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
