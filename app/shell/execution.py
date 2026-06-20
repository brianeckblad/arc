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
                    f"  To enable: set [bold]\"{flag}\": true[/bold] in [bold]settings/features.json[/bold]\n"
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

        # Enforce scope declared on the CommandDef before calling the handler.
        if cmd_def.scope == "device" and not ctx.device:
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

        data = cmd_def.api_handler(ctx, args)
        self._render(key, cmd_def, data)

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

        host = str(device.get("ip_address") or device.get("hostname") or "")
        if not host:
            console.print("[red]Cannot determine device IP/hostname for SSH.[/red]")
            return

        ssh_cmd = self._resolve_ssh_command(cmd_def, args)

        cfg_ssh = self._config.ssh
        ssh_user = str(cfg_ssh.user)
        ssh_key_path = str(cfg_ssh.key_path)
        ssh_password = str(cfg_ssh.password)
        ssh_port = int(cfg_ssh.port)
        console.print(
            f"[dim]SSH → {ssh_user}@{host}:{ssh_port}  cmd: {ssh_cmd}[/dim]"
        )

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
        render_hint = cmd_def.render

        # Unwrap log tuple
        if render_hint == "logs" and isinstance(data, tuple):
            log_type, rows = data
            if isinstance(rows, list):
                console.print(fmt.format_logs(rows, log_type=log_type))
            else:
                console.print(fmt.format_raw(str(rows), title=key))
            return

        # XML element fallback — ET is imported at module level
        if isinstance(data, ET.Element):
            raw = ET.tostring(data, encoding="unicode")
            console.print(fmt.format_raw(raw, title=key))
            return

        if isinstance(data, str):
            console.print(fmt.format_raw(data, title=key))
            return

        # If the handler embedded a _render override key (e.g. snippet_detail_full
        # returned from show snippet <name> details), honour it BEFORE consulting
        # the dispatch table — otherwise cmd_def.render would call the wrong formatter.
        if isinstance(data, dict) and "_render" in data:
            render_hint = data["_render"]
        else:
            render_hint = cmd_def.render

        dispatch = {
            "system_info":     lambda d: fmt.format_system_info(d),
            "raw":             lambda d: fmt.format_raw(str(d), title=key),
            "devices":         lambda d: fmt.format_devices(d),
            "device_detail":   lambda d: fmt.format_device_detail(
                                   d.get("device", d) if isinstance(d, dict) else d),
            "device_snippets": lambda d: fmt.format_snippets(
                                   d.get("snippets", []) if isinstance(d, dict) else d,
                                   device_filter=d.get("device_name", "") if isinstance(d, dict) else ""),
            "snippets":        lambda d: fmt.format_snippets(d if isinstance(d, list) else []),
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
                    console.print(renderable)
            else:
                console.print(result)
        elif isinstance(data, list):
            if data and isinstance(data[0], dict):
                console.print(fmt._list_table(data, title=key))
            else:
                for item in data:
                    console.print(item)
        elif isinstance(data, dict):
            console.print(fmt.format_dict(data, title=key))
        else:
            console.print(fmt.format_raw(str(data), title=key))

    def _make_context(self) -> ExecutionContext:
        return ExecutionContext(
            scm=self._scm,
            ssh=self._ssh,
            config=self._config,
            device=self._state.device,
            folder=self._state.folder,
            tsg_id=self._state.tsg_id,
        )
