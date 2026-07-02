---
command: "show sase internal-dns-servers id"
description: "Get an internal DNS server"
category: sase
scope: global
---

# show sase internal-dns-servers id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an internal DNS server

## Usage

```
show sase internal-dns-servers id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase internal-dns-servers id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase internal-dns-servers id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase internal-dns-servers id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
