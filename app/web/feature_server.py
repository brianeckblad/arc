"""On-demand browser GUI for managing ARC feature flags.

``feature gui`` starts a tiny local HTTP server (127.0.0.1 only), opens the
default browser at the editor page, and *blocks the shell* until the user
closes the editor — either by clicking **Done** in the browser (which POSTs
``/api/close``) or pressing Ctrl-C in the terminal.  On close the server shuts
down and control returns to the prompt.  Nothing persists after the command.

The editor lets the operator toggle each flag ON / DEV / OFF.  Saves go through
``app.settings.features.set_feature_state`` — the *same* helper the CLI
``feature enable`` uses — so the two never diverge on how/where a flag is
stored.  Changes are also applied to the live shell (``shell._features`` plus
the visible-keys cache) so ``?`` / completion reflect them immediately.

Grouping: flags are grouped for display by the owning command's ``category``
(a clean axis — no flag spans two categories), while persistence still targets
each flag's owning glossary file via ``feature_file_for``.
"""

from __future__ import annotations

import json
import logging
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

logger = logging.getLogger(__name__)

_HTML_FILE = Path(__file__).with_name("feature_gui.html")


class _QuietThreadingHTTPServer(ThreadingHTTPServer):
    """ThreadingHTTPServer that ignores client-disconnect errors.

    Browsers routinely cancel in-flight requests (fast navigation, refresh,
    duplicate fetches); the resulting BrokenPipe/ConnectionReset is harmless but
    the default handler prints a full traceback to stderr, spamming the shell.
    """

    daemon_threads = True

    def handle_error(self, request, client_address):  # noqa: D102
        import sys
        exc = sys.exc_info()[1]
        if isinstance(exc, (BrokenPipeError, ConnectionResetError, ConnectionError)):
            return  # client went away — nothing to report
        super().handle_error(request, client_address)


# ---------------------------------------------------------------------------
# Feature-editor themes.  These style the browser GUI only (never the terminal
# shell, which uses settings/theme.json).  The user's choice + per-token tweaks
# live in config/<user>/preferences.json under `feature_gui_theme`.
# ---------------------------------------------------------------------------

# The color CSS variables the GUI uses (layout tokens like --radius are fixed).
GUI_THEME_TOKENS = [
    "--bg", "--bg-sidebar", "--bg-card", "--bg-hover", "--bg-active", "--bg-code",
    "--border", "--text", "--text-2", "--text-3",
    "--brand", "--brand-hover", "--green", "--yellow", "--red", "--purple", "--teal",
    "--header-bg", "--overlay",
]

