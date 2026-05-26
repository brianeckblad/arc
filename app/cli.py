"""ARC entry point — bootstraps config and starts the interactive shell."""

from __future__ import annotations

import json
import stat
from typing import Optional

import httpx

import typer
from rich.console import Console

from app.api.client import SCMClient
from app.config import (
    clear_keychain,
    keychain_available,
    load_config,
    save_config,
    CONFIG_DIR,
    CONFIG_FILE,
)
from app.docs import (
    COMMAND_DOCS_ROOT,
    COMMANDS,
    DOCS_ROOT,
    open_docs_in_browser,
    render_help_topic,
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

    # --- Auto-sync docs on every launch (silent, local-only — no network) ---
    # Keeps command stubs and the docs bundle up to date without a manual
    # `arc cliup` run during development.  Change `silent=True` to `False`
    # here to see verbose output, or remove the call once the project matures.
    _do_cliup(silent=True, skip_vendor=True)


    cfg = load_config()
    if debug:
        cfg.debug = True

    shell = ArcShell(cfg)
    shell.run()


@app.command("docs")
def open_docs(
    topic: Optional[str] = typer.Argument(None, help="Command or topic to open directly."),
) -> None:
    """Open ARC documentation in the default browser (fully offline, no server)."""
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
    """Interactively configure ARC credentials.

    Secrets (bearer token, client secret, SSH password) are stored in the OS
    keychain (macOS Keychain / Linux Secret Service / Windows Credential
    Manager).  Non-sensitive values are saved to the config file.
    """
    cfg = load_config()
    kc = keychain_available()

    console.print("[bold cyan]ARC Credential Setup[/bold cyan]")
    if kc:
        console.print(
            f"  Secrets  → [green]OS keychain[/green]  (bearer token, client secret, SSH password)\n"
            f"  Config   → [dim]{CONFIG_FILE}[/dim]  (client_id, tsg_id, SSH user/key/port)\n"
        )
    else:
        console.print(
            f"  [yellow]⚠  OS keychain unavailable — secrets will be stored in {CONFIG_FILE}[/yellow]\n"
            "  Consider setting SCM_BEARER_TOKEN / SCM_CLIENT_SECRET as env vars instead.\n"
        )

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

    if kc:
        console.print(
            f"\n[green]✓[/green] Secrets saved to OS keychain\n"
            f"[green]✓[/green] Config file: [bold]{CONFIG_FILE}[/bold]  [dim](mode 0600)[/dim]"
        )
    else:
        console.print(f"\n[green]✓[/green] Saved to [bold]{CONFIG_FILE}[/bold]  [dim](mode 0600)[/dim]")


@auth_app.command("show")
def auth_show() -> None:
    """Display current configuration (credentials masked)."""
    cfg = load_config()
    kc = keychain_available()

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
    if kc:
        console.print("[bold cyan]Keychain:[/bold cyan] [green]available[/green]  (secrets stored in OS keychain)")
    else:
        console.print(
            "[bold cyan]Keychain:[/bold cyan] [yellow]unavailable[/yellow]  "
            "— secrets fall back to config file or env vars"
        )
    console.print()


@auth_app.command("clear")
def auth_clear() -> None:
    """Remove all ARC secrets from the OS keychain.

    This does not delete the config file.  Non-sensitive values (client_id,
    tsg_id, SSH user/key/port) are preserved.  Run ``arc auth login`` to
    re-enter credentials afterward.
    """
    clear_keychain()
    console.print("[green]✓[/green] ARC secrets removed from OS keychain.")
    console.print(
        f"  Config file [dim]{CONFIG_FILE}[/dim] unchanged  "
        "(run [bold]arc auth login[/bold] to re-enter credentials)"
    )


# ---------------------------------------------------------------------------
# config sub-command
# ---------------------------------------------------------------------------

config_app = typer.Typer(help="Manage the ARC config file.")
app.add_typer(config_app, name="config")

# Template written by `arc config generate`.
# _note fields are ignored by load_config() — they document the file for humans.
_CONFIG_TEMPLATE = {
    "_note": (
        "ARC config — fill in the REPLACE_WITH_* values then run: arc auth login  "
        "(secrets are moved to the OS keychain by that command)"
    ),
    "scm": {
        "_note": (
            "Use bearer_token OR the three OAuth fields (client_id + client_secret + tsg_id), "
            "not both.  Leave bearer_token blank to use OAuth."
        ),
        "bearer_token": "",
        "client_id":    "REPLACE_WITH_SCM_CLIENT_ID",
        "client_secret": "REPLACE_WITH_SCM_CLIENT_SECRET",
        "tsg_id":       "REPLACE_WITH_SCM_TSG_ID",
    },
    "ssh": {
        "_note": (
            "SSH is used for --remote, remote <device>, and connect commands.  "
            "Prefer key_path over password — leave password blank if using a key."
        ),
        "user":     "admin",
        "key_path": "",
        "password": "",
        "port":     22,
    },
    "default_folder": "Shared",
}


@config_app.command("generate")
def config_generate(
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite an existing config file."),
) -> None:
    """Generate a starter config.json with annotated placeholders and mode 0600.

    Creates the config directory if needed, writes template values, and sets
    file permissions to 0600 (owner read/write only).  Secrets are left blank
    or as REPLACE_WITH_* placeholders — run ``arc auth login`` afterward to
    enter real values and migrate secrets to the OS keychain.
    """
    if CONFIG_FILE.exists() and not force:
        console.print(
            f"[yellow]Config file already exists:[/yellow] [bold]{CONFIG_FILE}[/bold]\n"
            "  Use [bold]--force[/bold] to overwrite, or [bold]arc auth show[/bold] "
            "to see current values."
        )
        raise typer.Exit(1)

    already_existed = CONFIG_FILE.exists()
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(_CONFIG_TEMPLATE, indent=2))
    CONFIG_FILE.chmod(stat.S_IRUSR | stat.S_IWUSR)

    action = "Overwrote" if already_existed else "Created"
    console.print(
        f"\n[green]✓[/green] {action} [bold]{CONFIG_FILE}[/bold]  [dim](mode 0600)[/dim]\n"
    )
    console.print(
        "[bold]Next steps:[/bold]\n"
        f"  1. Edit the file and replace [cyan]REPLACE_WITH_*[/cyan] values:\n"
        f"       [dim]{CONFIG_FILE}[/dim]\n"
        "  2. Run [bold]arc auth login[/bold] — migrates secrets to the OS keychain\n"
        "  3. Run [bold]arc auth show[/bold]  — confirm everything is configured\n\n"
        "  See [bold]help config osx[/bold] / [bold]help config win[/bold] / "
        "[bold]help config nix[/bold] for platform-specific keychain CLI commands."
    )


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

