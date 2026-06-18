# CommandDef Quick Reference

**Instead of reading `app/commands/base.py`, use this table.**

Every command lives in one of the domain modules' `COMMANDS` dict and has a `CommandDef` descriptor. This table shows every field.

| Field | Type | Required | Common values | Notes |
|-------|------|----------|----------------|-------|
| `description` | `str` | ✓ | "Show things" | One-line help text shown in `?` output |
| `category` | `str` | ✓ | `'objects'`, `'network'`, `'security'`, `'setup'`, `'operations'` | Grouping for help output |
| `scope` | `str` | ✓ | `'folder'` (default), `'device'`, `'global'` | Context requirement — see "Scope Rules" below |
| `api_handler` | callable | ✓ | `_show_thing` | Private module-level function: `(ctx: ExecutionContext, args: dict) -> Any`. Called for API mode. |
| `ssh_command` | `str` or callable | optional | `'show thing'`, `_ssh_ping_host` | Static string or function that returns PAN-OS command. `None` = API-only (config commands). |
| `render` | `str` | required | `'list'`, `'dict'`, `'raw'`, `'interfaces'`, etc. | Key into `ArcShell._render()` dispatch. See `docs/RENDER_CATALOG.md` |
| `feature_flag` | `str` | optional (default: `""`) | `'nat_rules'`, `'decryption_policy'` | Empty string = always enabled. When present, command hidden & blocked until flag is True in `app/features.py`. |

## Scope Rules (Every CommandDef Must Declare)

| `scope=` | Meaning | Example | Guards |
|----------|---------|---------|--------|
| `"folder"` (most common) | Config stored in SCM at folder/snippet level; handler passes `folder=ctx.folder` to SCM. | `show address`, `show interface`, `show security-policy` | `require_scm(ctx)` + active folder is passed to API |
| `"device"` | Live operational state; requires `cd <device>` first. | `show log`, `ping <host>`, `show system info` | `require_device(ctx)` + can use `--remote` flag |
| `"global"` | TSG-wide data; no folder/device filter. | `show devices`, `show jobs all`, `commit` | `require_scm(ctx)` only |

## Template

```python
from app.commands.base import CommandDef, ExecutionContext, require_scm, require_device

def _my_handler(ctx: ExecutionContext, args: dict) -> Any:
    """Brief docstring: what this command does."""
    scm = require_scm(ctx)
    # ... handler implementation
    return result

COMMANDS: dict[str, CommandDef] = {
    'show my resource': CommandDef(
        description='Show my resource',
        category='objects',       # or 'network', 'security', 'setup', 'operations'
        scope='folder',           # or 'device', 'global'
        api_handler=_my_handler,
        ssh_command='show my resource',   # or None, or a Callable
        render='list',            # See docs/RENDER_CATALOG.md
    ),
}
```

## Handler Signature

Every `api_handler` receives:

```python
def _handler(ctx: ExecutionContext, args: dict) -> Any:
    """
    ctx.scm          — SCMClient instance (if configured)
    ctx.ssh          — SSHManager instance
    ctx.device       — dict: current device record (if scope='device')
    ctx.folder       — str: active folder name (default: 'Shared')
    ctx.target       — str: device serial (shorthand for ctx.device['serial'])
    ctx.device_host  — str: IP/hostname for SSH (shorthand)
    ctx.config       — ArcConfig instance
    ctx.tsg_id       — str: current TSG ID
    
    args             — dict: remaining tokens after command prefix
                       e.g., 'show thing <name>' -> args = {'name': <value>}
    """
    return data_for_rendering
```

## SSH Command Signature (if callable)

When `ssh_command` is a function instead of a string:

```python
def _ssh_ping(args: dict) -> str:
    """Return the PAN-OS SSH command string for dynamic args."""
    host = args.get('host')
    if not host:
        raise ValueError("Usage: ping host <IP>")
    return f"ping host {host}"
```

---

**See also:**
- `docs/COMMAND_PATTERNS.md` — copy a minimal working example
- `docs/RENDER_CATALOG.md` — pick a render= key
- `app/commands/base.py` — full definitions (50 lines)

