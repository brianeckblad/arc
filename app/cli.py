"""ARC entry point — bootstraps config and starts the interactive shell."""

from __future__ import annotations

import json
import os
import shlex
import stat
from typing import List, Optional

import httpx

import typer
from rich.console import Console

from app.api.client import SCMClient
from app.config import (
    AUTH_FILE,
    CONFIG_DIR,
    CONFIG_FILE,
    ConfigSecurityError,
    clear_keychain,
    delete_profile,
    get_active_profile,
    has_configured_profiles,
    keychain_available,
    list_profiles,
    load_config,
    save_config,
    set_active_profile,
)
from app.docs import DOCS_ROOT, open_docs_in_browser, slugify
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
err_console = Console(stderr=True)


# ---------------------------------------------------------------------------
# Wizard helpers — shared by the credential wizards (keychain + env-var)
# ---------------------------------------------------------------------------

# The credential wizard + its prompt helpers live in app/auth/wizard.py so the
# in-shell `scm setup` command shares the exact same implementation.  Imported
# here under the original private names to keep the env-var wizard below unchanged.
from app.auth.wizard import (  # noqa: E402
    WizardCancelled as _WizardCancelled,
    run_credential_wizard,
    run_wizard_guarded as _run_wizard_guarded,
    select_or_create_profile,
    wizard_confirm as _wizard_confirm,
    wizard_prompt as _wizard_prompt,
)


def _detect_shell_style() -> str:
    """Return 'powershell' or 'posix' for the invoking shell."""
    import os as _os
    import platform as _platform

    if _os.environ.get("PSModulePath"):
        return "powershell"
    if _platform.system() == "Windows" and not _os.environ.get("SHELL"):
        return "powershell"
    return "posix"


def _export_line(name: str, value: str, style: str) -> str:
    """Render a single environment-variable assignment for the target shell."""
    if style == "powershell":
        return f'$env:{name} = "{value}"'
    return f"export {name}={shlex.quote(value)}"


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

    # No file generation at launch: command help is synthesized from the
    # registry (app/docs.py), and the browser bundle is rebuilt explicitly
    # with `arc cliup`. A shell start must never write to the repo.
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


@app.command("help")
def show_help(
    topic: Optional[List[str]] = typer.Argument(
        None, help="Help topic (e.g. configuration) or command name. Omit to list topics."
    ),
) -> None:
    """Show ARC help topics in the terminal (configuration, setup, command help).

    Renders the same pages the in-shell `help` command shows — e.g.
    `arc help configuration`.  Use `arc docs [topic]` for the browser reference.
    """
    from app.docs import render_help_topic

    topic_str = " ".join(topic).strip() if topic else ""
    if not topic_str:
        console.print(
            "\n[bold cyan]ARC commands[/bold cyan]  [dim](run from your terminal)[/dim]\n"
            "  [cyan]arc[/cyan]                 launch the interactive shell\n"
            "  [cyan]arc setup[/cyan]           guided setup — credentials + per-OS guides\n"
            "  [cyan]arc auth[/cyan]            manage credentials (configure/show/test/clear)\n"
            "  [cyan]arc config[/cyan]          manage the config file\n"
            "  [cyan]arc docs[/cyan]            open the browser docs portal\n"
            "  [cyan]arc scm[/cyan]             raw SCM API passthrough\n"
            "  [cyan]arc help[/cyan]            this list + help topics\n"
        )
        console.print(
            "\n[bold cyan]Help topics[/bold cyan]\n"
            "  [cyan]arc help configuration[/cyan]   full configuration reference\n"
            "  [cyan]arc help setup[/cyan]           getting-started overview\n"
            "  [cyan]arc help device-access[/cyan]   device auth planes (SCM proxy vs SSH/2FA)\n"
            "  [cyan]arc help <command>[/cyan]        help for any ARC command\n"
        )
        console.print(
            "\n  [dim]Full CLI usage: [bold]arc --help[/bold]  ·  browser reference: [bold]arc docs[/bold]\n"
            "  Want unquoted [bold]arc ?[/bold] to work? In zsh it's a shell wildcard — run "
            "[bold]arc setup shell[/bold] to add the one-line fix.[/dim]\n"
        )
        return
    if not render_help_topic(console, topic_str, use_pager=False):
        console.print(
            f"[yellow]No help topic:[/yellow] [bold]{topic_str}[/bold]\n"
            "  Run [bold]arc help[/bold] to list topics, or [bold]arc docs[/bold] "
            "for the full browser reference."
        )
        raise typer.Exit(1)


# ---------------------------------------------------------------------------
# setup group — guided onboarding, run from the terminal (outside the shell)
# ---------------------------------------------------------------------------

setup_app = typer.Typer(help="Set up ARC — credential wizard and per-OS guides.")
app.add_typer(setup_app, name="setup")

_OS_GUIDE_LABELS = {"osx": "macOS", "linux": "Linux / WSL", "win": "Windows"}


