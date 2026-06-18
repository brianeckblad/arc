# set address-group

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a static address group — set address-group <name> static <member1> ...

## Usage

```
set address-group [--remote]
```

## Examples

Run via SCM API:
```
arc > set address-group
```

Run directly on device via SSH:
```
arc:fw-01 > set address-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set address-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
