"""ARC entry point — bootstraps config and starts the interactive shell."""

from __future__ import annotations

import getpass
import json
import stat
from typing import Optional

import httpx

import typer
from rich.console import Console

from app.api.client import SCMClient
from app.config import (
    CONFIG_DIR,
    CONFIG_FILE,
    ConfigSecurityError,
    clear_keychain,
    keychain_available,
    load_config,
    save_config,
)
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

    SCM service accounts provide a client_id and client_secret — ARC uses
    these to obtain a fresh OAuth token on every startup.  Secrets are stored
    in the OS keychain; non-sensitive values go to the config file.

    Press Enter to keep any value that is already stored.
    """
    cfg = load_config()
    kc = keychain_available()

    console.print("\n[bold cyan]ARC Credential Setup[/bold cyan]")
    console.print(
        "  Press [bold]Enter[/bold] to keep an existing value.\n"
        "  Secrets are shown as [dim]****[/dim] when already stored in the keychain.\n"
    )
    if kc:
        console.print(
            f"  Secrets  → [green]OS keychain[/green]  (client_secret, SSH password)\n"
            f"  Config   → [dim]{CONFIG_FILE}[/dim]  (client_id, tsg_id, SSH user/key/port)\n"
        )
    else:
        console.print(
            "  [yellow]⚠  OS keychain unavailable — ARC will not write secrets to disk.[/yellow]\n"
            "  Use environment variables for secrets until keychain access is available.\n"
        )

    def _prompt(label: str, current: str, secret: bool = False, hint: str = "") -> str:
        """Prompt for a value.  Returns the existing value unchanged if the user presses Enter."""
        display_current = "****" if (secret and current) else (current or "")
        display_hint = f" [dim][{display_current}][/dim]" if display_current else ""
        extra_hint = f"\n    [dim]{hint}[/dim]" if hint else ""
        console.print(f"  {label}{display_hint}{extra_hint}: ", end="")
        try:
            val = getpass.getpass("") if secret else input()
        except (EOFError, KeyboardInterrupt):
            val = ""
        # Empty input = keep existing value
        return val.strip() or current

    # ── SCM service account (primary auth method) ────────────────────────────
    console.print("[yellow]─ Strata Cloud Manager — Service Account ─[/yellow]")
    console.print(
        "  [dim]Your service account credentials come from the Palo Alto SCM portal.[/dim]\n"
        "  [dim]SCM portal → Settings → Identity & Access → Service Accounts → your account[/dim]\n"
    )

    cfg.scm.client_id = scm_client_id or _prompt(
        "Client ID",
        cfg.scm.client_id,
        hint="From SCM portal: the service account email, e.g. pa-api-you@1234567890.iam.panserviceaccount.com",
    )
    cfg.scm.client_secret = scm_secret or _prompt(
        "Client Secret",
        cfg.scm.client_secret,
        secret=True,
        hint="From SCM portal: the secret shown when you created or reset the service account",
    )
    cfg.scm.tsg_id = scm_tsg or _prompt(
        "TSG ID",
        cfg.scm.tsg_id,
        hint="Your Tenant Services Group ID — the number in your SCM URL or service account name",
    )

    # ── Bearer token (advanced / optional) ───────────────────────────────────
    console.print(
        "\n[yellow]─ Bearer Token (optional — leave blank if using client credentials above) ─[/yellow]"
    )
    console.print(
        "  [dim]Only needed for pre-issued tokens or testing.  ARC prefers client credentials.[/dim]\n"
    )
    cfg.scm.bearer_token = scm_bearer_token or _prompt(
        "Bearer Token",
        cfg.scm.bearer_token,
        secret=True,
        hint="Leave blank to have ARC generate tokens automatically from your client credentials",
    )

    # ── SSH Defaults ─────────────────────────────────────────────────────────
    console.print("\n[yellow]─ SSH Defaults ─[/yellow]")
    cfg.ssh.user = ssh_user or _prompt(
        "SSH Username",
        cfg.ssh.user,
        hint="Username for SSH sessions to managed devices (default: admin)",
    )
    cfg.ssh.key_path = ssh_key or _prompt(
        "SSH Key Path",
        cfg.ssh.key_path,
        hint="Path to your SSH private key, e.g. ~/.ssh/id_ed25519 (leave blank to use password)",
    )
    cfg.ssh.password = _prompt(
        "SSH Password",
        cfg.ssh.password,
        secret=True,
        hint="Leave blank if using key auth or SSH agent",
    )

    try:
        save_config(cfg)
    except ConfigSecurityError as exc:
        console.print(f"\n[yellow]⚠[/yellow] {exc}")
        console.print(
            f"[green]✓[/green] Non-sensitive config saved to [bold]{CONFIG_FILE}[/bold]  "
            "[dim](mode 0600)[/dim]"
        )
        raise typer.Exit(1) from exc

    if kc:
        console.print(
            f"\n[green]✓[/green] Secrets saved to OS keychain\n"
            f"[green]✓[/green] Config file: [bold]{CONFIG_FILE}[/bold]  [dim](mode 0600)[/dim]\n"
        )
    else:
        console.print(
            f"\n[green]✓[/green] Non-sensitive config saved to [bold]{CONFIG_FILE}[/bold]  "
            "[dim](mode 0600)[/dim]\n"
        )

    console.print(
        "Run [bold]arc auth test[/bold] to verify your credentials work end-to-end."
    )


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
            "— secrets must come from environment variables"
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


def _short_err(err_str: str) -> str:
    """Return the first line of an error string — avoids huge httpx tracebacks in test output."""
    return err_str.split("\n")[0]


@auth_app.command("test")
def auth_test() -> None:
    """Test connectivity using stored credentials.

    Checks (in order):

    1. **Keychain** — verifies the OS keychain is readable and reports which
       secrets are present.
    2. **SCM authentication** — attempts to obtain / validate a bearer token.
    3. **SCM API** — fetches ``/iam/v1/tenants`` as a lightweight live call.
       Falls back to ``/sse/config/v1/folders`` if the IAM endpoint is not
       authorised.
    4. **Config file** — reports the path and whether it exists.

    Exit code 0 = all configured checks passed.
    Exit code 1 = at least one check failed.
    """
    import sys

    cfg = load_config()
    all_ok = True

    # ── 1. Keychain ──────────────────────────────────────────────────────────
    console.print("\n[bold cyan]1. OS Keychain[/bold cyan]")
    kc = keychain_available()
    if kc:
        console.print("  [green]✓[/green] Keychain is accessible")
        bearer_stored  = bool(cfg.scm.bearer_token)
        secret_stored  = bool(cfg.scm.client_secret)
        ssh_pass_stored = bool(cfg.ssh.password)
        console.print(
            f"  bearer_token  : {'[green]present[/green]' if bearer_stored  else '[dim]not set[/dim]'}"
        )
        console.print(
            f"  client_secret : {'[green]present[/green]' if secret_stored  else '[dim]not set[/dim]'}"
        )
        console.print(
            f"  ssh.password  : {'[green]present[/green]' if ssh_pass_stored else '[dim]not set[/dim]'}"
        )
    else:
        console.print(
            "  [yellow]⚠[/yellow]  Keychain unavailable — secrets must be supplied "
            "via environment variables"
        )
        # Not fatal — env vars may still configure everything.

    # ── 2. Config file ───────────────────────────────────────────────────────
    console.print("\n[bold cyan]2. Config file[/bold cyan]")
    console.print(f"  Path: [dim]{CONFIG_FILE}[/dim]")
    if CONFIG_FILE.exists():
        console.print("  [green]✓[/green] Config file exists")
    else:
        console.print(
            "  [yellow]⚠[/yellow]  Config file not found — "
            "run [bold]arc auth login[/bold] to create it"
        )

    # ── 3. SCM credentials present ───────────────────────────────────────────
    console.print("\n[bold cyan]3. SCM credentials[/bold cyan]")
    if not cfg.scm.is_configured:
        console.print(
            "  [red]✗[/red]  SCM is not configured.  "
            "Run [bold]arc auth login[/bold] and provide:\n"
            "    • client_id + client_secret + tsg_id  (recommended — service account flow)\n"
            "    • OR a pre-issued bearer token"
        )
        all_ok = False
        console.print()
        raise typer.Exit(1)

    # Determine which auth path will be used (mirrors SCMClient priority).
    using_oauth = bool(cfg.scm.client_id and cfg.scm.client_secret and cfg.scm.tsg_id)
    if using_oauth:
        console.print(
            f"  [green]✓[/green] OAuth client credentials present\n"
            f"    client_id : {cfg.scm.client_id}\n"
            f"    tsg_id    : {cfg.scm.tsg_id}\n"
            f"    [dim]ARC will use these to obtain a fresh token (bearer_token in keychain is ignored)[/dim]"
        )
    else:
        console.print(
            "  [green]✓[/green] Bearer token present (no client credentials — token used directly)\n"
            "  [yellow]⚠[/yellow]  Consider running [bold]arc auth login[/bold] to store "
            "client_id + client_secret + tsg_id for automatic token refresh."
        )

    # ── 4. SCM authentication ────────────────────────────────────────────────
    console.print("\n[bold cyan]4. SCM authentication[/bold cyan]")
    if using_oauth:
        console.print(
            f"  [dim]Obtaining OAuth token for TSG {cfg.scm.tsg_id}…[/dim]"
        )
    else:
        console.print("  [dim]Using pre-issued bearer token…[/dim]")
    try:
        client = SCMClient(cfg.scm)
        if using_oauth:
            console.print(
                f"  [green]✓[/green] OAuth token obtained for TSG [bold]{cfg.scm.tsg_id}[/bold]"
            )
        else:
            console.print("  [green]✓[/green] Bearer token accepted by SCMClient")
    except Exception as exc:
        console.print(f"  [red]✗[/red]  SCM authentication failed: {exc}")
        all_ok = False
        console.print()
        raise typer.Exit(1) from exc

    # ── 5. SCM API connectivity ─────────────────────────────────────────────
    console.print("\n[bold cyan]5. SCM API connectivity[/bold cyan]")
    # Probe results: track what worked so we can give an accurate summary.
    probe_results: list[tuple[str, bool, str]] = []  # (label, ok, note)

    def _probe(label: str, path: str, params: dict | None = None) -> bool:
        try:
            resp = client._http.get(
                f"https://api.sase.paloaltonetworks.com{path}",
                headers=client._headers(),
                params=params,
            )
            if resp.status_code < 400:
                data = resp.json()
                count = len(data.get("data", data.get("items", [])))
                note = f"{count} item(s)"
                console.print(f"  [green]✓[/green] {label}  [dim]→ {note}[/dim]")
                probe_results.append((label, True, note))
                return True
            else:
                console.print(f"  [yellow]⚠[/yellow]  {label}  [dim]→ HTTP {resp.status_code}[/dim]")
                probe_results.append((label, False, f"HTTP {resp.status_code}"))
                return False
        except Exception as exc:
            console.print(f"  [yellow]⚠[/yellow]  {label}  [dim]→ {_short_err(str(exc))}[/dim]")
            probe_results.append((label, False, _short_err(str(exc))))
            return False

    # These are ordered: first failure doesn't stop the rest — we want to know
    # exactly which capabilities the service account has.
    _probe("GET /sse/config/v1/addresses?folder=Shared  (policy read)",
           "/sse/config/v1/addresses", {"folder": "Shared"})
    _probe("GET /sse/config/v1/security-rules?folder=Shared (policy read)",
           "/sse/config/v1/security-rules", {"folder": "Shared", "position": "pre"})
    _probe("GET /sse/config/v1/devices?folder=Shared     (device read)",
           "/sse/config/v1/devices", {"folder": "Shared"})
    _probe("GET /sse/config/v1/folders                   (folder list)",
           "/sse/config/v1/folders")
    _probe("GET /iam/v1/tenants                          (tenant/TSG list)",
           "/iam/v1/tenants")

    any_ok = any(ok for _, ok, _ in probe_results)
    all_probes_ok = all(ok for _, ok, _ in probe_results)

    if not any_ok:
        err_codes = {note for _, ok, note in probe_results if not ok}
        is_forbidden = any("403" in n for n in err_codes)
        is_unauthorized = any("401" in n for n in err_codes)
        if is_forbidden:
            console.print(
                f"\n  [red]✗[/red]  All API probes returned 403.\n"
                f"  Token is valid (OAuth succeeded) but the service account has no\n"
                f"  read access to TSG [bold]{cfg.scm.tsg_id}[/bold].\n\n"
                f"  [bold]Most likely cause:[/bold] your tsg_id is a child TSG that the\n"
                f"  service account was not assigned permissions to.  Try authenticating\n"
                f"  with the [bold]parent TSG ID[/bold] instead:\n\n"
                f"    1. Find your parent TSG ID in the SCM portal URL or\n"
                f"         Settings → Identity → Tenant Hierarchy\n"
                f"    2. Run [bold]arc auth login[/bold] → update TSG ID to the parent.\n"
                f"    3. Use [bold]tsg <child-id>[/bold] inside ARC to switch down.\n"
            )
        elif is_unauthorized:
            console.print(
                f"\n  [red]✗[/red]  All API probes returned 401.\n"
                f"  The token was accepted by the auth server but rejected by the API.\n"
                f"  Verify tsg_id [bold]{cfg.scm.tsg_id}[/bold] is the TSG the service\n"
                f"  account was created under.\n"
            )
        all_ok = False
    elif not all_probes_ok:
        console.print(
            f"\n  [dim]Some probes returned 403 — that is normal if your service account\n"
            f"  is scoped to policy/config objects only (read-only admin role).\n"
            f"  The probes that succeeded confirm API connectivity is working.[/dim]"
        )

    client.close()

    # ── Summary ──────────────────────────────────────────────────────────────
    console.print()
    if all_ok:
        if all_probes_ok:
            console.print("[bold green]All checks passed.[/bold green]")
        else:
            ok_count  = sum(1 for _, ok, _ in probe_results if ok)
            tot_count = len(probe_results)
            console.print(
                f"[bold green]Connected.[/bold green]  "
                f"{ok_count}/{tot_count} API probes succeeded — "
                f"partial access is normal for read-only service accounts."
            )
    else:
        console.print("[bold red]One or more checks failed.[/bold red]  See details above.")
        sys.exit(1)


# ---------------------------------------------------------------------------
# config sub-command
# ---------------------------------------------------------------------------

config_app = typer.Typer(help="Manage the ARC config file.")
app.add_typer(config_app, name="config")

# Template written by `arc config generate`.
# _note fields are ignored by load_config() — they document the file for humans.
_CONFIG_TEMPLATE = {
    "_note": (
        "ARC config — fill in non-secret REPLACE_WITH_* values, then run: arc auth login  "
        "(secrets are prompted securely and stored in the OS keychain)"
    ),
    "scm": {
        "_note": (
            "Use bearer_token OR OAuth. Do not put secrets in this file; leave bearer_token "
            "and client_secret blank and enter them via arc auth login or env vars."
        ),
        "bearer_token": "",
        "client_id":    "REPLACE_WITH_SCM_CLIENT_ID",
        "client_secret": "",
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

