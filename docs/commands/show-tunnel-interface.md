# show tunnel-interface

List **tunnel-interface** objects in the active SCM folder.

## Feature flag

This command requires **`ipsec_vpn`** to be enabled:

```bash
arc> feature enable ipsec_vpn
```

## Syntax

```text
show tunnel-interface
show tunnel-interface --remote    # live device state via SSH
```

## API

```
GET /config/network/v1/tunnel-interfaces?folder=<active-folder>
```

Notes: IPsec/GRE tunnel interface

## Output

Returns a table of tunnel-interface objects with key fields.

## Example

```text
arc:global > feature enable ipsec_vpn
arc:global > show tunnel-interface
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set tunnel-interface <name>` — create a tunnel-interface object
- `delete tunnel-interface <name>` — remove a tunnel-interface object
- `help features` — manage feature flags

---
*Generated stub.*