# Built-in palettes, macOS-Terminal inspired.  Each provides all color tokens so
# switching is clean.  "Default" mirrors the shipped dark theme.
_GUI_THEMES: dict[str, dict[str, str]] = {
    "Default": {
        "--bg": "#0B0E1A", "--bg-sidebar": "#111525", "--bg-card": "#171B2E",
        "--bg-hover": "#1E2340", "--bg-active": "rgba(0,112,209,.15)", "--bg-code": "#0D1020",
        "--border": "#1E2340", "--text": "#D8DCF0", "--text-2": "#8896B8", "--text-3": "#6B7A9C",
        "--brand": "#0070D1", "--brand-hover": "#3395E8", "--green": "#22C55E",
        "--yellow": "#F59E0B", "--red": "#EF4444", "--purple": "#A78BFA", "--teal": "#009CA6",
        "--header-bg": "rgba(11,14,26,.95)", "--overlay": "rgba(6,8,16,.7)",
    },
    "Dark": {
        "--bg": "#1E1E1E", "--bg-sidebar": "#252526", "--bg-card": "#2D2D2D",
        "--bg-hover": "#37373D", "--bg-active": "rgba(120,120,120,.2)", "--bg-code": "#181818",
        "--border": "#3C3C3C", "--text": "#E4E4E4", "--text-2": "#A0A0A0", "--text-3": "#6E6E6E",
        "--brand": "#4EA1FF", "--brand-hover": "#6FB4FF", "--green": "#4EC94E",
        "--yellow": "#E5C07B", "--red": "#E06C75", "--purple": "#C678DD", "--teal": "#56B6C2",
        "--header-bg": "rgba(30,30,30,.95)", "--overlay": "rgba(0,0,0,.7)",
    },
    "Light": {
        "--bg": "#FFFFFF", "--bg-sidebar": "#F3F3F3", "--bg-card": "#FAFAFA",
        "--bg-hover": "#ECECEC", "--bg-active": "rgba(0,112,209,.1)", "--bg-code": "#F0F0F0",
        "--border": "#D6D6D6", "--text": "#1A1A1A", "--text-2": "#555555", "--text-3": "#888888",
        "--brand": "#0066CC", "--brand-hover": "#0052A3", "--green": "#1A9E3F",
        "--yellow": "#B8860B", "--red": "#CC3333", "--purple": "#8A4FBE", "--teal": "#0A8A93",
        "--header-bg": "rgba(255,255,255,.95)", "--overlay": "rgba(20,24,40,.35)",
    },
    "Clear Dark": {
        "--bg": "#05070C", "--bg-sidebar": "#0A0D15", "--bg-card": "#0E1220",
        "--bg-hover": "#161C30", "--bg-active": "rgba(120,160,255,.14)", "--bg-code": "#070910",
        "--border": "#1A2033", "--text": "#E8ECF8", "--text-2": "#98A4C0", "--text-3": "#5C6885",
        "--brand": "#5B8DEF", "--brand-hover": "#7BA5F5", "--green": "#3DD68C",
        "--yellow": "#F2C55C", "--red": "#F26D6D", "--purple": "#B499F0", "--teal": "#3EC8D8",
        "--header-bg": "rgba(5,7,12,.9)", "--overlay": "rgba(0,0,0,.72)",
    },
    "Clear Light": {
        "--bg": "#FCFCFD", "--bg-sidebar": "#F5F6FA", "--bg-card": "#FFFFFF",
        "--bg-hover": "#EEF0F6", "--bg-active": "rgba(0,112,209,.09)", "--bg-code": "#F2F4F9",
        "--border": "#E1E4EE", "--text": "#232733", "--text-2": "#5B6478", "--text-3": "#98A0B2",
        "--brand": "#2B7DE0", "--brand-hover": "#1E63BE", "--green": "#1FA855",
        "--yellow": "#C08A18", "--red": "#D6493F", "--purple": "#8C57C7", "--teal": "#128A97",
        "--header-bg": "rgba(252,252,253,.92)", "--overlay": "rgba(20,24,40,.3)",
    },
    "Grass": {
        "--bg": "#13290A", "--bg-sidebar": "#183310", "--bg-card": "#1E3D15",
        "--bg-hover": "#274D1C", "--bg-active": "rgba(140,220,90,.18)", "--bg-code": "#0F2208",
        "--border": "#2C5220", "--text": "#E8F5D8", "--text-2": "#A7C48C", "--text-3": "#6E8A57",
        "--brand": "#8FD14F", "--brand-hover": "#A6E066", "--green": "#7FD858",
        "--yellow": "#E5D25C", "--red": "#E88A5A", "--purple": "#C8A0E0", "--teal": "#5FC79B",
        "--header-bg": "rgba(19,41,10,.94)", "--overlay": "rgba(5,15,3,.72)",
    },
    "Homebrew": {
        "--bg": "#000000", "--bg-sidebar": "#050805", "--bg-card": "#0A0F0A",
        "--bg-hover": "#12200F", "--bg-active": "rgba(40,220,40,.16)", "--bg-code": "#020402",
        "--border": "#1A3315", "--text": "#28C828", "--text-2": "#1F9E1F", "--text-3": "#166616",
        "--brand": "#33D633", "--brand-hover": "#5CE85C", "--green": "#28C828",
        "--yellow": "#C8C828", "--red": "#E05050", "--purple": "#28C8C8", "--teal": "#28C8A0",
        "--header-bg": "rgba(0,0,0,.95)", "--overlay": "rgba(0,0,0,.8)",
    },
    "Man Page": {
        "--bg": "#FEF9E7", "--bg-sidebar": "#F5EFD5", "--bg-card": "#FFFDF2",
        "--bg-hover": "#EDE6C8", "--bg-active": "rgba(0,90,160,.1)", "--bg-code": "#F0EAD0",
        "--border": "#D8CFA8", "--text": "#1A1A1A", "--text-2": "#5A5440", "--text-3": "#8A8468",
        "--brand": "#1560A8", "--brand-hover": "#0F4A85", "--green": "#2C8A2C",
        "--yellow": "#A8801A", "--red": "#B83232", "--purple": "#7A4FB0", "--teal": "#0F7A85",
        "--header-bg": "rgba(254,249,231,.94)", "--overlay": "rgba(40,36,20,.3)",
    },
    "Novel": {
        "--bg": "#DFDBC3", "--bg-sidebar": "#D5D0B5", "--bg-card": "#E7E3CD",
        "--bg-hover": "#CDC7A8", "--bg-active": "rgba(140,80,40,.14)", "--bg-code": "#D0CAAE",
        "--border": "#BDB593", "--text": "#3B2822", "--text-2": "#6B5548", "--text-3": "#94836F",
        "--brand": "#8A4B2E", "--brand-hover": "#6E3A22", "--green": "#5C7A2E",
        "--yellow": "#A07818", "--red": "#B04326", "--purple": "#7A4F6E", "--teal": "#3E7A6E",
        "--header-bg": "rgba(223,219,195,.94)", "--overlay": "rgba(59,40,34,.3)",
    },
    "Ocean": {
        "--bg": "#0A2A4A", "--bg-sidebar": "#0D3358", "--bg-card": "#124066",
        "--bg-hover": "#1A4E78", "--bg-active": "rgba(120,200,255,.18)", "--bg-code": "#082138",
        "--border": "#1E5688", "--text": "#DCEBFA", "--text-2": "#94B4D4", "--text-3": "#5E82A6",
        "--brand": "#4FB0F0", "--brand-hover": "#6FC2F5", "--green": "#4FD0A8",
        "--yellow": "#F0CE6C", "--red": "#F07A7A", "--purple": "#A0A8F0", "--teal": "#4FC8D8",
        "--header-bg": "rgba(10,42,74,.94)", "--overlay": "rgba(4,20,38,.72)",
    },
    "Pro": {
        "--bg": "#000000", "--bg-sidebar": "#0A0A0A", "--bg-card": "#141414",
        "--bg-hover": "#1F1F1F", "--bg-active": "rgba(255,255,255,.12)", "--bg-code": "#050505",
        "--border": "#2A2A2A", "--text": "#F2F2F2", "--text-2": "#A8A8A8", "--text-3": "#6A6A6A",
        "--brand": "#4A9EFF", "--brand-hover": "#6BB1FF", "--green": "#4CD964",
        "--yellow": "#FFCC00", "--red": "#FF453A", "--purple": "#BF5AF2", "--teal": "#5AC8D8",
        "--header-bg": "rgba(0,0,0,.95)", "--overlay": "rgba(0,0,0,.75)",
    },
}


def build_theme(shell) -> dict:
    """Return the built-in palettes + the user's active selection."""
    prefs = getattr(shell, "_prefs", None)
    active = getattr(prefs, "feature_gui_theme", None) or {}
    base = active.get("base") if isinstance(active, dict) else None
    overrides = active.get("overrides") if isinstance(active, dict) else {}
    if base not in _GUI_THEMES:
        base = "Default"
    if not isinstance(overrides, dict):
        overrides = {}
    return {
        "tokens": GUI_THEME_TOKENS,
        "themes": [{"name": name, "colors": colors} for name, colors in _GUI_THEMES.items()],
        "active": {"base": base, "overrides": overrides},
    }


def _valid_color(val: str) -> bool:
    """Accept hex (#rgb/#rrggbb/#rrggbbaa) or rgb()/rgba() strings."""
    import re
    v = str(val).strip()
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}", v):
        return True
    if re.fullmatch(r"rgba?\([0-9.,\s]+\)", v):
        return True
    return False

