# update tag

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update tag color/comments — update tag <name> color <color> [comments <text>]

## Usage

```
update tag [--remote]
```

## Examples

Run via SCM API:
```
arc > update tag
```

Run directly on device via SSH:
```
arc:fw-01 > update tag --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update tag
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
