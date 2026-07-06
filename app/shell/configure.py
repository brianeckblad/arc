"""ArcShell configure mixin — configure mode, cli theme, feature flags."""
from __future__ import annotations

import platform  # For OS detection in setup wizard
import threading  # commit-confirmed auto-revert timer

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


def _prefs_file_label() -> str:
    """Repo-relative path of the preferences file, for display."""
    from app.settings.user_prefs import PREFS_FILE
    try:
        return str(PREFS_FILE.relative_to(PREFS_FILE.parents[2]))
    except (ValueError, IndexError):
        return str(PREFS_FILE)


def capture_write_ops(scm, handler, ctx, args) -> list[dict]:
    """Run a write handler against a recording client and capture its mutations.

    GET requests pass through to SCM unchanged — that is the validation step
    (name→id resolution, existence checks, folder lookups all really run).
    POST/PUT/PATCH/DELETE requests are captured instead of sent; the handler
    receives a synthetic response so it can finish normally.  Returns the
    captured operations for later replay by ``commit``.
    """
    captured: list[dict] = []
    real_request = scm._request

    def _recording(method, base_url, path, *, params=None, json=None):
        if method.upper() == "GET":
            return real_request(method, base_url, path, params=params, json=json)
        captured.append({
            "method": method.upper(),
            "base_url": base_url,
            "path": path,
            "params": params,
            "json": json,
        })
        # Synthetic response — enough for handlers that read an id/name back.
        return {"id": "(staged)", "name": "(staged)"}

    scm._request = _recording
    try:
        handler(ctx, args)
    finally:
        scm._request = real_request
    return captured