# Max commands listed per flag in the API payload — some flags (e.g. panos-ops
# families) gate thousands of commands; showing them all bloats the response.
_MAX_CMDS_PER_FLAG = 25


def _flag_to_commands() -> dict[str, list[str]]:
    """Build flag_name -> sorted list of command keys it gates."""
    from app.commands.registry import COMMANDS

    result: dict[str, list[str]] = {}
    for cmd_key, cmd_def in COMMANDS.items():
        if cmd_def.feature_flag:
            result.setdefault(cmd_def.feature_flag, []).append(cmd_key)
    for flag in result:
        result[flag].sort()
    return result


def _flag_category() -> dict[str, str]:
    """Map each flag to a display category (from the gated command's category)."""
    from app.commands.registry import COMMANDS

    cat: dict[str, str] = {}
    for cmd_def in COMMANDS.values():
        flag = cmd_def.feature_flag
        if flag and flag not in cat:
            cat[flag] = cmd_def.category or "explicit"
    return cat


def _flag_universe(shell) -> set[str]:
    """All known flag names (registry + settings), minus internal sentinels."""
    return {k for k in shell._features if not k.startswith("_")} | set(_flag_to_commands())


def _state_of(shell, flag: str) -> str:
    from app.settings.features import feature_state
    st = feature_state(shell._features, flag)
    return st if st in ("on", "dev", "off", "hidden") else "off"


# ---------------------------------------------------------------------------
# Section payload builders — one per GUI section.  All naming comes from the
# shared app.settings.feature_labels layer so the CLI and GUI agree.
# ---------------------------------------------------------------------------

def build_areas(shell) -> dict:
    """Dedicated Areas section: every area with a real enabled/disabled switch."""
    from app.settings.feature_labels import area_label, load_labels

    labels = load_labels()
    flag_cat = _flag_category()
    disabled_areas = set(getattr(shell, "_disabled_areas", set()))

    areas: dict[str, dict] = {}
    for flag in _flag_universe(shell):
        cat = flag_cat.get(flag, "explicit")
        st = _state_of(shell, flag)
        a = areas.setdefault(cat, {
            "area": cat,
            "label": area_label(cat, labels),
            "counts": {"on": 0, "dev": 0, "off": 0, "hidden": 0},
            "feature_count": 0,
            "disabled": cat in disabled_areas,
        })
        a["counts"][st] += 1
        a["feature_count"] += 1

    ordered = sorted(areas.values(), key=lambda a: a["label"].lower())
    return {"areas": ordered}


def build_features(shell, area: str | None = None) -> dict:
    """Features for one area (excludes disabled areas).

    Each feature carries a human title/subtitle plus per-command effective scope.
    """
    from app.commands.registry import COMMANDS
    from app.settings.feature_labels import area_label, flag_label, load_labels
    from app.settings.features import feature_file_for

    labels = load_labels()
    flag_cmds = _flag_to_commands()
    flag_cat = _flag_category()
    disabled_areas = set(getattr(shell, "_disabled_areas", set()))

    groups: dict[str, dict] = {}
    totals = {"on": 0, "dev": 0, "off": 0, "hidden": 0, "flags": 0}

    for flag in sorted(_flag_universe(shell)):
        cat = flag_cat.get(flag, "explicit")
        if area is not None and cat != area:
            continue
        if cat in disabled_areas:
            continue  # a disabled area is off — never shown in the editor

        st = _state_of(shell, flag)
        cmd_keys = flag_cmds.get(flag, [])
        label = flag_label(flag, flag_cmds, commands=COMMANDS, labels=labels)
        try:
            owning = feature_file_for(flag).name
        except Exception:
            owning = "local.json"

        cmd_entries = []
        for cmd_key in cmd_keys[:_MAX_CMDS_PER_FLAG]:
            cmd_def = COMMANDS.get(cmd_key)
            if cmd_def is None:
                continue
            eff = shell.resolve_scope(cmd_key, cmd_def)
            cmd_entries.append({
                "command": cmd_key,
                "code_scope": cmd_def.scope,
                "effective_scope": eff,
                "overridden": eff != cmd_def.scope,
                "ssh": cmd_def.ssh_command is not None,
                "description": cmd_def.description or "",
            })

        grp = groups.setdefault(cat, {
            "area": cat,
            "label": area_label(cat, labels),
            "counts": {"on": 0, "dev": 0, "off": 0, "hidden": 0},
            "flags": [],
        })
        grp["counts"][st] += 1
        grp["flags"].append({
            "flag": flag,
            "title": label["title"],
            "subtitle": label["subtitle"],
            "action": label["action"],
            "state": st,
            "file": owning,
            "command_count": len(cmd_keys),
            "commands": cmd_entries,
        })
        totals[st] += 1
        totals["flags"] += 1

    ordered = sorted(groups.values(), key=lambda g: g["label"].lower())
    return {"groups": ordered, "totals": totals, "area": area}


def build_domains(shell) -> dict:
    """Advanced / Files view: per-file _default and _carry with human names.

    Files that belong entirely to disabled areas are omitted (they're off).
    """
    from app.settings.features import load_file_meta

    disabled_areas = set(getattr(shell, "_disabled_areas", set()))
    file_cats = _file_categories(shell)
    domains = []
    for stem, m in sorted(load_file_meta().items()):
        if stem == "local":
            continue
        cats = file_cats.get(stem, set())
        if cats and cats <= disabled_areas:
            continue
        domains.append({
            "stem": stem,
            "label": _domain_label(stem),
            "default": m["default"],
            "carry": m["carry"],
            "readme": m["readme"],
        })
    return {"domains": domains}


def build_aliases(shell) -> dict:
    """System + personal aliases for the Aliases section."""
    from app.settings.aliases import load_system_aliases

    system = [{"name": k, "expansion": v} for k, v in sorted(load_system_aliases().items())]
    user_map = getattr(getattr(shell, "_prefs", None), "aliases", {}) or {}
    user = [{"name": k, "expansion": v} for k, v in sorted(user_map.items())]
    return {"system": system, "user": user}


