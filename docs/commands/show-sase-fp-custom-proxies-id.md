---
command: "show sase fp-custom-proxies id"
description: "Get a GlobalProtect regional and custom proxy"
category: sase
scope: global
---

# show sase fp-custom-proxies id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a GlobalProtect regional and custom proxy

## Usage

```
show sase fp-custom-proxies id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-custom-proxies id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-custom-proxies id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-custom-proxies id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
