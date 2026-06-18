# delete dns-proxy

Delete a **dns-proxy** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`dns_proxy`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete dns-proxy <name>
```

## API

```
DELETE /config/network/v1/dns-proxies/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete dns-proxy MyObject
  ✓ Dns-Proxy MyObject deleted.
```

## Related commands

- `show dns-proxy` — list dns-proxy objects (to confirm name)
- `set dns-proxy <name>` — create a dns-proxy object

---
*Generated stub.*