def build_structure_list(shell) -> dict:
    """List of set/update/delete commands that can carry a structure, by area."""
    from app.commands.registry import COMMANDS
    from app.settings.command_structure import load_command_structure
    from app.settings.feature_labels import area_label, load_labels

    labels = load_labels()
    struct = load_command_structure()
    groups: dict[str, list] = {}
    for key, cmd_def in COMMANDS.items():
        if key.split()[0] not in ("set", "update", "delete"):
            continue
        entry = struct.get(key)
        groups.setdefault(cmd_def.category or "explicit", []).append({
            "command": key,
            "description": cmd_def.description or "",
            "has_structure": entry is not None,
            "override": bool(entry.get("override")) if entry else False,
            "field_count": len(entry.get("args", [])) if entry else 0,
        })
    out = []
    for cat in sorted(groups, key=lambda c: area_label(c, labels).lower()):
        cmds = sorted(groups[cat], key=lambda c: c["command"])
        out.append({"area": cat, "label": area_label(cat, labels), "commands": cmds})
    return {"areas": out}


def build_structure(shell, command: str) -> dict:
    """Editable field spec for one command."""
    from app.commands.registry import COMMANDS
    from app.settings.command_structure import arg_spec, load_command_structure

    if command not in COMMANDS:
        return {"error": f"unknown command: {command!r}"}
    entry = load_command_structure().get(command)
    args = arg_spec(command) or []
    return {
        "command": command,
        "description": COMMANDS[command].description or "",
        "override": bool(entry.get("override")) if entry else False,
        "has_structure": entry is not None,
        "fields": [
            {
                "name": a.get("name", ""),
                "kind": a.get("kind", "value"),
                "required": bool(a.get("required", False)),
                "hint": a.get("hint", ""),
                "choices": a.get("choices", []),
            }
            for a in args
        ],
    }


def _domain_label(stem: str) -> str:
    """Human name for a feature-file stem — delegates to the shared naming layer."""
    from app.settings.feature_labels import file_label
    return file_label(stem)


# Functional grouping for shell builtins (settings/builtin-commands.json has no
# category).  Keys are builtin command keys; value is the sidebar group.  Any
# builtin not listed falls back to "Tools".
_BUILTIN_GROUPS = {
    "Navigation": ["cd", "folder", "tsg", "connect", "close connection",
                   "show connections", "pwd", "clear"],
    "Configure & Write": ["configure", "set", "update", "delete", "commit",
                          "abandon", "unstage", "show config"],
    "Info & Help": ["?", "help", "docs", "find", "status", "watch", "history"],
    "Session & Profile": ["account", "setup", "terminal", "alias", "exit", "quit"],
    "Tools": ["feature", "cli", "arc", "catalog", "command-structure"],
}


def _builtin_group_of(name: str) -> str:
    for group, members in _BUILTIN_GROUPS.items():
        if name in members:
            return group
    return "Tools"


# ---------------------------------------------------------------------------
# Unified navigation + section builders.  Every section answers two questions
# the same way: build_nav() -> left-sidebar groups; a per-section builder ->
# the items for the selected group.
# ---------------------------------------------------------------------------

# Cached flag->file / file->categories maps.  The registry and catalog are
# static at runtime, so this is computed once per process.
_FILE_CATEGORIES_CACHE: dict[str, set] | None = None


def _file_categories(shell) -> dict[str, set]:
    """Map each settings/features file stem -> set of command categories it gates.

    Uses the resource catalog (spec -> ``scm-<spec>`` file, plus category) so the
    mapping is structural and covers flags that are OFF (and therefore absent
    from their domain file).  Also folds in the live registry for non-catalog
    (explicit / PAN-OS) flags via their owning file.

    Cached: the previous version called ``feature_file_for`` per command (~4855
    times), each re-reading all 34 feature files from disk (~5s).  Now the
    flag->file map is read ONCE via ``load_features_with_sources`` and the whole
    result is memoized.
    """
    global _FILE_CATEGORIES_CACHE
    if _FILE_CATEGORIES_CACHE is not None:
        return _FILE_CATEGORIES_CACHE

    result: dict[str, set] = {}
    try:
        from app.commands.resource_catalog import CATALOG
        for entry in CATALOG:
            spec = entry.get("spec")
            cat = entry.get("category") or "explicit"
            if spec:
                result.setdefault(f"scm-{spec}", set()).add(cat)
    except Exception:
        pass
    try:
        from app.commands.registry import COMMANDS
        from app.settings.features import load_features_with_sources
        # Single disk read: flag -> owning file path.
        _flags, sources = load_features_with_sources()
        for cmd_def in COMMANDS.values():
            flag = cmd_def.feature_flag
            if not flag:
                continue
            src = sources.get(flag)
            stem = src.stem if src is not None else "local"
            if stem != "local":
                result.setdefault(stem, set()).add(cmd_def.category or "explicit")
    except Exception:
        pass
    _FILE_CATEGORIES_CACHE = result
    return result


