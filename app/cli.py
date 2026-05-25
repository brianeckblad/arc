"""ARC entry point — bootstraps config and starts the interactive shell."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from app.api.client import SCMClient
from app.config import load_config, save_config, CONFIG_FILE
from app.docs import (
    COMMAND_DOCS_ROOT,
    COMMANDS,
    DOCS_ROOT,
    open_docs_in_browser,
    slugify,
)
from app.shell import ArcShell

app = typer.Typer(
    name="arc",
    help=(
        "ARC — Assisted Remote Console. "
        "A PAN-OS-style interactive shell for Palo Alto Networks SCM environments."
    ),
    no_args_is_help=False,
    add_completion=False,
)

console = Console()


# ---------------------------------------------------------------------------
# Default command — launch the interactive shell
# ---------------------------------------------------------------------------

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable verbose debug output."),
) -> None:
    """Launch the ARC interactive shell."""
    if ctx.invoked_subcommand is not None:
        return

    cfg = load_config()
    if debug:
        cfg.debug = True

    shell = ArcShell(cfg)
    shell.run()


@app.command("docs")
def open_docs(
    topic: Optional[str] = typer.Argument(None, help="Command or topic to open directly."),
) -> None:
    """Open ARC documentation in the default browser (pan.dev-style portal)."""
    url = open_docs_in_browser(topic or "")
    console.print(f"[green]Docs opened:[/green] {url}")


# ---------------------------------------------------------------------------
# auth sub-command
# ---------------------------------------------------------------------------

auth_app = typer.Typer(help="Manage ARC credentials.")
app.add_typer(auth_app, name="auth")


@auth_app.command("login")
def auth_login(
    scm_bearer_token: Optional[str] = typer.Option(None, "--scm-bearer-token"),
    scm_client_id: Optional[str] = typer.Option(None, "--scm-client-id"),
    scm_secret: Optional[str] = typer.Option(None, "--scm-client-secret"),
    scm_tsg: Optional[str] = typer.Option(None, "--scm-tsg-id"),
    ssh_user: Optional[str] = typer.Option(None, "--ssh-user"),
    ssh_key: Optional[str] = typer.Option(None, "--ssh-key"),
) -> None:
    """Interactively configure ARC credentials and save to ~/.arc/config.json."""
    cfg = load_config()

    console.print("[bold cyan]ARC Credential Setup[/bold cyan]")
    console.print(f"Config will be saved to: [dim]{CONFIG_FILE}[/dim]\n")

    def _prompt(label: str, current: str, secret: bool = False) -> str:
        placeholder = "****" if (secret and current) else (current or "")
        hint = f" [[dim]{placeholder}[/dim]]" if placeholder else ""
        console.print(f"  {label}{hint}: ", end="")
        try:
            val = input()
        except (EOFError, KeyboardInterrupt):
            val = ""
        return val.strip() or current

    # SCM
    console.print("[yellow]─ Strata Cloud Manager ─[/yellow]")
    cfg.scm.bearer_token = scm_bearer_token or _prompt(
        "Bearer Token (leave blank to use client credentials)",
        cfg.scm.bearer_token,
        secret=True,
    )
    cfg.scm.client_id = scm_client_id or _prompt("Client ID", cfg.scm.client_id)
    cfg.scm.client_secret = scm_secret or _prompt("Client Secret", cfg.scm.client_secret, secret=True)
    cfg.scm.tsg_id = scm_tsg or _prompt("TSG ID", cfg.scm.tsg_id)

    # SSH
    console.print("\n[yellow]─ SSH Defaults ─[/yellow]")
    cfg.ssh.user = ssh_user or _prompt("SSH Username", cfg.ssh.user)
    cfg.ssh.key_path = ssh_key or _prompt("SSH Key Path", cfg.ssh.key_path)

    save_config(cfg)
    console.print(f"\n[green]✓[/green] Saved to [bold]{CONFIG_FILE}[/bold]")


@auth_app.command("show")
def auth_show() -> None:
    """Display current configuration (credentials masked)."""
    cfg = load_config()

    def _mask(s: str) -> str:
        return ("*" * 8) if s else "[dim](not set)[/dim]"

    console.print("\n[bold cyan]SCM[/bold cyan]")
    console.print(f"  bearer_token:  {_mask(cfg.scm.bearer_token)}")
    console.print(f"  client_id:     {cfg.scm.client_id or '[dim](not set)[/dim]'}")
    console.print(f"  client_secret: {_mask(cfg.scm.client_secret)}")
    console.print(f"  tsg_id:        {cfg.scm.tsg_id or '[dim](not set)[/dim]'}")

    console.print("\n[bold cyan]SSH[/bold cyan]")
    console.print(f"  user:    {cfg.ssh.user}")
    console.print(f"  key:     {cfg.ssh.key_path or '[dim](not set)[/dim]'}")
    console.print(f"  port:    {cfg.ssh.port}")

    console.print(f"\n[bold cyan]Config file:[/bold cyan] {CONFIG_FILE}")
    console.print()


# ---------------------------------------------------------------------------
# cliup — sync docs with registered commands
# ---------------------------------------------------------------------------

_COMMAND_STUB_TEMPLATE = """\
# {key}

