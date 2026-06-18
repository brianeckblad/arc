# update address

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update address — update address <name> ip-netmask|fqdn|ip-range|ip-wildcard|description|tag <value>

## Usage

```
update address [--remote]
```

## Examples

Run via SCM API:
```
arc > update address
```

Run directly on device via SSH:
```
arc:fw-01 > update address --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update address
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