# Vendor JS/CSS files downloaded once to docs/vendor/ by cliup.
# All paths are CDN URLs; local filenames are the last path component.
_VENDOR_DIR = DOCS_ROOT / "vendor"
_VENDOR_FILES = [
    ("marked.min.js",        "https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js"),
    ("highlight.min.js",     "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"),
    ("github-dark.min.css",  "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css"),
    ("github.min.css",       "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css"),
]


def _ensure_vendor_files() -> list[str]:
    """Download vendor JS/CSS to docs/vendor/ if not already present.

    Uses httpx (already a project dependency).  Files already on disk are
    skipped so subsequent ``cliup`` runs are fully offline.
    Returns a list of filenames that were newly downloaded.
    """
    _VENDOR_DIR.mkdir(parents=True, exist_ok=True)
    downloaded: list[str] = []
    for filename, url in _VENDOR_FILES:
        dest = _VENDOR_DIR / filename
        if dest.exists():
            continue
        try:
            resp = httpx.get(url, follow_redirects=True, timeout=15)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            downloaded.append(filename)
        except Exception as exc:
            console.print(f"  [yellow]⚠[/yellow] Could not download {filename}: {exc}")
    return downloaded


def _build_docs_bundle() -> int:
    """Embed all docs/*.md files into docs/docs-bundle.js.

    The bundle sets ``window.DOCS_CONTENT`` to a plain JS object keyed by
    relative path (e.g. ``"commands/cd.md"``).  Loading it with a plain
    ``<script src="docs-bundle.js">`` tag works under ``file://`` — no server
    or fetch() required.

    Returns the number of Markdown files bundled.
    """
    pages: dict[str, str] = {}
    for md_path in sorted(DOCS_ROOT.rglob("*.md")):
        rel = md_path.relative_to(DOCS_ROOT).as_posix()
        pages[rel] = md_path.read_text(encoding="utf-8")

    js_entries = ",\n".join(
        f"  {json.dumps(key)}: {json.dumps(value)}"
        for key, value in pages.items()
    )
    bundle_path = DOCS_ROOT / "docs-bundle.js"
    bundle_path.write_text(
        "// ARC docs bundle — auto-generated by `arc cliup`. Do not edit by hand.\n"
        f"window.DOCS_CONTENT = {{\n{js_entries}\n}};\n",
        encoding="utf-8",
    )
    return len(pages)


