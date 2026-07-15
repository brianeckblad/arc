"""ArcShell execution mixin — API / SSH command execution + result rendering."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class ExecutionMixin:
    def _execute_api(self, key: str, cmd_def: CommandDef, args: dict) -> None:
        # Feature flag check — block before any other validation.
        if not is_enabled(self._features, cmd_def.feature_flag, self._dev_mode):
            flag = cmd_def.feature_flag
            if feature_state(self._features, flag) == "dev":
                # Under development — revealed by development mode, not by editing JSON.
                console.print(
                    f"[yellow]Under development:[/yellow] [bold]{key}[/bold]\n"
                    f"  Flag [bold]{flag}[/bold] is marked [magenta]dev[/magenta].\n"
                    f"  Type [bold]dev[/bold] to enter development mode, then retry."
                )
            else:
                console.print(
                    f"[yellow]Feature not enabled:[/yellow] [bold]{key}[/bold]\n"
                    f"  Flag [bold]{flag}[/bold] is currently off.\n"
                    f"  To enable: set [bold]\"{flag}\": true[/bold] in its [bold]settings/features/[/bold] file\n"
                    f"  or set env var [bold]ARC_FEATURE_{flag.upper()}=on[/bold]"
                )
            return

        if key == "commit" and not self._state.configure_mode:
            console.print(
                f"[yellow]Write operation blocked:[/yellow] [bold]{key}[/bold] requires configure mode.\n"
                "  Enter [bold]configure[/bold] first, then retry."
            )
            return

        # All set/delete/update registered commands are write operations — block outside configure mode.
        if (key.startswith(("set ", "delete ", "update "))) and not self._state.configure_mode:
            console.print(
                f"[yellow]Write operation blocked:[/yellow] [bold]{key}[/bold] requires configure mode.\n"
                "  Enter [bold]configure[/bold] first, then retry."
            )
            return

        ctx = self._make_context()

        # Enforce scope (with per-command override) before calling the handler.
        if self.resolve_scope(key, cmd_def) == "device" and not ctx.device:
            device_hint = (
                "Use [bold]cd <device>[/bold] to select a device first, "
                "then run this command again.\n"
                f"Or run [bold]{key} --remote <device>[/bold] to target a "
                "device directly without changing context.\n"
                "Tab after 'cd ' or '--remote ' to see available devices."
            )
            console.print(
                f"[yellow]'{key}'[/yellow] requires a device context  "
                f"[dim](scope: device)[/dim]\n  {device_hint}"
            )
            return

        if cmd_def.api_handler is None:
            console.print(f"[yellow]No API handler for '{key}'.[/yellow]")
            return

        try:
            # Configure-mode writes are STAGED, not executed: the handler runs
            # against a recording client (GETs pass through for validation;
            # mutations are captured). `commit` replays them; `abandon` drops
            # them. SCM is untouched until commit.
            if key.startswith(("set ", "delete ", "update ")):
                self._stage_write(key, cmd_def, ctx, args)
                return

            # Spinner while the API call runs — skipped when output is being
            # captured for a pipe filter, the console is not a terminal (rich
            # Live displays don't nest under capture), or the user turned it
            # off (`terminal spinner off`).
            use_spinner = (
                console.is_terminal
                and not getattr(self, "_piping", False)
                and getattr(getattr(self, "_prefs", None), "spinner", True)
            )
            if use_spinner:
                status_ctx = console.status("[dim]querying SCM…[/dim]", spinner="dots")
                # Attach a progress reporter so paginated fetches update the
                # spinner text as each page arrives, keeping the operator informed.
                if self._scm is not None:
                    def _on_page(fetched: int, total: int) -> None:
                        status_ctx.update(f"[dim]fetching… {fetched}/{total}[/dim]")
                    self._scm._page_reporter = _on_page
                try:
                    with status_ctx:
                        data = cmd_def.api_handler(ctx, args)
                finally:
                    if self._scm is not None:
                        self._scm._page_reporter = None
            else:
                data = cmd_def.api_handler(ctx, args)
            self._render(key, cmd_def, data)
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            if status == 401:
                console.print(
                    "[red]Authentication failed (401).[/red] Token may be expired — "
                    "run [bold]arc auth test[/bold] outside the shell, or "
                    "[bold]account <profile>[/bold] to re-select credentials."
                )
            elif status == 403:
                console.print(
                    "[red]Permission denied (403).[/red] Your role or TSG scope may "
                    "not allow this — check [bold]tsg[/bold] and your "
                    "service-account role."
                )
            elif status == 404:
                console.print(
                    "[red]Not found (404)[/red] — the resource or folder may not "
                    "exist in this TSG. Active folder: "
                    f"[bold]{self._state.folder}[/bold]."
                )
            else:
                raw_detail = (exc.response.text or "").strip()
                # Sanitize: mask anything that looks like a bearer token or secret
                # before displaying to avoid leaking credentials from API error bodies.
                import re as _re
                sanitized = _re.sub(
                    r'(Bearer\s+)[A-Za-z0-9\-._~+/]+=*',
                    r'\1[REDACTED]',
                    raw_detail,
                    flags=_re.IGNORECASE,
                )
                sanitized = _re.sub(
                    r'("(?:token|secret|password|bearer)"\s*:\s*")[^"]{8,}(")',
                    r'\1[REDACTED]\2',
                    sanitized,
                    flags=_re.IGNORECASE,
                )
                # Collapse whitespace and truncate at a word boundary so we
                # never chop a useful error message mid-word.  400 chars gives
                # enough context for most SCM error bodies.
                collapsed = " ".join(sanitized.split())
                if len(collapsed) > 400:
                    trunc = collapsed[:400]
                    last_space = trunc.rfind(" ")
                    collapsed = (trunc[:last_space] if last_space > 300 else trunc) + " …"
                detail = collapsed
                console.print(
                    f"[red]API error ({status}).[/red] {detail}"
                    if detail else f"[red]API error ({status}).[/red]"
                )
        except httpx.HTTPError as exc:
            console.print(
                f"[red]Cannot reach SCM API:[/red] {exc}. Check network/VPN and retry."
            )
        except ValueError as exc:
            console.print(f"[yellow]{exc}[/yellow]")

    def _execute_remote(self, key: str, cmd_def: CommandDef, args: dict) -> None:
        if cmd_def.ssh_command is None:
            console.print(
                f"[yellow]'{key}' has no SSH equivalent — it is a config/API-only command.[/yellow]\n"
                "Falling back to API path."
            )
            self._execute_api(key, cmd_def, args)
            return

        device = self._state.device
        if not device:
            console.print(
                "[red]--remote requires a device context.[/red] "
                "Use [bold]cd <device>[/bold] first."
            )
            return

        # Warn when the active device is a stub (created from a direct name/IP
        # when the SCM device cache was empty).  SSH may still work if the host
        # is directly reachable, but SCM fields like serial and model are absent.
        if device.get("_is_stub"):
            console.print(
                f"[yellow]⚠  Device '{device.get('name')}' is a direct-entry stub "
                "(not verified against SCM).[/yellow]\n"
                "  [dim]Use [bold]show devices[/bold] + [bold]cd device <name>[/bold] "
                "for a fully verified device context.[/dim]"
            )

        host = device_ssh_host(device)
        if not host:
            console.print(
                "[red]Cannot determine SSH target — no IP or hostname for this device.[/red]\n"
                "  Check [bold]show devices[/bold] for the device's IP address, "
                "or use [bold]arc auth configure[/bold] to set up SSH credentials."
            )
            return

        ssh_cmd = self._resolve_ssh_command(cmd_def, args)

        cfg_ssh = self._config.ssh
        ssh_user = str(cfg_ssh.user)
        ssh_key_path = str(cfg_ssh.key_path)
        ssh_password = str(cfg_ssh.password)
        ssh_port = int(cfg_ssh.port)

        # Pre-flight: validate SSH config before attempting the connection so
        # the operator gets an actionable message immediately rather than a
        # cryptic paramiko/auth error after a TCP handshake.
        if not ssh_user:
            console.print(
                "[red]SSH username is not configured.[/red]\n"
                "  Run [bold]arc auth configure[/bold] and set the SSH Username field.\n"
                "  Or set env var [bold]ARC_SSH_USER=admin[/bold] for this session."
            )
            return
        import os as _os
        if ssh_key_path and not _os.path.exists(_os.path.expanduser(ssh_key_path)):
            console.print(
                f"[red]SSH key file not found:[/red] {ssh_key_path}\n"
                "  Update the path with [bold]arc auth configure[/bold] or remove it to use "
                "SSH agent / password auth."
            )
            return

        console.print(
            f"[dim]SSH → {ssh_user}@{host}:{ssh_port}  cmd: {ssh_cmd}[/dim]"
        )

        if cmd_def.category == "panos-config":
            # Break-glass: device-local config drifts from SCM. Say so every
            # time, and run through the scripted configure-mode channel
            # (PAN-OS set/delete only work inside `configure`).
            console.print(
                "[yellow]⚠ DRIFT WARNING:[/yellow] this changes DEVICE-LOCAL config. "
                "SCM does not know about it and may overwrite it at the next push. "
                "Commit on the device with [bold]commit --remote[/bold] when done."
            )
            output = self._ssh.run_config_commands(
                host=host,
                commands=[ssh_cmd],
                user=ssh_user,
                key_path=ssh_key_path,
                password=ssh_password,
                port=ssh_port,
            )
        else:
            output = self._ssh.execute(
                host=host,
                command=ssh_cmd,
                user=ssh_user,
                key_path=ssh_key_path,
                password=ssh_password,
                port=ssh_port,
            )
        console.print(fmt.format_raw(output, title=f"SSH: {key}"))

    def _resolve_ssh_command(self, cmd_def: CommandDef, args: dict) -> str:
        """Return the concrete SSH command string for a registered command."""
        ssh_command = cmd_def.ssh_command
        if ssh_command is None:
            raise RuntimeError("Command has no SSH equivalent.")
        if isinstance(ssh_command, str):
            return ssh_command
        return ssh_command(args)

    def _render(self, key: str, cmd_def: CommandDef, data) -> None:  # noqa: C901
        # `<command> | json` — emit the raw data as JSON, bypassing all table formatters.
        # console.print with markup=False is used so the output goes into console.capture()
        # when piping; console.file.write would bypass the capture buffer.
        if getattr(self, "_render_as_json", False):
            import json as _json
            try:
                text = _json.dumps(data, indent=2, default=str, sort_keys=False)
            except (TypeError, ValueError):
                text = _json.dumps(str(data))
            console.print(text, markup=False, highlight=False)
            return

        # Paging is handled globally in the run loop (paging_stdout context manager),
        # so _render just writes to console unconditionally.
        self._do_render(key, cmd_def, data, console)

    def _do_render(self, key: str, cmd_def: CommandDef, data, con) -> None:  # noqa: C901
        """Render *data* to *con* (a Rich Console). Called by _render."""
        render_hint = cmd_def.render

        # Unwrap log tuple
        if render_hint == "logs" and isinstance(data, tuple):
            log_type, rows = data
            if isinstance(rows, list):
                con.print(fmt.format_logs(rows, log_type=log_type))
            else:
                con.print(fmt.format_raw(str(rows), title=key))
            return

        # XML element fallback — ET is imported at module level
        if isinstance(data, ET.Element):
            raw = ET.tostring(data, encoding="unicode")
            con.print(fmt.format_raw(raw, title=key))
            return

        if isinstance(data, str):
            con.print(fmt.format_raw(data, title=key))
            return

        # If the handler embedded a _render override key (e.g. snippet_detail_full
        # returned from show snippet <name> details), honour it BEFORE consulting
        # the dispatch table — otherwise cmd_def.render would call the wrong formatter.
        if isinstance(data, dict) and "_render" in data:
            render_hint = data["_render"]

        dispatch = {
            "system_info":     lambda d: fmt.format_system_info(d),
            "raw":             lambda d: fmt.format_raw(str(d), title=key),
            "list":            lambda d: fmt._list_table(d if isinstance(d, list) else [], title=key),
            "devices":         lambda d: fmt.format_devices(d),
            "device_detail":   lambda d: fmt.format_device_detail(
                                   d.get("device", d) if isinstance(d, dict) else d),
            "device_snippets": lambda d: fmt.format_snippets(
                                   d.get("snippets", []) if isinstance(d, dict) else d,
                                   device_filter=d.get("device_name", "") if isinstance(d, dict) else ""),
            "snippets_scoped": lambda d: fmt.format_snippets_scoped(d if isinstance(d, dict) else {}),
            "snippet_detail":  lambda d: fmt.format_snippet_detail(d if isinstance(d, dict) else {}) or [],
            "snippet_detail_full": lambda d: fmt.format_snippet_detail_full(d if isinstance(d, dict) else {}) or [],
            "interfaces":      lambda d: fmt.format_interfaces(d),
            "routes":          lambda d: fmt.format_routes(d),
            "security_policy": lambda d: fmt.format_security_policy(d),
            "jobs":            lambda d: fmt.format_jobs(d),
            "logs":            lambda d: fmt.format_logs(d),
            "address_objects": lambda d: fmt.format_address_objects(d),
            "address_groups":  lambda d: fmt.format_address_groups(d),
            "services":        lambda d: fmt.format_services(d),
            "tags":            lambda d: fmt.format_tags(d if isinstance(d, list) else []),
            "edl_list":        lambda d: fmt.format_edl_list(d if isinstance(d, list) else []),
            "url_categories":  lambda d: fmt._list_table(d if isinstance(d, list) else [], title="URL Categories"),
            "zones":           lambda d: fmt.format_zones(d),
            "ha":              lambda d: fmt.format_ha(d, title=key),
            "dict":            lambda d: fmt.format_dict(d, title=key),
        }
        renderer = dispatch.get(render_hint)
        if renderer:
            result = renderer(data)
            # format_snippet_detail returns a list of renderables; others return one.
            if isinstance(result, list):
                for renderable in result:
                    con.print(renderable)
            else:
                con.print(result)
        elif isinstance(data, list):
            if data and isinstance(data[0], dict):
                con.print(fmt._list_table(data, title=key))
            else:
                for item in data:
                    con.print(item)
        elif isinstance(data, dict):
            con.print(fmt.format_dict(data, title=key))
        else:
            con.print(fmt.format_raw(str(data), title=key))

    def _make_context(self) -> ExecutionContext:
        return ExecutionContext(
            scm=self._scm,
            ssh=self._ssh,
            config=self._config,
            device=self._state.device,
            folder=self._state.folder,
            tsg_id=self._state.tsg_id,
        )
