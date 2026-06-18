# show vlan-interface

List **vlan-interface** objects in the active SCM folder.

## Feature flag

This command requires **`show_interface`** to be enabled:

```bash
arc> feature enable show_interface
```

## Syntax

```text
show vlan-interface
show vlan-interface --remote    # live device state via SSH
```

## API

```
GET /config/network/v1/vlan-interfaces?folder=<active-folder>
```

Notes: VLAN (layer 3 sub-interface)

## Output

Returns a table of vlan-interface objects with key fields.

## Example

```text
arc:global > feature enable show_interface
arc:global > show vlan-interface
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set vlan-interface <name>` — create a vlan-interface object
- `delete vlan-interface <name>` — remove a vlan-interface object
- `help features` — manage feature flags

---
*Generated stub.*
