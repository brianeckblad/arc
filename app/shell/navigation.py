"""ArcShell navigation mixin — cd / folder / tsg / account / pwd + cache refresh."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


# A cd/folder miss re-fetches its cache when older than this before erroring.
_CACHE_MAX_AGE_S = 300


class NavigationMixin:
    @staticmethod
    def _cache_stale(loaded_at: float) -> bool:
        """True when a navigation cache is old enough to warrant a re-fetch."""
        return time.monotonic() - loaded_at > _CACHE_MAX_AGE_S

    def _cmd_cd(self, args: list[str]) -> None:
        """Change device, folder, or snippet context (navigation only).

        Usage:
          cd device <name>   — set device context (Tab -> device list)
          cd folder <name>   — set folder context (Tab -> folder list)
          cd folder ..       — reset folder to Shared
          cd snippet <name>  — enter a snippet container (Tab -> snippet list);
                               object set/show/clone then target the snippet
          cd snippet ..      — leave the snippet, back to folder context
          cd ..  |  cd /     — context-aware back: leaves snippet, else clears
                               device, else resets folder to Shared
          cd <name>          — shorthand for 'cd device <name>' (backward compat)
          cd                 — show current context

        To list or create folders, use the 'folder' command (configure mode).
        """
        # Bare `cd` — show current position
        if not args:
            dev = self._state.device
            folder = self._state.folder
            snippet = self._state.snippet
            container = (
                f"[cyan]snippet:[/cyan] [bold magenta]{snippet}[/bold magenta]"
                if snippet
                else f"[cyan]folder:[/cyan] [bold green]{folder}[/bold green]"
            )
            if dev:
                name = device_display_name(dev, "?")
                console.print(f"[cyan]device:[/cyan] [bold]{name}[/bold]  {container}")
            else:
                console.print(f"[cyan]context:[/cyan] global  {container}")
            console.print("[dim]  cd device <name>  |  cd folder <name>  |  cd snippet <name>  |  cd .. → back (snippet → device → folder → global)[/dim]")
            return

        # cd ..  or  cd /  — context-aware navigation:
        #   • snippet is set → exit snippet (return to folder context)
        #   • device is set → clear device (return to folder-only context)
        #   • no device, folder is set → reset folder to Shared (return to global)
        #   • already global → no-op with a hint
        if args[0] in ("..", "/"):
            if self._state.snippet:
                prev = self._state.snippet
                self._state.snippet = None
                console.print(
                    f"[cyan]Left snippet[/cyan] [bold]{prev}[/bold]  "
                    f"[dim](folder context: {self._state.folder})[/dim]"
                )
            elif self._state.device:
                self._state.device = None
                self._state.attached = False
                console.print(_cd_hint("clear"))
            elif self._state.folder and self._state.folder.lower() != "shared":
                self._state.folder = "Shared"
                console.print("[cyan]SCM folder reset to:[/cyan] [bold]Shared[/bold]  [dim](global context)[/dim]")
            else:
                console.print("[dim]Already at global context — no device or folder to clear.[/dim]")
            return

        # Subcommand dispatch
        sub = args[0].lower()
        rest = args[1:]

        if sub == "device":
            if not rest:
                console.print("[yellow]Usage:[/yellow] cd device <hostname | serial | ip>")
                return
            self._cmd_cd_device(" ".join(rest))
            return

        if sub == "folder":
            if not rest:
                console.print("[yellow]Usage:[/yellow] cd folder <name>  (Tab to list folders)")
                return
            target = rest[0]
            if target in ("..", "/"):
                self._state.folder = "Shared"
                self._state.snippet = None
                console.print("[cyan]SCM folder reset to:[/cyan] [bold]Shared[/bold]")
            else:
                self._switch_folder(" ".join(rest))
            return

        if sub == "snippet":
            if not rest:
                console.print("[yellow]Usage:[/yellow] cd snippet <name>  (Tab to list snippets)")
                return
            target = rest[0]
            if target in ("..", "/"):
                self._state.snippet = None
                console.print("[cyan]Left snippet context[/cyan]  [dim](folder: "
                              f"{self._state.folder})[/dim]")
            else:
                self._switch_snippet(" ".join(rest))
            return

        # Backward compat: `cd <name>` with no subcommand keyword → device
        self._cmd_cd_device(" ".join(args))

    def _cmd_cd_device(self, target: str) -> None:
        """Switch the active SCM/API device context to *target*.

        Fuzzy-matches hostname, serial, name, or IP against the device cache.
        Never starts an SSH session — use `connect` for that.
        """
        if not self._state.devices_cache:
            self._refresh_devices()

        match = self._find_device(target)
        # Miss on a stale cache → one silent re-fetch before the hard error,
        # so devices onboarded after startup are still found.
        if match is None and self._cache_stale(self._state.devices_loaded_at):
            self._refresh_devices(silent=True)
            match = self._find_device(target)
        if match:
            self._state.device = match
            self._state.attached = False  # new device: any warm SSH session is stale
            name    = device_display_name(match, target)
            serial  = match.get("serial_number") or match.get("serial") or match.get("name") or "n/a"
            ip_raw  = match.get("ip_address") or match.get("ip-address") or ""
            ip      = ip_raw if ip_raw and ip_raw.lower() not in ("unknown", "none") else "n/a"
            model   = match.get("model") or ""
            sw_ver  = match.get("software_version") or match.get("sw_version") or ""
            connected = (
                "  [green]connected[/green]" if match.get("is_connected")
                else "  [red]disconnected[/red]" if match.get("is_connected") is False
                else ""
            )
            parts = [f"[cyan]SCM device:[/cyan] [bold]{name}[/bold]"]
            parts.append(f"serial: [bold]{serial}[/bold]")
            parts.append(f"ip: {ip}")
            if model:
                parts.append(f"model: {model}")
            if sw_ver:
                parts.append(f"sw: {sw_ver}")
            console.print("  ".join(parts) + connected)
            console.print(f"  [dim]{_cd_hint('device', name)}[/dim]")
            return

        if self._state.devices_cache:
            active_tsg = active_tsg_label(self._state, self._config)
            console.print(
                f"[red]Device '{target}' not found in TSG {active_tsg}.[/red]\n"
                f"  [dim]Use [bold]show devices[/bold] to see "
                f"the {len(self._state.devices_cache)} device(s) visible in this TSG.\n"
                "  Use [bold]tsg <id>[/bold] to switch to a different tenant.[/dim]"
            )
        else:
            console.print(
                f"[yellow]Device list unavailable — creating stub for '{target}'.[/yellow]\n"
                "  [dim]SSH with [bold]remote[/bold] / [bold]connect[/bold] may still "
                "work if the device is reachable directly.[/dim]"
            )
            self._state.device = {
                "name": target, "hostname": target,
                "ip_address": target, "serial_number": "",
                "_is_stub": True,
            }
            self._state.attached = False

    def _find_device(self, query: str) -> Optional[dict]:
        """Find a device in the cache by hostname, serial, name, or IP.

        Checks all field-name variants the SCM API may return.
        Iterates over a snapshot of the cache to be safe against concurrent refresh.
        """
        q = query.lower()
        for d in list(self._state.devices_cache):  # snapshot guards against mutation during iteration
            if (
                (d.get("hostname") or "").lower() == q
                or (d.get("display_name") or "").lower() == q
                or (d.get("name") or "").lower() == q
                or (d.get("serial_number") or "").lower() == q
                or (d.get("serial") or "").lower() == q
                or (d.get("ip_address") or "").lower() == q
            ):
                return d
        return None

    def _refresh_devices(self, silent: bool = False) -> None:
        """Fetch managed devices and populate the cache used by tab completion and cd.

        Uses self._scm directly (same pattern as _refresh_folders / _refresh_tsgs)
        rather than going through _make_context().  The devices endpoint returns
        all managed devices TSG-wide regardless of the active folder, so no folder
        parameter is passed.
        """
        if not self._scm:
            return
        # Stamp the attempt (not just success) so a failing SCM doesn't get
        # re-hammered on every cache miss for the next few minutes.
        self._state.devices_loaded_at = time.monotonic()
        try:
            devices = self._scm.get_devices()
            if devices:
                self._state.devices_cache = devices
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh device list: {exc}[/yellow]")

    def _refresh_folders(self, silent: bool = False) -> None:
        """Fetch SCM folder names and populate the cache used by 'folder' tab completion."""
        if not self._scm:
            return
        self._state.folders_loaded_at = time.monotonic()
        try:
            folders = self._scm.get_folders()
            if folders:
                self._state.folders_cache = folders
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh folder list: {exc}[/yellow]")

    def _refresh_tsgs(self, silent: bool = False) -> None:
        """Fetch TSG entries from SCM IAM and populate the cache used by 'tsg' tab completion.

        Each entry is a dict with at minimum 'id' and 'display_name'.  The list
        may be empty if the token lacks IAM read permissions — the completer falls
        back to the configured TSG ID in that case.
        """
        if not self._scm:
            return
        try:
            tenants = self._scm.get_tenants()
            if tenants:
                self._state.tsgs_cache = tenants
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh TSG list: {exc}[/yellow]")

    def _cmd_pwd(self) -> None:
        """Show current device context, active SCM folder, TSG, and SSH credential status."""
        if self._state.device:
            d = self._state.device
            name    = device_display_name(d, "?")
            serial  = d.get("serial_number") or d.get("name") or "n/a"
            ip      = d.get("ip_address") or "n/a"
            model   = d.get("model") or ""
            sw_ver  = d.get("software_version") or ""
            connected = "[green]connected[/green]" if d.get("is_connected") else "[red]disconnected[/red]"
            snippets = d.get("snippets") or []
            console.print(
                f"[bold cyan]Device:[/bold cyan] {name}  "
                f"serial: {serial}  ip: {ip}  {model}  {sw_ver}  {connected}"
            )
            if snippets:
                console.print(
                    f"[bold cyan]Snippets:[/bold cyan] {', '.join(snippets)}"
                )
            console.print(
                "[dim]  show device snippets → full snippet list  |  "
                "show snippet <name> → snippet detail[/dim]"
            )
        else:
            console.print("[bold cyan]Context:[/bold cyan] SCM / global  [API mode]")
            console.print(
                "[dim]  show devices → list devices  |  "
                "cd <device> → enter device context  |  "
                "show device <name> → device detail[/dim]"
            )
        # Folder is always shown — it is the primary SCM scope for all API calls.
        console.print(
            f"[bold cyan]SCM folder:[/bold cyan] [bold green]{self._state.folder}[/bold green]"
            "  [dim](all API calls scoped to this folder — change with 'folder <name>')[/dim]"
        )
        if self._state.snippet:
            console.print(
                f"[bold cyan]SCM snippet:[/bold cyan] [bold magenta]{self._state.snippet}[/bold magenta]"
                "  [dim](object set/show/clone target this snippet instead of the folder — cd .. to leave)[/dim]"
            )
        active_tsg = self._state.tsg_id or "(root / config default)"
        console.print(f"[bold cyan]TSG:[/bold cyan] [cyan]{active_tsg}[/cyan]")

        # Show active profile — always useful to see which account you are on.
        profile_name = self._config.profile_name
        client_id    = self._config.scm.client_id or "(bearer token)"
        console.print(
            f"[bold cyan]Account profile:[/bold cyan] [bold]{profile_name}[/bold]  "
            f"[dim]{client_id}[/dim]"
        )

    def _switch_folder(self, new_folder: str) -> None:
        """Validate and apply a folder context change — called only by `cd folder <name>`."""
        # Always attempt validation when cache is populated.  The previous
        # logic skipped validation when cache == ["Shared", "Global"] (the
        # TSG default), which allowed silently switching to non-existent folders.
        # If the cache looks stale, refresh it once before checking.
        if self._state.folders_cache:
            if new_folder not in self._state.folders_cache:
                if self._cache_stale(self._state.folders_loaded_at):
                    self._refresh_folders(silent=True)
            if new_folder not in self._state.folders_cache:
                active_tsg = active_tsg_label(self._state, self._config)
                console.print(
                    f"[red]Folder '{new_folder}' not found in TSG {active_tsg}.[/red]\n"
                    f"  [dim]Available folders: {', '.join(sorted(self._state.folders_cache))}\n"
                    "  Tab after 'cd folder ' to complete, or 'folder' to list folders.[/dim]"
                )
                return

        self._state.folder = new_folder
        self._state.snippet = None
        if self._state.device:
            device_name = device_display_name(self._state.device)
            self._state.device = None
            self._state.attached = False
            console.print(
                f"[cyan]SCM folder set to:[/cyan] [bold]{new_folder}[/bold]  "
                f"[dim](device context {device_name} cleared — use cd to re-enter)[/dim]"
            )
        else:
            console.print(f"[cyan]SCM folder set to:[/cyan] [bold]{new_folder}[/bold]")

    def _switch_snippet(self, new_snippet: str) -> None:
        """Validate and apply a snippet context change — called by `cd snippet <name>`.

        A snippet is a config container that is mutually exclusive with a folder:
        while a snippet context is active, object reads/writes target it via
        ?snippet= instead of the active folder.  `cd ..` (or `cd snippet ..`)
        leaves the snippet and returns to the folder context.
        """
        if not self._state.snippets_cache or self._cache_stale(self._state.snippets_loaded_at):
            self._refresh_snippets(silent=True)
        names = self._state.snippets_cache
        if names and new_snippet not in names:
            match = next((n for n in names if n.lower() == new_snippet.lower()), None)
            if match:
                new_snippet = match
            else:
                active_tsg = active_tsg_label(self._state, self._config)
                console.print(
                    f"[red]Snippet '{new_snippet}' not found in TSG {active_tsg}.[/red]\n"
                    f"  [dim]Available snippets: {', '.join(sorted(names)[:20])}"
                    f"{' …' if len(names) > 20 else ''}\n"
                    "  Tab after 'cd snippet ' to complete, or 'show snippets global' to list.[/dim]"
                )
                return
        self._state.snippet = new_snippet
        console.print(
            f"[cyan]SCM snippet context:[/cyan] [bold magenta]{new_snippet}[/bold magenta]  "
            f"[dim](object set/show/clone now target this snippet — cd .. to leave)[/dim]"
        )

    def _refresh_snippets(self, silent: bool = False) -> None:
        """Fetch SCM snippet names and populate the cache used by 'cd snippet' completion."""
        if not self._scm:
            return
        self._state.snippets_loaded_at = time.monotonic()
        try:
            snippets = self._scm.get_snippets()
            if snippets:
                self._state.snippets_cache = [
                    s.get("name") for s in snippets if isinstance(s, dict) and s.get("name")
                ]
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh snippet list: {exc}[/yellow]")

    def _cmd_folder(self, args: list[str]) -> None:
        """Manage SCM folders — list available folders or create a new one.

        Requires configure mode.  Use 'cd folder <name>' to switch the active folder.

        Usage:
          folder                  — list available folders and show the active one
          folder create <name>    — create a new folder (interactive parent selection)
          folder attach-snippet <snippet>   — attach a snippet to the active folder
          folder detach-snippet <snippet>   — detach a snippet from the active folder
        """
        if not self._state.configure_mode:
            console.print(
                "[yellow]The folder command requires configure mode.[/yellow]\n"
                "  Enter [bold]configure[/bold] first, or use "
                "[bold]cd folder <name>[/bold] to switch folders."
            )
            return

        # Subcommand: folder create <name>
        if args and args[0].lower() == "create":
            folder_name = args[1] if len(args) > 1 else None
            self._cmd_folder_create(folder_name)
            return

        # Subcommand: folder attach-snippet / detach-snippet <snippet>
        if args and args[0].lower() in ("attach-snippet", "detach-snippet"):
            attach = args[0].lower() == "attach-snippet"
            snippet_name = " ".join(args[1:]).strip()
            self._cmd_folder_snippet(snippet_name, attach=attach)
            return

        # Redirect switch attempts
        if args and args[0] not in ("create",):
            console.print(
                "[yellow]Use 'cd folder <name>' to switch folders.[/yellow]\n"
                "  [dim]'folder' manages folders (list, create, attach-snippet, "
                "detach-snippet). 'cd folder <name>' changes your active folder.[/dim]"
            )
            return

        # Bare `folder` — list available folders
        console.print(f"[cyan]Active SCM folder:[/cyan] [bold]{self._state.folder}[/bold]")
        if self._state.folders_cache:
            console.print("\n[bold yellow]Available Folders[/bold yellow]  "
                          "[dim](use 'cd folder <name>' to switch)[/dim]")
            for name in sorted(self._state.folders_cache):
                marker = " [green]◀ active[/green]" if name == self._state.folder else ""
                console.print(f"  [green]{name}[/green]{marker}")
        else:
            console.print(
                "[dim]No folder list cached — run [bold]show devices[/bold] or "
                "[bold]folder[/bold] after SCM is connected to populate.[/dim]"
            )
            self._refresh_folders(silent=False)
            if self._state.folders_cache:
                console.print("\n[bold yellow]Available Folders[/bold yellow]")
                for name in sorted(self._state.folders_cache):
                    marker = " [green]◀ active[/green]" if name == self._state.folder else ""
                    console.print(f"  [green]{name}[/green]{marker}")
        console.print(
            "\n[dim]  cd folder <name> → switch  |  "
            "folder create <name> → new folder[/dim]"
        )

    def _cmd_folder_create(self, name: Optional[str]) -> None:
        """Interactive folder creation: prompt for a parent, confirm, and POST to SCM.

        Displays the full folder hierarchy as a numbered list so the operator
        can see the tree and pick the parent by number or by name.

        "above" = pick a folder closer to the root (shorter path).
        "below" = pick a folder deeper in the tree (longer path / a child folder).
        The new folder will be created as a direct child of the selected parent.
        """
        if not name or not name.strip():
            console.print(
                "[yellow]Usage:[/yellow] folder create <name>\n"
                "  Example: folder create Production-West"
            )
            return

        name = name.strip()

        if not self._scm:
            console.print("[red]SCM is not configured — run [bold]arc auth configure[/bold] to set up credentials.[/red]")
            return

        console.print("[dim]Fetching folder list…[/dim]", end="\r")
        folders = self._scm.get_folders_full()
        console.print(" " * 40, end="\r")

        if not folders:
            console.print("[yellow]No folders returned — cannot determine placement.[/yellow]")
            return

        # Build a flat ordered list: [(depth, name, full_path), …]
        flat = fmt._folder_flat_list(folders)

        # Display the numbered selection table.
        console.print(f"\n[bold]Creating folder:[/bold] [cyan]{name}[/cyan]\n")
        console.print(
            "[bold yellow]Select parent folder[/bold yellow]  "
            "[dim]('above' → pick a shorter path; 'below' → pick a deeper path)[/dim]\n"
        )

        # Header row
        console.print(f"  [dim]{'#':<5}{'Folder':<35}Path[/dim]")
        console.print("  " + "─" * 65)

        for i, (depth, fname, path) in enumerate(flat, start=1):
            indent   = "  " * depth
            name_col = f"{indent}{fname}"
            console.print(
                f"  [cyan]{i:<5}[/cyan]"
                f"[green]{name_col:<35}[/green]"
                f"[dim]{path}[/dim]"
            )

        console.print()

        # Prompt for the parent.
        try:
            raw = input("  Enter # or folder name for parent [Shared]: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Cancelled.[/dim]")
            return

        # Resolve selection to a folder name.
        parent_name = "Shared"  # sensible default
        if raw:
            if raw.isdigit():
                idx = int(raw) - 1
                if 0 <= idx < len(flat):
                    parent_name = flat[idx][1]
                else:
                    console.print(f"[red]Invalid number: {raw}  (valid range 1–{len(flat)})[/red]")
                    return
            else:
                # Accept a raw folder name too.
                known_names = {f[1] for f in flat}
                if raw in known_names:
                    parent_name = raw
                else:
                    console.print(
                        f"[red]Folder '{raw}' not found.[/red]\n"
                        "  Enter a number from the list or an exact folder name."
                    )
                    return

        # Confirm.
        console.print(
            f"\n  Create [bold cyan]{name}[/bold cyan] "
            f"inside [bold green]{parent_name}[/bold green]?"
        )
        try:
            confirm = input("  [y/n]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Cancelled.[/dim]")
            return

        if confirm not in ("y", "yes"):
            console.print("[dim]Cancelled.[/dim]")
            return

        # Create via API.
        try:
            result       = self._scm.create_folder(name, parent_name)
            created_id   = result.get("id", "")
            created_name = result.get("name") or name
            console.print(
                f"\n[green]✓[/green] Folder [bold cyan]{created_name}[/bold cyan] created "
                f"inside [bold green]{parent_name}[/bold green]"
                + (f"  [dim](id: {created_id})[/dim]" if created_id else "")
            )
        except Exception as exc:
            from app.shell.write_cmd import _explain_folder_error
            _explain_folder_error(name, exc)
            return

        # Refresh folder cache so the new folder appears in completions immediately.
        self._refresh_folders(silent=True)
        total = len(self._state.folders_cache)
        console.print(
            f"[dim]Folder list refreshed — {total} folder(s) total.  "
            f"Use [bold]folder {created_name}[/bold] to switch into it.[/dim]"
        )

    def _cmd_folder_snippet(self, snippet_name: str, *, attach: bool) -> None:
        """Attach or detach a snippet on the active folder (edits folder.snippets[]).

        Operates on the current folder context (``cd folder <name>`` first).
        SCM stores folder→snippet membership as the folder record's ``snippets``
        list, so this reads the folder record, adds/removes the snippet, and
        PUTs the updated record back.
        """
        verb = "attach" if attach else "detach"
        if not snippet_name:
            console.print(
                f"[yellow]Usage:[/yellow] folder {verb}-snippet <snippet>\n"
                "  [dim]Attaches to the active folder — use 'cd folder <name>' first.[/dim]"
            )
            return
        if not self._scm:
            console.print("[red]SCM is not configured.[/red]")
            return
        folder = self._state.folder
        if folder.lower() == "shared":
            console.print(
                "[yellow]Switch to a specific folder first[/yellow] — "
                "[bold]cd folder <name>[/bold]  [dim](cannot edit the Shared root's snippets).[/dim]"
            )
            return
        record = self._scm.get_folder_record(folder)
        if record is None:
            console.print(f"[red]Folder '{folder}' not found in SCM.[/red]")
            return
        # Validate the snippet exists (case-insensitive), using the canonical name.
        if not self._state.snippets_cache or self._cache_stale(self._state.snippets_loaded_at):
            self._refresh_snippets(silent=True)
        canonical = next(
            (n for n in self._state.snippets_cache if n.lower() == snippet_name.lower()),
            snippet_name,
        )
        current = list(record.get("snippets") or [])
        present = any(s.lower() == canonical.lower() for s in current)
        if attach and present:
            console.print(f"[dim]Snippet '{canonical}' is already attached to '{folder}'.[/dim]")
            return
        if not attach and not present:
            console.print(f"[dim]Snippet '{canonical}' is not attached to '{folder}'.[/dim]")
            return
        if attach:
            current.append(canonical)
        else:
            current = [s for s in current if s.lower() != canonical.lower()]

        payload = {k: v for k, v in record.items() if not str(k).startswith("@")}
        payload["snippets"] = current
        folder_id = record.get("id")
        if not folder_id:
            console.print(f"[red]Folder '{folder}' has no id — cannot update.[/red]")
            return
        try:
            self._scm.update_folder(folder_id, payload)
        except Exception as exc:  # noqa: BLE001
            console.print(f"[red]Failed to {verb} snippet: {exc}[/red]")
            return
        arrow = "attached to" if attach else "detached from"
        console.print(
            f"[green]✓[/green] Snippet [bold magenta]{canonical}[/bold magenta] "
            f"{arrow} folder [bold green]{folder}[/bold green]  "
            f"[dim](now: {', '.join(current) or 'none'})[/dim]"
        )

    def _reset_tenant_context(self, new_tsg: str) -> None:
        """Point shell state at *new_tsg* and rebuild the navigation caches.

        Device/folder context from the previous tenant is never valid in the
        new one, so everything cached is dropped and re-fetched.
        """
        self._state.tsg_id = new_tsg
        self._state.device = None
        self._state.attached = False
        self._state.folder = self._config.default_folder
        self._state.devices_cache = []
        self._state.folders_cache = ["Shared", "Global"]
        self._state.tsgs_cache = []
        self._refresh_devices(silent=True)
        self._refresh_folders(silent=True)
        self._refresh_tsgs(silent=True)

    def _cmd_tsg(self, args: list[str]) -> None:
        """Switch the active Tenant Services Group (TSG) context.

        ARC authenticates to the parent / root TSG at startup.  Use this
        command to switch into a child TSG so that all subsequent API calls
        (devices, policy, addresses…) are scoped to that tenant.

        ARC re-authenticates automatically via OAuth to obtain a token
        scoped to the new TSG — no manual token management needed.

        Usage:
          tsg                  — show current TSG and list available child TSGs
          tsg <id>             — switch to the given TSG ID
        """
        if not args:
            active = self._state.tsg_id or self._config.scm.tsg_id or "(not set)"
            console.print(f"[cyan]Active TSG:[/cyan] [bold]{active}[/bold]")

            # Show cached child TSGs if available
            if self._state.tsgs_cache:
                console.print("\n[bold yellow]Available TSGs[/bold yellow]  "
                              "[dim](Tab after 'tsg ' to complete)[/dim]")
                for entry in self._state.tsgs_cache:
                    tsg_id, name = tsg_display(entry)
                    marker = " [green]◀ active[/green]" if tsg_id == active else ""
                    console.print(f"  [cyan]{tsg_id:<20}[/cyan] {name}{marker}")
            else:
                console.print(
                    "[dim]No TSG list cached — ARC will attempt to fetch child TSGs.[/dim]"
                )
                self._refresh_tsgs(silent=False)
                if self._state.tsgs_cache:
                    console.print("\n[bold yellow]Available TSGs[/bold yellow]")
                    for entry in self._state.tsgs_cache:
                        tsg_id, name = tsg_display(entry)
                        console.print(f"  [cyan]{tsg_id:<20}[/cyan] {name}")
                else:
                    console.print(
                        "[yellow]No child TSGs found.[/yellow]  "
                        "Your service account may only have access to "
                        f"TSG [bold]{active}[/bold] itself.\n"
                        "Use [bold]tsg <id>[/bold] to switch if you know the child TSG ID."
                    )
            return

        new_tsg = args[0].strip()
        if not new_tsg:
            console.print("[yellow]TSG ID cannot be blank.[/yellow]")
            return

        previous_tsg    = self._state.tsg_id
        previous_device = self._state.device
        previous_folder = self._state.folder
        has_client_creds = bool(
            self._config.scm.client_id and self._config.scm.client_secret
        )

        if not has_client_creds:
            # Bearer-token-only mode: we cannot mint a new token scoped to a
            # different TSG. Keep a local context switch so operators can still
            # organize state, but make it explicit that API visibility may not
            # actually change until re-auth with client credentials.
            self._reset_tenant_context(new_tsg)
            console.print(
                f"[yellow]⚠[/yellow] Set active TSG to [bold]{new_tsg}[/bold] in bearer-token mode.\n"
                "  [dim]To fully re-scope API access, configure OAuth client credentials and restart ARC.[/dim]"
            )
            return

        # OAuth client credentials available — perform a real token re-scope.
        try:
            if not self._scm:
                self._scm = SCMClient(self._config.scm)
            self._scm.reauthenticate(new_tsg)

            self._reset_tenant_context(new_tsg)

            console.print(
                f"[green]✓[/green] Switched active TSG to [bold]{new_tsg}[/bold]  "
                f"[dim]{len(self._state.devices_cache)} device(s), {len(self._state.folders_cache)} folder(s)[/dim]"
            )
            if not self._state.devices_cache:
                console.print(
                    "[yellow]No devices visible in this TSG.[/yellow]  "
                    "[dim]Use [bold]tsg[/bold] to list alternatives or verify account permissions.[/dim]"
                )

        except Exception as exc:
            # Roll back fully on failure so context is consistent.
            self._state.tsg_id = previous_tsg
            self._state.device = previous_device
            self._state.folder = previous_folder
            if self._scm:
                try:
                    self._scm.reauthenticate(previous_tsg or self._config.scm.tsg_id)
                except Exception:
                    pass
            console.print(
                f"[red]TSG switch failed:[/red] {exc}\n"
                f"[dim]Context restored to TSG {previous_tsg or self._config.scm.tsg_id}.[/dim]"
            )

    def _cmd_account(self, args: list[str]) -> None:
        """List or switch named credential profiles.

        Profiles hold a separate set of SCM credentials (client_id, client_secret,
        tsg_id) stored under their own keychain entries.  A typical setup has a
        read-only profile for day-to-day monitoring and a read-write profile for
        making policy changes.

        Create profiles outside the shell with:
          arc auth configure --profile <name>

        Usage:
          account               — list all profiles with active marker
          account <name>        — switch to the named profile
        """
        profiles = list_profiles()

        if not args:
            # List all configured profiles.
            active_name = self._config.profile_name

            if len(profiles) == 1 and profiles[0]["name"] == "default":
                p = profiles[0]
                client_id = p["client_id"] or "(not set)"
                tsg_id    = p["tsg_id"]    or "(not set)"
                console.print(
                    f"\n[cyan]Active account:[/cyan] [bold]{active_name}[/bold]\n"
                    f"  client_id : {client_id}\n"
                    f"  tsg_id    : {tsg_id}\n\n"
                    "[dim]Create additional profiles with: "
                    "[bold]arc auth configure --profile <name>[/bold][/dim]"
                )
                return

            console.print(
                "\n[bold yellow]Credential Profiles[/bold yellow]  "
                "[dim](use [bold]account <name>[/bold] to switch)[/dim]\n"
            )
            for p in profiles:
                marker      = " [green]◀ active[/green]" if p["active"] else ""
                name_col    = f"[bold]{p['name']}[/bold]" if p["active"] else p["name"]
                client_id   = p["client_id"] or "[dim](not set)[/dim]"
                tsg_id      = p["tsg_id"]    or "[dim](not set)[/dim]"
                console.print(f"  {name_col:<22} {client_id:<55} {tsg_id}{marker}")
            return

        target       = args[0].strip()
        profile_names = [p["name"] for p in profiles]

        if target not in profile_names:
            console.print(
                f"[red]Profile '{target}' not found.[/red]\n"
                f"  Available: [bold]{', '.join(profile_names)}[/bold]\n"
                f"  Create it with: [bold]arc auth configure --profile {target}[/bold]"
            )
            return

        if target == self._config.profile_name:
            p = next(p for p in profiles if p["name"] == target)
            console.print(
                f"[cyan]Already using profile:[/cyan] [bold]{target}[/bold]  "
                f"[dim](TSG: {p['tsg_id'] or 'n/a'})[/dim]"
            )
            return

        console.print(f"[dim]Loading profile '{target}'…[/dim]")

        previous_config = self._config
        previous_scm    = self._scm

        try:
            new_cfg = load_config(profile=target)
            new_cfg.debug = self._config.debug  # preserve session debug flag

            if new_cfg.scm.is_configured:
                new_scm: Optional[SCMClient] = SCMClient(new_cfg.scm)
            else:
                new_scm = None

            # Swap config and client atomically.
            self._config = new_cfg
            self._scm    = new_scm

            # Clear all context — new account = different TSG + devices.
            self._state.device         = None
            self._state.folder         = new_cfg.default_folder
            self._state.tsg_id         = new_cfg.scm.tsg_id
            self._state.devices_cache  = []
            self._state.folders_cache  = ["Shared", "Global"]
            self._state.tsgs_cache     = []

            # Persist the new active profile to disk so the next launch uses it.
            set_active_profile(target)

            if new_scm:
                console.print(f"[dim]Refreshing caches for profile '{target}'…[/dim]")
                self._refresh_devices(silent=True)
                self._refresh_folders(silent=True)
                self._refresh_tsgs(silent=True)

                device_count = len(self._state.devices_cache)
                console.print(
                    f"[green]✓[/green] Switched to profile [bold]{target}[/bold]  "
                    f"[dim]|  TSG:[/dim] [cyan]{new_cfg.scm.tsg_id}[/cyan]  "
                    f"[dim]{device_count} device(s)[/dim]"
                )
                if device_count == 0:
                    console.print(
                        "[yellow]No devices visible.[/yellow]  "
                        "[dim]Check your service account has Device Administrator access, "
                        "or use [bold]tsg <id>[/bold] to switch to a TSG with devices.[/dim]"
                    )
            else:
                console.print(
                    f"[yellow]⚠[/yellow] Switched to profile [bold]{target}[/bold] "
                    f"but SCM is not configured for this profile.\n"
                    f"  Run [bold]arc auth configure --profile {target}[/bold] to add credentials."
                )

        except Exception as exc:
            # Roll back to the previous config on any failure.
            self._config = previous_config
            self._scm    = previous_scm
            console.print(
                f"[red]Failed to switch to profile '{target}':[/red] {exc}\n"
                f"[dim]Still using profile '{previous_config.profile_name}'.[/dim]"
            )
