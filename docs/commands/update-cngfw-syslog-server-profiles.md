---
command: "update cngfw syslog-server-profiles"
description: "Update a syslog server profile"
category: cloudngfw
scope: global
---

# update cngfw syslog-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a syslog server profile

## Usage

```
update cngfw syslog-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw syslog-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw syslog-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw syslog-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
