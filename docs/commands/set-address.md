# set address

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an address object — set address <name> ip-netmask|fqdn|ip-range <value>

## Usage

```
set address [--remote]
```

## Examples

Run via SCM API:
```
arc > set address
```

Run directly on device via SSH:
```
arc:fw-01 > set address --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set address
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