@setup_app.callback(invoke_without_command=True)
def setup_menu(ctx: typer.Context) -> None:
    """Guided setup overview — the credential wizard and per-OS guides.

    Run `arc setup scm` for the credential wizard, or
    `arc setup osx|linux|win` for a platform walkthrough.
    """
    if ctx.invoked_subcommand is not None:
        return

    import platform as _platform

    os_name = _platform.system()  # "Darwin" | "Linux" | "Windows"
    detected = {"Darwin": "osx", "Linux": "linux", "Windows": "win"}.get(os_name, "")
    os_label = {"Darwin": "macOS", "Linux": "Linux / WSL", "Windows": "Windows"}.get(os_name, os_name)

    console.print("\n[bold cyan]ARC Setup[/bold cyan]")
    console.print(f"[dim]Detected platform: {os_label}[/dim]\n")
    console.print("  Choose what to set up:\n")
    rows = [
        ("arc setup scm", "Credentials as session env vars (no keychain) — set by hand or wizard"),
        ("arc setup scm keystore", "Credentials in the OS keychain (persistent, secure)"),
        ("arc setup osx", "macOS step-by-step guide (Keychain, Touch ID)"),
        ("arc setup linux", "Linux / WSL guide (libsecret / Secret Service / env vars)"),
        ("arc setup win", "Windows guide (Credential Manager / PowerShell)"),
        ("arc setup shell", "Make an unquoted `arc ?` work in your terminal (zsh)"),
    ]
    for cmd, desc in rows:
        mark = "  [green]◀ your platform[/green]" if detected and cmd.endswith(detected) else ""
        console.print(f"  [cyan]{cmd:<24}[/cyan] {desc}{mark}")
    console.print()
    console.print(
        "  [dim]Full reference: [bold]arc help configuration[/bold][/dim]"
    )
    if detected:
        console.print(
            f"\n  [dim]Tip: start with [bold]arc setup {detected}[/bold] or [bold]arc setup scm[/bold].[/dim]"
        )
    console.print()


scm_app = typer.Typer(
    help="Set up SCM credentials — session env vars (default) or the OS keychain."
)
setup_app.add_typer(scm_app, name="scm")


@scm_app.callback(invoke_without_command=True)
def setup_scm(
    ctx: typer.Context,
    export: bool = typer.Option(
        False, "--export", "-e",
        help='Print only export lines to stdout (for: eval "$(arc setup scm --export)").',
    ),
) -> None:
    """Set up SCM credentials as session-only environment variables (no keychain).

    Bare: prints the export commands to set by hand, then offers a guided wizard.
    `--export`: runs the wizard and emits only the export lines (eval-ready).
    For OS-keychain storage instead, run `arc setup scm keystore`.
    """
    if ctx.invoked_subcommand is not None:
        return
    if export:
        _run_wizard_guarded(_run_env_wizard, export_mode=True)
        return
    _run_wizard_guarded(_scm_manual_and_offer)


@scm_app.command("wizard")
def setup_scm_wizard(
    export: bool = typer.Option(
        False, "--export", "-e",
        help='Print only export lines to stdout (for: eval "$(arc setup scm wizard --export)").',
    ),
) -> None:
    """Guided wizard that builds session-only SCM env vars (no keychain)."""
    _run_wizard_guarded(_run_env_wizard, export_mode=export)


@scm_app.command("keystore")
def setup_scm_keystore() -> None:
    """Store SCM/SSH credentials in the OS keychain (persistent, secure)."""
    _run_wizard_guarded(run_credential_wizard)


def _scm_manual_and_offer() -> None:
    """Print the manual export commands for the detected shell, then offer the wizard."""
    style = _detect_shell_style()
    one = 'eval "$(arc setup scm --export)"' if style != "powershell" else "arc setup scm --export | iex"

    console.print("\n[bold cyan]Set up SCM — environment variables (no keychain)[/bold cyan]")
    console.print(
        "  [dim]Session-only: these live in the current terminal and are gone when\n"
        "  you close it or reboot. The guided wizard builds them for you, or set\n"
        "  them by hand.  Prefer persistent secrets? [bold]arc setup scm keystore[/bold][/dim]\n"
    )

    if _wizard_confirm("Build these with a guided wizard now?"):
        _run_env_wizard(export_mode=False)
        return

    # Declined the wizard — fall back to the manual reference.
    console.print("\n[dim]No problem — here are the variables to set by hand:[/dim]\n")
    console.print("[yellow]─ Option A: a token (recommended — no secret on the machine) ─[/yellow]")
    console.print("    " + _export_line("SCM_BEARER_TOKEN", "<your-token>", style))
    console.print("    " + _export_line("SCM_TSG_ID", "<tsg-id>", style) + "   [dim](optional)[/dim]")
    console.print("\n[yellow]─ Option B: a service account (ARC mints fresh tokens each launch) ─[/yellow]")
    console.print(
        "  [dim]This puts the client secret in your environment — prefer "
        "[bold]arc setup scm keystore[/bold] for that.[/dim]"
    )
    for name, val in (("SCM_CLIENT_ID", "<client-id>"),
                      ("SCM_CLIENT_SECRET", "<client-secret>"),
                      ("SCM_TSG_ID", "<tsg-id>")):
        console.print("    " + _export_line(name, val, style))
    console.print("\n[yellow]─ Optional device SSH ─[/yellow]")
    for name, val in (("ARC_SSH_USER", "admin"), ("ARC_SSH_KEY", "~/.ssh/panos_key")):
        console.print("    " + _export_line(name, val, style))
    console.print(
        f"\n  [dim]One-step: [bold]{one}[/bold] runs the wizard and sets the vars for you.\n"
        "  Keychain instead? [bold]arc setup scm keystore[/bold][/dim]\n"
    )


