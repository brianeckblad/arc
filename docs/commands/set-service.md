# set service

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a service object — set service <name> tcp|udp port <n>

## Usage

```
set service [--remote]
```

## Examples

Run via SCM API:
```
arc > set service
```

Run directly on device via SSH:
```
arc:fw-01 > set service --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set service
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
