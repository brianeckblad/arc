# Command Patterns — Minimal Working Examples

Copy and adapt one of these minimal patterns when adding a new command.

---

## Pattern 1: List objects (folder-scoped) — use the factory

A plain "list everything in the active folder" command needs **no handler
function** — `show_handler()` from `app/commands/base.py` builds it:

```python
# In app/commands/objects.py (or whichever module)
COMMANDS: dict[str, CommandDef] = {
    ...
    'show thing': CommandDef(
        description='Show things',
        category='objects',       # matches module domain
        scope='folder',           # scoped to active folder
        api_handler=show_handler('get_things'),        # calls scm.get_things(folder=ctx.folder)
        ssh_command='show objects thing',  # PAN-OS equivalent
        render='list',            # generic table
    ),
}
# TSG-wide list (no folder param): show_handler('get_devices', folder_scoped=False)
```

Write a hand-rolled `def _show_thing(ctx, args)` only when there is extra
logic (client-side filtering, multiple calls, post-processing).

**Docs:** optional — `help show thing` is synthesized from the CommandDef.
Add `docs/commands/show-thing.md` only when you have more to say.

**Smoke:** `python dev/smoke_test.py --only 1,2,3`

---

## Pattern 2: Show single object with detail (folder-scoped)

```python
def _show_thing_detail(ctx: ExecutionContext, args: dict) -> Any:
    """Show detail for one thing by name."""
    scm = require_scm(ctx)
    name = args.get('name')
    if not name:
        raise ValueError("Usage: show thing <name>")
    things = scm.get_things(folder=ctx.folder)
    # Client-side filter
    match = next((t for t in things if t.get('name') == name), None)
    if not match:
        raise ValueError(f"Thing '{name}' not found in folder {ctx.folder}")
    return match

COMMANDS: dict[str, CommandDef] = {
    ...
    'show thing': CommandDef(
        description='Show thing detail by name',
        category='objects',
        scope='folder',
        api_handler=_show_thing_detail,
        ssh_command='show objects thing',
        render='dict',            # key/value detail
    ),
}
```

---

## Pattern 3: Create object (config mode, folder-scoped)

```python
def _create_thing(ctx: ExecutionContext, args: dict) -> Any:
    """Create a new thing."""
    scm = require_scm(ctx)
    name = args.get('name')
    value = args.get('value')
    if not name or not value:
        raise ValueError("Usage: create thing <name> <value>")
    # POST to SCM
    return scm.post(
        f"/config/objects/v1/things",
        json={"name": name, "value": value},
        params={"folder": ctx.folder},
    )

COMMANDS: dict[str, CommandDef] = {
    ...
    'create thing': CommandDef(
        description='Create a thing',
        category='objects',
        scope='folder',
        api_handler=_create_thing,
        ssh_command=None,         # config-only; no SSH equivalent
        render='dict',
    ),
}
```

**Guard in shell:** Blocked automatically unless in configure mode (checked before handler runs)

---

## Pattern 3b: Delete by name — use the factory

The standard "list → find id by name → DELETE" sequence is also factory-built:

```python
'delete thing': CommandDef(
    description='Delete a thing by name',
    category='objects',
    scope='folder',
    api_handler=delete_handler(
        'Thing', 'get_things', 'delete_thing',
        usage='Usage: delete thing <name>',
    ),
    ssh_command=None,
    render='raw',
),
```

---

## Pattern 4: Live device command (SSH --remote)

```python
def _show_logs(ctx: ExecutionContext, args: dict) -> Any:
    """Show system logs from the active device."""
    device = require_device(ctx)  # Enforces: device must be set
    # SSH execution happens in shell.py via --remote flag
    # This handler is only called in API mode as fallback
    raise RuntimeError(
        "System logs require live device access. "
        "Use: show log system --remote"
    )

COMMANDS: dict[str, CommandDef] = {
    ...
    'show log system': CommandDef(
        description='Show system logs',
        category='operations',
        scope='device',           # requires cd <device>
        api_handler=_show_logs,   # API fallback (shows helpful error)
        ssh_command='show log system',  # Actual command run on device
        render='raw',             # unstructured log output
    ),
}
```

---

## Pattern 5: Global (TSG-wide) command

```python
def _show_all_jobs(ctx: ExecutionContext, args: dict) -> Any:
    """Show all SCM jobs regardless of folder."""
    scm = require_scm(ctx)
    # No folder param: returns TSG-wide jobs
    return scm.get_jobs()

COMMANDS: dict[str, CommandDef] = {
    ...
    'show jobs all': CommandDef(
        description='Show all jobs',
        category='operations',
        scope='global',           # no folder/device filter
        api_handler=_show_all_jobs,
        ssh_command='show jobs processed',
        render='jobs',
    ),
}
```

---

## Patterns Summary

| Pattern | Scope | Requires | Render | Use for |
|---------|-------|----------|--------|---------|
| List objects | `folder` | `require_scm()` | `list` | `show X` |
| Detail | `folder` | `require_scm()` | `dict` | `show X <name>` |
| Create | `folder` | config mode + `require_scm()` | `dict` | `create X` |
| Delete | `folder` | config mode + `require_scm()` | `raw` | `delete X` |
| Live device | `device` | `require_device()` + SSH | `raw` | `show log`, `ping`, live state |
| TSG-wide | `global` | `require_scm()` | varies | `show jobs`, `commit`, `show devices` |

---

**See also:**
- `docs/RENDER_CATALOG.md` — available render= keys
- `app/commands/base.py` — CommandDef field reference
- `dev/API_INDEX.md` — find endpoints for your resource