def _run_env_wizard(*, export_mode: bool) -> None:
    """Collect SCM/SSH credentials and emit shell `export` lines (writes nothing)."""
    from app.api._auth import oauth_token

    style = _detect_shell_style()
    ui = err_console if export_mode else console  # prompts/status never touch stdout in export mode

    ui.print("\n[bold cyan]ARC SCM env-var setup[/bold cyan]  [dim](session-only, no keychain)[/dim]")
    ui.print(
        "  [bold]1[/bold]  Paste a static SCM bearer token\n"
        "  [bold]2[/bold]  Mint a temporary token from a service account\n"
    )
    choice = _wizard_prompt("Choose 1 or 2", "1", out=ui)

    pairs: "list[tuple[str, str]]" = []

    if choice == "2":
        client_id = _wizard_prompt("Client ID", out=ui,
                                   hint="service account email from the SCM portal")
        client_secret = _wizard_prompt("Client Secret", secret=True, out=ui,
                                       hint="used once to mint a token — never stored")
        tsg = _wizard_prompt("TSG ID", os.environ.get("SCM_TSG_ID", ""), out=ui,
                             hint="your Tenant Services Group ID")
        if not (client_id and client_secret and tsg):
            ui.print("[yellow]Client ID, secret, and TSG are all required to mint a token.[/yellow]")
            raise typer.Exit(1)
        ui.print("[dim]Minting token…[/dim]")
        try:
            with httpx.Client(timeout=30) as http:
                token, expires_in = oauth_token(http, client_id, client_secret, tsg)
        except Exception as exc:  # noqa: BLE001
            ui.print(f"[red]Token request failed:[/red] {exc}")
            raise typer.Exit(1)
        mins = f" (~{expires_in // 60} min)" if expires_in else ""
        ui.print(f"[green]✓[/green] Token minted{mins}.")
        pairs.append(("SCM_BEARER_TOKEN", token))
        pairs.append(("SCM_TSG_ID", tsg))
    else:
        token = _wizard_prompt("Bearer token", secret=True, out=ui,
                               hint="paste a pre-issued SCM token")
        if not token:
            ui.print("[yellow]No token entered.[/yellow]")
            raise typer.Exit(1)
        pairs.append(("SCM_BEARER_TOKEN", token))
        tsg = _wizard_prompt("TSG ID", os.environ.get("SCM_TSG_ID", ""), out=ui, hint="optional")
        if tsg:
            pairs.append(("SCM_TSG_ID", tsg))

    # Optional device SSH
    ssh_user = _wizard_prompt("SSH username", os.environ.get("ARC_SSH_USER", ""), out=ui,
                              hint="optional — device SSH")
    if ssh_user:
        pairs.append(("ARC_SSH_USER", ssh_user))
    ssh_key = _wizard_prompt("SSH key path", os.environ.get("ARC_SSH_KEY", ""), out=ui, hint="optional")
    if ssh_key:
        # Expand ~ now so the exported value is a literal path (quoting would
        # otherwise stop the shell from expanding the tilde).
        pairs.append(("ARC_SSH_KEY", os.path.expanduser(ssh_key)))

    lines = [_export_line(name, val, style) for name, val in pairs]

    if export_mode:
        for line in lines:
            print(line)  # stdout only — eval-ready
        ui.print("\n[dim]Set for this shell. Verify with: arc auth test[/dim]")
        return

    console.print("\n[bold]Run these in your terminal[/bold] "
                  "[dim](session-only — gone on close/reboot)[/dim]:\n")
    for line in lines:
        console.print(f"  [green]{line}[/green]")
    one = 'eval "$(arc setup scm --export)"' if style != "powershell" else "arc setup scm --export | iex"
    console.print(
        f"\n  [dim]Or set them in one step: [bold]{one}[/bold]\n"
        "  Then verify: [bold]arc auth test[/bold][/dim]\n"
    )


def _render_os_guide(os_key: str) -> None:
    """Print the 'three ways to configure' header, then the platform guide."""
    from app.docs import os_setup_doc, render_doc_file

    doc = os_setup_doc(os_key)
    label = _OS_GUIDE_LABELS.get(os_key, os_key)
    console.print(
        f"\n[bold cyan]Set up ARC on {label} — three ways[/bold cyan]\n"
        "  [bold]1. Session env vars[/bold]  → [cyan]arc setup scm[/cyan]  (no keychain; gone on reboot)\n"
        "  [bold]2. OS keychain[/bold]       → [cyan]arc setup scm keystore[/cyan]  (persistent, secure)\n"
        "  [bold]3. Manual[/bold]            → follow the platform steps below"
    )
    if not doc or not render_doc_file(console, doc, title=f"Set up ARC — {label}", use_pager=False):
        console.print(
            f"\n[yellow]Guide not found for {label}.[/yellow] "
            "Try [bold]arc setup scm[/bold] or [bold]arc setup scm keystore[/bold].\n"
        )


@setup_app.command("osx")
def setup_osx() -> None:
    """macOS setup guide (Keychain, Touch ID)."""
    _render_os_guide("osx")


@setup_app.command("linux")
def setup_linux() -> None:
    """Linux / WSL setup guide (libsecret / Secret Service / env vars)."""
    _render_os_guide("linux")


@setup_app.command("win")
def setup_win() -> None:
    """Windows setup guide (Credential Manager / PowerShell)."""
    _render_os_guide("win")