class ConfigureMixin:
    def _cmd_configure(self, args: list[str]) -> None:
        """Enter configure mode (Cisco-style).

        In configure mode, 'set' creates objects and 'exit' leaves configure mode.
        """
        if args and args[0].lower() not in ("t", "terminal"):
            console.print(
                "[yellow]Usage:[/yellow] configure | conf | conf t\n"
                "  Then use [bold]set[/bold] to create objects, [bold]cli[/bold] for theme operations."
            )
            return

        if self._state.configure_mode:
            console.print("[dim]Already in configure mode.[/dim]")
            return

        self._state.configure_mode = True
        self._state.device = None
        self._state.folder = "Shared"
        for line in _configure_banner().splitlines():
            console.print(f"[green]{line.strip()}[/green]" if line.strip() else "")

    def _stage_write(self, key: str, cmd_def: CommandDef, ctx: ExecutionContext, args: dict) -> None:
        """Validate a configure-mode write and stage it locally (no SCM change).

        Runs the command's real handler against a recording client — read
        calls pass through (so name→id resolution and existence checks really
        validate against SCM), mutating calls are captured. The captured
        operations are replayed later by ``commit``.
        """
        if ctx.scm is None:
            cmd_def.api_handler(ctx, args)  # raises the standard "SCM is not configured"
            return
        ops = capture_write_ops(ctx.scm, cmd_def.api_handler, ctx, args)
        if not ops:
            console.print(
                f"[yellow]'{key}' made no configuration change — nothing staged.[/yellow]"
            )
            return
        detail = str(args.get("name") or (args.get("_positional") or [""])[0] or "").strip()
        # args are kept so `commit check` can re-run validation later.
        self._state.staged_ops.append(
            {"command": key, "detail": detail, "folder": ctx.folder, "args": args, "ops": ops}
        )
        shown = f"{key} {detail}".strip()
        console.print(
            f"[green]✓[/green] Validated and staged: [bold]{shown}[/bold]  "
            f"[dim]({len(self._state.staged_ops)} pending — "
            "show config to review, commit to apply)[/dim]"
        )

    def _cmd_show_pending(self) -> None:
        """List the locally staged configure-mode changes (`show config`)."""
        staged = self._state.staged_ops
        if not staged:
            console.print(
                "[dim]No staged changes. Configure-mode writes queue here until commit.[/dim]"
            )
            return
        rows = [
            {
                "#": str(index),
                "command": f"{entry['command']} {entry['detail']}".strip(),
                "folder": entry["folder"],
                "api": "; ".join(f"{op['method']} {op['path']}" for op in entry["ops"]),
            }
            for index, entry in enumerate(staged, 1)
        ]
        console.print(fmt._list_table(rows, title=f"Staged changes ({len(staged)}) — local, not yet in SCM"))
        console.print(
            "[dim]Staged changes are not visible in show output until commit.  "
            "commit → apply all  |  abandon → discard all[/dim]"
        )

    def _cmd_abandon(self, args: list[str]) -> None:
        """Discard all locally staged changes (configure mode only)."""
        del args
        if not self._state.configure_mode:
            console.print(
                "[yellow]abandon is a configure-mode command.[/yellow] "
                "Enter [bold]configure[/bold] first."
            )
            return
        count = len(self._state.staged_ops)
        if count == 0:
            console.print("[dim]No staged changes to abandon.[/dim]")
            return
        answer = console.input(
            f"Discard {count} staged change(s)? They were never sent to SCM. [y/N] "
        ).strip().lower()
        if answer not in ("y", "yes"):
            console.print("[dim]Cancelled — staged changes kept.[/dim]")
            return
        self._state.staged_ops = []
        console.print("[green]✓[/green] Staged changes discarded — SCM was never touched.")

    # ------------------------------------------------------------------
    # commit confirmed — Junos-style auto-revert safety net
    # ------------------------------------------------------------------

    def _rollback_version(self) -> int | None:
        """Version number of the CURRENT running config (the revert target)."""
        try:
            data = self._scm._request(
                "GET", self._scm.OPERATIONS_URL, "/config-versions/running"
            )
        except Exception:  # noqa: BLE001 — caller refuses to arm without a target
            return None
        records = data.get("data") if isinstance(data, dict) and isinstance(data.get("data"), list) else data
        if isinstance(records, dict):
            records = [records]
        for record in records or []:
            version = record.get("version")
            if isinstance(version, int):
                return version
            if isinstance(version, str) and version.isdigit():
                return int(version)
        return None

    def _arm_commit_confirmed(self, minutes: int, version: int) -> None:
        self._cancel_commit_confirmed(silent=True)
        timer = threading.Timer(minutes * 60, self._commit_confirmed_expired)
        timer.daemon = True
        self._pending_confirm = {"timer": timer, "version": version, "minutes": minutes}
        timer.start()
        console.print(
            f"[yellow]⏱ commit confirmed:[/yellow] auto-revert to config version "
            f"[bold]{version}[/bold] in [bold]{minutes} min[/bold] unless you type "
            "[bold]commit confirm[/bold]."
        )

    def _cancel_commit_confirmed(self, silent: bool = False) -> bool:
        pending = getattr(self, "_pending_confirm", None)
        if not pending:
            if not silent:
                console.print("[dim]No commit awaiting confirmation.[/dim]")
            return False
        pending["timer"].cancel()
        self._pending_confirm = None
        if not silent:
            console.print(
                "[green]✓ Commit confirmed[/green] — changes are permanent; auto-revert cancelled."
            )
        return True

    def _commit_confirmed_expired(self) -> None:
        """Timer thread: the operator never confirmed — revert and re-push."""
        pending = getattr(self, "_pending_confirm", None)
        if not pending:
            return
        self._pending_confirm = None
        version = pending["version"]
        console.print(
            f"\n[red]⏱ commit confirmed EXPIRED[/red] — loading config version "
            f"[bold]{version}[/bold] and pushing the revert…"
        )
        try:
            self._scm._request(
                "POST", self._scm.OPERATIONS_URL, "/config-versions:load",
                json={"version": version},
            )
            job = self._scm.push_config(
                description=f"arc auto-revert to v{version} (commit confirmed expired)"
            )
            job_id = job.get("id") or job.get("job_id") or "?"
            console.print(
                f"[yellow]Auto-revert push started (job {job_id}).[/yellow] "
                "Next time: [bold]commit confirm[/bold] within the window."
            )
        except Exception as exc:  # noqa: BLE001 — a failed revert must be LOUD
            console.print(
                f"[red]AUTO-REVERT FAILED:[/red] {exc}\n"
                f"  Manual recovery: [bold]load config version {version} confirm[/bold], then [bold]commit[/bold]."
            )

    def _cmd_commit_staged(self, args: list[str]) -> None:
        """Apply all staged changes to SCM, then push the candidate to devices.

        ``commit`` — apply + push, print the job ID.
        ``commit watch`` — same, then poll the push job until it finishes.
        ``commit confirmed [minutes]`` — push, then AUTO-REVERT to the current
        running version unless ``commit confirm`` arrives in time (default 10).
        ``commit confirm`` — make a pending confirmed-commit permanent.
        ``commit check`` — re-validate staged changes without applying.
        All accept a trailing ``description <text>``.
        """
        tokens = list(args)
        if tokens and tokens[0].lower() == "check":
            self._commit_check()
            return
        if tokens and tokens[0].lower() == "confirm":
            self._cancel_commit_confirmed()
            return
        confirmed_minutes = 0
        if tokens and tokens[0].lower() == "confirmed":
            tokens.pop(0)
            confirmed_minutes = 10
            if tokens and tokens[0].isdigit():
                confirmed_minutes = max(1, min(120, int(tokens[0])))
                tokens.pop(0)
        watch = bool(tokens) and tokens[0].lower() == "watch"
        if watch:
            tokens.pop(0)
        if tokens and tokens[0].lower() == "description":
            tokens.pop(0)
        description = " ".join(tokens).strip().strip('"')

        if not self._scm:
            console.print("[red]SCM not connected — cannot commit.[/red]")
            return

        # commit confirmed: capture the revert target BEFORE anything changes.
        rollback_version: int | None = None
        if confirmed_minutes:
            rollback_version = self._rollback_version()
            if rollback_version is None:
                console.print(
                    "[red]Cannot determine the current running config version — "
                    "refusing to arm auto-revert.[/red]\n"
                    "  Run a plain [bold]commit[/bold], or check [bold]show config versions[/bold]."
                )
                return

        staged = self._state.staged_ops
        applied = 0
        if staged:
            total = len(staged)
            console.print(f"Applying {total} staged change(s) to SCM…")
            for index, entry in enumerate(staged, 1):
                label = f"{entry['command']} {entry['detail']}".strip()
                try:
                    for op in entry["ops"]:
                        self._scm._request(
                            op["method"], op["base_url"], op["path"],
                            params=op["params"], json=op["json"],
                        )
                except Exception as exc:  # noqa: BLE001 — report, keep the rest staged
                    self._state.staged_ops = staged[index - 1:]
                    console.print(
                        f"  [red]✗[/red] {index}/{total}  {label} — {exc}\n"
                        f"[yellow]{applied} change(s) applied; "
                        f"{len(self._state.staged_ops)} still staged (push skipped).[/yellow]\n"
                        "  Fix or [bold]abandon[/bold] the failing change, then commit again."
                    )
                    return
                console.print(f"  [green]✓[/green] {index}/{total}  {label}")
                applied += 1
            self._state.staged_ops = []
        else:
            console.print("[dim]No staged changes — pushing the existing SCM candidate config.[/dim]")

        folder = self._state.folder
        folders = [folder] if folder and folder.lower() != "shared" else None
        try:
            job = self._scm.push_config(folders=folders, description=description)
        except Exception as exc:  # noqa: BLE001
            console.print(
                f"[red]Push failed:[/red] {exc}\n"
                f"[yellow]{applied} applied change(s) are in the SCM candidate config — "
                "run [bold]commit[/bold] again to retry the push.[/yellow]"
            )
            return
        console.print(fmt.format_jobs([job] if isinstance(job, dict) else job))
        job_id = str(job.get("id") or job.get("job_id") or "") if isinstance(job, dict) else ""
        # Arm the auto-revert BEFORE watch — the countdown must run while the
        # operator verifies they still have connectivity to what they changed.
        if confirmed_minutes and rollback_version is not None:
            self._arm_commit_confirmed(confirmed_minutes, rollback_version)
        if watch and job_id:
            self._watch_job(job_id)
        elif job_id:
            console.print(
                f"[dim]Track with: [bold]show jobs id {job_id}[/bold]  "
                "(or use [bold]commit watch[/bold] next time)[/dim]"
            )

    def _commit_check(self) -> None:
        """Re-validate every staged change against CURRENT SCM state (Junos-style).

        The world can change between staging and commit — a colleague may have
        deleted the object your update targets. Each entry's handler is re-run
        through the recording client (fresh GETs, no mutations); entries that
        still validate get their captured ops refreshed (ids re-resolved),
        failures are reported and left staged for the operator to fix or abandon.
        """
        staged = self._state.staged_ops
        if not staged:
            console.print("[dim]No staged changes to check.[/dim]")
            return
        if not self._scm:
            console.print("[red]SCM not connected — cannot validate.[/red]")
            return
        failures = 0
        for index, entry in enumerate(staged, 1):
            label = f"{entry['command']} {entry['detail']}".strip()
            cmd_def = COMMANDS.get(entry["command"])
            if cmd_def is None or cmd_def.api_handler is None:
                failures += 1
                console.print(f"  [red]✗[/red] {index}/{len(staged)}  {label} — command no longer registered")
                continue
            ctx = ExecutionContext(
                scm=self._scm, ssh=self._ssh, config=self._config,
                device=self._state.device, folder=entry["folder"],
                tsg_id=self._state.tsg_id,
            )
            try:
                entry["ops"] = capture_write_ops(
                    self._scm, cmd_def.api_handler, ctx, entry.get("args") or {}
                )
                console.print(f"  [green]✓[/green] {index}/{len(staged)}  {label}")
            except Exception as exc:  # noqa: BLE001 — each failure reported individually
                failures += 1
                console.print(f"  [red]✗[/red] {index}/{len(staged)}  {label} — {exc}")
        if failures:
            console.print(
                f"[yellow]commit check: {failures} of {len(staged)} staged change(s) no longer valid.[/yellow]\n"
                "  Fix or [bold]abandon[/bold] before committing."
            )
        else:
            console.print(f"[green]commit check: all {len(staged)} staged change(s) valid.[/green]")

    def _watch_job(self, job_id: str, timeout_s: int = 900) -> None:
        """Poll a push job every few seconds until it finishes (or timeout)."""
        deadline = time.monotonic() + timeout_s
        job: dict = {}
        try:
            with console.status(f"[dim]commit job {job_id} running…[/dim]", spinner="dots"):
                while time.monotonic() < deadline:
                    job = self._scm.get_job(job_id) or {}
                    if str(job.get("status", "")).upper() == "FIN":
                        break
                    time.sleep(5)
        except Exception as exc:  # noqa: BLE001 — polling must never crash the shell
            console.print(f"[yellow]Stopped watching job {job_id}:[/yellow] {exc}")
            return
        if str(job.get("status", "")).upper() != "FIN":
            console.print(
                f"[yellow]Job {job_id} still running after {timeout_s // 60} min[/yellow] — "
                f"check later with [bold]show jobs id {job_id}[/bold]"
            )
            return
        result = str(job.get("result", "")).upper()
        if result == "OK":
            console.print(f"[green]✓ Commit job {job_id} finished: OK[/green]")
        else:
            console.print(
                f"[red]✗ Commit job {job_id} finished: {result or 'unknown'}[/red] — "
                f"details: [bold]show jobs id {job_id}[/bold]"
            )

    def _confirm_configure_exit(self) -> bool:
        """Ask what to do with staged changes when leaving configure mode.

        Returns True when the operator may leave (changes committed, abandoned,
        or none staged); False to stay in configure mode.
        """
        count = len(self._state.staged_ops)
        if count == 0:
            return True
        console.print(
            f"\n[yellow]Uncommitted changes:[/yellow] {count} staged locally — nothing has been sent to SCM.\n"
            "  [bold]commit[/bold]   — apply the changes and push to managed devices\n"
            "  [bold]abandon[/bold]  — discard the staged changes (SCM untouched)\n"
            "  [bold]cancel[/bold]   — stay in configure mode\n"
        )
        while True:
            answer = console.input("configure exit (commit/abandon/cancel): ").strip().lower()
            if answer == "commit":
                self._cmd_commit_staged([])
                return not self._state.staged_ops
            if answer == "abandon":
                self._state.staged_ops = []
                console.print("[green]✓[/green] Staged changes discarded — SCM was never touched.")
                return True
            if answer in ("cancel", ""):
                console.print("[dim]Staying in configure mode.[/dim]")
                return False
            console.print("[dim]Type commit, abandon, or cancel.[/dim]")

    def _cmd_terminal(self, args: list[str]) -> None:
        """Per-user terminal preferences — persisted to config/<user>/preferences.json.

        terminal                     show current settings and how to change them
        terminal length <n>          page long output after n lines (0 = never page)
        terminal width <n>           force render width in columns (0 = auto-detect)
        terminal spinner on|off      toggle the "querying SCM…" spinner
        """
        p = self._prefs
        t = self._theme

        if not args or args[0] in ("?", "help"):
            length_note = f"{p.terminal_length} lines" if p.terminal_length else "off  (no paging)"
            width_note  = f"{p.terminal_width} columns" if p.terminal_width else "auto-detect"
            spinner_note = "on" if p.spinner else "off"
            w = 30
            console.print(
                f"\n  [bold]Terminal Settings[/bold]  "
                f"[dim]{_prefs_file_label()}[/dim]\n"
            )
            # Current values
            console.print(f"  [dim]{'Setting':<{w}} Current     How to change[/dim]")
            console.print(f"  [dim]{'─' * (w + 40)}[/dim]")
            console.print(
                f"  {self._styled(f'terminal length', t.command_name):<{w+10}} "
                f"{length_note:<12} "
                f"[dim]terminal length <n>   (0 = disable paging)[/dim]"
            )
            console.print(
                f"  {self._styled(f'terminal width', t.command_name):<{w+10}} "
                f"{width_note:<12} "
                f"[dim]terminal width <n>    (0 = auto-detect)[/dim]"
            )
            console.print(
                f"  {self._styled(f'terminal spinner', t.command_name):<{w+10}} "
                f"{spinner_note:<12} "
                f"[dim]terminal spinner on|off[/dim]"
            )
            console.print()
            console.print(
                "  [dim]Examples:\n"
                "    terminal length 40    → page after 40 lines (good for slow reading)\n"
                "    terminal length 0     → disable paging entirely\n"
                "    terminal width 120    → force 120-column output\n"
                "    terminal spinner off  → remove the spinner (e.g. for CI / scripting)[/dim]"
            )
            console.print()
            return

        sub = args[0].lower()

        if sub == "length":
            if len(args) < 2:
                console.print(
                    "[yellow]Usage:[/yellow] terminal length <n>\n"
                    "  [dim]0 = disable paging entirely\n"
                    f"  Current: {p.terminal_length or 0}[/dim]"
                )
                return
            if not args[1].isdigit():
                console.print("[yellow]Usage:[/yellow] terminal length <n>  (whole number, 0 = no paging)")
                return
            value = int(args[1])
            p.terminal_length = value
            set_page_length(value)
            note = f"paging after {value} lines" if value else "paging disabled"

        elif sub == "width":
            if len(args) < 2:
                console.print(
                    "[yellow]Usage:[/yellow] terminal width <n>\n"
                    "  [dim]0 = auto-detect from your terminal window\n"
                    f"  Current: {p.terminal_width or 0}[/dim]"
                )
                return
            if not args[1].isdigit():
                console.print("[yellow]Usage:[/yellow] terminal width <n>  (whole number, 0 = auto)")
                return
            value = int(args[1])
            p.terminal_width = value
            console.width = value if value > 0 else None
            note = f"render width {value} columns" if value else "auto-detect width"

        elif sub == "spinner":
            state = (args[1].lower() if len(args) > 1 else "").strip()
            if state not in ("on", "off"):
                console.print(
                    "[yellow]Usage:[/yellow] terminal spinner on|off\n"
                    f"  [dim]Current: {'on' if p.spinner else 'off'}[/dim]"
                )
                return
            p.spinner = state == "on"
            note = f"spinner {state}"

        else:
            console.print(
                f"[yellow]Unknown terminal setting:[/yellow] [bold]{sub}[/bold]\n\n"
                "  terminal length <n>       page after n lines  [dim](0 = off)[/dim]\n"
                "  terminal width <n>        force column width  [dim](0 = auto)[/dim]\n"
                "  terminal spinner on|off   show/hide spinner\n"
            )
            return

        saved = save_prefs(p)
        suffix = "" if saved else "  [yellow](preferences.json not writable — applies to this session only)[/yellow]"
        console.print(f"[green]✓[/green] {note}{suffix}")

    def _cmd_cli(self, args: list[str]) -> None:
        """Read/write CLI theme settings (configure mode only)."""
        if not self._state.configure_mode:
            console.print(
                "[yellow]Write operation blocked:[/yellow] enter [bold]configure[/bold] mode first.\n"
                "  Then use: [bold]cli show[/bold], [bold]cli color <key> <style>[/bold], [bold]cli reset[/bold]."
            )
            return

        t = self._theme
        sub = args[0].lower() if args else "show"

        if sub == "show":
            console.print()
            console.print("  [bold]ARC CLI Theme[/bold]  [dim](settings/theme.json)[/dim]")
            console.print()
            for key, label in THEME_KEYS.items():
                current = getattr(t, key)
                display = self._styled(f"  {current or '(none)'}  ", current) if current else "[dim](none)[/dim]"
                console.print(f"    [cyan]{key:<28}[/cyan] {display}  [dim]{label}[/dim]")
            console.print()
            console.print("  [dim]cli color <key> <style>  → change colour  |  cli reset  → defaults[/dim]")
            console.print()
            return

        if sub == "color":
            if len(args) < 2:
                console.print(
                    "[yellow]Usage:[/yellow] cli color <key> <style>\n"
                    f"  Keys: {', '.join(THEME_KEYS)}"
                )
                return
            key = args[1].lower()
            if not hasattr(self._theme, key):
                console.print(
                    f"[yellow]Unknown theme key:[/yellow] {key!r}\n"
                    f"  Valid keys: {', '.join(THEME_KEYS)}"
                )
                return
            style = " ".join(args[2:])
            setattr(self._theme, key, style)
            save_theme(self._theme)
            preview = self._styled(f"  {style or '(none)'}  ", style) if style else "[dim](none)[/dim]"
            console.print(f"[green]✓[/green] {key} = {preview}  [dim](saved to settings/theme.json)[/dim]")
            return

        if sub == "reset":
            self._theme = reset_theme()
            console.print("[green]✓[/green] Theme reset to defaults  [dim](saved to settings/theme.json)[/dim]")
            return

        console.print(
            f"[yellow]Unknown cli subcommand:[/yellow] {sub!r}\n"
            "  Usage: cli show | cli color <key> <style> | cli reset"
        )

    def _cmd_feature(self, args: list[str]) -> None:
        """Show or change feature-flag states at runtime.

        Subcommands:
          feature show                 — list all flags grouped ON / DEV / OFF
          feature show on|off|dev      — list only flags in one state
          feature show <name>          — list flags matching a name fragment
          feature find <text>          — search flags AND the commands they gate
          feature enable <flag>        — set a flag ON (saved to its settings/features/ file)
          feature disable <flag>       — set a flag OFF (saved)
          feature dev <flag>           — mark a flag DEV (saved)
          feature ?                    — show this usage summary

        Flag states: ON (everyone), DEV (only in development mode — see the
        hidden 'dev' command), OFF (hidden for everyone).  Changes take effect
        immediately and are persisted to the flag's own file under
        settings/features/ (the per-domain glossary).
        """
        sub = args[0].lower() if args else "show"

        # ── ? suffix handling ─────────────────────────────────────────────────
        if sub == "?":
            console.print()
            console.print(f"  [bold yellow]feature[/bold yellow]  [dim]— feature flag management[/dim]")
            console.print()
            console.print(f"  [cyan]feature show[/cyan]           List all flags grouped ON / DEV / OFF")
            console.print(f"  [cyan]feature show on[/cyan]        List only enabled flags")
            console.print(f"  [cyan]feature show off[/cyan]       List only disabled flags")
            console.print(f"  [cyan]feature show dev[/cyan]       List only development flags")
            console.print(f"  [cyan]feature show <name>[/cyan]    Show matching feature flag(s)")
            console.print(f"  [cyan]feature enable <flag>[/cyan]  Set a flag ON and save")
            console.print(f"  [cyan]feature disable <flag>[/cyan] Set a flag OFF and save")
            console.print(f"  [cyan]feature dev <flag>[/cyan]     Mark a flag DEV and save")
            console.print(f"  [cyan]feature help[/cyan]           Open full feature flag documentation")
            console.print()
            console.print(f"  [dim]DEV flags appear only after you type [bold]dev[/bold] to enter development mode.[/dim]")
            console.print(f"  [dim]feature enable ?  → flags not yet ON   |   feature disable ?  → flags not yet OFF[/dim]")
            console.print()
            return

        # Helper: build flag→commands reverse map (used by show and enable/disable ?)
        def _flag_to_cmds() -> dict[str, list[str]]:
            result: dict[str, list[str]] = {}
            for cmd_key, cmd_def in COMMANDS.items():
                if cmd_def.feature_flag:
                    result.setdefault(cmd_def.feature_flag, []).append(cmd_key)
            return result

        # The universe of known flags = those in settings/features/ plus any
        # referenced by a command in the registry (so newly-added flags appear).
        def _all_flags() -> list[str]:
            names = set(self._features) | set(_flag_to_cmds())
            return sorted(names)

        def _persist_feature_state(flag_name: str, state: str) -> None:
            """Write one flag state to its owning settings/features/ file."""
            import json  # Deferred: used only when changing a feature flag.

            from app.settings.features import feature_file_for

            target = feature_file_for(flag_name)
            try:
                raw = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}
            except (json.JSONDecodeError, OSError) as exc:
                raise RuntimeError(f"Could not read {target.name}: {exc}") from exc
            if not isinstance(raw, dict):
                raise RuntimeError(f"{target.name} must contain a JSON object")

            raw_value: bool | str
            if state == "on":
                raw_value = True
            elif state == "dev":
                raw_value = "dev"
            else:
                raw_value = False

            raw[flag_name] = raw_value
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(raw, indent=2) + "\n", encoding="utf-8")
            except OSError as exc:
                raise RuntimeError(f"Could not write {target.name}: {exc}") from exc
            self._features[flag_name] = state
            self._invalidate_visible_keys()

        def _print_feature_rows(title: str, flags: list[str], colour: str, flag_cmds: dict[str, list[str]]) -> None:
            """Print a compact flag list with command mappings."""
            console.print(f"\n  [bold {colour}]{title}[/bold {colour}]  [dim]({len(flags)})[/dim]")
            if not flags:
                console.print("    [dim]No matching flags.[/dim]")
                return
            for flag in flags:
                state = feature_state(self._features, flag)
                cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                console.print(f"    {flag:<35} [{colour}]{state}[/{colour}]  [dim]{cmds}[/dim]")

        if sub in ("enable", "disable", "dev") and len(args) >= 2 and args[1] == "?":
            flag_cmds = _flag_to_cmds()
            console.print()
            if sub == "enable":
                candidates = [f for f in _all_flags() if feature_state(self._features, f) != "on"]
                console.print(f"  [bold yellow]feature enable <flag>[/bold yellow]  [dim]— flags not yet ON[/dim]")
                console.print(f"  [dim]  Saves immediately to the flag's settings/features/ file[/dim]")
            elif sub == "dev":
                candidates = [f for f in _all_flags() if feature_state(self._features, f) != "dev"]
                console.print(f"  [bold yellow]feature dev <flag>[/bold yellow]  [dim]— flags not yet DEV[/dim]")
            else:
                candidates = [f for f in _all_flags() if feature_state(self._features, f) != "off"]
                console.print(f"  [bold yellow]feature disable <flag>[/bold yellow]  [dim]— flags not yet OFF[/dim]")
            console.print()
            if not candidates:
                console.print(f"  [dim]No matching flags.[/dim]")
            else:
                for flag in candidates:
                    cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                    console.print(f"    [bold]{flag:<35}[/bold]  [dim]{cmds}[/dim]")
            console.print()
            console.print(f"  [dim]feature enable <flag>  |  feature disable <flag>  |  feature dev <flag>  |  feature show[/dim]")
            console.print()
            return

        if sub == "help":
            if not render_help_topic(console, "features"):
                console.print("[dim]No docs found for 'features' — run 'help features'.[/dim]")
            return

        if sub == "find":
            # Flag-centric search: `feature find address` matches flag names AND
            # the commands they gate; shows the owning glossary file so the
            # operator knows exactly what to edit. Composable with | match.
            pattern = " ".join(args[1:]).strip().lower()
            if not pattern:
                console.print(
                    "[yellow]Usage:[/yellow] feature find <text>   "
                    "[dim](searches flags and the commands they gate; also: find command keyword <text>)[/dim]"
                )
                return
            from app.settings.features import load_features_with_sources
            _states, sources = load_features_with_sources()
            flag_cmds = _flag_to_cmds()
            hits = []
            for flag in _all_flags():
                gated = flag_cmds.get(flag, [])
                if pattern in flag.lower() or any(pattern in c.lower() for c in gated):
                    hits.append((flag, gated))
            if not hits:
                console.print(f"[yellow]No flags or gated commands match:[/yellow] [bold]{pattern}[/bold]")
                return
            console.print()
            for flag, gated in hits[:80]:
                state = feature_state(self._features, flag)
                colour = {"on": "green", "dev": "magenta"}.get(state, "red")
                file_label = sources.get(flag)
                file_note = f"  [dim]{file_label.name}[/dim]" if file_label is not None else ""
                shown_cmds = ", ".join(gated[:3]) + (f", +{len(gated) - 3} more" if len(gated) > 3 else "")
                console.print(f"  [{colour}]{state:<4}[/{colour}] [bold]{flag}[/bold]{file_note}")
                if shown_cmds:
                    console.print(f"        [dim]{shown_cmds}[/dim]")
            footer = f"{len(hits)} flag(s) match '{pattern}'"
            if len(hits) > 80:
                footer += " — showing 80; narrow it or pipe: | match <text>"
            console.print(f"\n[dim]{footer}  |  feature enable <flag> to turn one on[/dim]\n")
            return

        if sub == "show":
            flag_cmds = _flag_to_cmds()
            names = _all_flags()
            on  = [f for f in names if feature_state(self._features, f) == "on"]
            dev = [f for f in names if feature_state(self._features, f) == "dev"]
            off = [f for f in names if feature_state(self._features, f) == "off"]
            filter_token = args[1].lower() if len(args) >= 2 else ""

            mode = (
                "[magenta]ON[/magenta]" if self._dev_mode
                else "[dim]off[/dim]"
            )
            console.print()
            console.print(
                f"  [bold yellow]Feature Flags[/bold yellow]  "
                f"[dim]— development mode:[/dim] {mode}  "
                f"[dim](changes save to the flag's settings/features/ file)[/dim]"
            )

            if filter_token in ("on", "enabled", "true"):
                _print_feature_rows("ON — visible to everyone", on, "green", flag_cmds)
                console.print()
                return
            if filter_token in ("off", "disabled", "false"):
                _print_feature_rows("OFF — hidden for everyone", off, "red", flag_cmds)
                console.print()
                return
            if filter_token in ("dev", "development"):
                dev_hint = "shown now" if self._dev_mode else "hidden — type 'dev' to reveal"
                _print_feature_rows(f"DEV — {dev_hint}", dev, "magenta", flag_cmds)
                console.print()
                return
            if filter_token:
                matches = [
                    flag for flag in names
                    if filter_token in flag.lower()
                    or any(filter_token in cmd.lower() for cmd in flag_cmds.get(flag, []))
                ]
                _print_feature_rows(f"MATCHES — {filter_token}", matches, "cyan", flag_cmds)
                console.print()
                return

            _print_feature_rows("ON — visible to everyone", on, "green", flag_cmds)
            dev_hint = "shown now" if self._dev_mode else "hidden — type 'dev' to reveal"
            _print_feature_rows(f"DEV — {dev_hint}", dev, "magenta", flag_cmds)
            _print_feature_rows("OFF — hidden for everyone", off, "red", flag_cmds)

            console.print()
            console.print("  [dim]  feature show on|off|dev|<name>  |  feature enable <flag>  |  feature disable <flag>  |  feature dev <flag>[/dim]")
            console.print()
            return

        if sub in ("enable", "disable", "dev"):
            if len(args) < 2:
                console.print(f"[yellow]Usage:[/yellow] feature {sub} <flag_name>")
                console.print(f"  Tip: [bold]feature {sub} ?[/bold]  lists the flags you can {sub}")
                return
            flag_name = args[1].lower()
            if flag_name not in _all_flags():
                console.print(
                    f"[red]Unknown feature flag:[/red] {flag_name!r}\n"
                    f"  Run [bold]feature {sub} ?[/bold] to see all available flags."
                )
                return
            new_state = {"enable": "on", "disable": "off", "dev": "dev"}[sub]
            try:
                _persist_feature_state(flag_name, new_state)
            except RuntimeError as exc:
                console.print(f"[red]Could not save feature flag:[/red] {exc}")
                return
            colour = {"on": "green", "dev": "magenta", "off": "red"}[new_state]
            note = ""
            if new_state == "dev" and not self._dev_mode:
                note = "  [dim](type 'dev' to reveal dev commands)[/dim]"
            console.print(
                f"  {flag_name}  →  [{colour}]{new_state}[/{colour}]{note}  "
                f"[dim](saved to its settings/features/ file)[/dim]"
            )
            return

        console.print(
            f"[yellow]Unknown feature subcommand:[/yellow] {sub!r}\n"
            "  Usage: feature show [on|off|dev|<name>] | feature enable <flag> | feature disable <flag> | feature dev <flag>"
        )


    # ------------------------------------------------------------------
    # command-structure helpers
    # ------------------------------------------------------------------

    def _cs_tier(self, cmd_key: str) -> str:
        """Return the tier label based on override flag in command-structure.json."""
        from app.settings import command_structure as cs
        from app.commands.registry import COMMANDS

        # Check the unified structure (override:true = tier 1, override:false = tier 1g)
        struct = cs.load_command_structure()
        entry = struct.get(cmd_key)
        if entry:
            return "1" if entry.get("override", False) else "1g"

        # Check field_catalog (tier 2)
        try:
            from app.settings.field_catalog import FIELD_CATALOG
            if cmd_key in FIELD_CATALOG:
                return "2"
        except Exception:
            pass

        # Check usage-string fallback (tier 3)
        cmd_def = COMMANDS.get(cmd_key)
        if cmd_def and cmd_def.usage:
            spec = cs._parse_usage_spec(cmd_key, cmd_def.usage)
            if spec:
                return "3"

        return "-"

    @staticmethod
    def _format_spec(spec: list[dict]) -> str:
        """Format a command arg spec in PAN-OS style.

        kind=value   → <fieldname>         (user supplies free text)
        kind=choice  → choice1|choice2     (fixed options, tab-completable)
        kind=keyword → [keyword]           (optional trailing keyword)
        """
        parts = []
        for arg in spec[:8]:  # cap at 8 for display width
            name = arg.get("name", "?")
            kind = arg.get("kind", "value")
            if kind == "value":
                parts.append(f"<{name}>")
            elif kind == "choice":
                choices = arg.get("choices") or []
                if choices:
                    parts.append("|".join(choices[:4]) + ("…" if len(choices) > 4 else ""))
                else:
                    parts.append(f"<{name}>")
            elif kind == "keyword":
                parts.append(f"[{name}]")
            else:
                parts.append(f"<{name}>")
        suffix = " …" if len(spec) > 8 else ""
        return " ".join(parts) + suffix

    def _cs_list(self, mode: str = "enabled", match: str = "") -> None:
        """List enabled/disabled commands with PAN-OS-style field display and pagination."""
        from app.commands.registry import COMMANDS
        from app.settings.features import is_enabled, feature_state
        from app.settings import command_structure as cs
        from app.docs import page_length

        t = self._theme
        cs.invalidate_cache()

        # Build candidate list based on mode
        if mode == "disabled":
            candidates = sorted([
                k for k in COMMANDS
                if COMMANDS[k].feature_flag
                and not is_enabled(self._features, COMMANDS[k].feature_flag, self._dev_mode)
            ])
            mode_label = "disabled"
        else:  # "enabled" (default)
            candidates = sorted([
                k for k in COMMANDS
                if COMMANDS[k].feature_flag
                and is_enabled(self._features, COMMANDS[k].feature_flag, self._dev_mode)
            ])
            mode_label = "enabled"

        # Apply match filter
        if match:
            candidates = [k for k in candidates if match.lower() in k.lower()]

        tier_colors = {
            "1": "green", "1g": "cyan", "2": "blue", "3": "yellow", "-": "red",
        }
        tier_labels = {
            "1":  "hand-curated",
            "1g": "cli-generated",
            "2":  "openapi-spec",
            "3":  "usage-parsed",
            "-":  "NO SPEC",
        }
        col_cmd  = 46
        col_tier = 14

        filter_note = f" | match '{match}'" if match else ""
        lines: list[str] = []
        lines.append("")
        lines.append(
            f"  [bold yellow]COMMAND HELP SPEC COVERAGE[/bold yellow]  "
            f"[dim]— {len(candidates)} {mode_label} commands{filter_note}  "
            "| 'command-structure list ?' for tier definitions[/dim]"
        )
        lines.append("")
        lines.append(
            f"  [dim]{'Command':<{col_cmd}} {'Help spec tier':<{col_tier}} Fields[/dim]"
        )
        lines.append(f"  [dim]{'─' * (col_cmd + col_tier + 30)}[/dim]")

        counts: dict[str, int] = {}
        for key in candidates:
            tier = self._cs_tier(key)
            counts[tier] = counts.get(tier, 0) + 1
            color = tier_colors.get(tier, "white")
            label = tier_labels.get(tier, tier)
            spec = cs.arg_spec(key)
            fields_preview = self._format_spec(spec) if spec else "—"
            cmd_cell  = f"{key:<{col_cmd}}"
            tier_cell = f"[{color}]{label:<{col_tier}}[/{color}]"
            lines.append(
                f"  {self._styled(cmd_cell, t.command_name)} {tier_cell} [dim]{fields_preview}[/dim]"
            )

        lines.append("")
        summary_parts = []
        for tier, label in tier_labels.items():
            n = counts.get(tier, 0)
            if n:
                color = tier_colors[tier]
                summary_parts.append(f"[{color}]{n} {label}[/{color}]")
        if summary_parts:
            lines.append("  " + "  ".join(summary_parts))

        need = counts.get("3", 0) + counts.get("-", 0)
        if need and mode == "enabled":
            lines.append(
                f"  [dim]→ {need} command(s) can be improved: "
                "run [bold]command-structure update[/bold][/dim]"
            )
        lines.append("")

        output = "\n".join(lines)
        pg = page_length()
        if pg > 0 and len(lines) > pg:
            with console.pager(styles=True):
                console.print(output)
        else:
            console.print(output)


    def _cs_update(self, targets: list[str]) -> None:
        """Stream dev/commandupdate.py — same script the LLM 'commandupdate' trigger runs."""
        import sys as _sys
        import subprocess as _sp
        from app.paths import REPO_ROOT
        from app.settings import command_structure as cs

        script = REPO_ROOT / "dev" / "commandupdate.py"
        if not script.exists():
            console.print("[red]dev/commandupdate.py not found.[/red]")
            return

        extra: list[str] = list(targets)  # specific command, if given
        console.print("\n[magenta]● command-structure update[/magenta]\n")
        try:
            proc = _sp.Popen(
                [_sys.executable, str(script)] + extra,
                stdout=_sp.PIPE, stderr=_sp.STDOUT,
                text=True, bufsize=1, cwd=str(REPO_ROOT),
            )
            assert proc.stdout
            for raw_line in proc.stdout:
                console.print(raw_line.rstrip())
            proc.wait()
        except Exception as exc:
            console.print(f"[red]Failed to run commandupdate.py:[/red] {exc}")
            return

        cs.invalidate_cache()
        console.print(
            "\n  [dim]Updated specs are live immediately — no restart needed.\n"
            "  To get richer field metadata, edit [bold]settings/command-structure.json[/bold].[/dim]\n"
        )


    def _cs_clear(self) -> None:
        """Remove all override:false (cli-generated) entries from command-structure.json."""
        import json as _json
        from app.paths import COMMAND_STRUCTURE_JSON, COMMAND_STRUCTURE_GENERATED_JSON
        from app.settings import command_structure as cs

        if COMMAND_STRUCTURE_JSON.exists():
            raw = _json.loads(COMMAND_STRUCTURE_JSON.read_text(encoding="utf-8"))
            before = sum(1 for k, v in raw.items()
                        if not k.startswith("_") and isinstance(v, dict) and not v.get("override", True))
            cleaned = {k: v for k, v in raw.items()
                      if k.startswith("_") or not isinstance(v, dict) or v.get("override", True)}
            COMMAND_STRUCTURE_JSON.write_text(
                _json.dumps(cleaned, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            cs.invalidate_cache()
            console.print(f"[cyan]Removed {before} cli-generated (override:false) entries.[/cyan]")
        # Also remove legacy generated file if it exists
        if COMMAND_STRUCTURE_GENERATED_JSON.exists():
            COMMAND_STRUCTURE_GENERATED_JSON.unlink()
            console.print("[dim]Removed legacy command-structure-generated.json[/dim]")

    # =========================================================================
    # Dev shell — modal sub-shell entered by typing `dev` at any prompt.
    # =========================================================================

    def _cmd_dev(self, args: list[str]) -> None:
        """Enter the dev shell (modal, like configure mode).

        Type ``dev`` to enter.  Inside the dev shell the prompt shows ``:dev``
        and the following commands are available:

          status                       health dashboard
          docs update [--scm|--panos]  pull latest pan.dev specs + regenerate
          docs status                  spec/doc freshness
          catalog rebuild              regenerate code artifacts (no network)
          command-structure list       contextual ? help coverage
          command-structure update     generate entries for missing commands
          command-structure clear      wipe the generated entries file
          exit                         leave dev shell

        For non-interactive/CI use: ``dev on`` / ``dev off`` still work as before.
        """
        if not args:
            # Bare `dev` — enter the dev shell
            self._dev_shell_enter()
            return

        action = args[0].lower()
        if action in ("on", "enable", "true"):
            self._dev_mode = True
            self._invalidate_visible_keys()
            self._print_dev_status()
        elif action in ("off", "disable", "false"):
            self._dev_mode = False
            self._state.dev_shell = False
            self._invalidate_visible_keys()
            self._print_dev_status()
        elif action == "status":
            self._print_dev_status()
        else:
            console.print(
                "[yellow]Usage:[/yellow] dev  (enter dev shell)  "
                "| dev on | dev off | dev status"
            )

    def _dev_shell_enter(self) -> None:
        """Enter the dev shell — enable dev mode and show the dev menu."""
        self._state.dev_shell = True
        self._dev_mode = True
        self._invalidate_visible_keys()
        t = self._theme
        console.print()
        console.print(
            f"  [magenta bold]● DEV SHELL[/magenta bold]  "
            f"[dim]— self-service operator console[/dim]"
        )
        console.print()
        rows = [
            ("status",                     "Health dashboard — docs freshness, catalog drift, help coverage"),
            ("docs update",                "Pull latest pan.dev specs + regenerate all catalogs"),
            ("docs status",                "Show spec/doc timestamps and change summary"),
            ("catalog rebuild",            "Regenerate code artifacts (field catalog, resource catalog, …)"),
            ("command-structure list",     "Show contextual ? help coverage for all enabled commands"),
            ("command-structure update",   "Auto-generate contextual help entries for enabled commands"),
            ("command-structure clear",    "Wipe auto-generated entries (reset to tier 3 fallback)"),
            ("exit",                       "Leave dev shell"),
        ]
        w = 32
        for cmd, desc in rows:
            console.print(
                f"  {self._styled(f'{cmd:<{w}}', t.command_name)} "
                f"{self._styled(desc, t.description_dim)}"
            )
        console.print()
        console.print(f"  [dim]Prompt is now  arc:…:dev >  — type a command above or exit.[/dim]")
        console.print()

    def _dev_shell_exit(self) -> None:
        """Leave the dev shell."""
        import os as _os
        self._state.dev_shell = False
        # Only turn off dev mode if it wasn't pre-enabled via environment.
        if not _os.environ.get("ARC_DEV_MODE"):
            self._dev_mode = False
            self._invalidate_visible_keys()
        console.print("[cyan]Left dev shell.[/cyan]")

    def _dispatch_dev_shell(self, line: str) -> bool | None:
        """Route dev-shell commands.

        Handles ``<cmd> ?`` for inline contextual help on any dev sub-command.
        Returns a bool (handled) or None (not a dev command — fall through to
        normal dispatch so regular ARC commands still work from the dev shell).
        """
        tokens = line.split()
        if not tokens:
            return None
        cmd = tokens[0].lower()

        # Inline ? on a dev sub-command → show that command's help
        if len(tokens) >= 2 and tokens[-1] == "?":
            self._dev_inline_help(tokens[:-1])
            return False

        if cmd in ("exit", "quit"):
            self._dev_shell_exit()
            return False

        if cmd in ("?", "help") and len(tokens) == 1:
            self._dev_shell_help()
            return False

        if cmd == "status":
            self._dev_status()
            return False

        if cmd == "docs":
            self._dev_docs(tokens[1:])
            return False

        if cmd == "catalog":
            self._dev_catalog(tokens[1:])
            return False

        if cmd == "command-structure":
            sub = tokens[1].lower() if len(tokens) > 1 else "?"
            if sub in ("?", "help"):
                self._dev_inline_help(["command-structure"])
                return False
            if sub == "list":
                # Parse: list [enabled|disabled] [| match <word>]
                rest = tokens[2:]
                mode = "enabled"
                match_word = ""
                # Check for pipe filter
                if "|" in rest:
                    pipe_idx = rest.index("|")
                    pipe_args = rest[pipe_idx + 1:]
                    rest = rest[:pipe_idx]
                    if pipe_args and pipe_args[0].lower() == "match" and len(pipe_args) > 1:
                        match_word = " ".join(pipe_args[1:])
                if rest and rest[0].lower() == "?":
                    self._cs_tier_legend()
                elif rest and rest[0].lower() in ("enabled", "disabled"):
                    mode = rest[0].lower()
                    self._cs_list(mode=mode, match=match_word)
                else:
                    self._cs_list(mode=mode, match=match_word)
            elif sub == "update":
                self._cs_update(tokens[2:])
            elif sub == "clear":
                self._cs_clear()
            else:
                self._dev_inline_help(["command-structure"])
            return False

        # Not a dev-shell command — fall through to normal dispatch.
        return None

    def _dev_inline_help(self, prefix_tokens: list[str]) -> None:
        """Show contextual help for a dev shell command or sub-command."""
        t = self._theme
        w = 36
        cmd = prefix_tokens[0].lower() if prefix_tokens else ""
        sub = prefix_tokens[1].lower() if len(prefix_tokens) > 1 else ""

        def _row(name: str, desc: str) -> None:
            console.print(
                f"  {self._styled(f'{name:<{w}}', t.command_name)} "
                f"{self._styled(desc, t.description_dim)}"
            )

        console.print()

        if cmd == "docs" and not sub:
            console.print(f"  [bold yellow]docs[/bold yellow]  — manage pan.dev API documentation\n")
            _row("docs update",           "Pull latest pan.dev specs + regenerate all catalogs")
            _row("docs update --scm",     "Pull SCM API specs only")
            _row("docs update --panos",   "Pull PAN-OS CLI docs only")
            _row("docs status",           "Show last pull date, spec ages, CHANGES.md summary")

        elif cmd == "docs" and sub == "update":
            console.print(f"  [bold yellow]docs update[/bold yellow]  — pull latest pan.dev specs\n")
            console.print(
                "  Runs [bold]dev/docsupdate.py[/bold] as a subprocess with live output.\n"
                "  After completion, run [bold]catalog rebuild[/bold] to regenerate code artifacts.\n\n"
                "  Flags:\n"
                "    [cyan]--scm[/cyan]    Pull SCM API specs only (skip PAN-OS)\n"
                "    [cyan]--panos[/cyan]  Pull PAN-OS CLI docs only (skip SCM)\n"
                "    (no flag)  Pull both\n"
            )

        elif cmd == "docs" and sub == "status":
            console.print(f"  [bold yellow]docs status[/bold yellow]  — show documentation freshness\n")
            console.print(
                "  Reads [bold]docs/scm-api/MANIFEST.md[/bold] for the last pull date.\n"
                "  Lists each spec file with its age and the CHANGES.md summary.\n"
            )

        elif cmd == "catalog" or (cmd == "catalog" and sub in ("rebuild", "")):
            console.print(f"  [bold yellow]catalog rebuild[/bold yellow]  — regenerate all code artifacts\n")
            console.print(
                "  Runs all generator scripts in sequence (no network required):\n"
                "    [cyan]generate_resource_catalog.py[/cyan]  → app/commands/resource_catalog.py\n"
                "    [cyan]generate_feature_flags.py[/cyan]     → settings/features/\n"
                "    [cyan]generate_field_library.py[/cyan]     → app/settings/field_catalog.py\n"
                "    [cyan]generate_command_docs.py[/cyan]      → docs/commands/\n"
                "    [cyan]generate_api_index.py[/cyan]         → dev/API_INDEX.md\n"
                "    [cyan]generate_code_map.py[/cyan]          → dev/CODE_MAP.md\n\n"
                "  Caches are invalidated automatically — changes are live without restart.\n"
                "  Run [bold]docs update[/bold] first if you want fresh specs.\n"
            )

        elif cmd == "command-structure":
            console.print(f"  [bold yellow]command-structure[/bold yellow]  — manage contextual ? help specs\n")
            _row("command-structure list",          "Show all enabled commands + their help spec tier")
            _row("command-structure list ?",        "Explain what each tier means")
            _row("command-structure update",        "Auto-generate help specs for all commands missing one")
            _row("command-structure update <cmd>",  "Generate help spec for one specific command")
            _row("command-structure clear",         "Wipe the auto-generated specs file and start fresh")
            console.print()
            console.print(
                "  [dim]After enabling a new feature, run [bold]command-structure update[/bold]\n"
                "  to give that command full field-by-field ? help.\n"
                "  Generated specs go in [bold]settings/command-structure-generated.json[/bold].\n"
                "  For richer metadata (choices, hints), edit [bold]settings/command-structure.json[/bold].[/dim]"
            )

        elif cmd == "command-structure" and sub == "list":
            console.print(f"  [bold yellow]command-structure list[/bold yellow]  — help spec coverage\n")
            self._cs_tier_legend()

        elif cmd == "status":
            console.print(f"  [bold yellow]status[/bold yellow]  — dev shell health dashboard\n")
            console.print(
                "  Shows at a glance:\n"
                "    • [bold]Docs[/bold]     — how old the last pan.dev spec pull is\n"
                "    • [bold]Features[/bold] — count of on / dev / off feature flags\n"
                "    • [bold]Help spec[/bold]— how many enabled commands have contextual ? help\n"
                "    • [bold]Git[/bold]      — whether there are uncommitted changes\n"
            )
        else:
            self._dev_shell_help()

        console.print()

    def _dev_shell_help(self) -> None:
        """Print full dev shell command reference."""
        t = self._theme
        w = 36
        console.print()
        console.print(
            "  [magenta bold]DEV SHELL COMMANDS[/magenta bold]  "
            "[dim]— type <command> ? for detailed help[/dim]\n"
        )
        rows = [
            ("status",                              "Health dashboard — docs age, feature counts, help coverage, git"),
            ("docs update [--scm|--panos]",         "Pull latest pan.dev specs + regenerate all catalogs"),
            ("docs status",                         "Last pull date, spec ages, CHANGES.md summary"),
            ("catalog rebuild",                     "Regenerate code artifacts from pulled specs (no network)"),
            ("command-structure list",              "Show all enabled commands and their contextual ? help tier"),
            ("command-structure update [<cmd>]",    "Auto-generate ? help specs for commands that are missing one"),
            ("command-structure clear",             "Wipe auto-generated specs (reset to usage-string fallback)"),
            ("exit",                                "Leave dev shell (restores normal prompt)"),
        ]
        for cmd, desc in rows:
            console.print(
                f"  {self._styled(f'{cmd:<{w}}', t.command_name)} "
                f"{self._styled(desc, t.description_dim)}"
            )
        console.print()
        console.print(
            "  [dim]Regular ARC commands (show, cd, feature …) work here too.\n"
            "  Type any command followed by [bold]?[/bold] for contextual help.[/dim]"
        )
        console.print()

    def _cs_tier_legend(self) -> None:
        """Print the tier legend for command-structure list."""
        t = self._theme
        w = 16
        console.print(
            "  [bold yellow]HELP SPEC TIERS[/bold yellow]  "
            "[dim]— how each command gets its contextual ? help[/dim]\n"
        )
        tiers = [
            ("hand-curated",  "green",  "settings/command-structure.json",
             "Best quality. You wrote the field order and the field metadata\n"
             "    (choices, hints, required flags) is in command_structure.py.\n"
             "    update/delete variants are auto-derived from the set entry."),
            ("cli-generated", "cyan",   "settings/command-structure-generated.json",
             "Run 'command-structure update' to generate this. Parses the\n"
             "    command's usage string and writes inline arg specs. Good enough\n"
             "    for most commands. Promote to hand-curated for richer metadata."),
            ("openapi-spec",  "blue",   "app/settings/field_catalog.py",
             "Auto-generated from the SCM OpenAPI specs by docsupdate.\n"
             "    Covers generated 'set cngfw ...' commands. Regenerated by\n"
             "    'catalog rebuild' after 'docs update'."),
            ("usage-parsed",  "yellow", "(runtime only, not persisted)",
             "Fallback: the usage string on the CommandDef is parsed at\n"
             "    runtime. Works for simple commands. Run 'command-structure\n"
             "    update' to promote these to cli-generated (persisted)."),
            ("NO SPEC",       "red",    "(none)",
             "No help spec found and no usage string to parse. ? shows\n"
             "    only the command description. Run 'command-structure update'\n"
             "    — if usage= is missing, add it to the CommandDef first."),
        ]
        for label, color, source, explanation in tiers:
            console.print(
                f"  [{color}]{label:<{w}}[/{color}]  "
                f"[dim]source: {source}[/dim]"
            )
            for line in explanation.split("\n"):
                console.print(f"  [dim]{line}[/dim]")
            console.print()



    # ------------------------------------------------------------------
    # dev status
    # ------------------------------------------------------------------

    def _dev_status(self) -> None:  # noqa: C901
        """Unified health dashboard for the dev shell."""
        import re as _re
        import time as _time
        import subprocess as _sp
        from app.commands.registry import COMMANDS
        from app.settings.features import is_enabled
        from app.settings import command_structure as cs
        from app.paths import REPO_ROOT, COMMAND_STRUCTURE_GENERATED_JSON

        console.print()
        console.print("  [magenta bold]ARC DEV STATUS[/magenta bold]\n")

        # ── docs freshness — parse pull date from MANIFEST.md ─────────
        manifest = REPO_ROOT / "docs" / "scm-api" / "MANIFEST.md"
        specs_dir = REPO_ROOT / "docs" / "scm-api" / "specs"
        if manifest.exists():
            txt = manifest.read_text(encoding="utf-8")
            m = _re.search(r"Pulled on (\d{4}-\d{2}-\d{2})", txt)
            pull_date = m.group(1) if m else "unknown"
            specs = list(specs_dir.glob("*.yaml")) if specs_dir.exists() else []
            if specs:
                newest_mtime = max(s.stat().st_mtime for s in specs)
                age_h = (_time.time() - newest_mtime) / 3600
                age_str = f"{age_h:.0f}h ago" if age_h < 48 else f"{age_h/24:.0f}d ago"
                color = "green" if age_h < 72 else "yellow" if age_h < 168 else "red"
                console.print(
                    f"  [bold]Docs[/bold]     Last pulled [bold]{pull_date}[/bold]  "
                    f"[{color}]({age_str})[/{color}]  "
                    f"[dim]{len(specs)} spec files[/dim]"
                )
            else:
                console.print(f"  [bold]Docs[/bold]     Last pulled [bold]{pull_date}[/bold]  "
                              "[dim](no spec files found)[/dim]")
        else:
            console.print("  [bold]Docs[/bold]     [red]not pulled yet[/red]  "
                          "[dim]run: docs update[/dim]")

        # ── feature coverage ──────────────────────────────────────────
        all_flags = list(self._features.keys())
        on_flags  = [f for f in all_flags if is_enabled(self._features, f, False)]
        dev_flags = [f for f in all_flags if feature_state(self._features, f) == "dev"]
        off_flags = [f for f in all_flags if not is_enabled(self._features, f, True)]
        console.print(
            f"  [bold]Features[/bold] [green]{len(on_flags)} enabled[/green]  "
            f"[yellow]{len(dev_flags)} dev-only[/yellow]  "
            f"[dim]{len(off_flags)} off  ({len(all_flags)} total)[/dim]"
        )

        # ── command-structure coverage ────────────────────────────────
        cs.invalidate_cache()
        enabled = [
            k for k in COMMANDS
            if COMMANDS[k].feature_flag
            and is_enabled(self._features, COMMANDS[k].feature_flag, self._dev_mode)
        ]
        tiers = {k: self._cs_tier(k) for k in enabled}
        t1  = sum(1 for v in tiers.values() if v == "1")
        t1g = sum(1 for v in tiers.values() if v == "1g")
        t2  = sum(1 for v in tiers.values() if v == "2")
        t3  = sum(1 for v in tiers.values() if v == "3")
        tn  = sum(1 for v in tiers.values() if v == "-")
        need_update = t3 + tn
        console.print(
            f"  [bold]Help spec[/bold] [green]{t1} hand-curated[/green]  "
            f"[cyan]{t1g} cli-generated[/cyan]  "
            f"[blue]{t2} openapi[/blue]  "
            f"[yellow]{t3} usage-parsed[/yellow]  "
            f"[red]{tn} none[/red]  "
            f"[dim]({len(enabled)} enabled commands)[/dim]"
        )
        if need_update > 0:
            console.print(
                f"  [dim]  → {need_update} command(s) can be improved: "
                "run [bold]command-structure update[/bold][/dim]"
            )

        # ── git status ────────────────────────────────────────────────
        result = _sp.run(["git", "status", "--short"], capture_output=True, text=True,
                         cwd=str(REPO_ROOT))
        changed = [l for l in result.stdout.splitlines() if l.strip()]
        if changed:
            console.print(
                f"  [bold]Git[/bold]      [yellow]{len(changed)} uncommitted change(s)[/yellow]  "
                f"[dim](run 'git status' for details)[/dim]"
            )
        else:
            console.print("  [bold]Git[/bold]      [green]working tree clean[/green]")

        console.print()
        console.print(
            "  [dim]Type [bold]docs status[/bold] for spec-by-spec ages  |  "
            "[bold]command-structure list[/bold] for full help coverage  |  "
            "[bold]?[/bold] for all dev commands[/dim]"
        )
        console.print()

    # ------------------------------------------------------------------
    # dev docs
    # ------------------------------------------------------------------

    def _dev_docs(self, args: list[str]) -> None:
        """Handle dev-shell 'docs' sub-commands."""
        sub = args[0].lower() if args else "?"
        if sub in ("?", "help"):
            self._dev_inline_help(["docs"])
        elif sub == "update":
            self._dev_docs_update(args[1:])
        elif sub == "status":
            self._dev_docs_status()
        else:
            console.print(f"[yellow]Unknown docs sub-command:[/yellow] {sub!r}  "
                         "(try: docs update | docs status | docs ?)")

    def _dev_docs_update(self, flags: list[str]) -> None:
        """Stream docsupdate.py to pull latest pan.dev specs and regenerate catalogs."""
        import sys as _sys
        import subprocess as _sp
        from app.paths import REPO_ROOT

        script = REPO_ROOT / "dev" / "docsupdate.py"
        if not script.exists():
            console.print("[red]dev/docsupdate.py not found.[/red]")
            return

        extra: list[str] = []
        lf = [f.lower() for f in flags]
        if "--scm" in lf:
            extra += ["--scm-only"]
        elif "--panos" in lf:
            extra += ["--panos-only"]

        console.print(
            f"\n[magenta]● docs update[/magenta]  "
            f"[dim]running dev/docsupdate.py … (30–120 s)[/dim]\n"
        )
        try:
            proc = _sp.Popen(
                [_sys.executable, str(script)] + extra,
                stdout=_sp.PIPE, stderr=_sp.STDOUT,
                text=True, bufsize=1, cwd=str(REPO_ROOT),
            )
            assert proc.stdout
            for raw_line in proc.stdout:
                console.print(raw_line.rstrip())
            rc = proc.wait()
        except Exception as exc:
            console.print(f"[red]Failed to run docsupdate.py:[/red] {exc}")
            return

        if rc == 0:
            console.print("\n[green]✓ docs update complete.[/green]  "
                         "[dim]Run [bold]catalog rebuild[/bold] to regenerate code artifacts.[/dim]\n")
        else:
            console.print(f"\n[yellow]docsupdate.py exited with code {rc}[/yellow]\n")

    def _dev_docs_status(self) -> None:
        """Show doc/spec freshness with last pull date from MANIFEST.md."""
        import re as _re
        import time as _time
        from app.paths import REPO_ROOT
        from app.docs import page_length

        manifest  = REPO_ROOT / "docs" / "scm-api" / "MANIFEST.md"
        specs_dir = REPO_ROOT / "docs" / "scm-api" / "specs"
        changes   = REPO_ROOT / "docs" / "scm-api" / "CHANGES.md"

        lines: list[str] = []

        # ── last pull date ────────────────────────────────────────────
        if manifest.exists():
            txt = manifest.read_text(encoding="utf-8")
            m = _re.search(r"Pulled on (\d{4}-\d{2}-\d{2})", txt)
            pull_date = m.group(1) if m else "unknown"
            lines.append(f"  [bold]Last pulled:[/bold] [green]{pull_date}[/green]")
        else:
            lines.append("  [red]MANIFEST.md not found — run 'docs update' first.[/red]")

        # ── spec file ages ────────────────────────────────────────────
        if specs_dir.exists():
            specs = sorted(specs_dir.glob("*.yaml"))
            lines.append(f"\n  [bold]SCM Specs[/bold]  ({len(specs)} files)\n")
            now = _time.time()
            for s in specs:
                age_h = (now - s.stat().st_mtime) / 3600
                age_str = f"{age_h:.0f}h" if age_h < 48 else f"{age_h/24:.1f}d"
                color = "green" if age_h < 72 else "yellow" if age_h < 168 else "red"
                lines.append(f"    [{color}]{age_str:>7}[/{color}]  {s.name}")
        else:
            lines.append("\n  [red]docs/scm-api/specs/ not found — run 'docs update'[/red]")

        # ── CHANGES.md ────────────────────────────────────────────────
        if changes.exists():
            lines.append("\n  [bold]CHANGES.md[/bold]\n")
            for line in changes.read_text(encoding="utf-8").splitlines():
                lines.append(f"  {line}")

        output = "\n".join(lines) + "\n"
        pg = page_length()
        if pg > 0 and len(lines) > pg:
            with console.pager(styles=True):
                console.print(output)
        else:
            console.print()
            console.print(output)

    # ------------------------------------------------------------------
    # dev catalog
    # ------------------------------------------------------------------

    def _dev_catalog(self, args: list[str]) -> None:
        """Handle dev-shell 'catalog' sub-commands."""
        sub = args[0].lower() if args else "rebuild"
        if sub in ("rebuild", "regen", "update"):
            self._dev_catalog_rebuild()
        elif sub in ("?", "help"):
            self._dev_inline_help(["catalog"])
        else:
            console.print(f"[yellow]Unknown catalog sub-command:[/yellow] {sub!r}  "
                         "(try: catalog rebuild | catalog ?)")

    def _dev_catalog_rebuild(self) -> None:  # noqa: C901
        """Run all generator scripts to rebuild code artifacts."""
        import sys as _sys
        import subprocess as _sp
        from app.paths import REPO_ROOT
        from app.settings import command_structure as cs

        scripts = [
            ("dev/generate_resource_catalog.py",  "resource catalog    → app/commands/resource_catalog.py"),
            ("dev/generate_feature_flags.py",      "feature flags       → settings/features/"),
            ("dev/generate_field_library.py",      "field library       → app/settings/field_catalog.py"),
            ("dev/generate_command_docs.py",       "command docs        → docs/commands/"),
            ("dev/generate_api_index.py",          "API index           → dev/API_INDEX.md"),
            ("dev/generate_code_map.py",           "code map            → dev/CODE_MAP.md"),
        ]

        console.print("\n[magenta]● catalog rebuild[/magenta]\n")
        all_ok = True
        for script_rel, label in scripts:
            p = REPO_ROOT / script_rel
            if not p.exists():
                console.print(f"  [dim]skip  {label}  (script not found)[/dim]")
                continue
            result = _sp.run(
                [_sys.executable, str(p)],
                capture_output=True, text=True, cwd=str(REPO_ROOT),
            )
            if result.returncode == 0:
                out_lines = [l for l in result.stdout.splitlines() if l.strip()]
                summary = out_lines[-1] if out_lines else "ok"
                console.print(f"  [green]✓[/green]  {label}  [dim]{summary}[/dim]")
            else:
                all_ok = False
                console.print(f"  [red]✗[/red]  {label}  [red](exit {result.returncode})[/red]")
                for line in (result.stderr or result.stdout).splitlines()[-5:]:
                    console.print(f"       [dim]{line}[/dim]")

        cs.invalidate_cache()
        try:
            from app.settings.features import _reload_cache
            _reload_cache()
        except Exception:
            pass

        console.print()
        if all_ok:
            console.print(
                "[green]✓ catalog rebuild complete.[/green]  "
                "[dim]Changes are live immediately — no restart needed.[/dim]\n"
            )
        else:
            console.print(
                "[yellow]catalog rebuild finished with errors — check output above.[/yellow]\n"
            )



    def _print_dev_status(self) -> None:
        """Print current dev mode state (used by 'dev on/off' outside the shell)."""
        dev_flags = [f for f in self._features if feature_state(self._features, f) == "dev"]
        if self._dev_mode or self._state.dev_shell:
            console.print(
                f"[magenta]● Development mode ON[/magenta] — "
                f"{len(dev_flags)} dev command group(s) visible.  "
                f"[dim]Type 'dev' to enter dev shell.[/dim]"
            )
        else:
            console.print(
                f"[dim]○ Development mode OFF[/dim] — "
                f"{len(dev_flags)} dev command group(s) hidden.  "
                f"[dim]Type 'dev' to enter dev shell.[/dim]"
            )


    def _cmd_setup(self, args: list[str]) -> None:  # noqa: C901 (acceptable complexity)
        """Interactive credential setup wizard.

        Auto-detects the host OS, asks two short questions (SCM auth method and
        SSH auth method), then prints the exact commands the operator needs to
        run — nothing is written to disk until the operator follows those steps.

        Side effects: prints to console only.  Does not modify any config files.
        """
        # If any args were given treat them as a passthrough to `help setup`.
        if args:
            from app.docs import render_help_topic  # Deferred: avoids circular at module level
            render_help_topic(console, "setup")
            return

        os_name = platform.system()  # "Darwin" | "Linux" | "Windows"
        os_label = {"Darwin": "macOS", "Linux": "Linux / WSL", "Windows": "Windows"}.get(os_name, os_name)
        keychain_name = {
            "Darwin":  "macOS Keychain",
            "Linux":   "Secret Service (libsecret) or config file",
            "Windows": "Windows Credential Manager",
        }.get(os_name, "the OS keychain")

        console.print()
        console.print("[bold cyan]ARC Credential Setup Wizard[/bold cyan]")
        console.print(f"[dim]Detected platform: {os_label}  ·  Secrets stored in: {keychain_name}[/dim]")
        console.print()

        # ── Question 1: SCM auth method ──────────────────────────────────────
        console.print(
            "[bold]Q1[/bold]  What SCM credentials do you have?\n"
            "  [bold cyan]1[/bold cyan]  A pre-issued bearer token\n"
            "  [bold cyan]2[/bold cyan]  OAuth client ID + secret  (service account)\n"
            "  [bold cyan]3[/bold cyan]  Neither — I need to create a service account first"
        )
        try:
            scm_choice = console.input("  → ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Setup cancelled.[/dim]")
            return

        if scm_choice not in ("1", "2", "3"):
            console.print("[yellow]Invalid choice — please type 1, 2, or 3.[/yellow]")
            return

        # ── Question 2: SSH auth method ──────────────────────────────────────
        console.print()
        console.print(
            "[bold]Q2[/bold]  How will you SSH to managed devices?\n"
            "  [bold cyan]1[/bold cyan]  SSH key file  (recommended — no password stored)\n"
            "  [bold cyan]2[/bold cyan]  Password"
        )
        try:
            ssh_choice = console.input("  → ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Setup cancelled.[/dim]")
            return

        if ssh_choice not in ("1", "2"):
            console.print("[yellow]Invalid choice — please type 1 or 2.[/yellow]")
            return

        console.print()
        console.print("[bold]─── Steps to follow (run these outside ARC) ───[/bold]")
        console.print()

        # ── SCM instructions ─────────────────────────────────────────────────
        if scm_choice == "1":
            console.print("[bold cyan]SCM — bearer token:[/bold cyan]")
            _setup_bearer_instructions(console, os_name)
        elif scm_choice == "2":
            console.print("[bold cyan]SCM — OAuth client credentials:[/bold cyan]")
            _setup_oauth_instructions(console, os_name)
        else:
            console.print("[bold cyan]SCM — create a service account first:[/bold cyan]")
            console.print(
                "  1. Log in to https://stratacloudmanager.paloaltonetworks.com/\n"
                "  2. Navigate to Settings → Identity & Access → Service Accounts\n"
                "  3. Add a service account; copy Client ID, Client Secret, and TSG ID.\n"
                "     (The secret is shown only once — save it now.)\n"
                "  4. Come back and run [bold]setup[/bold] again — choose option 2 (OAuth)."
            )
            console.print()

        # ── SSH instructions ─────────────────────────────────────────────────
        if ssh_choice == "1":
            console.print()
            console.print("[bold cyan]SSH — key file:[/bold cyan]")
            console.print(
                "  # Generate a dedicated key (run once):\n"
                "  ssh-keygen -t ed25519 -f ~/.ssh/panos_key -C arc-panos\n\n"
                "  # Tell ARC to use it:\n"
                "  arc auth configure --ssh-key ~/.ssh/panos_key"
            )
        else:
            console.print()
            console.print("[bold cyan]SSH — password:[/bold cyan]")
            console.print(
                "  arc auth configure\n"
                "  # When prompted:\n"
                "  #   SSH username: admin\n"
                f"  #   SSH password: <paste>   ← stored in {keychain_name}"
            )

        # ── Final verification ────────────────────────────────────────────────
        console.print()
        console.print("[bold]─── Verify afterwards ───[/bold]")
        console.print(
            "  arc auth show    # confirm config values (secrets masked)\n"
            "  arc auth test    # live API call to SCM\n"
            "  Then restart ARC — the prompt should show [green]✓ SCM connected[/green]."
        )
        console.print()
        console.print(
            "[dim]Full setup guide: [bold]help setup[/bold]  ·  "
            "Platform details: [bold]help config osx[/bold] / [bold]help config nix[/bold] / [bold]help config win[/bold][/dim]"
        )
        console.print()


# ---------------------------------------------------------------------------
# Private helpers — per-platform SCM setup instructions.
# ---------------------------------------------------------------------------

def _setup_bearer_instructions(console, os_name: str) -> None:  # type: ignore[type-arg]
    """Print bearer-token setup commands for the detected OS."""
    if os_name == "Darwin":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 1 (bearer token)\n"
            "  #   Token: <paste>   ← stored in macOS Keychain, NOT on disk\n\n"
            "  # Or store manually via the security CLI:\n"
            "  security add-generic-password -U -s arc -a arc.bearer.token -w YOUR_TOKEN"
        )
    elif os_name == "Windows":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 1 (bearer token)\n"
            "  #   Token: <paste>   ← stored in Windows Credential Manager\n\n"
            "  # Or set for this PowerShell session only:\n"
            "  $env:SCM_BEARER_TOKEN = 'YOUR_TOKEN'"
        )
    else:
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 1 (bearer token)\n"
            "  #   Token: <paste>   ← stored via libsecret or config file (0600)\n\n"
            "  # Or set for this terminal session only:\n"
            "  export SCM_BEARER_TOKEN=your-bearer-token"
        )


def _setup_oauth_instructions(console, os_name: str) -> None:  # type: ignore[type-arg]
    """Print OAuth client credential setup commands for the detected OS."""
    if os_name == "Darwin":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 2 (OAuth)\n"
            "  #   Client ID:     <paste>  ← safe to store in config file\n"
            "  #   Client secret: <paste>  ← stored in macOS Keychain\n"
            "  #   TSG ID:        <paste>  ← safe to store in config file"
        )
    elif os_name == "Windows":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 2 (OAuth)\n"
            "  #   Client ID:     <paste>  ← safe to store in config file\n"
            "  #   Client secret: <paste>  ← stored in Windows Credential Manager\n"
            "  #   TSG ID:        <paste>  ← safe to store in config file"
        )
    else:
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 2 (OAuth)\n"
            "  #   Client ID:     <paste>  ← safe to store in config file\n"
            "  #   Client secret: <paste>  ← stored via libsecret / config file 0600\n"
            "  #   TSG ID:        <paste>  ← safe to store in config file\n\n"
            "  # Or export for this session:\n"
            "  export SCM_CLIENT_ID=...\n"
            "  export SCM_CLIENT_SECRET=...\n"
            "  export SCM_TSG_ID=..."
        )

