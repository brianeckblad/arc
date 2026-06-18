# show dhcp-interface

List **dhcp-interface** objects in the active SCM folder.

## Feature flag

This command requires **`dhcp`** to be enabled:

```bash
arc> feature enable dhcp
```

## Syntax

```text
show dhcp-interface
show dhcp-interface --remote    # live device state via SSH
```

## API

```
GET /config/network/v1/dhcp-interfaces?folder=<active-folder>
```

Notes: DHCP server or relay on an interface

## Output

Returns a table of dhcp-interface objects with key fields.

## Example

```text
arc:global > feature enable dhcp
arc:global > show dhcp-interface
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set dhcp-interface <name>` — create a dhcp-interface object
- `delete dhcp-interface <name>` — remove a dhcp-interface object
- `help features` — manage feature flags

---
*Generated stub.*
