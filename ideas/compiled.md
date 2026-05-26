# ARC — Compiled & Distributed Binary: Design Ideas

**Status:** Concept / Not Implemented  
**Author:** Brian Eckblad  
**Date:** 2026-05-25

---

## The Problem

ARC is currently distributed as **raw Python source code** in a Git repository.
Anyone who clones it can read every line — the command logic, the API client, any
licensing checks, and all business rules are fully visible.

The goal of this document is to explore how to ship ARC as a **compiled artifact**
where the Python source is not present on the end-user's machine.

---

## Option Comparison at a Glance

| Approach | Source hidden? | Single binary? | Native speed | Complexity | Best for |
|----------|---------------|----------------|--------------|------------|---------|
| `.pyc` bytecode only | Partial (weak) | No | No | Low | Nothing serious |
| PyInstaller | Yes | Yes | No | Low-Medium | Fast distribution |
| cx_Freeze | Yes | No (folder) | No | Low | Windows installers |
| **Nuitka** | **Yes** | **Yes** | **Yes (near C)** | Medium | **Recommended for ARC** |
| Cython (selective) | Yes (partial) | No | Yes (hot paths) | High | Libraries, not CLIs |
| mypyc | Partial | No | Yes (moderate) | Medium | Type-annotated codebases |
| Codon | Yes | Yes | Yes | Very High | Scientific/numeric only |

---

## Option 1 — `.pyc` Bytecode Distribution (Do Not Use)

Python compiles `.py` files to `.pyc` bytecode files (stored in `__pycache__/`).
You could ship only `.pyc` files and omit `.py` sources.

```bash
python -m compileall app/
# Produces: app/__pycache__/cli.cpython-311.pyc etc.
```

**Why this is not real protection:**

- `.pyc` files are trivially decompiled back to readable Python using
  `decompile3`, `uncompyle6`, or `pycdc` — takes seconds
- The bytecode format is documented and stable
- No obfuscation, no binary encoding — it is just a serialised AST

**Verdict:** Skip this. It provides a false sense of security.

---

## Option 2 — PyInstaller

PyInstaller bundles the Python interpreter, all dependencies, and your code
(as `.pyc` bytecode) into a single executable or a self-contained folder.

### How it works

```
pip install pyinstaller
pyinstaller --onefile --name arc run.py
```

Produces: `dist/arc` — a single binary (~15–40 MB for ARC given its deps).

Under the hood it:
1. Traces all imports recursively
2. Compiles all `.py` to `.pyc`
3. Packs them into a `PKG` archive embedded in a native launcher binary
4. On run, extracts to a temp dir (`/tmp/_MEI...`) and runs from there

### Pros

- Single `arc` binary — drop it in `/usr/local/bin/`, done
- Source `.py` files are not on disk
- Works on macOS, Linux, Windows
- Reasonably mature (10+ years old)

### Cons

- `.pyc` bytecode inside the binary is still **decompilable** — PyInstaller does
  not encrypt or obfuscate it; a determined attacker can `binwalk` the binary,
  extract the PKG archive, and decompile the bytecode
- Slow cold-start on first run (~0.5–2 s on some systems) due to extraction
- Binary is large; every dependency (httpx, paramiko, rich, prompt-toolkit) is bundled
- Must rebuild for each platform separately (no cross-compilation)
- `--onefile` extracts to `/tmp` on every run — breaks some corporate security policies

### PyInstaller + PyArmor (obfuscation layer)

PyArmor is an add-on that encrypts `.pyc` bytecode inside the PyInstaller bundle
and injects a native decryption stub. The encryption key is embedded in a
platform-specific `.so`/`.dll`.

```bash
pip install pyarmor
pyarmor gen --pack onefile run.py
```

This raises the reversal effort significantly — the key is in native code, the
bytecode is AES-encrypted at rest. Not unbreakable by a professional reverse
engineer, but it defeats casual inspection.

**Verdict for ARC:** Good for a quick distribution path. Add PyArmor if source
protection matters. Does not produce native-speed code.

---

## Option 3 — Nuitka ⭐ Recommended for ARC

Nuitka is a **Python-to-C compiler**. It translates your Python source into C code,
then compiles that C into a real native binary using `gcc`/`clang`/`MSVC`.

The output binary:
- Contains **no Python source, no `.pyc` bytecode, no PKG archive**
- Is a true compiled executable (ELF on Linux, Mach-O on macOS, PE on Windows)
- Runs at near-C speed for CPU-bound code
- Embeds the CPython runtime statically (or links dynamically to system Python)

### Basic build

```bash
pip install nuitka
# One-file standalone binary:
python -m nuitka \
    --onefile \
    --standalone \
    --output-filename=arc \
    --include-package=app \
    --include-package=typer \
    --include-package=rich \
    --include-package=prompt_toolkit \
    --include-package=httpx \
    --include-package=paramiko \
    --include-package=pydantic \
    run.py
```

Output: `arc.bin` → rename to `arc` → ship it.

