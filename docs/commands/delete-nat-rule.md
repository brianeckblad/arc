---
command: "delete nat-rule"
description: "Delete a NAT rule — delete nat-rule <name>"
feature_flag: nat_rules
category: network
scope: folder
---

---
command: "delete nat-rule"
description: "Delete a NAT rule — delete nat-rule <name>"
feature_flag: nat_rules
category: network
scope: folder
---

# delete nat-rule

Delete a **nat-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`create_nat_rule`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete nat-rule <name>
```

## API

```
DELETE /config/network/v1/nat-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete nat-rule MyObject
  ✓ Nat-Rule MyObject deleted.
```

## Related commands

- `show nat-rule` — list nat-rule objects (to confirm name)
- `set nat-rule <name>` — create a nat-rule object

---
*Generated stub.*