def build_nav(shell, section: str) -> dict:
    """Return the left-sidebar groups for a section: {groups:[{key,label,count,meta}]}.

    Features and Command Structure exclude DISABLED areas; Advanced excludes files
    whose categories are all disabled.  Disabled areas are managed in the Areas
    section only.
    """
    from app.settings.feature_labels import area_label, load_labels
    labels = load_labels()
    disabled_areas = set(getattr(shell, "_disabled_areas", set()))

    if section in ("features", "structure"):
        flag_cat = _flag_category()
        if section == "features":
            counts: dict[str, int] = {}
            active: dict[str, int] = {}
            for flag in _flag_universe(shell):
                cat = flag_cat.get(flag, "explicit")
                if cat in disabled_areas:
                    continue
                counts[cat] = counts.get(cat, 0) + 1
                if _state_of(shell, flag) in ("on", "dev"):
                    active[cat] = active.get(cat, 0) + 1
            groups = [{
                "key": cat, "label": area_label(cat, labels), "count": counts[cat],
                "meta": {"active": active.get(cat, 0)},
            } for cat in counts]
        else:  # structure — only areas with editable commands (enabled)
            from app.commands.registry import COMMANDS
            counts = {}
            for key, cmd_def in COMMANDS.items():
                if key.split()[0] in ("set", "update", "delete"):
                    cat = cmd_def.category or "explicit"
                    if cat in disabled_areas:
                        continue
                    counts[cat] = counts.get(cat, 0) + 1
            groups = [{"key": cat, "label": area_label(cat, labels), "count": counts[cat], "meta": {}}
                      for cat in counts]
        groups.sort(key=lambda g: g["label"].lower())
        return {"section": section, "groups": groups}

    if section == "aliases":
        from app.settings.aliases import load_system_aliases
        user_map = getattr(getattr(shell, "_prefs", None), "aliases", {}) or {}
        return {"section": section, "groups": [
            {"key": "system", "label": "System (shared)", "count": len(load_system_aliases()), "meta": {}},
            {"key": "user", "label": "My aliases", "count": len(user_map), "meta": {}},
        ]}

    if section == "builtins":
        from app.settings.commands import load_builtins_full
        full = load_builtins_full()
        counts = {}
        for name in full:
            counts.setdefault(_builtin_group_of(name), 0)
            counts[_builtin_group_of(name)] += 1
        order = list(_BUILTIN_GROUPS.keys())
        groups = [{"key": g, "label": g, "count": counts.get(g, 0), "meta": {}}
                  for g in order if counts.get(g, 0)]
        return {"section": section, "groups": groups}

    if section == "advanced":
        from app.settings.features import load_file_meta
        file_cats = _file_categories(shell)
        groups = []
        for stem in sorted(load_file_meta()):
            if stem == "local":
                continue
            cats = file_cats.get(stem, set())
            # Hide a file only when it has categories and ALL are disabled.
            if cats and cats <= disabled_areas:
                continue
            groups.append({"key": stem, "label": _domain_label(stem), "count": 0, "meta": {}})
        groups.sort(key=lambda g: g["label"].lower())
        return {"section": section, "groups": groups}

    return {"section": section, "groups": []}


def build_features_header(shell, area: str) -> dict:
    """Area-level controls shown atop the Features main pane."""
    from app.settings.feature_labels import area_label, load_labels
    labels = load_labels()
    flag_cat = _flag_category()
    counts = {"on": 0, "dev": 0, "off": 0, "hidden": 0}
    for flag in _flag_universe(shell):
        if flag_cat.get(flag, "explicit") == area:
            counts[_state_of(shell, flag)] += 1
    return {
        "area": area,
        "label": area_label(area, labels),
        "counts": counts,
        "disabled": area in set(getattr(shell, "_disabled_areas", set())),
    }


def build_structure_area(shell, area: str) -> dict:
    """All editable set/update/delete commands in an area (Command Structure)."""
    from app.commands.registry import COMMANDS
    from app.settings.command_structure import load_command_structure
    from app.settings.feature_labels import area_label, load_labels
    labels = load_labels()
    struct = load_command_structure()
    cmds = []
    for key, cmd_def in COMMANDS.items():
        if key.split()[0] not in ("set", "update", "delete"):
            continue
        if (cmd_def.category or "explicit") != area:
            continue
        entry = struct.get(key)
        cmds.append({
            "command": key,
            "description": cmd_def.description or "",
            "has_structure": entry is not None,
            "override": bool(entry.get("override")) if entry else False,
            "field_count": len(entry.get("args", [])) if entry else 0,
        })
    cmds.sort(key=lambda c: c["command"])
    return {"area": area, "label": area_label(area, labels), "commands": cmds}


def build_builtins(shell, group: str) -> dict:
    """Builtins in a functional group, for the Built-ins editor."""
    from app.settings.commands import load_builtins_full
    full = load_builtins_full()
    items = []
    for name, meta in sorted(full.items()):
        if _builtin_group_of(name) != group:
            continue
        items.append({"name": name, **meta})
    return {"group": group, "items": items}



# Static help blurbs for the non-command sections (shown by the ? icons).
_SECTION_HELP = {
    "areas": (
        "<h3>Feature Areas</h3><p>Each <strong>area</strong> is a major capability "
        "(Advanced DNS Security, Cloud NGFW, …). Toggle an area "
        "<strong>Enabled/Disabled</strong>. <strong>Disabling</strong> an area is a "
        "real off switch: every command in it is hidden from <code>?</code>, "
        "blocked from running, and removed from the Features, Command Structure, "
        "and Advanced sections. Your individual feature settings are remembered "
        "and restored when you re-enable the area.</p>"
    ),
    "features": (
        "<h3>Features</h3><p>A <strong>feature</strong> turns one or more "
        "commands on or off. States: <code>ON</code> (everyone), "
        "<code>DEV</code> (only in development mode), <code>OFF</code> (hidden "
        "and blocked), <code>HIDDEN</code> (works but not shown in normal "
        "help). Expand a feature to choose <strong>where each command runs</strong> "
        "— Global, Folder, or Device.</p>"
    ),
    "structure": (
        "<h3>Command Structure</h3><p>Controls how a <code>set</code>/"
        "<code>update</code>/<code>delete</code> command parses its arguments "
        "and offers tab-completion. Reorder fields and edit each field's type "
        "(value / choice / keyword), whether it is required, its hint, and its "
        "choices. Saving locks the entry so regeneration won't overwrite it.</p>"
    ),
    "aliases": (
        "<h3>Aliases</h3><p>Shortcuts you type instead of a full command. "
        "<strong>System</strong> aliases are shared by everyone "
        "(<code>settings/command-aliases.json</code>); <strong>My aliases</strong> "
        "are personal to you. An alias cannot shadow a built-in or a real "
        "command word.</p>"
    ),
    "files": (
        "<h3>Advanced · Files</h3><p>These are <strong>regeneration settings, "
        "not on/off switches</strong>. To turn features on or off use "
        "<strong>Features</strong>; to disable a whole area use "
        "<strong>Areas</strong>. Each card is a <code>settings/features/</code> "
        "file. <strong>Default state</strong> applies to commands not explicitly "
        "listed in that file. <strong>Keep my edits</strong> stops the "
        "regenerator from overwriting your on/dev values when the API specs are "
        "refreshed. Most users never need these.</p>"
    ),
    "builtins": (
        "<h3>Built-in Commands</h3><p>The shell's own commands (cd, configure, "
        "commit, feature, …). Set each one's <strong>visibility</strong>: "
        "<code>Shown</code> (everyone), <code>Dev</code> (development mode only), "
        "<code>Hidden</code> (works but not listed in <code>?</code>), or "
        "<code>Disabled</code> (blocked). You can also edit the display name, "
        "help text, and whether it only appears in configure mode. Changes save "
        "to <code>settings/builtin-commands.json</code> and apply live.</p>"
    ),
    "settings": (
        "<h3>Settings · Theme</h3><p>Personalize the editor's colors. Pick a base "
        "theme (macOS-Terminal inspired) then tweak individual colors — changes "
        "preview live. <strong>Save</strong> writes to your "
        "<code>config/&lt;user&gt;/preferences.json</code> and styles this "
        "browser editor only (never the ARC terminal, which uses "
        "<code>settings/theme.json</code>).</p>"
    ),
}