### What the output actually is

```
arc  (Mach-O / ELF binary, ~25–60 MB)
  └─ compiled C code from all Python sources
  └─ embedded CPython runtime (libpython)
  └─ compiled C extensions (.so) for paramiko, cryptography, etc.
  └─ non-Python data files (docs/, config/) if included
```

A reverse engineer can disassemble the binary but will see **C-level code with
mangled function names**, not Python. There is no bytecode to decompile.

### Nuitka Commercial (optional)

Nuitka has a paid "Commercial" tier that adds:

- **Code obfuscation** — string constants scrambled, symbol names stripped
- **Anti-debugging** stubs
- **Onefile encryption** — the payload is encrypted with a key derived from hardware

For a CLI tool like ARC, the free tier is likely sufficient — the C output alone
removes casual inspection. Commercial adds the extra layer if needed.

### Platform matrix and CI

Since Nuitka produces platform-native binaries, you need a build job per platform:

```yaml
# .github/workflows/release.yml (sketch)
strategy:
  matrix:
    os: [ubuntu-22.04, macos-14, windows-2022]
    python-version: ["3.11"]

steps:
  - uses: actions/setup-python@v5
  - run: pip install nuitka ordered-set zstandard
  - run: python -m nuitka --onefile --standalone ...
  - uses: actions/upload-artifact@v4
    with:
      name: arc-${{ matrix.os }}
      path: arc.bin
```

### Nuitka build time

Nuitka compiles C — it is slow:
- First build: **5–15 minutes** depending on dep count
- Incremental rebuild (only changed modules): **1–3 minutes**
- Use `--jobs=4` to parallelise C compilation

Cache the `build/` directory in CI to speed up incremental builds.

### Pros

- **True native binary** — no Python source or bytecode in the output
- Near-C performance for tight loops (matters for tab completion, output rendering)
- Reverse engineering requires C-level disassembly, not bytecode decompilation
- Supports all of ARC's dependencies (httpx, paramiko, rich, prompt-toolkit, pydantic)
- Free tier is production-ready

### Cons

- Slow build times (not a dev workflow tool, only for releases)
- Must build per platform — no cross-compilation
- Some dynamic Python patterns (e.g. `importlib` trickery, `__import__` with computed strings) can break; ARC should be fine
- Binary size (~50 MB) larger than a pip install on a machine that already has Python

**Verdict:** Nuitka is the right answer for ARC. It produces a real compiled binary,
hides all source code at the C level, and has proven support for all of ARC's deps.

---

## Option 4 — Cython (Compile Selected Modules)

Cython is a **superset of Python** that compiles `.pyx` or annotated `.py` files
to C extension modules (`.so` / `.pyd`). It is primarily a performance tool for
libraries, not an application packaging tool.

### How it would work for ARC

Compile the sensitive modules (API client, license check, registry) to `.so`:

```bash
pip install cython
cython --embed app/api/client.py   # → client.c
gcc -shared -fPIC -O2 \
    -o app/api/client.so \
    client.c $(python3-config --includes --ldflags)
```

Users would still need Python installed. You'd distribute:
- `app/shell.py` (plain Python — the REPL glue)
- `app/api/client.so` (compiled — the sensitive HTTP logic)
- `app/commands/registry.so` (compiled — the command definitions)

### Comparison with Nuitka

| | Cython | Nuitka |
|---|---|---|
| Output | `.so` per module | Single binary |
| Python required on target | Yes | No (standalone mode) |
| Source hidden | Yes (compiled modules) | Yes (all modules) |
| Selective compilation | Yes (can keep some `.py`) | No (all or nothing) |
| CLI distribution | Awkward | Natural |

### Why Cython is not ideal for a CLI like ARC

- You still need to distribute `.py` files for the modules you don't compile,
  and users need a matching Python version for the `.so` files
- A single compiled `.so` in a sea of `.py` files doesn't meaningfully protect the codebase
- Cython shines for performance-critical library extensions (numpy-style), not full apps

**Verdict:** Use Cython only if you need to selectively accelerate a hot path
(tab completion scanning, JSON parsing in the formatter) while using Nuitka for the
full application binary. Do not use Cython as the primary distribution strategy.

---

## Option 5 — mypyc

`mypyc` (from the mypy project) compiles **fully type-annotated Python** to C
extension modules, similar to Cython but using standard Python type hints rather
than Cython's custom syntax.

```bash
pip install mypy[mypyc]
mypyc app/api/client.py app/commands/registry.py
```

Same distribution shape as Cython — produces `.so` files, requires Python on target.
Benchmarks show 2–5× speedup for type-annotated code.

**Verdict:** Good option if ARC's modules are already fully type-annotated and you
want a performance boost without changing syntax. Still not a full-app solution.

---

## Recommended Distribution Architecture for ARC

### Phase 1 — Quick win: PyInstaller + PyArmor

Low effort, ships in a week:

