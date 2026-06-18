# show decryption-exclusion

List **decryption-exclusion** objects in the active SCM folder.

## Feature flag

This command requires **`decryption_policy`** to be enabled:

```bash
arc> feature enable decryption_policy
```

## Syntax

```text
show decryption-exclusion
show decryption-exclusion --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/decryption-exclusions?folder=<active-folder>
```

Notes: hosts excluded from SSL decryption

## Output

Returns a table of decryption-exclusion objects with key fields.

## Example

```text
arc:global > feature enable decryption_policy
arc:global > show decryption-exclusion
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set decryption-exclusion <name>` — create a decryption-exclusion object
- `delete decryption-exclusion <name>` — remove a decryption-exclusion object
- `help features` — manage feature flags

---
*Generated stub.*
