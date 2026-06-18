# delete address

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an address object — delete address <name>

## Usage

```
delete address [--remote]
```

## Examples

Run via SCM API:
```
arc > delete address
```

Run directly on device via SSH:
```
arc:fw-01 > delete address --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete address
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
