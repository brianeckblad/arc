# Command Visibility (commands.json)

## Overview

The `settings/commands.json` file provides fine-grained control over individual command visibility. This is **independent of feature flags** (its settings/features/ file).

## Purpose

- **Feature flags** (`its settings/features/ file`): Enable/disable entire functional areas (e.g., "nat_rules", "delete_objects")
- **Command visibility** (`settings/commands.json`): Hide/show specific individual commands

## Use Cases

1. **Deprecate commands** without removing code
2. **Hide experimental commands** from general users
3. **Customize shell** per deployment/environment
4. **Gradually phase out** old command names

## File Format

```json
{
  "_README": "Command visibility control...",
  "cd": true,
  "pwd": true,
  "show devices": true,
  "show old-command": false,
  "_example_1": "Comments start with underscore"
}
```

## Behavior

- **Not listed**: Command visible by default
- **Set to `true`**: Explicitly visible
- **Set to `false`**: Hidden from help and blocked from execution
- **Keys with `_` prefix**: Ignored (comments/metadata)

## Enforcement

Commands hidden in `commands.json`:
1. Do not appear in `?` help output
2. Do not appear in tab completion
3. Are blocked from execution with an error message

## Priority Order

When a command is evaluated:
1. Check `commands.json` visibility (if false, hide regardless of features)
2. Check device/configure mode requirements
3. Check feature flag (from `its settings/features/ file`)

## Examples

### Hide a specific command

```json
{
  "show old-api-endpoint": false
}
```

### Deprecation workflow

1. Add to `commands.json` with `false`
2. Test that command is properly hidden
3. After sufficient time, remove code from registry
4. Remove entry from `commands.json`

## Related

- `its settings/features/ file` — functional area feature flags
- `help features` — feature flag system documentation
- `app/settings/commands.py` — visibility loader implementation