def _command_help_html(key: str) -> str:
    """Render synthesized command help to a small HTML fragment for the modal."""
    from app.docs import synthesize_command_help

    md = synthesize_command_help(key)
    import html as _html
    import re

    out: list[str] = []
    for line in md.splitlines():
        raw = line.rstrip()
        if not raw:
            continue
        esc = _html.escape(raw)
        esc = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc)
        esc = re.sub(r"`(.+?)`", r"<code>\1</code>", esc)
        if raw.startswith("# "):
            out.append(f"<h3>{esc[2:]}</h3>")
        elif raw.startswith("- "):
            out.append(f"<li>{esc[2:]}</li>")
        elif raw.startswith("    "):
            out.append(f"<pre>{_html.escape(raw.strip())}</pre>")
        else:
            out.append(f"<p>{esc}</p>")
    return "\n".join(out)


def _flag_help_html(shell, flag: str) -> str:
    """Human help for a feature flag: title + what it does + gated commands."""
    from app.commands.registry import COMMANDS
    from app.settings.feature_labels import flag_label

    flag_cmds = _flag_to_commands()
    gated = flag_cmds.get(flag, [])
    label = flag_label(flag, flag_cmds, commands=COMMANDS)
    parts = [f"<h3>{label['title']}</h3>"]
    if label["subtitle"]:
        parts.append(f"<p>{label['subtitle']}</p>")
    parts.append(f"<p><code>{flag}</code></p>")
    if gated:
        parts.append(f"<p>Controls {len(gated)} command(s):</p>")
        for cmd_key in gated[:_MAX_CMDS_PER_FLAG]:
            parts.append("<hr/>" + _command_help_html(cmd_key))
    return "\n".join(parts)