@setup_app.command("shell")
def setup_shell(
    apply: bool = typer.Option(
        False, "--apply", help="Append the alias to your shell rc file (default: show it only)."
    ),
) -> None:
    """Make an unquoted `arc ?` work in your terminal.

    In zsh, `?` is a filename wildcard, so the shell errors on `arc ?` before
    arc ever runs. A one-line alias (`alias arc='noglob arc'`) suppresses that
    so arc receives `?` and shows help. bash, fish, and PowerShell already pass
    an unquoted `?` through, so nothing is needed there.
    """
    shell = os.path.basename(os.environ.get("SHELL", "")).lower()
    home = os.path.expanduser("~")

    if shell == "zsh":
        rc = os.path.join(home, ".zshrc")
        alias_line = "alias arc='noglob arc'"
        marker = "# ARC: let an unquoted `arc ?` reach arc (zsh globs ? otherwise)"
        try:
            existing = open(rc, encoding="utf-8").read()
        except FileNotFoundError:
            existing = ""
        if "noglob arc" in existing:
            console.print(
                f"[green]✓[/green] Already configured in [bold]{rc}[/bold].\n"
                "  Reload with [bold]source ~/.zshrc[/bold] (or open a new terminal), "
                "then [bold]arc ?[/bold] works."
            )
            return
        if apply:
            with open(rc, "a", encoding="utf-8") as fh:
                fh.write(f"\n{marker}\n{alias_line}\n")
            console.print(
                f"\n[green]✓[/green] Added to [bold]{rc}[/bold]:\n    [cyan]{alias_line}[/cyan]\n\n"
                "  Reload: [bold]source ~/.zshrc[/bold] (or open a new terminal), "
                "then [bold]arc ?[/bold] shows help.\n"
            )
        else:
            console.print(
                "\n[bold cyan]zsh detected[/bold cyan] — an unquoted [bold]arc ?[/bold] is eaten by "
                "the shell's [bold]?[/bold] wildcard.\n"
                "  Add this one line to fix it:\n"
                f"    [cyan]{alias_line}[/cyan]\n\n"
                f"  Auto-add it: [bold]arc setup shell --apply[/bold]  [dim](writes to {rc})[/dim]\n"
                "  Then: [bold]source ~/.zshrc[/bold] (or open a new terminal).\n"
                "  [dim]Until then, [bold]arc '?'[/bold] (quoted) and [bold]arc help[/bold] work as-is.[/dim]\n"
            )
    elif shell == "bash":
        console.print(
            "\n[green]✓[/green] bash passes an unquoted [bold]?[/bold] through unchanged — "
            "[bold]arc ?[/bold] already works (it maps to --help).\n"
        )
    else:
        label = shell or "your shell"
        console.print(
            f"\n[bold cyan]{label}[/bold cyan]: most shells (bash, fish, PowerShell) pass an "
            "unquoted [bold]?[/bold] through, so [bold]arc ?[/bold] already works.\n"
            "  If yours globs [bold]?[/bold] like zsh, alias arc to suppress it, e.g. "
            "[cyan]alias arc='noglob arc'[/cyan].\n"
        )


# ---------------------------------------------------------------------------
# auth sub-command
# ---------------------------------------------------------------------------

auth_app = typer.Typer(help="Manage ARC credentials.")
app.add_typer(auth_app, name="auth")


@auth_app.command("configure")
def auth_configure(
    scm_bearer_token: Optional[str] = typer.Option(None, "--scm-bearer-token"),
    scm_client_id: Optional[str] = typer.Option(None, "--scm-client-id"),
    scm_secret: Optional[str] = typer.Option(None, "--scm-client-secret"),
    scm_tsg: Optional[str] = typer.Option(None, "--scm-tsg-id"),
    ssh_user: Optional[str] = typer.Option(None, "--ssh-user"),
    ssh_key: Optional[str] = typer.Option(None, "--ssh-key"),
    profile: str = typer.Option("default", "--profile", "-p", help="Named credential profile to create or update."),
) -> None:
    """Interactively configure ARC credentials.

    SCM service accounts provide a client_id and client_secret — ARC uses
    these to obtain a fresh OAuth token on every startup.  Secrets are stored
    in the OS keychain; non-sensitive values go to the config file.

    Without --profile you'll be shown a menu to pick an existing profile or
    create a new one, so --profile is optional.  Switch between profiles inside
    the ARC shell with `scm login`.

    Press Enter to keep any value that is already stored.
    """
    _run_wizard_guarded(
        run_credential_wizard,
        profile=profile,
        scm_bearer_token=scm_bearer_token,
        scm_client_id=scm_client_id,
        scm_secret=scm_secret,
        scm_tsg=scm_tsg,
        ssh_user=ssh_user,
        ssh_key=ssh_key,
    )


