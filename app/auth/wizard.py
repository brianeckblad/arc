"""Shared interactive credential wizard.

One implementation of SCM credential capture + profile create/select/edit, used
by both the `arc` launcher (`arc auth configure`, `arc setup scm keystore`) and
the in-shell `scm setup` command — so the two surfaces never drift.

The wizard reads with plain ``input()`` / ``getpass`` and prints with Rich, which
works identically at a terminal (CLI) and inside the ARC REPL command dispatch.
"""
from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console

from app.config import (
    AUTH_FILE,
    CONFIG_FILE,
    ArcConfig,
    ConfigSecurityError,
    get_active_profile,
    has_configured_profiles,
    keychain_available,
    list_profiles,
    load_config,
    save_config,
    set_active_profile,
)
from app.docs import slugify

console = Console()
err_console = Console(stderr=True)


class WizardCancelled(Exception):
    """Raised inside a wizard prompt when the user hits Ctrl-C / Ctrl-D."""


def wizard_prompt(
    label: str,
    current: str = "",
    *,
    secret: bool = False,
    hint: str = "",
    out: "Console | None" = None,
) -> str:
    """Prompt for a value. Enter keeps the existing value; Ctrl-C/Ctrl-D aborts.

    ``out`` is the Console the label is printed to — pass the stderr console in
    --export mode so stdout carries only the export lines.
    """
    import getpass

    out = out or console
    display_current = "****" if (secret and current) else (current or "")
    display_hint = f" [dim][{display_current}][/dim]" if display_current else ""
    extra_hint = f"\n    [dim]{hint}[/dim]" if hint else ""
    out.print(f"  {label}{display_hint}{extra_hint}: ", end="")
    try:
        val = getpass.getpass("") if secret else input()
    except (EOFError, KeyboardInterrupt):
        raise WizardCancelled()
    # Empty input = keep existing value
    return val.strip() or current


def wizard_confirm(prompt: str, *, out: "Console | None" = None) -> bool:
    """Yes/No prompt (default No). Ctrl-C/Ctrl-D aborts the wizard."""
    out = out or console
    out.print(f"  {prompt} [dim][y/N][/dim]: ", end="")
    try:
        ans = input()
    except (EOFError, KeyboardInterrupt):
        raise WizardCancelled()
    return ans.strip().lower() in ("y", "yes")


def run_wizard_guarded(fn, *args, **kwargs):
    """Run a wizard function, turning a Ctrl-C/Ctrl-D abort into a clean exit.

    For the CLI: a cancel becomes ``typer.Exit(130)``.  In-shell callers should
    NOT use this — catch ``WizardCancelled`` directly so the REPL keeps running.
    """
    try:
        return fn(*args, **kwargs)
    except WizardCancelled:
        err_console.print("\n[yellow]Cancelled — nothing saved.[/yellow]")
        raise typer.Exit(130)


def select_or_create_profile(*, out: "Console | None" = None) -> Optional[str]:
    """Interactive profile picker for setup.

    Lists existing profiles (numbered) plus a "create new" option.  Returns:
      • the chosen existing profile name, or
      • a typed new profile name, or
      • ``None`` to create a new profile whose name is auto-derived from the
        account (``client_id`` stem) after credentials are entered.
    Raises ``WizardCancelled`` on Ctrl-C/D.
    """
    out = out or console
    profiles = list_profiles()
    active = get_active_profile()

    out.print("\n[bold cyan]SCM profiles[/bold cyan]  [dim](pick one to edit, or create new)[/dim]")
    for i, p in enumerate(profiles, start=1):
        mark = " [green](active)[/green]" if p.get("active") else ""
        cid = p.get("client_id") or "—"
        out.print(f"  [cyan]{i:<3}[/cyan][green]{p['name']:<22}[/green][dim]{cid}[/dim]{mark}")
    out.print(f"  [cyan]{'n':<3}[/cyan][green]{'Create a new profile':<22}[/green]")
    out.print()

    try:
        raw = input("  Edit #/name, or 'n' for new [active]: ").strip()
    except (EOFError, KeyboardInterrupt):
        raise WizardCancelled()

    if not raw:
        return active
    if raw.lower() in ("n", "new"):
        try:
            name = input("  New profile name (blank = derive from account): ").strip()
        except (EOFError, KeyboardInterrupt):
            raise WizardCancelled()
        return name or None
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(profiles):
            return profiles[idx]["name"]
        out.print(f"[red]Invalid number: {raw} (valid range 1–{len(profiles)})[/red]")
        raise WizardCancelled()
    # A typed name: existing → edit it; unknown → create it.
    return raw


