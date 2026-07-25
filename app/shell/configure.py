"""ArcShell configure mixin — configure mode, cli theme, feature flags."""
from __future__ import annotations

import threading  # commit-confirmed auto-revert timer

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


def _prefs_file_label() -> str:
    """Repo-relative path of the config file (holds preferences), for display."""
    from app.config import CONFIG_FILE
    try:
        return str(CONFIG_FILE.relative_to(CONFIG_FILE.parents[2]))
    except (ValueError, IndexError):
        return str(CONFIG_FILE)


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
    _cparam = ctx.container[0] if ctx is not None else "folder"
    scm._container_override = ctx.container if (ctx is not None and _cparam == "snippet") else None
    try:
        handler(ctx, args)
    finally:
        scm._request = real_request
        scm._container_override = None
    return captured


class ConfigureMixin:
    def _cmd_configure(self, args: list[str]) -> None:
        """Enter configure mode (Cisco-style).

        In configure mode, 'set' creates objects and 'exit' leaves configure mode.
        Shortcuts like 'conf' and 'conf t' are defined in settings/builtin-commands.json.
        """
        if args:
            console.print(
                "[yellow]Usage:[/yellow] configure\n"
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
        # Soft schema pre-check against the endpoint's OpenAPI request schema —
        # warn (never block) if the body looks like SCM will reject it; still stage.
        from app.commands.request_validate import validate_request_body_by_route
        warn: list[str] = []
        for op in ops:
            warn.extend(validate_request_body_by_route(
                op.get("method"), op.get("base_url"), op.get("path"),
                op.get("json"), op.get("params"),
            ))
        if warn:
            console.print(
                "[yellow]⚠ may be rejected by SCM:[/yellow] " + "; ".join(warn)
                + " [dim](staged anyway — re-checked at commit)[/dim]"
            )
        detail = str(args.get("name") or (args.get("_positional") or [""])[0] or "").strip()
        # args are kept so `commit check` can re-run validation later.
        self._state.staged_ops.append(
            {"command": key, "detail": detail, "folder": ctx.folder,
             "snippet": ctx.snippet, "args": args, "ops": ops}
        )
        shown = f"{key} {detail}".strip()
        n = len(self._state.staged_ops)
        review_hint = "show config to review" if n > 1 else "show config to review"
        unstage_hint = f"  unstage {n} to remove this one  |  " if n > 1 else "  "
        console.print(
            f"[green]✓[/green] Validated and staged: [bold]{shown}[/bold]  "
            f"[dim]({n} pending —{unstage_hint}"
            f"{review_hint}  |  commit to apply)[/dim]"
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
                "folder": (f"snippet:{entry['snippet']}" if entry.get("snippet") else entry["folder"]),
                "api": "; ".join(f"{op['method']} {op['path']}" for op in entry["ops"]),
            }
            for index, entry in enumerate(staged, 1)
        ]
        console.print(fmt._list_table(rows, title=f"Staged changes ({len(staged)}) — local, not yet in SCM"))
        console.print(
            "[dim]Staged changes are not visible in show output until commit.  "
            "commit → apply all  |  unstage <n> → remove one  |  abandon → discard all\n"
            "  Tip: [bold]show config format set[/bold] shows the running config as replayable set commands.  "
            "Pipe to save a backup: [bold]show config format set | save /tmp/backup.sh[/bold][/dim]"
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

    def _cmd_unstage(self, args: list[str]) -> None:
        """Remove a single staged change by its index number (configure mode only).

        Usage: unstage <n>   — remove item <n> from 'show config' list
        """
        if not self._state.configure_mode:
            console.print(
                "[yellow]unstage is a configure-mode command.[/yellow] "
                "Enter [bold]configure[/bold] first."
            )
            return
        staged = self._state.staged_ops
        if not staged:
            console.print("[dim]No staged changes to unstage.[/dim]")
            return
        if not args or not args[0].isdigit():
            console.print(
                f"[yellow]Usage:[/yellow] unstage <n>   (1–{len(staged)} from [bold]show config[/bold])"
            )
            return
        n = int(args[0])
        if not (1 <= n <= len(staged)):
            console.print(
                f"[yellow]Index {n} out of range[/yellow] — "
                f"valid range is 1–{len(staged)} ([bold]show config[/bold] to review)."
            )
            return
        removed = staged.pop(n - 1)
        label = f"{removed['command']} {removed['detail']}".strip()
        console.print(
            f"[green]✓[/green] Removed staged change #{n}: [bold]{label}[/bold]  "
            f"[dim]({len(staged)} remaining — SCM was never touched)[/dim]"
        )

    # ------------------------------------------------------------------
    # commit confirmed — Junos-style auto-revert safety net
    # ------------------------------------------------------------------

    def _rollback_version(self) -> int | None:
        """Version number of the CURRENT running config (the revert target)."""
        try:
            data = self._scm._request(
                "GET", self._scm.OPERATIONS_URL, "/config-versions/running"
            )
        except Exception as exc:  # noqa: BLE001
            # Log visibly so the operator knows WHY we can't arm auto-revert,
            # rather than silently failing and leaving them unprotected.
            console.print(
                f"[yellow]⚠ Could not fetch running config version:[/yellow] {exc}\n"
                "  commit confirmed will be skipped — run a plain [bold]commit[/bold] instead."
            )
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
        self._pending_confirm = {
            "timer": timer,
            "version": version,
            "minutes": minutes,
            "armed_at": time.monotonic(),
        }
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
        ``commit check`` — pre-flight staged changes without applying: offline
        schema validation (required fields, enums, length/pattern) plus, when
        connected, a re-check against current SCM state.
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
            console.print("[red]SCM is not configured — run [bold]arc auth configure[/bold] to set up credentials.[/red]")
            return

        # Schema pre-flight over the whole staged queue — if anything looks
        # invalid, ask how to proceed (never silently abandon).
        if not self._commit_preflight():
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
                    # Surface the REAL SCM rejection (which field / why), sanitized —
                    # not the bare httpx "400 Bad Request" line.
                    reason = self._format_api_error(exc)
                    console.print(
                        f"  [red]✗[/red] {index}/{total}  {label} — {reason}\n"
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

    def _commit_preflight(self) -> bool:
        """Validate the staged queue against endpoint schemas before applying.

        Returns True to proceed with the commit, False to stop.  When problems are
        found, prompts the operator: [P]roceed anyway, [F]ix (stop, keep the queue
        intact), or [A]bandon (discard the queue, stop).  Enter or Ctrl-C = Fix —
        the staged config is NEVER discarded unless the operator chooses Abandon.
        """
        from app.commands.request_validate import validate_request_body_by_route

        problems: list[tuple[str, list[str]]] = []
        for entry in self._state.staged_ops:
            issues: list[str] = []
            for op in entry.get("ops") or []:
                issues.extend(validate_request_body_by_route(
                    op.get("method"), op.get("base_url"), op.get("path"),
                    op.get("json"), op.get("params"),
                ))
            if issues:
                problems.append((f"{entry['command']} {entry['detail']}".strip(), issues))

        if not problems:
            return True

        console.print("[yellow]Schema pre-flight found problems before commit:[/yellow]")
        for label, issues in problems:
            console.print(f"  [red]✗[/red] {label} — " + "; ".join(issues))
        console.print(
            "  [dim]SCM is the final authority — these are local schema checks.[/dim]"
        )
        try:
            choice = input(
                "  [P]roceed anyway, [F]ix (keep staged, stop), or [A]bandon (discard)? [F]: "
            ).strip().lower()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Stopped — staged changes kept. Fix or abandon, then commit.[/dim]")
            return False

        if choice in ("p", "proceed"):
            return True
        if choice in ("a", "abandon"):
            self._state.staged_ops = []
            console.print("[yellow]Abandoned all staged changes.[/yellow]")
            return False
        console.print("[dim]Stopped — staged changes kept. Fix or abandon, then commit.[/dim]")
        return False

    def _commit_check(self) -> None:
        """Pre-flight every staged change before commit (Junos-style).

        Two passes, combined into one report per entry:

        1. **Schema (offline):** each captured request body is validated against
           the OpenAPI request schema of the endpoint it hits (route-keyed, so it
           covers EVERY command — generated and hand-written) — required fields
           present, enums valid, length/pattern/range satisfied. No network; works
           even when SCM is not connected.
        2. **State (needs SCM):** when connected, each entry's handler is re-run
           through the recording client (fresh GETs, no mutations) to catch drift
           — e.g. a colleague deleted the object your update targets — and to
           refresh captured ops (ids re-resolved).

        Failures are reported and left staged for the operator to fix or abandon.
        """
        from app.commands.request_validate import validate_request_body_by_route

        staged = self._state.staged_ops
        if not staged:
            console.print("[dim]No staged changes to check.[/dim]")
            return

        connected = self._scm is not None
        failures = 0
        for index, entry in enumerate(staged, 1):
            label = f"{entry['command']} {entry['detail']}".strip()
            problems: list[str] = []

            # 1. Offline schema check of each captured request body vs. its route.
            for op in entry.get("ops") or []:
                problems.extend(validate_request_body_by_route(
                    op.get("method"), op.get("base_url"), op.get("path"),
                    op.get("json"), op.get("params"),
                ))

            # 2. Live state re-check (re-run the handler) when connected.
            if connected:
                cmd_def = COMMANDS.get(entry["command"])
                if cmd_def is None or cmd_def.api_handler is None:
                    problems.append("command no longer registered")
                else:
                    ctx = ExecutionContext(
                        scm=self._scm, ssh=self._ssh, config=self._config,
                        device=self._state.device, folder=entry["folder"],
                        snippet=entry.get("snippet"),
                        tsg_id=self._state.tsg_id,
                    )
                    try:
                        entry["ops"] = capture_write_ops(
                            self._scm, cmd_def.api_handler, ctx, entry.get("args") or {}
                        )
                    except Exception as exc:  # noqa: BLE001 — reported per entry
                        problems.append(self._format_api_error(exc))

            if problems:
                failures += 1
                console.print(
                    f"  [red]✗[/red] {index}/{len(staged)}  {label} — "
                    + "; ".join(problems)
                )
            else:
                console.print(f"  [green]✓[/green] {index}/{len(staged)}  {label}")

        if not connected:
            console.print(
                "[dim]SCM not connected — validated offline against the schema only; "
                "reconnect to also re-check against current SCM state.[/dim]"
            )
        if failures:
            console.print(
                f"[yellow]commit check: {failures} of {len(staged)} staged change(s) have problems.[/yellow]\n"
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
                    # Interruptible poll — check every 0.2 s so Ctrl-C is
                    # responsive instead of blocking for the full 5 s sleep.
                    poll_deadline = time.monotonic() + 5
                    while time.monotonic() < poll_deadline:
                        time.sleep(min(0.2, poll_deadline - time.monotonic()))
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
        """Per-user terminal preferences — persisted to config/<user>/config.json (preferences block).

        terminal                     show current settings and how to change them
        terminal length <n>          page long output after n lines (0 = never page)
        terminal width <n>           force render width in columns (0 = auto-detect)
        terminal height <n>          force render height in rows (0 = auto-detect)
        terminal spinner on|off      toggle the "querying SCM…" spinner
        """
        p = self._prefs
        t = self._theme

        if not args or args[0] in ("?", "help"):
            length_note = f"{p.terminal_length} lines" if p.terminal_length else "off  (no paging)"
            width_note  = f"{p.terminal_width} columns" if p.terminal_width else "auto-detect"
            height_note = f"{p.terminal_height} rows" if p.terminal_height else "auto-detect"
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
                f"  {self._styled(f'terminal height', t.command_name):<{w+10}} "
                f"{height_note:<12} "
                f"[dim]terminal height <n>   (0 = auto-detect)[/dim]"
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
                "    terminal height 40    → force 40-row height for rich tables\n"
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

        elif sub == "height":
            if len(args) < 2:
                console.print(
                    "[yellow]Usage:[/yellow] terminal height <n>\n"
                    "  [dim]0 = auto-detect from your terminal window\n"
                    f"  Current: {p.terminal_height or 0}[/dim]"
                )
                return
            if not args[1].isdigit():
                console.print("[yellow]Usage:[/yellow] terminal height <n>  (whole number, 0 = auto)")
                return
            value = int(args[1])
            p.terminal_height = value
            if value > 0:
                console.height = value
            else:
                console.height = None
            note = f"render height {value} rows" if value else "auto-detect height"

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
                "  terminal height <n>       force row height    [dim](0 = auto)[/dim]\n"
                "  terminal spinner on|off   show/hide spinner\n"
            )
            return

        saved = save_prefs(p)
        suffix = "" if saved else "  [yellow](config.json not writable — applies to this session only)[/yellow]"
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
            console.print(f"  [cyan]feature show[/cyan]           List all flags grouped ON / DEV / OFF / HIDDEN")
            console.print(f"  [cyan]feature show on|off|dev|hidden[/cyan]  List only flags in one state")
            console.print(f"  [cyan]feature show <name>[/cyan]    Show matching feature flag(s)")
            console.print(f"  [cyan]feature gui-configure[/cyan]   Open the browser feature editor")
            console.print(f"  [cyan]feature area[/cyan]           List areas + which are enabled/disabled")
            console.print(f"  [cyan]feature area <name> enable|disable[/cyan]  Turn a whole area on/off")
            console.print(f"  [cyan]feature info <flag>[/cyan]    Show what a flag does + its gated commands")
            console.print(f"  [cyan]feature enable <flag>[/cyan]  Set a flag ON and save")
            console.print(f"  [cyan]feature disable <flag>[/cyan] Set a flag OFF and save")
            console.print(f"  [cyan]feature dev <flag>[/cyan]     Mark a flag DEV and save")
            console.print(f"  [cyan]feature hidden <flag>[/cyan]  Mark a flag HIDDEN (runs, not shown in ?)")
            console.print(f"  [cyan]feature scope <cmd> <global|folder|device|remote|reset>[/cyan]  Override where a command runs")
            console.print(f"  [cyan]feature default <domain> <on|dev|off>[/cyan]  Set a domain's default state")
            console.print(f"  [cyan]feature carry <domain> <on|off>[/cyan]        Keep manual edits on regenerate")
            console.print(f"  [cyan]feature help[/cyan]           Open full feature flag documentation")
            console.print()
            console.print(f"  [dim]DEV flags appear only after you type [bold]dev[/bold] to enter development mode.[/dim]")
            console.print(f"  [dim]feature enable ?  → flags not yet ON   |   feature disable ?  → flags not yet OFF[/dim]")
            console.print()
            return

        # ── gui-configure — launch the browser feature editor (blocks until closed) ─
        # `feature gui` stays as a hidden back-compat alias.
        if sub in ("gui-configure", "gui"):
            self._cmd_feature_gui()
            return

        # ── info — describe a flag and the commands it gates ──────────────────
        if sub == "info":
            self._cmd_feature_info(args[1:])
            return

        # ── scope — set/clear a per-command run-scope override ────────────────
        if sub == "scope":
            self._cmd_feature_scope(args[1:])
            return

        # ── area — list areas / hide/show a whole area in the editor ──────────
        if sub in ("area", "areas"):
            self._cmd_feature_area(args[1:])
            return

        # ── default / carry — per-domain file meta ────────────────────────────
        if sub in ("default", "carry"):
            self._cmd_feature_meta(sub, args[1:])
            return

        # ── feature <flag> ? — info for a specific flag ──────────────────────
        if len(args) == 2 and args[1] == "?":
            self._cmd_feature_info([args[0]])
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
        # Filter out internal sentinel keys (_domain_default_*, etc.) — these
        # are loader implementation details, not user-facing flags.
        def _all_flags() -> list[str]:
            names = (
                {k for k in self._features if not k.startswith("_")}
                | set(_flag_to_cmds())
            )
            return sorted(names)

        def _persist_feature_state(flag_name: str, state: str) -> None:
            """Write one flag state to its owning settings/features/ file and
            update the live shell (flag map + visible-keys cache)."""
            from app.settings.features import set_feature_state

            set_feature_state(flag_name, state)
            self._features[flag_name] = state
            self._invalidate_visible_keys()

        def _print_feature_rows(title: str, flags: list[str], colour: str, flag_cmds: dict[str, list[str]]) -> None:
            """Print a compact flag list with human titles + command mappings."""
            from app.settings.feature_labels import flag_label, load_labels
            labels = load_labels()
            console.print(f"\n  [bold {colour}]{title}[/bold {colour}]  [dim]({len(flags)})[/dim]")
            if not flags:
                console.print("    [dim]No matching flags.[/dim]")
                return
            for flag in flags:
                state = feature_state(self._features, flag)
                gated = sorted(flag_cmds.get(flag, []))
                # Effective-scope summary across the flag's gated commands.
                scopes = {
                    self.resolve_scope(c, COMMANDS[c])
                    for c in gated if c in COMMANDS
                }
                scope_tag = ""
                if scopes:
                    label = next(iter(scopes)) if len(scopes) == 1 else "mixed"
                    scope_tag = f"  [dim]<{label}>[/dim]"
                human = flag_label(flag, flag_cmds, commands=COMMANDS, labels=labels)["title"]
                console.print(
                    f"    [white]{human:<26}[/white] [{colour}]{state:<7}[/{colour}]{scope_tag}"
                    f"  [dim]{flag}[/dim]"
                )

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
            # Uses word-boundary matching so "ping" won't match "mapping".
            import re as _re
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
            pat = _re.compile(r'(?<![a-z])' + _re.escape(pattern) + r'(?![a-z])')
            hits = []
            for flag in _all_flags():
                gated = flag_cmds.get(flag, [])
                if pat.search(flag.replace("_", " ").lower()) or any(
                    pat.search(c.replace("-", " ").lower()) for c in gated
                ):
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
            import re as _re

            flag_cmds = _flag_to_cmds()
            names = _all_flags()
            on  = [f for f in names if feature_state(self._features, f) == "on"]
            dev = [f for f in names if feature_state(self._features, f) == "dev"]
            off = [f for f in names if feature_state(self._features, f) == "off"]
            hid = [f for f in names if feature_state(self._features, f) == "hidden"]
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
            if filter_token in ("hidden", "stealth"):
                _print_feature_rows("HIDDEN — works but not shown in ?", hid, "yellow", flag_cmds)
                console.print()
                return
            if filter_token in ("dev", "development"):
                dev_hint = "shown now" if self._dev_mode else "hidden — type 'dev' to reveal"
                _print_feature_rows(f"DEV — {dev_hint}", dev, "magenta", flag_cmds)
                console.print()
                return
            if filter_token:
                # Use word-boundary matching so "ping" doesn't match "mapping".
                # Flag name matches use substring (underscores = word separators).
                pat = _re.compile(r'(?<![a-z])' + _re.escape(filter_token) + r'(?![a-z])')
                matches = [
                    flag for flag in names
                    if pat.search(flag.replace("_", " ").lower())
                    or any(pat.search(cmd.replace("-", " ").lower()) for cmd in flag_cmds.get(flag, []))
                ]
                _print_feature_rows(f"MATCHES — {filter_token}", matches, "cyan", flag_cmds)
                console.print()
                return

            # Default show: ON and DEV in full; OFF collapsed to a summary line
            # (the OFF list can be thousands of catalog-generated flags — showing
            # them all creates unreadable noise; use 'show feature off' to list them).
            _print_feature_rows("ON — visible to everyone", on, "green", flag_cmds)
            dev_hint = "shown now" if self._dev_mode else "hidden — type 'dev' to reveal"
            _print_feature_rows(f"DEV — {dev_hint}", dev, "magenta", flag_cmds)
            if hid:
                _print_feature_rows("HIDDEN — works but not shown in ?", hid, "yellow", flag_cmds)
            if off:
                console.print(
                    f"\n  [bold red]OFF — hidden for everyone[/bold red]  "
                    f"[dim]({len(off)})[/dim]"
                )
                console.print(
                    f"    [dim]Run [bold]feature show off[/bold] to list all disabled flags.[/dim]"
                )

            console.print()
            console.print("  [dim]  feature show on|off|dev|hidden|<name>  |  feature enable|disable|dev|hidden <flag>  |  feature area[/dim]")
            console.print()
            return

        if sub in ("enable", "disable", "dev", "hidden"):
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
            new_state = {"enable": "on", "disable": "off", "dev": "dev", "hidden": "hidden"}[sub]
            try:
                _persist_feature_state(flag_name, new_state)
            except RuntimeError as exc:
                console.print(f"[red]Could not save feature flag:[/red] {exc}")
                return
            colour = {"on": "green", "dev": "magenta", "off": "red", "hidden": "yellow"}[new_state]
            note = ""
            if new_state == "dev" and not self._dev_mode:
                note = "  [dim](type 'dev' to reveal dev commands)[/dim]"
            elif new_state == "hidden":
                note = "  [dim](runs, but not shown in normal ? help)[/dim]"
            console.print(
                f"  {flag_name}  →  [{colour}]{new_state}[/{colour}]{note}  "
                f"[dim](saved to its settings/features/ file)[/dim]"
            )
            return

        console.print(
            f"[yellow]Unknown feature subcommand:[/yellow] {sub!r}\n"
            "  Usage: feature show [on|off|dev|hidden|<name>] | feature gui-configure | feature info <flag> |\n"
            "         feature enable|disable|dev|hidden <flag> | feature area [<name> show|hide] |\n"
            "         feature scope <cmd> <global|folder|device|remote|reset> |\n"
            "         feature default <domain> <on|dev|off> | feature carry <domain> <on|off>"
        )


    def _cmd_feature_info(self, args: list[str]) -> None:
        """Describe a flag: state, gated commands, and their effective scope."""
        from app.settings.features import feature_file_for

        if not args:
            console.print("[yellow]Usage:[/yellow] feature info <flag>")
            return
        flag = args[0].lower()
        flag_cmds: dict[str, list[str]] = {}
        for cmd_key, cmd_def in COMMANDS.items():
            if cmd_def.feature_flag:
                flag_cmds.setdefault(cmd_def.feature_flag, []).append(cmd_key)
        known = set(self._features) | set(flag_cmds)
        if flag not in {k for k in known if not k.startswith("_")}:
            console.print(
                f"[red]Unknown feature flag:[/red] {flag!r}\n"
                f"  Run [bold]feature show {flag}[/bold] to search, or [bold]feature show[/bold] to list all."
            )
            return

        state = feature_state(self._features, flag)
        colour = {"on": "green", "dev": "magenta", "hidden": "yellow"}.get(state, "red")
        gated = sorted(flag_cmds.get(flag, []))
        source = feature_file_for(flag).name

        from app.settings.feature_labels import area_label, flag_label, load_labels
        labels = load_labels()
        human = flag_label(flag, flag_cmds, commands=COMMANDS, labels=labels)
        cat = COMMANDS[gated[0]].category if gated else ""
        area = area_label(cat, labels) if cat else ""

        console.print()
        console.print(
            f"  [bold white]{human['title']}[/bold white]  [{colour}]{state}[/{colour}]"
            + (f"  [dim]· {area}[/dim]" if area else "")
        )
        if human["subtitle"]:
            console.print(f"  [dim]{human['subtitle']}[/dim]")
        console.print(f"  [dim]flag: {flag}  ({source})[/dim]")
        if not gated:
            console.print("  [dim]No registered commands reference this flag.[/dim]\n")
            return
        console.print(f"  [dim]Gates {len(gated)} command(s):[/dim]")
        for cmd_key in gated:
            cmd_def = COMMANDS[cmd_key]
            code_scope = cmd_def.scope
            eff = self.resolve_scope(cmd_key, cmd_def)
            scope_note = (
                f"[cyan]{eff}[/cyan]" if eff == code_scope
                else f"[cyan]{eff}[/cyan] [dim](override; code: {code_scope})[/dim]"
            )
            ssh = " [dim](SSH/--remote)[/dim]" if cmd_def.ssh_command else ""
            console.print(f"    [bold]{cmd_key}[/bold]  <{scope_note}>{ssh}")
            if cmd_def.description:
                console.print(f"        [dim]{cmd_def.description}[/dim]")
        console.print(
            "\n  [dim]feature scope <command> <global|folder|device|remote|reset> to override where a command runs.[/dim]\n"
        )

    def _cmd_feature_area(self, args: list[str]) -> None:
        """List areas, or enable/disable a whole area.

        Usage: feature area                      — list all areas + enabled state
               feature area <name> enable|disable  — turn an area on/off (name or key)
        Disabling an area is a real OFF switch: its commands are hidden from ?,
        blocked at execution, and removed from every feature-editor section.
        Individual feature-flag values are preserved and restored on re-enable.
        """
        from app.settings.feature_labels import area_label, load_labels
        from app.settings.features import load_disabled_areas, set_area_disabled

        labels = load_labels()
        # Build category -> feature count + state counts.
        cats: dict[str, dict] = {}
        for cmd_def in COMMANDS.values():
            flag = cmd_def.feature_flag
            if not flag:
                continue
            cat = cmd_def.category or "explicit"
            entry = cats.setdefault(cat, {"flags": set()})
            entry["flags"].add(flag)
        disabled = load_disabled_areas()

        if args and args[0] not in ("?",):
            # Resolve name-or-key -> category key.
            target = " ".join(args[:-1]).strip() if len(args) >= 2 else args[0]
            action = args[-1].lower() if len(args) >= 2 else ""
            key = None
            tl = target.strip().lower()
            for cat in cats:
                if cat == tl or area_label(cat, labels).lower() == tl:
                    key = cat
                    break
            if key is None:
                console.print(
                    f"[red]Unknown area:[/red] {target!r}\n"
                    "  Run [bold]feature area[/bold] to list areas."
                )
                return
            if action not in ("enable", "disable", "on", "off"):
                console.print("[yellow]Usage:[/yellow] feature area <name> enable|disable")
                return
            want_disabled = action in ("disable", "off")
            try:
                set_area_disabled(key, want_disabled)
                self._disabled_areas = load_disabled_areas()
                self._invalidate_visible_keys()
            except RuntimeError as exc:
                console.print(f"[red]Could not update area:[/red] {exc}")
                return
            state = "[red]disabled[/red] — all its commands are off" if want_disabled else "[green]enabled[/green]"
            console.print(f"  [bold white]{area_label(key, labels)}[/bold white]  →  {state}")
            return

        # List all areas.
        console.print()
        console.print("  [bold yellow]Feature Areas[/bold yellow]  [dim](disable = the whole area is turned off everywhere)[/dim]")
        for cat in sorted(cats, key=lambda c: area_label(c, labels).lower()):
            flags = cats[cat]["flags"]
            on = sum(1 for f in flags if feature_state(self._features, f) == "on")
            off_area = cat in disabled
            mark = "[red]disabled[/red]" if off_area else "[green]enabled[/green] "
            console.print(
                f"    {area_label(cat, labels):<30} {mark}  "
                f"[dim]{on}/{len(flags)} features on[/dim]"
            )
        console.print("\n  [dim]feature area <name> enable|disable  to turn a whole area on/off[/dim]\n")

    def _cmd_feature_scope(self, args: list[str]) -> None:
        """Set or clear a per-command run-scope override.

        Usage: feature scope <command> <global|folder|device|remote|reset>
        The command is matched against the registry; 'reset' clears the override.
        """
        from app.settings.features import (VALID_SCOPES, coerce_scope,
                                            load_scope_overrides, set_scope_override)

        if args and args[-1] == "?":
            args = args[:-1]
        if len(args) < 2:
            console.print(
                "[yellow]Usage:[/yellow] feature scope <command> <global|folder|device|remote|reset>\n"
                "  [dim]e.g. feature scope 'ping host' device   |   feature scope 'show bgp' reset[/dim]"
            )
            return
        # The scope token is the last arg; everything before it is the command key.
        scope_token = args[-1].lower()
        cmd_key = " ".join(args[:-1]).strip().lower()

        if cmd_key not in COMMANDS:
            key, cmd_def, _ = match_command(cmd_key.split())
            if key is None:
                console.print(
                    f"[red]Unknown command:[/red] [bold]{cmd_key}[/bold]\n"
                    "  [dim]Give the full command key, e.g. [bold]show bgp[/bold] or [bold]ping host[/bold].[/dim]"
                )
                return
            cmd_key = key

        cmd_def = COMMANDS[cmd_key]
        if scope_token in ("reset", "default", "clear", "none"):
            try:
                set_scope_override(cmd_key, None)
            except RuntimeError as exc:
                console.print(f"[red]Could not save scope override:[/red] {exc}")
                return
            self._scope_overrides = load_scope_overrides()
            self._invalidate_visible_keys()
            console.print(
                f"  [bold]{cmd_key}[/bold]  →  scope reset to code default "
                f"[cyan]{cmd_def.scope}[/cyan]"
            )
            return

        norm = coerce_scope(scope_token)
        if norm is None:
            console.print(
                f"[red]Invalid scope:[/red] {scope_token!r}  "
                f"[dim](valid: {', '.join(VALID_SCOPES)}, or 'reset')[/dim]"
            )
            return
        try:
            set_scope_override(cmd_key, norm)
        except RuntimeError as exc:
            console.print(f"[red]Could not save scope override:[/red] {exc}")
            return
        self._scope_overrides = load_scope_overrides()
        self._invalidate_visible_keys()
        warn = ""
        if norm != cmd_def.scope:
            warn = f"  [dim](code default: {cmd_def.scope})[/dim]"
        if norm == "remote":
            warn += "\n  [yellow]Note:[/yellow] remote = runs via SSH to the device — expect the device login/2FA."
        elif norm == "device":
            warn += "\n  [dim]device = runs via the SCM device tunnel (no SSH/2FA); needs [bold]cd <device>[/bold].[/dim]"
        console.print(
            f"  [bold]{cmd_key}[/bold]  →  scope [cyan]{norm}[/cyan]{warn}  "
            f"[dim](saved to local.json)[/dim]"
        )

    def _cmd_feature_meta(self, which: str, args: list[str]) -> None:
        """Set per-domain file meta: default state or carry flag.

        Usage: feature default <domain> <on|dev|off>
               feature carry <domain> <on|off>
        """
        from app.settings.features import load_file_meta, set_file_meta

        meta = load_file_meta()
        if args and args[-1] == "?":
            args = args[:-1]
        if len(args) < 2:
            console.print(
                f"[yellow]Usage:[/yellow] feature {which} <domain> "
                f"<{'on|dev|off' if which == 'default' else 'on|off'}>\n"
                f"  [dim]Domains: {', '.join(sorted(meta)[:6])}"
                f"{' …' if len(meta) > 6 else ''}  (see feature show for the full list)[/dim]"
            )
            return
        domain = args[0]
        value = args[1].lower()
        if domain not in meta:
            console.print(
                f"[red]Unknown domain file:[/red] {domain!r}\n"
                f"  [dim]Valid: {', '.join(sorted(meta))}[/dim]"
            )
            return
        try:
            if which == "default":
                if value not in ("on", "dev", "off"):
                    console.print("[yellow]Default must be one of:[/yellow] on | dev | off")
                    return
                set_file_meta(domain, default=value)
                console.print(
                    f"  [bold]{domain}[/bold]  default state  →  [cyan]{value}[/cyan]  "
                    f"[dim](commands not listed inherit this)[/dim]"
                )
            else:  # carry
                if value not in ("on", "off", "true", "false", "yes", "no"):
                    console.print("[yellow]Carry must be:[/yellow] on | off")
                    return
                carry = value in ("on", "true", "yes")
                set_file_meta(domain, carry=carry)
                console.print(
                    f"  [bold]{domain}[/bold]  keep-manual-edits  →  "
                    f"[cyan]{'on' if carry else 'off'}[/cyan]  "
                    f"[dim](regenerator {'preserves' if carry else 'overwrites'} your true/dev values)[/dim]"
                )
        except RuntimeError as exc:
            console.print(f"[red]Could not save domain meta:[/red] {exc}")


    def _cmd_feature_gui(self) -> None:
        """Launch the browser-based feature editor and block until it closes.

        Starts a local HTTP server (127.0.0.1:<port> from config.features_gui),
        opens the default browser, and waits until the user clicks Save & Exit
        in the page (or presses Ctrl-C here).  Saves go through the same helper
        as `feature enable`, so changes persist to each flag's settings/features/
        file and apply to this running shell live.
        """
        gui_cfg = getattr(self._config, "features_gui", None)
        if gui_cfg is not None and not gui_cfg.enabled:
            console.print(
                "[yellow]The feature editor is disabled.[/yellow]\n"
                "  Set [bold]features_gui.enabled = true[/bold] in your config.json "
                "(see [bold]arc auth show[/bold] for its path), or use "
                "[bold]feature show[/bold] / [bold]feature enable <flag>[/bold] instead."
            )
            return

        port = gui_cfg.port if gui_cfg is not None else 4445

        from app.web.feature_server import FeatureGuiServer

        server = FeatureGuiServer(self, port=port)
        console.print(
            f"\n[green]Feature editor running[/green] → [bold]{server.url}[/bold]\n"
            "  [dim]Toggle flags in the browser (changes save + apply live). "
            "Click [bold]Save & Exit[/bold] there, or press [bold]Ctrl-C[/bold] here, to return.[/dim]\n"
        )
        try:
            status = server.serve()
        except KeyboardInterrupt:
            server.stop()
            status = "Feature editor closed."
        console.print(f"[cyan]{status}[/cyan]")

    def _cmd_arc_gui(self) -> None:
        """Launch the browser-based ARC settings console and block until closed.

        Mirrors `_cmd_feature_gui`: starts a local HTTP server on
        127.0.0.1:<port> (from config.arc_gui), opens the browser, and waits
        until the user clicks Save & Exit (or presses Ctrl-C here).  Every
        change made in the console goes through the same settings/config/
        keychain helpers the CLI uses.
        """
        gui_cfg = getattr(self._config, "arc_gui", None)
        if gui_cfg is not None and not gui_cfg.enabled:
            console.print(
                "[yellow]The ARC settings console is disabled.[/yellow]\n"
                "  Set [bold]arc_gui.enabled = true[/bold] in your config.json "
                "(see [bold]arc show paths[/bold] for its location)."
            )
            return

        port = gui_cfg.port if gui_cfg is not None else 4444

        from app.web.arc_server import ArcGuiServer

        server = ArcGuiServer(self, port=port)
        console.print(
            f"\n[green]ARC settings console running[/green] → [bold]{server.url}[/bold]\n"
            "  [dim]Manage credentials, config, preferences, appearance, branding, "
            "sources and maintenance in the browser. Click [bold]Save & Exit[/bold] "
            "there, or press [bold]Ctrl-C[/bold] here, to return.[/dim]\n"
        )
        try:
            status = server.serve()
        except KeyboardInterrupt:
            server.stop()
            status = "ARC settings console closed."
        console.print(f"[cyan]{status}[/cyan]")

    def _cmd_scm(self, args: list[str]) -> None:
        """Manage SCM credentials and profiles.

          scm                 — show active profile, TSG and connection status
          scm status          — same as bare `scm`
          scm login [profile] — switch to a profile and authenticate (prompts if omitted)
          scm setup [profile] — create or edit a credential profile (interactive)
          scm delete <name>   — delete a credential profile
          scm gui             — open the browser settings console (profiles, creds…)
        """
        sub = args[0].lower() if args else "status"
        rest = args[1:]

        if sub in ("?", "help"):
            console.print(
                "[bold]scm[/bold] — manage SCM credentials & profiles\n"
                "  [bold]scm[/bold] / [bold]scm status[/bold]    show active profile, TSG, connection\n"
                "  [bold]scm login [profile][/bold]   switch profile + authenticate (prompts if omitted)\n"
                "  [bold]scm setup [profile][/bold]   create/edit a profile (interactive wizard)\n"
                "  [bold]scm delete <name>[/bold]     delete a profile\n"
                "  [bold]scm gui[/bold]               open the browser settings console"
            )
            return

        if sub == "status":
            self._cmd_scm_status()
        elif sub == "login":
            self._cmd_scm_login(rest)
        elif sub == "setup":
            self._cmd_scm_setup(rest)
        elif sub == "delete":
            self._cmd_scm_delete(rest)
        elif sub == "gui":
            self._cmd_arc_gui()
        else:
            console.print(
                f"[yellow]Unknown scm subcommand:[/yellow] {sub!r}\n"
                "  Try: [bold]scm login[/bold] · [bold]scm setup[/bold] · "
                "[bold]scm status[/bold] · [bold]scm delete <name>[/bold] · [bold]scm gui[/bold]"
            )

    def _cmd_scm_status(self) -> None:
        """Show the profile table plus the live connection state."""
        self._print_profile_list()
        active = self._config.profile_name
        tsg = self._config.scm.tsg_id or "n/a"
        if self._scm is not None:
            state = "[green]connected[/green]"
        else:
            state = "[yellow]not authenticated — run [bold]scm login[/bold][/yellow]"
        console.print(
            f"\n  Active: [bold]{active}[/bold]   TSG: [cyan]{tsg}[/cyan]   SCM: {state}\n"
        )

    def _cmd_scm_login(self, rest: list[str]) -> None:
        """Switch to a profile and authenticate. No arg → numbered picker."""
        if not has_configured_profiles():
            console.print(
                "[yellow]No SCM profiles configured yet.[/yellow]\n"
                "  Run [bold]scm setup[/bold] to create one."
            )
            return

        if rest:
            target = rest[0].strip()
            names = [p["name"] for p in list_profiles()]
            if target not in names:
                console.print(
                    f"[red]Profile '{target}' not found.[/red]\n"
                    f"  Available: [bold]{', '.join(names)}[/bold]  ·  "
                    "create one with [bold]scm setup[/bold]"
                )
                return
            self._switch_profile(target)
            return

        target = self._pick_profile()
        if target:
            self._switch_profile(target)

    def _pick_profile(self) -> "Optional[str]":
        """Numbered profile chooser for `scm login`. Returns a name or None."""
        profiles = list_profiles()
        active = self._config.profile_name

        console.print("\n  [dim]Select a profile to log into:[/dim]")
        for i, p in enumerate(profiles, start=1):
            mark = " [green](active)[/green]" if p["name"] == active else ""
            cid  = p["client_id"] or "[dim](not set)[/dim]"
            console.print(f"  [cyan]{i:<3}[/cyan][green]{p['name']:<22}[/green][dim]{cid}[/dim]{mark}")
        console.print()

        try:
            raw = input(f"  Enter # or name [{active}]: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Cancelled.[/dim]")
            return None

        if not raw:
            return active
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(profiles):
                return profiles[idx]["name"]
            console.print(f"[red]Invalid number: {raw} (valid range 1–{len(profiles)})[/red]")
            return None
        names = {p["name"] for p in profiles}
        if raw in names:
            return raw
        console.print(f"[red]Profile '{raw}' not found.[/red]")
        return None

    def _cmd_scm_setup(self, rest: list[str]) -> None:
        """Run the interactive credential wizard, then log into the saved profile."""
        from app.auth.wizard import WizardCancelled, run_credential_wizard

        profile = rest[0].strip() if rest else None
        try:
            saved = run_credential_wizard(profile=profile)
        except WizardCancelled:
            console.print("\n[yellow]Cancelled — nothing saved.[/yellow]")
            return
        if saved:
            self._switch_profile(saved)

    def _cmd_scm_delete(self, rest: list[str]) -> None:
        """Delete a credential profile (cannot delete the active one)."""
        if not rest:
            console.print("[yellow]Usage:[/yellow] scm delete <profile>")
            return
        name = rest[0].strip()
        if name == self._config.profile_name:
            console.print(
                f"[red]Cannot delete the active profile '{name}'.[/red]\n"
                "  Switch to another first: [bold]scm login <other>[/bold]."
            )
            return
        try:
            delete_profile(name)
        except ValueError as exc:
            console.print(f"[red]{exc}[/red]")
            return
        console.print(f"[green]✓[/green] Deleted profile [bold]{name}[/bold].")


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
        from app.settings.features import is_enabled
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
        """Stream app/scripts/commandupdate.py — same script the LLM 'commandupdate' trigger runs."""
        import sys as _sys
        import subprocess as _sp
        from app.paths import REPO_ROOT
        from app.settings import command_structure as cs

        script = REPO_ROOT / "app" / "scripts" / "commandupdate.py"
        if not script.exists():
            console.print("[red]app/scripts/commandupdate.py not found.[/red]")
            return

        extra: list[str] = list(targets)  # specific command, if given
        console.print("\n[magenta]● command-structure update[/magenta]\n")
        try:
            proc = _sp.Popen(
                [_sys.executable, str(script)] + extra,
                stdout=_sp.PIPE, stderr=_sp.STDOUT,
                text=True, bufsize=1, cwd=str(REPO_ROOT),
            )
            if not proc.stdout:
                raise RuntimeError("Popen stdout pipe not available — check subprocess flags")
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
            ("docs update",                "ONE-STOP: pull pan.dev specs + rebuild everything (catalogs, docs, command structure, code map, offline bundle)"),
            ("docs status",                "Show spec/doc timestamps and change summary"),
            ("catalog rebuild",            "Rebuild everything from current code — same as docs update, minus the network pull"),
            ("command-structure list",     "Show contextual ? help coverage for all enabled commands"),
            ("command-structure clear",    "Wipe auto-generated entries (reset to tier 3 fallback)"),
            ("exit",                       "Leave dev shell"),
        ]
        # (`command-structure update` is intentionally not listed — it now runs
        # automatically inside docs update / catalog rebuild.  Still typeable for
        # a quick single-command refresh.)
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

        # Inline ? on a dev-shell-specific command → show that command's help.
        # For all other commands (feature, show, cd, etc.) return None so the
        # normal dispatch handles ? — that way feature ?, show ?, etc. work
        # identically in dev shell mode and normal mode.
        _DEV_SHELL_CMDS = {"status", "docs", "catalog", "command-structure"}
        if len(tokens) >= 2 and tokens[-1] == "?":
            if cmd in _DEV_SHELL_CMDS:
                self._dev_inline_help(tokens[:-1])
                return False
            return None  # let normal dispatch handle ? for non-dev commands

        if cmd in ("exit", "quit"):
            self._dev_shell_exit()
            return False

        if cmd in ("?", "help") and len(tokens) == 1:
            # Fall through to normal ? / help dispatch so the full ARC command
            # tree is shown (dev mode reveals all non-false commands).
            # The dev shell menu is appended after by _print_shell_builtins
            # via the dev shell section printed in _cmd_help_inline.
            return None

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
                "  Runs [bold]app/scripts/docsupdate.py[/bold] as a subprocess with live output.\n"
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
                "    [cyan]generate_api_index.py[/cyan]         → app/scripts/API_INDEX.md\n"
                "    [cyan]generate_code_map.py[/cyan]          → app/scripts/CODE_MAP.md\n\n"
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
        from app.paths import REPO_ROOT

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

        script = REPO_ROOT / "app" / "scripts" / "docsupdate.py"
        if not script.exists():
            console.print("[red]app/scripts/docsupdate.py not found.[/red]")
            return

        lf = [f.lower() for f in flags]
        if "--scm" in lf or "--panos" in lf:
            console.print(
                "[dim]note: docs update runs a full SCM + PAN-OS refresh; "
                "--scm/--panos partial updates aren't supported.[/dim]"
            )

        console.print(
            f"\n[magenta]● docs update[/magenta]  "
            f"[dim]running app/scripts/docsupdate.py … (30–120 s)[/dim]\n"
        )
        try:
            proc = _sp.Popen(
                [_sys.executable, str(script)],
                stdout=_sp.PIPE, stderr=_sp.STDOUT,
                text=True, bufsize=1, cwd=str(REPO_ROOT),
            )
            if not proc.stdout:
                raise RuntimeError("Popen stdout pipe not available — check subprocess flags")
            for raw_line in proc.stdout:
                console.print(raw_line.rstrip())
            rc = proc.wait()
        except Exception as exc:
            console.print(f"[red]Failed to run docsupdate.py:[/red] {exc}")
            return

        if rc == 0:
            # docsupdate already ran the canonical catalog rebuild
            # (catalog_rebuild.py) end-to-end, so don't rebuild again — just
            # refresh the live shell's in-memory caches so changes show now.
            self._dev_invalidate_caches()
            console.print(
                "\n[green]✓ docs update complete.[/green]  "
                "[dim]Catalogs, docs, command structure + bundle regenerated; "
                "live caches refreshed — no restart needed.[/dim]\n"
            )
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

    def _dev_catalog_rebuild(self) -> None:
        """Run the canonical catalog rebuild, then refresh the live shell's caches.

        Delegates to app/scripts/catalog_rebuild.py — the SAME orchestration
        docsupdate runs — so the dev-shell and docsupdate can never regenerate
        different sets of artifacts.  That script regenerates every catalog + doc,
        command-structure.json (commandupdate), CODE_MAP.md, and the offline docs
        bundle (arc cliup).
        """
        import sys as _sys
        import subprocess as _sp
        from app.paths import REPO_ROOT

        script = REPO_ROOT / "app" / "scripts" / "catalog_rebuild.py"
        if not script.exists():
            console.print("[red]app/scripts/catalog_rebuild.py not found.[/red]")
            return

        console.print("\n[magenta]● catalog rebuild[/magenta]\n")
        try:
            proc = _sp.Popen(
                [_sys.executable, str(script)],
                stdout=_sp.PIPE, stderr=_sp.STDOUT,
                text=True, bufsize=1, cwd=str(REPO_ROOT),
            )
            if not proc.stdout:
                raise RuntimeError("Popen stdout pipe not available — check subprocess flags")
            for raw_line in proc.stdout:
                console.print(raw_line.rstrip())
            rc = proc.wait()
        except Exception as exc:
            console.print(f"[red]Failed to run catalog_rebuild.py:[/red] {exc}")
            return

        self._dev_invalidate_caches()
        console.print()
        if rc == 0:
            console.print(
                "[green]✓ catalog rebuild complete.[/green]  "
                "[dim]Changes are live immediately — no restart needed.[/dim]\n"
            )
        else:
            console.print(
                "[yellow]catalog rebuild finished with errors — check output above.[/yellow]\n"
            )

    def _dev_invalidate_caches(self) -> None:
        """Refresh the live shell's in-memory caches after generators rewrote
        their files on disk (command-structure + feature flags), so the changes
        are visible in this session without a restart."""
        from app.settings import command_structure as cs
        cs.invalidate_cache()
        try:
            from app.settings.features import _reload_cache
            _reload_cache()
        except ImportError:
            pass



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


    # =========================================================================
    # arc — application information and management
    # =========================================================================

    def _cmd_arc(self, args: list[str]) -> None:  # noqa: C901
        """ARC application information and management.

        arc show              — show all sections
        arc show version      — version, Python, platform
        arc show paths        — app root, settings, config directories
        arc show scm          — SCM API spec freshness and last changes
        arc show commands     — command counts and feature flag stats
        arc show settings     — settings file inventory
        arc show session      — active profile, TSG, folder, device, mode
        arc gui-configure     — open the browser settings console
        arc ?                 — list sub-commands
        """
        sub = args[0].lower() if args else "?"
        section = args[1].lower() if len(args) > 1 else "all"

        if sub == "gui-configure":
            self._cmd_arc_gui()
            return

        _SECTIONS = {
            "version":  self._arc_show_version,
            "paths":    self._arc_show_paths,
            "scm":      self._arc_show_scm,
            "commands": self._arc_show_commands,
            "settings": self._arc_show_settings,
            "session":  self._arc_show_session,
        }

        if sub == "show":
            if section == "all":
                # Print header then all sections
                console.print()
                console.print(
                    "  [bold cyan]ARC[/bold cyan]  "
                    "[dim]Assisted Remote Console — Palo Alto Networks SCM + PAN-OS[/dim]\n"
                )
                for fn in _SECTIONS.values():
                    fn(header=True)
            elif section in _SECTIONS:
                console.print()
                _SECTIONS[section](header=False)
                console.print()
            elif section == "?":
                self._arc_help()
            else:
                console.print(
                    f"[yellow]Unknown section:[/yellow] {section!r}\n"
                    "  arc show  |  arc show version  |  arc show paths  |  "
                    "arc show scm  |  arc show commands  |  arc show settings  |  arc show session"
                )

        elif sub in ("?", "help"):
            self._arc_help()
        else:
            console.print(
                f"[yellow]Unknown arc sub-command:[/yellow] {sub!r}\n"
                "  Try: [bold]arc show[/bold]  |  [bold]arc ?[/bold]"
            )

    def _arc_help(self) -> None:
        """Print arc sub-command reference."""
        t = self._theme
        w = 24
        console.print()
        console.print(
            "  [bold yellow]arc[/bold yellow]  "
            "[dim]— application information and management[/dim]\n"
        )
        rows = [
            ("arc show",          "All sections"),
            ("arc show version",  "Version, Python, platform"),
            ("arc show paths",    "App root, settings, config directories"),
            ("arc show scm",      "SCM API spec freshness and last changes"),
            ("arc show commands", "Command counts and feature flag stats"),
            ("arc show settings", "Settings file inventory"),
            ("arc show session",  "Active profile, TSG, folder, device, mode"),
            ("arc gui-configure", "Open the browser settings console"),
        ]
        for cmd, desc in rows:
            console.print(
                f"  {self._styled(f'{cmd:<{w}}', t.command_name)} "
                f"{self._styled(desc, t.description_dim)}"
            )
        console.print()

    # ------------------------------------------------------------------
    # arc show section helpers
    # ------------------------------------------------------------------

    def _arc_row(self, label: str, value: str, dim_note: str = "") -> None:
        """Print one labelled row in the arc show style."""
        lw = 24
        console.print(
            f"  {self._styled(f'{label:<{lw}}', self._theme.command_name)} {value}"
            + (f"  [dim]{dim_note}[/dim]" if dim_note else "")
        )

    def _arc_show_version(self, header: bool = False) -> None:
        """arc show version — version, Python, platform."""
        import sys as _sys, platform as _platform, subprocess as _sp
        from app import __version__
        from app.paths import REPO_ROOT

        if header:
            console.print(f"  [dim]{'─' * 52}[/dim]")
            console.print("  [bold]Version[/bold]\n")

        try:
            git_result = _sp.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True, text=True, cwd=str(REPO_ROOT)
            )
            git_ref = git_result.stdout.strip() if git_result.returncode == 0 else ""
        except OSError:
            git_ref = ""

        self._arc_row("Version",  f"[bold]{__version__}[/bold]",
                      f"commit {git_ref}" if git_ref else "")
        self._arc_row("Python",   _sys.version.split()[0],
                      _platform.python_implementation())
        self._arc_row("Platform", _platform.system() + " " + _platform.release())

    def _arc_show_paths(self, header: bool = False) -> None:
        """arc show paths — app root, settings, config directories."""
        from app.paths import REPO_ROOT, SETTINGS_DIR, CONFIG_DIR, FEATURES_DIR

        if header:
            console.print()
            console.print(f"  [dim]{'─' * 52}[/dim]")
            console.print("  [bold]Paths[/bold]\n")

        self._arc_row("App root",  str(REPO_ROOT))
        self._arc_row("Settings",  str(SETTINGS_DIR.relative_to(REPO_ROOT)))
        self._arc_row("Features",  str(FEATURES_DIR.relative_to(REPO_ROOT)))
        self._arc_row("Config",    str(CONFIG_DIR.relative_to(REPO_ROOT)),
                      "per-user, gitignored")

    def _arc_show_scm(self, header: bool = False) -> None:
        """arc show scm — SCM API spec freshness and last change."""
        import re as _re, datetime as _dt
        from app.paths import REPO_ROOT

        if header:
            console.print()
            console.print(f"  [dim]{'─' * 52}[/dim]")
            console.print("  [bold]SCM API Specs[/bold]\n")

        manifest  = REPO_ROOT / "docs" / "scm-api" / "MANIFEST.md"
        specs_dir = REPO_ROOT / "docs" / "scm-api" / "specs"
        changes   = REPO_ROOT / "docs" / "scm-api" / "CHANGES.md"

        if manifest.exists():
            txt = manifest.read_text(encoding="utf-8")
            m = _re.search(r"Pulled on (\d{4}-\d{2}-\d{2})", txt)
            if m:
                pull_date = m.group(1)
                pulled_dt = _dt.date.fromisoformat(pull_date)
                age = (_dt.date.today() - pulled_dt).days
                color = "green" if age <= 3 else "yellow" if age <= 14 else "red"
                self._arc_row("Last docsupdate", f"[bold]{pull_date}[/bold]",
                              f"[{color}]{age}d ago[/{color}]")
            else:
                self._arc_row("Last docsupdate", "[dim]unknown[/dim]")
        else:
            self._arc_row("Last docsupdate", "[red]never[/red]", "run: dev → docs update")

        if specs_dir.exists():
            specs = list(specs_dir.glob("*.yaml"))
            self._arc_row("Spec files", f"{len(specs)} yaml specs", "docs/scm-api/specs/")

        if changes.exists():
            for line in changes.read_text(encoding="utf-8").splitlines():
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and not stripped.startswith(">"):
                    self._arc_row("Last change", stripped[:64])
                    break

    def _arc_show_commands(self, header: bool = False) -> None:
        """arc show commands — command counts and feature flag stats."""
        from app.commands.registry import COMMANDS
        from app.settings.features import is_enabled, is_feature_visible, feature_state

        if header:
            console.print()
            console.print(f"  [dim]{'─' * 52}[/dim]")
            console.print("  [bold]Commands[/bold]\n")

        total   = len(COMMANDS)
        enabled = sum(1 for c in COMMANDS.values()
                      if is_enabled(self._features, c.feature_flag, self._dev_mode))
        visible = sum(1 for c in COMMANDS.values()
                      if is_feature_visible(self._features, c.feature_flag, self._dev_mode))
        dev_cnt = sum(1 for c in COMMANDS.values()
                      if feature_state(self._features, c.feature_flag) == "dev")
        gated   = sum(1 for c in COMMANDS.values() if c.feature_flag)

        self._arc_row("Total registered", f"{total:,}")
        self._arc_row("Enabled",          f"[green]{enabled:,}[/green]",    "executable")
        self._arc_row("Visible in ?",     f"[green]{visible:,}[/green]",    "shown in help")
        self._arc_row("Dev-mode only",    f"[yellow]{dev_cnt:,}[/yellow]",  "revealed by: dev on")
        self._arc_row("Always on",        f"{total - gated:,}",             "no feature gate")

        all_f = list(self._features.keys())
        on_f  = sum(1 for f in all_f if feature_state(self._features, f) == "on")
        dev_f = sum(1 for f in all_f if feature_state(self._features, f) == "dev")
        off_f = len(all_f) - on_f - dev_f
        self._arc_row("Feature flags",
                      f"[green]{on_f} on[/green]  [yellow]{dev_f} dev[/yellow]  [dim]{off_f} off[/dim]",
                      f"({len(all_f)} total in settings/features/)")

    def _arc_show_settings(self, header: bool = False) -> None:
        """arc show settings — settings file inventory."""
        from app.paths import SETTINGS_DIR, COMMAND_STRUCTURE_JSON, COMMAND_ALIASES_JSON

        if header:
            console.print()
            console.print(f"  [dim]{'─' * 52}[/dim]")
            console.print("  [bold]Settings Files[/bold]\n")

        files = [
            ("command-structure.json", COMMAND_STRUCTURE_JSON),
            ("command-aliases.json",   COMMAND_ALIASES_JSON),
            ("builtin-commands.json",  SETTINGS_DIR / "builtin-commands.json"),
            ("app-variables.json",     SETTINGS_DIR / "app-variables.json"),
            ("theme.json",             SETTINGS_DIR / "theme.json"),
            ("cli-structure.yaml",     SETTINGS_DIR / "cli-structure.yaml"),
        ]
        for name, path in files:
            if path.exists():
                size = path.stat().st_size
                self._arc_row(name, f"[dim]{size:,} bytes[/dim]")
            else:
                self._arc_row(name, "[red]missing[/red]")

    def _arc_show_session(self, header: bool = False) -> None:
        """arc show session — active profile, TSG, folder, device, modes."""
        if header:
            console.print()
            console.print(f"  [dim]{'─' * 52}[/dim]")
            console.print("  [bold]Active Session[/bold]\n")

        self._arc_row("Profile",   f"[bold]{self._config.profile_name}[/bold]")
        self._arc_row("TSG",       self._state.tsg_id or "(root)")
        self._arc_row("Folder",    self._state.folder)
        self._arc_row("Device",    device_display_name(self._state.device)
                      if self._state.device else "[dim]none[/dim]")
        self._arc_row("SCM",       "[green]connected[/green]" if self._scm
                      else "[dim]not connected[/dim]")
        self._arc_row("Dev mode",  "[magenta]on[/magenta]" if self._dev_mode
                      else "[dim]off[/dim]")
        self._arc_row("Configure", "[yellow]active[/yellow]" if self._state.configure_mode
                      else "[dim]off[/dim]")

    def _arc_show(self) -> None:
        """arc show (all) — kept for backward compat; calls _cmd_arc(['show'])."""
        self._cmd_arc(["show"])


