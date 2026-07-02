---
command: "set sase internal-dns-servers"
description: "Create a internal DNS server"
category: sase
scope: global
---

# set sase internal-dns-servers

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a internal DNS server

## Usage

```
set sase internal-dns-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase internal-dns-servers
```

Run directly on device via SSH:
```
arc:fw-01 > set sase internal-dns-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase internal-dns-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