@auth_app.command("show")
def auth_show(
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Show a specific named profile."),
) -> None:
    """Display current configuration (credentials masked).

    Without --profile: lists all configured profiles then shows the active one
    in detail.  With --profile <name>: shows only that profile.
    """
    kc = keychain_available()

    def _mask(s: str) -> str:
        return ("*" * 8) if s else "[dim](not set)[/dim]"

    profiles = list_profiles()
    active_name = get_active_profile()

    # Always print the profile list when multiple profiles exist.
    if len(profiles) > 1 and not profile:
        console.print("\n[bold cyan]Credential Profiles[/bold cyan]")
        for p in profiles:
            marker = " [green]◀ active[/green]" if p["active"] else ""
            name_col = f"[bold]{p['name']}[/bold]" if p["active"] else p["name"]
            client_id = p["client_id"] or "[dim](not set)[/dim]"
            tsg_id = p["tsg_id"] or "[dim](not set)[/dim]"
            console.print(f"  {name_col:<20}  client_id: {client_id}  tsg_id: {tsg_id}{marker}")
        console.print(
            f"\n[dim]Use [bold]arc auth show --profile <name>[/bold] to inspect a specific profile.[/dim]"
        )

    # Show detail for the requested or active profile.
    target = profile or active_name
    cfg = load_config(profile=target)

    console.print(f"\n[bold cyan]Profile: {target}[/bold cyan]"
                  + (" [green](active)[/green]" if target == active_name else ""))
    console.print("[bold cyan]SCM[/bold cyan]")
    console.print(f"  bearer_token:  {_mask(cfg.scm.bearer_token)}  [dim](keychain: arc.bearer.token)[/dim]")
    console.print(f"  client_id:     {cfg.scm.client_id or '[dim](not set)[/dim]'}  [dim](config.json)[/dim]")
    console.print(f"  client_secret: {_mask(cfg.scm.client_secret)}  [dim](keychain: arc.bearer.password)[/dim]")
    console.print(f"  tsg_id:        {cfg.scm.tsg_id or '[dim](not set)[/dim]'}  [dim](config.json)[/dim]")

    console.print("\n[bold cyan]SSH[/bold cyan]")
    console.print(f"  user:    {cfg.ssh.user}  [dim](keychain: arc.shell.username)[/dim]")
    console.print(f"  key:     {cfg.ssh.key_path or '[dim](not set)[/dim]'}  [dim](config.json)[/dim]")
    console.print(f"  port:    {cfg.ssh.port}  [dim](config.json)[/dim]")
    console.print(f"  password: {_mask(cfg.ssh.password)}  [dim](keychain: arc.shell.password)[/dim]")

    console.print(f"\n[bold cyan]Config file:[/bold cyan] {CONFIG_FILE}")
    if kc:
        console.print("[bold cyan]Keychain:[/bold cyan] [green]available[/green]  (secrets stored in OS keychain)")
        console.print(
            "\n[bold cyan]Keychain entries[/bold cyan]  [dim](macOS: open Keychain Access → search 'arc')[/dim]"
        )
        console.print("  Service: [bold]arc[/bold]")
        sfx = f".{target}" if target != "default" else ""
        console.print(f"  [dim]{'Account':<35}  Stores[/dim]")
        console.print(f"  [cyan]{'arc.bearer.token' + sfx:<35}[/cyan]  SCM pre-issued bearer token")
        console.print(f"  [cyan]{'arc.bearer.password' + sfx:<35}[/cyan]  SCM OAuth client secret")
        console.print(f"  [cyan]{'arc.shell.username' + sfx:<35}[/cyan]  SSH username for device connections")
        console.print(f"  [cyan]{'arc.shell.password' + sfx:<35}[/cyan]  SSH password for device connections")
    else:
        console.print(
            "[bold cyan]Keychain:[/bold cyan] [yellow]unavailable[/yellow]  "
            "— secrets must come from environment variables"
        )
    console.print()


@auth_app.command("clear")
def auth_clear(
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Clear secrets for a specific profile only."),
) -> None:
    """Remove ARC secrets from the OS keychain.

    Without --profile: removes secrets for all profiles.
    With --profile <name>: removes only that profile's secrets.

    This does not delete the config file.  Non-sensitive values (client_id,
    tsg_id, SSH user/key/port) are preserved.  Run ``arc auth configure`` to
    re-enter credentials afterward.
    """
    clear_keychain(profile=profile)
    if profile:
        console.print(f"[green]✓[/green] Secrets for profile [bold]{profile}[/bold] removed from OS keychain.")
    else:
        console.print("[green]✓[/green] All ARC secrets removed from OS keychain.")
    console.print(
        f"  Config file [dim]{CONFIG_FILE}[/dim] unchanged  "
        "(run [bold]arc auth configure[/bold] to re-enter credentials)"
    )


def _short_err(err_str: str) -> str:
    """Return the first line of an error string — avoids huge httpx tracebacks in test output."""
    return err_str.split("\n")[0]


@auth_app.command("migrate")
def auth_migrate(
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be migrated without writing."),
) -> None:
    """Migrate old keychain entries to the new arc.* naming scheme.

    ARC 1.x stored credentials under names like ``scm.bearer_token``.
    The current version uses ``arc.bearer.token``, ``arc.bearer.password``,
    ``arc.shell.username``, and ``arc.shell.password``.

    This command reads the old entries, writes them under the new names,
    and clears the old entries.  Run it once after upgrading from an older
    ARC version.  It is safe to run multiple times.
    """
    from app.config import (
        _LEGACY_KEY_SCM_BEARER, _LEGACY_KEY_SCM_SECRET,
        _LEGACY_KEY_SSH_PASSWORD, _KEY_SCM_BEARER, _KEY_SCM_SECRET,
        _KEY_SSH_PASSWORD, _keychain_get, _keychain_set, _keychain_delete,
        list_profiles,
    )

    profiles = list_profiles()
    migrated: list[str] = []

    for p in profiles:
        pname = p["name"]
        suffix = f".{pname}" if pname != "default" else ""

        legacy_map = {
            _LEGACY_KEY_SCM_BEARER:   _KEY_SCM_BEARER,
            _LEGACY_KEY_SCM_SECRET:   _KEY_SCM_SECRET,
            _LEGACY_KEY_SSH_PASSWORD: _KEY_SSH_PASSWORD,
        }

        for old_key, new_key in legacy_map.items():
            old_full = f"{old_key}{suffix}"
            new_full = f"{new_key}{suffix}"
            value = _keychain_get(old_full)
            if not value:
                continue
            if not dry_run:
                _keychain_set(new_full, value)
                _keychain_delete(old_full)
                migrated.append(f"{old_full} → {new_full}")
            else:
                migrated.append(f"[dry-run] {old_full} → {new_full}")

    if not dry_run:
        # Also clear the bare (non-suffixed) legacy keys.
        for key in (_LEGACY_KEY_SCM_BEARER, _LEGACY_KEY_SCM_SECRET, _LEGACY_KEY_SSH_PASSWORD):
            val = _keychain_get(key)
            if val:
                new_key = {
                    _LEGACY_KEY_SCM_BEARER:   _KEY_SCM_BEARER,
                    _LEGACY_KEY_SCM_SECRET:   _KEY_SCM_SECRET,
                    _LEGACY_KEY_SSH_PASSWORD: _KEY_SSH_PASSWORD,
                }[key]
                _keychain_set(new_key, val)
                _keychain_delete(key)
                migrated.append(f"{key} → {new_key}")

    if migrated:
        console.print(f"\n[green]✓[/green] Migrated {len(migrated)} keychain entry/entries:")
        for m in migrated:
            console.print(f"  {m}")
        if dry_run:
            console.print("\n[dim](dry-run — run without --dry-run to apply)[/dim]")
        else:
            console.print(
                "\n[dim]Old entries cleared.  "
                "Run [bold]arc auth show[/bold] to verify the new entries.[/dim]"
            )
    else:
        console.print("[green]✓[/green] Nothing to migrate — credentials are already using the new naming scheme.")
        console.print(f"  [dim]Looking for: {_KEY_SCM_BEARER}, {_KEY_SCM_SECRET}, {_KEY_SSH_PASSWORD}[/dim]")