class FeatureGuiServer:
    """A blocking, on-demand HTTP server for the feature-flag editor.

    Lifetime is scoped to a single ``serve()`` call: it binds, opens the
    browser, blocks until the editor signals close (or Ctrl-C), then shuts
    down.  A lock serializes state mutations so concurrent browser requests
    can't corrupt the shared shell state.
    """

    def __init__(self, shell, port: int = 4445, host: str = "127.0.0.1") -> None:
        self._shell = shell
        self._port = port
        self._host = host
        self._lock = threading.Lock()
        self._closed = threading.Event()
        self._httpd: ThreadingHTTPServer | None = None
        self._html = self._load_html()

    # -- helpers -----------------------------------------------------------

    @staticmethod
    def _load_html() -> bytes:
        try:
            return _HTML_FILE.read_bytes()
        except OSError as exc:  # pragma: no cover - packaging safety net
            logger.error("feature GUI HTML missing: %s", exc)
            return (
                b"<!doctype html><meta charset=utf-8>"
                b"<h1>feature_gui.html not found</h1>"
            )

    def _apply_change(self, flag: str, state: str) -> dict:
        """Persist a flag change and update live shell state (thread-safe)."""
        from app.settings.features import set_feature_state

        if state not in ("on", "dev", "off", "hidden"):
            raise ValueError(f"invalid state: {state!r}")
        with self._lock:
            target = set_feature_state(flag, state)
            self._shell._features[flag] = state
            self._shell._invalidate_visible_keys()
        return {"flag": flag, "state": state, "file": target.name}

    def _apply_area(self, area: str, disabled: bool) -> dict:
        """Enable/disable a whole area (real OFF gate); update live shell (thread-safe)."""
        from app.settings.features import load_disabled_areas, set_area_disabled

        with self._lock:
            set_area_disabled(area, disabled)
            self._shell._disabled_areas = load_disabled_areas()
            if hasattr(self._shell, "_invalidate_visible_keys"):
                self._shell._invalidate_visible_keys()
        return {"area": area, "disabled": area in self._shell._disabled_areas}

    def _apply_alias(self, scope: str, name: str, expansion: str | None) -> dict:
        """Create/update/delete a system or personal alias (thread-safe)."""
        from app.settings.aliases import (alias_conflict, load_system_aliases,
                                          set_system_alias)

        name = (name or "").strip()
        if not name:
            raise ValueError("alias name is required")
        if scope not in ("system", "user"):
            raise ValueError(f"invalid alias scope: {scope!r}")

        # Validate against builtins + command words (unless deleting).
        if expansion is not None and expansion.strip():
            builtins = None
            try:
                from app.shell import _SHELL_BUILTINS
                builtins = set(_SHELL_BUILTINS)
            except Exception:
                builtins = None
            reason = alias_conflict(name, builtins=builtins)
            if reason:
                raise ValueError(reason)

        with self._lock:
            if scope == "system":
                set_system_alias(name, expansion if expansion else None)
                self._shell._builtin_aliases = load_system_aliases()
            else:
                prefs = getattr(self._shell, "_prefs", None)
                if prefs is None:
                    raise RuntimeError("personal aliases unavailable (no prefs)")
                if expansion and expansion.strip():
                    prefs.aliases[name.lower()] = expansion.strip()
                else:
                    prefs.aliases.pop(name.lower(), None)
                from app.settings.user_prefs import save_prefs
                save_prefs(prefs)
        return {"scope": scope, "name": name.lower(),
                "expansion": (expansion or "").strip() or None}

    def _apply_structure(self, command: str, fields: list) -> dict:
        """Persist an override structure entry for a command (thread-safe)."""
        from app.commands.registry import COMMANDS
        from app.settings.command_structure import set_command_structure

        if command not in COMMANDS:
            raise ValueError(f"unknown command: {command!r}")
        with self._lock:
            set_command_structure(command, fields or [])
        return build_structure(self._shell, command)

    def _apply_builtin(self, name: str, field: str, value: object) -> dict:
        """Edit a builtin field; refresh live shell visibility (thread-safe)."""
        from app.settings.commands import (load_builtins_full,
                                           load_command_visibility, set_builtin_field)

        with self._lock:
            set_builtin_field(name, field, value)
            # Refresh live visibility so ?/dispatch/completion reflect it now.
            if hasattr(self._shell, "_command_visibility"):
                self._shell._command_visibility = load_command_visibility()
            if hasattr(self._shell, "_invalidate_visible_keys"):
                self._shell._invalidate_visible_keys()
            meta = load_builtins_full().get(name, {})
        return {"name": name, **meta}

    def _apply_theme(self, base: str, overrides: dict) -> dict:
        """Persist the feature-GUI theme to the user's preferences (thread-safe)."""
        from app.settings.user_prefs import save_prefs

        if base not in _GUI_THEMES:
            raise ValueError(f"unknown theme: {base!r}")
        clean: dict[str, str] = {}
        for token, val in (overrides or {}).items():
            if token in GUI_THEME_TOKENS and _valid_color(val):
                clean[token] = str(val).strip()
        prefs = getattr(self._shell, "_prefs", None)
        if prefs is None:
            raise RuntimeError("preferences unavailable (no prefs)")
        with self._lock:
            prefs.feature_gui_theme = {"base": base, "overrides": clean}
            save_prefs(prefs)
        return {"base": base, "overrides": clean}

    def _apply_scope(self, command: str, scope: str | None) -> dict:
        """Set/clear a per-command scope override; update live shell (thread-safe)."""
        from app.commands.registry import COMMANDS
        from app.settings.features import (coerce_scope, load_scope_overrides,
                                           set_scope_override)

        if command not in COMMANDS:
            raise ValueError(f"unknown command: {command!r}")
        norm = None
        if scope not in (None, "", "reset", "default"):
            norm = coerce_scope(scope)
            if norm is None:
                raise ValueError(f"invalid scope: {scope!r}")
        with self._lock:
            target = set_scope_override(command, norm)
            self._shell._scope_overrides = load_scope_overrides()
            self._shell._invalidate_visible_keys()
        code_scope = COMMANDS[command].scope
        eff = norm or code_scope
        return {
            "command": command, "effective_scope": eff, "code_scope": code_scope,
            "overridden": eff != code_scope, "file": target.name,
        }

    def _apply_meta(self, domain: str, default: str | None, carry: bool | None) -> dict:
        """Set a domain file's _default / _carry (thread-safe)."""
        from app.settings.features import load_file_meta, set_file_meta

        if domain not in load_file_meta():
            raise ValueError(f"unknown domain: {domain!r}")
        with self._lock:
            set_file_meta(domain, default=default, carry=carry)
            m = load_file_meta()[domain]
        return {"domain": domain, "default": m["default"], "carry": m["carry"]}

    def _payload(self) -> dict:
        """Legacy combined payload (kept for back-compat)."""
        with self._lock:
            return build_features(self._shell)

    def _section(self, name: str, query: dict) -> dict:
        """Build a section payload under the lock."""
        with self._lock:
            if name == "nav":
                return build_nav(self._shell, (query.get("section") or [""])[0])
            if name == "areas":
                return build_areas(self._shell)
            if name == "features":
                area = (query.get("area") or [None])[0]
                data = build_features(self._shell, area)
                if area:
                    data["header"] = build_features_header(self._shell, area)
                return data
            if name == "features-header":
                return build_features_header(self._shell, (query.get("area") or [""])[0])
            if name in ("domains", "files"):
                return build_domains(self._shell)
            if name == "aliases":
                return build_aliases(self._shell)
            if name == "builtins":
                return build_builtins(self._shell, (query.get("group") or [""])[0])
            if name == "structure-list":
                return build_structure_list(self._shell)
            if name == "structure-area":
                return build_structure_area(self._shell, (query.get("area") or [""])[0])
            if name == "structure":
                command = (query.get("command") or [""])[0]
                return build_structure(self._shell, command)
            if name == "theme":
                return build_theme(self._shell)
        return {"error": f"unknown section: {name}"}

    def _help(self, query: dict) -> dict:
        """Return help HTML for a command, flag, or static section topic."""
        from app.commands.registry import COMMANDS

        command = (query.get("command") or [""])[0]
        flag = (query.get("flag") or [""])[0]
        topic = (query.get("topic") or [""])[0]

        if command and command in COMMANDS:
            return {"kind": "command", "html": _command_help_html(command)}
        if flag:
            return {"kind": "flag", "html": _flag_help_html(self._shell, flag)}
        if topic in _SECTION_HELP:
            return {"kind": "topic", "html": _SECTION_HELP[topic]}
        return {"error": "no help for that target"}


    # -- lifecycle ---------------------------------------------------------

    def serve(self) -> str:
        """Start the server, open the browser, and BLOCK until the editor
        closes.  Returns a short status string for the caller to print.

        On a bind failure (port already in use) returns immediately without
        blocking so the shell stays responsive.
        """
        server = self  # captured by the handler

        class _Handler(BaseHTTPRequestHandler):
            # Silence the default stderr request logging.
            def log_message(self, *_args) -> None:  # noqa: N802
                pass

            def _send(self, code: int, body: bytes, ctype: str) -> None:
                # The browser may cancel a request mid-flight (fast navigation,
                # refresh, duplicate fetch) — that surfaces as BrokenPipe/
                # ConnectionReset while writing. It's harmless; swallow it so it
                # doesn't spam the shell with tracebacks.
                try:
                    self.send_response(code)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(body)
                except (BrokenPipeError, ConnectionResetError, ConnectionError):
                    pass

            def _send_json(self, obj: dict, code: int = 200) -> None:
                self._send(code, json.dumps(obj).encode("utf-8"), "application/json")

            def do_GET(self) -> None:  # noqa: N802
                from urllib.parse import parse_qs, urlparse

                parsed = urlparse(self.path)
                path = parsed.path
                qs = parse_qs(parsed.query)
                if path in ("/", "/index.html"):
                    self._send(200, server._html, "text/html; charset=utf-8")
                    return
                if path == "/api/help":
                    try:
                        self._send_json(server._help(qs))
                    except Exception as exc:  # pragma: no cover
                        self._send_json({"error": str(exc)}, 500)
                    return
                # Section data endpoints.
                _sections = {
                    "/api/nav": "nav",
                    "/api/areas": "areas",
                    "/api/features": "features",
                    "/api/features/header": "features-header",
                    "/api/domains": "domains",
                    "/api/files": "files",
                    "/api/aliases": "aliases",
                    "/api/builtins": "builtins",
                    "/api/structure/list": "structure-list",
                    "/api/structure/area": "structure-area",
                    "/api/structure/item": "structure",
                    "/api/structure": "structure",
                    "/api/theme": "theme",
                }
                if path in _sections:
                    try:
                        self._send_json(server._section(_sections[path], qs))
                    except Exception as exc:  # pragma: no cover
                        self._send_json({"error": str(exc)}, 500)
                    return
                self._send(404, b"not found", "text/plain")

            def do_POST(self) -> None:  # noqa: N802
                path = self.path.split("?", 1)[0]
                if path == "/api/close":
                    self._send_json({"ok": True, "closing": True})
                    server._closed.set()
                    return

                mutation_paths = (
                    "/api/feature", "/api/scope", "/api/meta",
                    "/api/area", "/api/alias", "/api/structure", "/api/builtin",
                    "/api/theme",
                )
                if path in mutation_paths:
                    try:
                        length = int(self.headers.get("Content-Length", 0))
                        raw = self.rfile.read(length) if length else b"{}"
                        data = json.loads(raw or b"{}")
                    except Exception as exc:
                        self._send_json({"error": f"bad request: {exc}"}, 400)
                        return
                    try:
                        if path == "/api/feature":
                            flag = str(data.get("flag", "")).strip()
                            state = str(data.get("state", "")).strip().lower()
                            if not flag:
                                self._send_json({"error": "missing flag"}, 400)
                                return
                            result = server._apply_change(flag, state)
                        elif path == "/api/scope":
                            command = str(data.get("command", "")).strip()
                            scope = data.get("scope")
                            scope = None if scope is None else str(scope).strip().lower()
                            if not command:
                                self._send_json({"error": "missing command"}, 400)
                                return
                            result = server._apply_scope(command, scope)
                        elif path == "/api/meta":
                            domain = str(data.get("domain", "")).strip()
                            default = data.get("default")
                            carry = data.get("carry")
                            if default is not None:
                                default = str(default).strip().lower()
                            if carry is not None:
                                carry = bool(carry)
                            if not domain:
                                self._send_json({"error": "missing domain"}, 400)
                                return
                            result = server._apply_meta(domain, default, carry)
                        elif path == "/api/area":
                            area = str(data.get("area", "")).strip()
                            disabled = bool(data.get("disabled", False))
                            if not area:
                                self._send_json({"error": "missing area"}, 400)
                                return
                            result = server._apply_area(area, disabled)
                        elif path == "/api/alias":
                            scope = str(data.get("scope", "")).strip().lower()
                            name = str(data.get("name", "")).strip()
                            expansion = data.get("expansion")
                            if expansion is not None:
                                expansion = str(expansion)
                            result = server._apply_alias(scope, name, expansion)
                        elif path == "/api/builtin":
                            name = str(data.get("name", "")).strip()
                            field = str(data.get("field", "")).strip()
                            value = data.get("value")
                            if not name or not field:
                                self._send_json({"error": "missing name/field"}, 400)
                                return
                            result = server._apply_builtin(name, field, value)
                        elif path == "/api/theme":
                            base = str(data.get("base", "")).strip()
                            overrides = data.get("overrides") or {}
                            if not isinstance(overrides, dict):
                                overrides = {}
                            result = server._apply_theme(base, overrides)
                        else:  # /api/structure
                            command = str(data.get("command", "")).strip()
                            fields = data.get("fields") or []
                            if not command:
                                self._send_json({"error": "missing command"}, 400)
                                return
                            result = server._apply_structure(command, fields)
                        self._send_json({"ok": True, **result})
                    except ValueError as exc:
                        self._send_json({"error": str(exc)}, 400)
                    except RuntimeError as exc:
                        self._send_json({"error": str(exc)}, 500)
                    except Exception as exc:  # pragma: no cover
                        self._send_json({"error": str(exc)}, 500)
                    return
                self._send(404, b"not found", "text/plain")

        try:
            self._httpd = _QuietThreadingHTTPServer((self._host, self._port), _Handler)
        except OSError as exc:
            return (
                f"[error] Could not start feature editor on "
                f"{self._host}:{self._port} — {exc}. "
                f"Is another editor already running, or the port in use?"
            )

        thread = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        thread.start()

        # Cache-bust the URL per launch so the browser opens a FRESH page (and
        # re-fetches saved prefs/theme) instead of re-focusing a stale tab from a
        # previous `feature gui` in the same session.
        import time as _time
        url = f"http://{self._host}:{self._port}/?v={int(_time.time())}"
        try:
            webbrowser.open(url)
        except Exception:  # pragma: no cover - headless safety net
            pass

        # Block the shell here until the editor is closed or Ctrl-C.
        try:
            self._closed.wait()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()
        return f"Feature editor closed — {url}"

    def stop(self) -> None:
        if self._httpd is not None:
            try:
                self._httpd.shutdown()
                self._httpd.server_close()
            except Exception:  # pragma: no cover
                pass
            self._httpd = None
        self._closed.set()

    @property
    def url(self) -> str:
        return f"http://{self._host}:{self._port}/"
