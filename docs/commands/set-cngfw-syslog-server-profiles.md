---
command: "set cngfw syslog-server-profiles"
description: "Create a syslog server profile"
category: cloudngfw
scope: global
---

# set cngfw syslog-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a syslog server profile

## Usage

```
set cngfw syslog-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw syslog-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw syslog-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw syslog-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