@auth_app.command("delete-profile")
def auth_delete_profile(
    name: str = typer.Argument(..., help="Profile name to delete (cannot delete 'default')."),
) -> None:
    """Delete a named credential profile from config.json and the OS keychain.

    The ``default`` profile cannot be deleted.  The active profile cannot be
    deleted while it is in use — switch to another profile first with
    ``account <name>`` inside the ARC shell.
    """
    try:
        active = get_active_profile()
        if name == active:
            console.print(
                f"[red]Cannot delete the active profile '{name}'.[/red]\n"
                "  Switch to a different profile first: "
                "[bold]arc auth configure --profile <other>[/bold] and use "
                "[bold]account <other>[/bold] inside ARC."
            )
            raise typer.Exit(1)
        delete_profile(name)
        console.print(
            f"[green]✓[/green] Profile [bold]{name}[/bold] removed from config.json and OS keychain."
        )
    except ValueError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(1) from exc


@auth_app.command("test")
def auth_test(
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Test a specific named profile."),
) -> None:
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

    active_name = get_active_profile()
    target = profile or active_name
    if target != active_name:
        console.print(f"\n[dim]Testing profile:[/dim] [bold]{target}[/bold]")

    cfg = load_config(profile=target)

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
            "run [bold]arc auth configure[/bold] to create it"
        )

    # ── 3. SCM credentials present ───────────────────────────────────────────
    console.print("\n[bold cyan]3. SCM credentials[/bold cyan]")
    if not cfg.scm.is_configured:
        console.print(
            "  [red]✗[/red]  SCM is not configured.  "
            "Run [bold]arc auth configure[/bold] and provide:\n"
            "    • client_id + client_secret + tsg_id  (recommended — service account flow)\n"
            "    • OR a pre-issued bearer token"
        )
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
            "  [yellow]⚠[/yellow]  Consider running [bold]arc auth configure[/bold] to store "
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
        console.print()
        raise typer.Exit(1) from exc

    # ── 5. SCM API connectivity ─────────────────────────────────────────────
    console.print("\n[bold cyan]5. SCM API connectivity[/bold cyan]")
    console.print(
        "  [dim]Probing all three pan.dev API gateways…[/dim]\n"
        "  [dim]Source: https://pan.app/scripts/scm/api/[/dim]"
    )
    probe_results: list[tuple[str, bool, str]] = []

    def _probe_url(label: str, url: str, params: dict | None = None) -> bool:
        try:
            resp = client._http.get(url, headers=client._headers(), params=params)
            code = resp.status_code
            if code < 400:
                data = resp.json()
                count = len(data.get("data", data.get("items", [])))
                console.print(f"  [green]✓[/green] {label}  [dim]→ {count} item(s)[/dim]")
                probe_results.append((label, True, f"{count} item(s)"))
                return True
            else:
                console.print(f"  [yellow]⚠[/yellow]  {label}  [dim]→ HTTP {code}[/dim]")
                probe_results.append((label, False, f"HTTP {code}"))
                return False
        except Exception as exc:
            console.print(f"  [yellow]⚠[/yellow]  {label}  [dim]→ {_short_err(str(exc))}[/dim]")
            probe_results.append((label, False, _short_err(str(exc))))
            return False

    strata = "https://api.strata.paloaltonetworks.com"
    sase = "https://api.sase.paloaltonetworks.com"

    console.print("  [dim]── Objects gateway (strata/config/objects/v1) ──[/dim]")
    _probe_url("GET /config/objects/v1/addresses",
               f"{strata}/config/objects/v1/addresses",
               {"folder": "Shared"})
    _probe_url("GET /config/objects/v1/services",
               f"{strata}/config/objects/v1/services",
               {"folder": "Shared"})

    console.print("  [dim]── Security gateway (strata/config/security/v1) ──[/dim]")
    _probe_url("GET /config/security/v1/security-rules",
               f"{strata}/config/security/v1/security-rules",
               {"folder": "Shared", "position": "pre"})

    console.print("  [dim]── Setup gateway (strata/config/setup/v1) ──[/dim]")
    _probe_url("GET /config/setup/v1/devices",
               f"{strata}/config/setup/v1/devices")
    _probe_url("GET /config/setup/v1/folders",
               f"{strata}/config/setup/v1/folders")

    console.print("  [dim]── IAM/Tenancy gateway (sase) ──[/dim]")
    _probe_url("GET /tenancy/v1/tenant_service_groups",
               f"{sase}/tenancy/v1/tenant_service_groups")

    any_ok       = any(ok for _, ok, _ in probe_results)
    all_ok_probes = all(ok for _, ok, _ in probe_results)
    ok_count     = sum(1 for _, ok, _ in probe_results if ok)
    tot_count    = len(probe_results)

    if not any_ok:
        err_codes = {note for _, ok, note in probe_results if not ok}
        is_forbidden    = any("403" in n for n in err_codes)
        is_unauthorized = any("401" in n for n in err_codes)
        if is_forbidden:
            console.print(
                f"\n  [red]✗[/red]  All probes returned 403 — token is valid but the\n"
                f"  service account has no read access to TSG [bold]{cfg.scm.tsg_id}[/bold].\n"
                f"  Check the role assignment in:\n"
                f"    SCM portal → Settings → Identity & Access → Service Accounts\n"
            )
        elif is_unauthorized:
            console.print(
                f"\n  [red]✗[/red]  All probes returned 401.\n"
                f"  Verify tsg_id [bold]{cfg.scm.tsg_id}[/bold] is correct.\n"
            )
    elif not all_ok_probes:
        failed_labels = [l for l, ok, _ in probe_results if not ok]
        console.print(
            f"\n  [dim]{ok_count}/{tot_count} probes succeeded.\n"
            f"  403s on: {', '.join(failed_labels)}\n"
            f"  This is normal if your service account role does not include those\n"
            f"  permissions (e.g. tenancy list requires a higher IAM role).[/dim]"
        )

    client.close()

    # ── SLS (Strata Logging Service) region info ──────────────────────────────
    import os as _os
    sls_region = _os.environ.get("ARC_SLS_REGION", "us")
    console.print(f"\n[bold cyan]6. SLS (Strata Logging Service)[/bold cyan]")
    console.print(
        f"  Region: [bold]{sls_region}[/bold]"
        + (" [dim](default)[/dim]" if sls_region == "us" else "")
    )
    if sls_region == "us":
        console.print(
            "  [dim]If your tenant is in a different region, set:\n"
            "    export ARC_SLS_REGION=nl    # Netherlands\n"
            "    export ARC_SLS_REGION=uk    # United Kingdom\n"
            "    export ARC_SLS_REGION=de    # Germany\n"
            "    export ARC_SLS_REGION=sg    # Singapore\n"
            "    export ARC_SLS_REGION=au    # Australia\n"
            "  Wrong region → 404 on 'show log' commands.[/dim]"
        )
    else:
        console.print(f"  [green]✓[/green] Custom region configured via ARC_SLS_REGION")

    # ── Summary ──────────────────────────────────────────────────────────────
    console.print()
    if not any_ok:
        console.print("[bold red]One or more checks failed.[/bold red]  See details above.")
        sys.exit(1)
    elif all_ok_probes:
        console.print("[bold green]All checks passed.[/bold green]")
    else:
        console.print(
            f"[bold green]Connected.[/bold green]  "
            f"{ok_count}/{tot_count} API probes succeeded."
        )


