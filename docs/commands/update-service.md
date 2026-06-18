# update service

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update service — update service <name> tcp|udp port <n> [source-port <n>]

## Usage

```
update service [--remote]
```

## Examples

Run via SCM API:
```
arc > update service
```

Run directly on device via SSH:
```
arc:fw-01 > update service --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update service
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
