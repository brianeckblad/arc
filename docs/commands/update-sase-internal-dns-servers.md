---
command: "update sase internal-dns-servers"
description: "Update an internal DNS server"
category: sase
scope: global
---

# update sase internal-dns-servers

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an internal DNS server

## Usage

```
update sase internal-dns-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase internal-dns-servers
```

Run directly on device via SSH:
```
arc:fw-01 > update sase internal-dns-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase internal-dns-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