# ---------------------------------------------------------------------------
# config sub-command
# ---------------------------------------------------------------------------

config_app = typer.Typer(help="Manage the ARC config file.")
app.add_typer(config_app, name="config")

# Template written by `arc config generate`.
# _note fields are ignored by load_config() — they document the file for humans.
# config.json holds NON-secret settings only; auth values live in auth.json
# (with secrets in the OS keychain unless auth.storage = "file").
_CONFIG_TEMPLATE = {
    "_note": (
        "ARC config.json — NON-secret, sectioned. Auth values live in auth.json "
        "(run: arc setup scm  — or  arc auth configure). Secrets go to the OS keychain "
        "unless auth.storage is set to 'file'."
    ),
    "preferences": {
        "_note": "Per-user shell prefs (terminal, aliases, GUI theme). Managed via the terminal/alias commands.",
    },
    "auth": {
        "_note": "preferred_method: service|bearer · storage: keychain (secure) | file (plaintext auth.json)",
        "preferred_method": "service",
        "storage": "keychain",
        "active_profile": "default",
    },
    "gui": {
        "features": {"enabled": True, "port": 4445},
        "arc":      {"enabled": True, "port": 4444},
    },
    "profiles": {
        "default": {"default_folder": "Shared"},
    },
}


@config_app.command("generate")
def config_generate(
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite an existing config file."),
) -> None:
    """Generate a starter config.json with annotated placeholders and mode 0600.

    Creates the config directory if needed, writes template values, and sets
    file permissions to 0600 (owner read/write only).  Secrets are left blank
    or as REPLACE_WITH_* placeholders — run ``arc auth configure`` afterward to
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
        "  1. Run [bold]arc setup scm[/bold] (or [bold]arc auth configure[/bold]) to enter\n"
        "     credentials — they're saved to auth.json (secrets → keychain by default).\n"
        "  2. Run [bold]arc auth show[/bold] — confirm everything is configured.\n\n"
        "  Platform steps: [bold]arc setup osx[/bold] / [bold]arc setup win[/bold] / "
        "[bold]arc setup linux[/bold]."
    )


# ---------------------------------------------------------------------------
# cliup — offline browser docs bundle
# ---------------------------------------------------------------------------

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
    """Embed every doc page into docs/docs-bundle.js.

    Two sources: (1) all hand-written ``docs/*.md`` files, and (2) a
    registry-synthesized page for every command without a file, so the portal
    is a COMPLETE reference for all commands (generated + feature-gated ones
    included) — no stub files are written to disk.

    The bundle sets ``window.DOCS_CONTENT`` to a plain JS object keyed by
    relative path (e.g. ``"commands/cd.md"``).  Loading it with a plain
    ``<script src="docs-bundle.js">`` tag works under ``file://`` — no server
    or fetch() required.

    Returns the number of Markdown pages bundled (files + synthesized).
    """
    pages: dict[str, str] = {}
    for md_path in sorted(DOCS_ROOT.rglob("*.md")):
        rel = md_path.relative_to(DOCS_ROOT).as_posix()
        # The SCM API reference (docs/scm-api/) is developer/agent material —
        # large OpenAPI endpoint listings pulled by `docsupdate`.  Keep it out
        # of the user-facing browser bundle so the docs portal stays light.
        if rel.startswith("scm-api/"):
            continue
        # Strip YAML front-matter (structured help fields) so the portal shows
        # only the readable body, matching the in-shell `help <command>` view.
        from app.settings.command_help import parse_front_matter
        _meta, body = parse_front_matter(md_path.read_text(encoding="utf-8"))
        pages[rel] = body

    # Full synthesis: every registered command WITHOUT a hand-written file gets a
    # registry-synthesized page embedded here too, so the offline portal is a
    # COMPLETE reference for all ~4,900 commands — including generated ones that
    # are feature-gated off.  That lets someone browsing the docs discover a
    # command and see the feature flag they'd enable to use it.  No stub files
    # are created on disk; the synthesized Markdown lives only in this bundle.
    from app.commands.registry import COMMANDS
    from app.docs import slugify, synthesize_command_help, synthesize_builtin_help
    for key in COMMANDS:
        rel = f"commands/{slugify(key)}.md"
        if rel in pages:
            continue  # a hand-written file already covers this command
        pages[rel] = synthesize_command_help(key)

    # Shell builtins (cd, feature, watch, …) live outside the registry; synthesize
    # a page for each so the offline portal documents every shell command too.
    from app.settings.commands import load_builtin_docs
    for name in load_builtin_docs():
        rel = f"commands/{slugify(name)}.md"
        if rel in pages:
            continue  # hand-written or already synthesized
        page = synthesize_builtin_help(name)
        if page:
            pages[rel] = page

    # System aliases (sh, ls, conf …) are typeable too — give each a short page
    # pointing at its target so no shell input leads to a missing portal page.
    from app.docs import synthesize_alias_help
    from app.settings.aliases import load_system_aliases
    for name in load_system_aliases():
        rel = f"commands/{slugify(name)}.md"
        if rel in pages:
            continue
        page = synthesize_alias_help(name)
        if page:
            pages[rel] = page

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


def _do_cliup(silent: bool = False, skip_vendor: bool = False) -> dict:
    """Core cliup logic — rebuild the offline browser docs bundle.

    Doc FILES are owned by app/scripts/generate_command_docs.py (which prunes stubs —
    commands without a file get registry-synthesized help).  The bundle embeds
    those files PLUS a synthesized page for every file-less command, so the
    browser portal covers the full command set; it still never creates files.

    Returns a stats dict with keys: downloaded, bundled.
    """
    downloaded: list[str] = []
    if not skip_vendor:
        if not silent:
            console.print("[dim]Checking vendor files…[/dim]")
        downloaded = _ensure_vendor_files()

    if not silent:
        console.print("[dim]Building docs bundle…[/dim]")
    bundled = _build_docs_bundle()

    return {"downloaded": downloaded, "bundled": bundled}


@app.command("cliup")
def cliup() -> None:
    """Rebuild the offline browser docs bundle.

    Steps performed:
    1. Download vendor JS/CSS to docs/vendor/ (once; skipped if already present).
    2. Rebuild docs/docs-bundle.js — embeds all Markdown so the browser portal
       works via file:// with no server required.

    Command doc files and index.md are owned by app/scripts/generate_command_docs.py.
    """
    stats = _do_cliup(silent=False, skip_vendor=False)
    downloaded = stats["downloaded"]
    bundled = stats["bundled"]

    console.print(
        f"\n[bold cyan]cliup[/bold cyan]\n"
        f"  [cyan]vendor:[/cyan]   {len(downloaded)} file(s) downloaded"
        + (" (all present)" if not downloaded else "") + "\n"
        f"  [cyan]bundle:[/cyan]   docs/docs-bundle.js ({bundled} pages)\n"
    )


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
        console.print("[red]SCM is not configured.[/red] Run [bold]arc auth configure[/bold].")
        raise typer.Exit(1)

    client = SCMClient(cfg.scm)
    data = client.get(path, params={"folder": folder})
    console.print_json(json.dumps(data, indent=2))


# ---------------------------------------------------------------------------
# Entry-point called by run.py and the 'arc' console_script
# ---------------------------------------------------------------------------

def run() -> None:
    # Cisco-style: treat a bare `?` token as `--help` so `arc ?`,
    # `arc setup ?`, `arc auth ?` all print Typer help.
    import sys

    sys.argv[1:] = ["--help" if a == "?" else a for a in sys.argv[1:]]
    app()


if __name__ == "__main__":
    run()
