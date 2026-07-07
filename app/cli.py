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
    delete_profile,
    get_active_profile,
    keychain_available,
    list_profiles,
    load_config,
    save_config,
)
from app.docs import DOCS_ROOT, open_docs_in_browser
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

    Use --profile to create or update a named profile (e.g. --profile readwrite).
    Switch between profiles inside the ARC shell with the `account` command.

    Press Enter to keep any value that is already stored.
    """
    cfg = load_config(profile=profile)
    kc = keychain_available()

    console.print("\n[bold cyan]ARC Credential Setup[/bold cyan]")
    if profile != "default":
        console.print(f"  Profile: [bold yellow]{profile}[/bold yellow]")
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
        save_config(cfg, profile=profile)
    except ConfigSecurityError as exc:
        console.print(f"\n[yellow]⚠[/yellow] {exc}")
        console.print(
            f"[green]✓[/green] Non-sensitive config saved to [bold]{CONFIG_FILE}[/bold]  "
            "[dim](mode 0600)[/dim]"
        )
        raise typer.Exit(1) from exc

    if kc:
        profile_label = f" (profile: [bold]{profile}[/bold])" if profile != "default" else ""
        console.print(
            f"\n[green]✓[/green] Secrets saved to OS keychain{profile_label}\n"
            f"[green]✓[/green] Config file: [bold]{CONFIG_FILE}[/bold]  [dim](mode 0600)[/dim]\n"
        )
    else:
        console.print(
            f"\n[green]✓[/green] Non-sensitive config saved to [bold]{CONFIG_FILE}[/bold]  "
            "[dim](mode 0600)[/dim]\n"
        )

    if profile != "default":
        console.print(
            f"Switch to this profile in ARC with: [bold]account {profile}[/bold]\n"
        )

    # Auto-verify credentials immediately so the operator knows right away
    # if something was entered incorrectly, without needing a separate command.
    if cfg.scm.is_configured:
        console.print("[dim]Verifying credentials…[/dim]")
        try:
            from app.api.client import SCMClient
            SCMClient(cfg.scm)
            console.print("[green]✓[/green] SCM credentials verified — token obtained successfully.\n")
        except Exception as exc:
            console.print(
                f"[yellow]⚠  Credential check failed:[/yellow] {exc}\n"
                "  Credentials were saved. Run [bold]arc auth test[/bold] for a full diagnostic,\n"
                "  or re-run [bold]arc auth configure[/bold] to correct the values.\n"
            )
    else:
        console.print(
            "Run [bold]arc auth test[/bold] to verify your credentials work end-to-end."
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
_CONFIG_TEMPLATE = {
    "_note": (
        "ARC config — fill in non-secret REPLACE_WITH_* values, then run: arc auth configure  "
        "(secrets are prompted securely and stored in the OS keychain)"
    ),
    "scm": {
        "_note": (
            "Use bearer_token OR OAuth. Do not put secrets in this file; leave bearer_token "
            "and client_secret blank and enter them via arc auth configure or env vars."
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
        f"  1. Edit the file and replace [cyan]REPLACE_WITH_*[/cyan] values:\n"
        f"       [dim]{CONFIG_FILE}[/dim]\n"
        "  2. Run [bold]arc auth configure[/bold] — migrates secrets to the OS keychain\n"
        "  3. Run [bold]arc auth show[/bold]  — confirm everything is configured\n\n"
        "  See [bold]help config osx[/bold] / [bold]help config win[/bold] / "
        "[bold]help config nix[/bold] for platform-specific keychain CLI commands."
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
    commands without a file get registry-synthesized help). cliup only bundles
    what exists for the browser portal; it never creates command docs.

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
    app()


if __name__ == "__main__":
    run()
