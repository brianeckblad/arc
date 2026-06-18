# delete authentication-rule

Delete a **authentication-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`authentication`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete authentication-rule <name>
```

## API

```
DELETE /config/identity/v1/authentication-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete authentication-rule MyObject
  ✓ Authentication-Rule MyObject deleted.
```

## Related commands

- `show authentication-rule` — list authentication-rule objects (to confirm name)
- `set authentication-rule <name>` — create a authentication-rule object

---
*Generated stub.*