def _build_stub(key: str, cmd) -> str:
    """Build a Markdown stub for a new command doc."""
    from app.commands.registry import CommandDef  # noqa: F401 — type reference only

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


def _do_cliup(silent: bool = False, skip_vendor: bool = False) -> dict:
    """Core cliup logic — create missing command stubs, regenerate index, rebuild bundle.

    Args:
        silent:      Suppress all console output (used for auto-run at shell startup).
        skip_vendor: Skip CDN vendor downloads (safe for startup; no internet required).

    Returns a stats dict with keys: created, existing, downloaded, bundled.
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

    downloaded: list[str] = []
    if not skip_vendor:
        if not silent:
            console.print("[dim]Checking vendor files…[/dim]")
        downloaded = _ensure_vendor_files()

    if not silent:
        console.print("[dim]Building docs bundle…[/dim]")
    bundled = _build_docs_bundle()

    return {
        "created":    created,
        "existing":   existing,
        "downloaded": downloaded,
        "bundled":    bundled,
    }


@app.command("cliup")
def cliup() -> None:
    """Sync docs with the registry and rebuild the offline docs bundle.

    Steps performed:
    1. Create Markdown stubs in docs/commands/ for any new registered commands.
    2. Regenerate docs/commands/index.md from the live registry.
    3. Download vendor JS/CSS to docs/vendor/ (once; skipped if already present).
    4. Rebuild docs/docs-bundle.js — embeds all Markdown so the browser portal
       works via file:// with no server required.

    Existing doc files are never overwritten.
    """
    stats = _do_cliup(silent=False, skip_vendor=False)
    created   = stats["created"]
    existing  = stats["existing"]
    downloaded = stats["downloaded"]
    bundled   = stats["bundled"]

    total = len(COMMANDS)
    console.print(
        f"\n[bold cyan]cliup[/bold cyan] — {total} registered commands\n"
        f"  [green]created:[/green]  {len(created)}\n"
        f"  [dim]existing:[/dim] {len(existing)}\n"
        f"  [cyan]index:[/cyan]    docs/commands/index.md regenerated\n"
        f"  [cyan]vendor:[/cyan]   {len(downloaded)} file(s) downloaded"
        + (" (all present)" if not downloaded else "") + "\n"
        f"  [cyan]bundle:[/cyan]   docs/docs-bundle.js ({bundled} pages)\n"
    )
    for key in created:
        console.print(f"  [green]+[/green] docs/commands/{slugify(key)}.md")
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