**Category:** {category}
**API mode:** {api_note}
**SSH mode:** {ssh_note}

## Description

{description}

## Usage

```
{key}{usage_args}
```

## Examples

Run via SCM API:
```
arc > {key}
```

Run directly on device via SSH:
```
arc:fw-01 > {key} --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > {key}
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
"""


def _build_stub(key: str, cmd) -> str:
    """Build a Markdown stub for a new command doc."""
    from app.commands.registry import CommandDef

    if cmd.api_handler is not None:
        fn_name = getattr(cmd.api_handler, "__name__", "")
        api_note = (
            "Translation pending — use `--remote` for live device output."
            if fn_name.startswith("_pending")
            else "✓ Live SCM data"
        )
    else:
        api_note = "Not available"

    if cmd.ssh_command is not None:
        ssh_cmd = cmd.ssh_command if isinstance(cmd.ssh_command, str) else "(dynamic)"
        ssh_note = f"`{ssh_cmd}`"
    else:
        ssh_note = "Not applicable (config read from SCM)"

    has_args = any(c in key for c in ("<", "["))
    usage_args = "" if has_args else " [--remote]"

    return _COMMAND_STUB_TEMPLATE.format(
        key=key,
        category=cmd.category,
        description=cmd.description,
        api_note=api_note,
        ssh_note=ssh_note,
        usage_args=usage_args,
    )


def _regenerate_index() -> None:
    """Rewrite docs/commands/index.md from the live COMMANDS registry."""
    lines = [
        "# Command Reference\n",
        "\n",
        "Use `help <command>` to open detailed docs for a command.\n",
        "\n",
    ]
    for key in sorted(COMMANDS):
        desc = COMMANDS[key].description
        lines.append(f"- `{key}` — {desc}\n")
    index_path = COMMAND_DOCS_ROOT / "index.md"
    index_path.write_text("".join(lines), encoding="utf-8")


@app.command("cliup")
def cliup() -> None:
    """Sync docs/commands/ with the registered command registry.

    For every command in COMMANDS:
    - Creates a Markdown stub in docs/commands/ if one is missing.
    - Leaves existing docs untouched.
    - Regenerates docs/commands/index.md from the live registry.

    Run this after adding a new command to the registry to scaffold its doc page.
    """
    COMMAND_DOCS_ROOT.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    existing: list[str] = []

    for key, cmd in COMMANDS.items():
        slug = slugify(key)
        doc_file = COMMAND_DOCS_ROOT / f"{slug}.md"
        if doc_file.exists():
            existing.append(key)
        else:
            stub = _build_stub(key, cmd)
            doc_file.write_text(stub, encoding="utf-8")
            created.append(key)

    _regenerate_index()

    total = len(COMMANDS)
    console.print(
        f"\n[bold cyan]cliup[/bold cyan] — {total} registered commands\n"
        f"  [green]created:[/green]  {len(created)}\n"
        f"  [dim]existing:[/dim] {len(existing)}\n"
        f"  [cyan]index:[/cyan]    docs/commands/index.md regenerated\n"
    )
    for key in created:
        slug = slugify(key)
        console.print(f"  [green]+[/green] docs/commands/{slug}.md")
    if not created:
        console.print("  [dim]All command docs are up to date.[/dim]")
    console.print()


# ---------------------------------------------------------------------------
# scm sub-command — raw SCM API passthrough
# ---------------------------------------------------------------------------

scm_app = typer.Typer(help="Raw SCM API passthrough.")
app.add_typer(scm_app, name="scm")


@scm_app.command("get")
def scm_get(
    path: str = typer.Argument(..., help="API path, e.g. /sse/config/v1/addresses"),
    folder: str = typer.Option("Shared", "--folder", "-f"),
) -> None:
    """Perform a raw GET request against the SCM API."""
    cfg = load_config()
    if not cfg.scm.is_configured:
        console.print("[red]SCM is not configured.[/red] Run [bold]arc auth login[/bold].")
        raise typer.Exit(1)

    client = SCMClient(cfg.scm)
    data = client.get(path, params={"folder": folder})
    console.print_json(json.dumps(data, indent=2))


# ---------------------------------------------------------------------------
# Entry-point called by run.py and the 'arc' console_script
# ---------------------------------------------------------------------------

def run() -> None:
    app()


if __name__ == "__main__":
    run()

