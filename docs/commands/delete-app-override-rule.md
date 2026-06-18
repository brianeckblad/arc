# delete app-override-rule

Delete a **app-override-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`app_override`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete app-override-rule <name>
```

## API

```
DELETE /config/security/v1/app-override-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete app-override-rule MyObject
  ✓ App-Override-Rule MyObject deleted.
```

## Related commands

- `show app-override-rule` — list app-override-rule objects (to confirm name)
- `set app-override-rule <name>` — create a app-override-rule object

---
*Generated stub.*
