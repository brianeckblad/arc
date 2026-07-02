---
command: "show cngfw syslog-server-profiles id"
description: "Get a syslog server profile"
category: cloudngfw
scope: global
---

# show cngfw syslog-server-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a syslog server profile

## Usage

```
show cngfw syslog-server-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw syslog-server-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw syslog-server-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw syslog-server-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