```
arc-macos-arm64      (PyInstaller onefile, PyArmor-obfuscated bytecode)
arc-linux-x86_64     (same)
arc-windows-x86_64   (same)
```

**Effort:** ~1–2 days. **Source protection:** Good (withstands casual inspection).
**Performance:** Same as interpreted Python.

### Phase 2 — Production: Nuitka

True compiled binary, ships with the license system:

```
arc-macos-arm64      (Nuitka onefile, C-compiled, ~50 MB)
arc-linux-x86_64     (same)
arc-windows-x86_64   (same)
```

**Effort:** ~3–5 days for build pipeline. **Source protection:** Strong (C-level).
**Performance:** 2–5× faster on CPU-bound paths.

### Distribution channels

| Channel | Format | Notes |
|---------|--------|-------|
| GitHub Releases | Single binary attached to tag | Simplest |
| Homebrew tap | `brew install brianeckblad/arc/arc` | macOS/Linux friendly |
| `pip install arc-cli` | Wheel with `.so` modules or PyInstaller wrapped | Fallback for Python users |
| Direct download script | `curl .../install.sh \| bash` | One-liner for ops teams |

### Install script sketch

```bash
#!/usr/bin/env bash
# install.sh — downloads the correct arc binary for the current platform

REPO="https://github.com/brianeckblad/arc/releases/latest/download"
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
[ "$ARCH" = "x86_64" ] && ARCH="amd64"
[ "$ARCH" = "arm64" ]  && ARCH="arm64"

curl -fsSL "$REPO/arc-$OS-$ARCH" -o /usr/local/bin/arc
chmod +x /usr/local/bin/arc
arc --version
```

---

## Data Files (docs/, config/)

The Markdown docs in `docs/` and `config/config.example.json` are **not Python** —
they cannot be compiled. Options:

1. **Embed them in the binary** — Nuitka supports `--include-data-files` and
   `--include-data-dir`; the files are compressed into the binary and extracted
   to a temp dir at runtime.
2. **Ship alongside the binary** — A `dist/` folder with `arc` + `docs/`.
   Simpler but users can see the docs source.
3. **Pre-built docs bundle** — Since ARC already generates `docs/docs-bundle.js`
   via `arc cliup`, that bundle can be embedded. The raw `.md` files need not ship.

For production, option 1 (embed) is cleanest for a single-binary distribution.

---

## Build Pipeline (GitHub Actions Sketch)

```yaml
# .github/workflows/build.yml
name: Build compiled binaries

on:
  push:
    tags: ['v*']

jobs:
  build:
    strategy:
      matrix:
        include:
          - os: ubuntu-22.04;  name: linux-x86_64
          - os: macos-14;      name: macos-arm64
          - os: windows-2022;  name: windows-x86_64

    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }

      - name: Install deps
        run: pip install uv && uv sync

      - name: Install Nuitka
        run: pip install nuitka ordered-set zstandard

      - name: Compile
        run: |
          python -m nuitka \
            --onefile \
            --standalone \
            --output-filename=arc \
            --include-package=app \
            --include-data-dir=docs=docs \
            --include-data-dir=config=config \
            run.py

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: arc-${{ matrix.name }}
          path: arc${{ runner.os == 'Windows' && '.exe' || '' }}

  release:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
      - uses: softprops/action-gh-release@v2
        with:
          files: arc-*/**
```

---

## Open Questions

- **Binary size vs startup time:** Nuitka onefile extracts to a temp dir on first run
  (~0.3–0.8 s overhead). Is that acceptable for a CLI tool users run interactively?
  Alternative: `--standalone` (folder, not single file) — faster startup but less
  portable.

- **macOS code signing:** Apple Gatekeeper will block unsigned binaries downloaded
  from the internet. Proper distribution requires an Apple Developer ID certificate
  and `codesign` + `notarytool`. Cost: ~$99/year for the Developer Program.

- **Windows SmartScreen:** Same problem on Windows — a self-signed or unsigned
  `.exe` triggers a "Windows protected your PC" warning. Requires Authenticode
  code signing (~$200–500/year for an EV certificate).

- **Auto-update:** A compiled binary can't `pip install --upgrade` itself. ARC would
  need a built-in update check: compare current version to GitHub Releases API,
  download new binary, replace itself (`os.execv` after download + chmod).

- **License system interaction:** The license check (from `ideas/security_system.md`)
  is significantly stronger when the verification code is compiled — patching it
  requires binary-level work rather than editing a Python file. Nuitka makes the
  license system materially harder to bypass.

---

## Summary

For ARC, the right approach is **Nuitka** for the compiled binary distribution:

1. All Python source compiles to C → true native binary
2. No Python required on the target machine
3. Single `arc` binary dropped in `$PATH` — identical UX to `curl | bash` installs
4. Pairs naturally with the license system (compiled = harder to bypass)
5. GitHub Actions matrix builds cover macOS/Linux/Windows automatically

Start with **PyInstaller + PyArmor** for a quick first distribution, then migrate
the build pipeline to **Nuitka** when the app is feature-stable.