def run_credential_wizard(
    profile: "str | None" = None,
    *,
    scm_bearer_token: Optional[str] = None,
    scm_client_id: Optional[str] = None,
    scm_secret: Optional[str] = None,
    scm_tsg: Optional[str] = None,
    ssh_user: Optional[str] = None,
    ssh_key: Optional[str] = None,
    out: "Console | None" = None,
) -> "str | None":
    """Interactive credential wizard — create or edit a profile's SCM/SSH creds.

    Profile resolution:
      • an explicit ``profile`` (not ``"default"``) always wins;
      • first-time setup (no profiles yet) stays ``"default"`` and is renamed
        after the account (``client_id`` stem);
      • otherwise the user picks an existing profile or "create new" via
        ``select_or_create_profile``.

    Returns the saved profile name (so callers can switch to it), or ``None`` if
    nothing was saved (e.g. a keychain write failure).  Raises ``WizardCancelled``
    if the user aborts.
    """
    out = out or console

    explicit = bool(profile) and profile != "default"
    derive = False   # derive the name from client_id after prompts
    known = {p["name"] for p in list_profiles()}

    if explicit:
        target = profile
    elif not has_configured_profiles():
        target, derive = "default", True
    else:
        sel = select_or_create_profile(out=out)
        if sel is None:
            target, derive = "default", True
        else:
            target = sel

    is_new = derive or (target not in known)

    # A brand-new profile must start blank — load_config() falls back to the
    # active profile for an unknown name, which would leak the active creds.
    cfg = ArcConfig() if is_new else load_config(profile=target)
    if is_new:
        cfg.profile_name = target
    kc = keychain_available()

    out.print("\n[bold cyan]ARC Credential Setup[/bold cyan]")
    if not is_new and target != "default":
        out.print(f"  Editing profile: [bold yellow]{target}[/bold yellow]")
    elif is_new and not derive:
        out.print(f"  New profile: [bold yellow]{target}[/bold yellow]")
    out.print(
        "  Press [bold]Enter[/bold] to keep an existing value.\n"
        "  Secrets are shown as [dim]****[/dim] when already stored.\n"
    )

    # ── Storage mode — where secrets live ────────────────────────────────────
    if kc:
        default_store = cfg.auth_storage if cfg.auth_storage in ("keychain", "file") else "keychain"
        choice = wizard_prompt(
            "Secret storage: keychain (recommended) or file",
            default_store,
            hint="'keychain' = OS secret store; 'file' = plaintext auth.json (mode 0600)",
            out=out,
        ).strip().lower()
        cfg.auth_storage = "file" if choice.startswith("f") else "keychain"
    else:
        out.print(
            "  [yellow]⚠  OS keychain unavailable on this system — using file storage.[/yellow]"
        )
        cfg.auth_storage = "file"

    if cfg.auth_storage == "keychain":
        out.print(
            f"\n  Secrets  → [green]OS keychain[/green]  (client_secret, SSH password)\n"
            f"  Config   → [dim]{CONFIG_FILE}[/dim]  (client_id, tsg_id, SSH user/key/port)\n"
        )
    else:
        out.print(
            f"\n  [yellow]Secrets  → plaintext {AUTH_FILE}[/yellow]  [dim](mode 0600)[/dim]\n"
            f"  Config   → [dim]{CONFIG_FILE}[/dim]  (client_id, tsg_id, SSH user/key/port)\n"
        )

    # ── SCM service account (primary auth method) ────────────────────────────
    out.print("[yellow]─ Strata Cloud Manager — Service Account ─[/yellow]")
    out.print(
        "  [dim]Your service account credentials come from the Palo Alto SCM portal.[/dim]\n"
        "  [dim]SCM portal → Settings → Identity & Access → Service Accounts → your account[/dim]\n"
    )

    cfg.scm.client_id = scm_client_id or wizard_prompt(
        "Client ID",
        cfg.scm.client_id,
        hint="From SCM portal: the service account email, e.g. pa-api-you@1234567890.iam.panserviceaccount.com",
        out=out,
    )
    cfg.scm.client_secret = scm_secret or wizard_prompt(
        "Client Secret",
        cfg.scm.client_secret,
        secret=True,
        hint="From SCM portal: the secret shown when you created or reset the service account",
        out=out,
    )
    cfg.scm.tsg_id = scm_tsg or wizard_prompt(
        "TSG ID",
        cfg.scm.tsg_id,
        hint="Your Tenant Services Group ID — the number in your SCM URL or service account name",
        out=out,
    )

    # ── Bearer token (advanced / optional) ───────────────────────────────────
    out.print(
        "\n[yellow]─ Bearer Token (optional — leave blank if using client credentials above) ─[/yellow]"
    )
    out.print(
        "  [dim]Only needed for pre-issued tokens or testing.  ARC prefers client credentials.[/dim]\n"
    )
    cfg.scm.bearer_token = scm_bearer_token or wizard_prompt(
        "Bearer Token",
        cfg.scm.bearer_token,
        secret=True,
        hint="Leave blank to have ARC generate tokens automatically from your client credentials",
        out=out,
    )

    # ── SSH Defaults ─────────────────────────────────────────────────────────
    out.print("\n[yellow]─ SSH Defaults ─[/yellow]")
    cfg.ssh.user = ssh_user or wizard_prompt(
        "SSH Username",
        cfg.ssh.user,
        hint="Username for SSH sessions to managed devices (default: admin)",
        out=out,
    )
    cfg.ssh.key_path = ssh_key or wizard_prompt(
        "SSH Key Path",
        cfg.ssh.key_path,
        hint="Path to your SSH private key, e.g. ~/.ssh/id_ed25519 (leave blank to use password)",
        out=out,
    )
    cfg.ssh.password = wizard_prompt(
        "SSH Password",
        cfg.ssh.password,
        secret=True,
        hint="Leave blank if using key auth or SSH agent",
        out=out,
    )

    # ── Effective profile name ───────────────────────────────────────────────
    # First-time / derive-new: name the profile after the account (client_id
    # stem, matching the shell prompt's account label) so it is meaningful.
    effective = target
    if derive:
        stem = (cfg.scm.client_id or "").split("@")[0]
        d = slugify(stem) if stem else ""
        if d:
            effective = d
    cfg.profile_name = effective

    try:
        save_config(cfg, profile=effective)
    except ConfigSecurityError as exc:
        out.print(f"\n[yellow]⚠[/yellow] {exc}")
        out.print(
            f"[green]✓[/green] Non-sensitive config saved to [bold]{CONFIG_FILE}[/bold]  "
            "[dim](mode 0600)[/dim]"
        )
        return None

    set_active_profile(effective)

    profile_label = f" (profile: [bold]{effective}[/bold])" if effective != "default" else ""
    if cfg.auth_storage == "keychain":
        out.print(
            f"\n[green]✓[/green] Secrets saved to OS keychain{profile_label}\n"
            f"[green]✓[/green] Config file: [bold]{CONFIG_FILE}[/bold]  [dim](mode 0600)[/dim]\n"
        )
    else:
        out.print(
            f"\n[green]✓[/green] Config saved{profile_label} — secrets in [bold]{AUTH_FILE}[/bold]  "
            "[dim](plaintext, mode 0600)[/dim]\n"
        )

    if effective != "default":
        out.print(
            f"Active profile is now [bold yellow]{effective}[/bold yellow] — "
            f"switch anytime with [bold]scm login {effective}[/bold]\n"
        )

    # Auto-verify credentials immediately so mistakes surface right away.
    if cfg.scm.is_configured:
        out.print("[dim]Verifying credentials…[/dim]")
        try:
            from app.api.client import SCMClient
            SCMClient(cfg.scm)
            out.print("[green]✓[/green] SCM credentials verified — token obtained successfully.\n")
        except Exception as exc:  # noqa: BLE001
            out.print(
                f"[yellow]⚠  Credential check failed:[/yellow] {exc}\n"
                "  Credentials were saved. Run [bold]arc auth test[/bold] for a full diagnostic,\n"
                "  or re-run setup to correct the values.\n"
            )
    else:
        out.print(
            "Run [bold]arc auth test[/bold] to verify your credentials work end-to-end."
        )

    return effective
