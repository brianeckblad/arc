# ARC — AES-Encrypted Bytecode + Hardened C Compilation

**Status:** Concept / Not Implemented  
**Author:** Brian Eckblad  
**Date:** 2026-05-25  
**Extends:** `ideas/compiled.md`

---

## The Idea in One Sentence

**AES-256-GCM encrypt every Python module before Nuitka sees it, then compile
the encrypted blobs + decryption stub into C, then compile that C with every
available hardening flag** — so extracting the source requires breaking both
the encryption layer AND the hardened native binary.

---

## Why Two Separate Layers?

Nuitka alone compiles Python to C — a reverse engineer who disassembles the
binary sees mangled C symbols instead of Python. That raises the bar, but the
bytecode structures are still recognisable in memory while the process is running.

Encrypting **before** compilation means:

```
On disk:  enc(AES-256-GCM, module_bytes)  →  looks like random bytes
In C:     static const uint8_t MODULE_SHELL_DATA[] = { 0x3F, 0xA2, ... };
In RAM:   decrypted only in a malloc'd buffer; freed/zeroised immediately after CPython loads it
```

Even if someone dumps the process memory at the right moment, they get the CPython
bytecode (`.pyc`) — not the Python source. And the bytecode is version-specific
and stripped of line info.

---

## Architecture: Three Concentric Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 3 — Hardened C binary (GCC/Clang hardening flags, stripped)  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  Layer 2 — Nuitka-compiled C (Python → C transpilation)       │  │
│  │  ┌─────────────────────────────────────────────────────────┐  │  │
│  │  │  Layer 1 — AES-256-GCM encrypted Python modules          │  │  │
│  │  │  (static byte arrays in the compiled C)                  │  │  │
│  │  └─────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

A reverse engineer has to peel all three layers:
1. Strip and ASLR-defeat the hardened binary (Layer 3)
2. Understand the Nuitka C runtime and de-mangle symbols (Layer 2)
3. Extract and decrypt the AES-encrypted module payloads (Layer 1)

---

## Layer 1 — AES-256-GCM Encryption of Python Modules

### What gets encrypted

Only the **sensitive modules** need this treatment. Encrypting `rich` or
`httpx` is pointless — they're open source. Target the ARC-specific code:

```
app/commands/registry.py      ← all command logic
app/api/client.py             ← SCM API implementation
app/auth/license.py           ← license verification + self-deletion
app/shell.py                  ← REPL dispatch
app/config.py                 ← config schema
```

### Key derivation

The AES key must be embedded in the binary but not as a plain constant (trivially
found with `strings arc`). Use a **multi-step derivation**:

```
build_secret  = random 32 bytes (generated once, stored in CI secret)
hw_salt       = BLAKE2b(machine_id || binary_sha256[:8])   ← optional device binding
derived_key   = HKDF-SHA256(build_secret, salt=hw_salt, info=b"arc-module-key")
```

For a non-device-bound build:

```
derived_key = HKDF-SHA256(build_secret, salt=b"arc-2026", info=b"arc-module-key")
```

The `build_secret` is never on disk outside CI; it is passed as an environment
variable during the build and embedded in the C source as a **transformed constant**
(split across multiple arrays, XOR'd with a mask) so `strings` does not find it.

### Build-time encryption script

```python
# scripts/encrypt_modules.py
import os, json
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

BUILD_SECRET = bytes.fromhex(os.environ["ARC_BUILD_SECRET"])   # 32 bytes from CI

def derive_key(build_secret: bytes) -> bytes:
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"arc-2026",
        info=b"arc-module-key",
    ).derive(build_secret)

AES_KEY = derive_key(BUILD_SECRET)
aesgcm  = AESGCM(AES_KEY)

TARGETS = [
    "app/commands/registry.py",
    "app/api/client.py",
    "app/auth/license.py",
    "app/shell.py",
    "app/config.py",
]

manifest = {}
for path in TARGETS:
    src  = Path(path).read_bytes()
    nonce = os.urandom(12)                      # 96-bit GCM nonce
    ct    = aesgcm.encrypt(nonce, src, None)    # ciphertext + 16-byte GCM tag
    blob  = nonce + ct                          # nonce prepended
    module_id = path.replace("/", "_").replace(".py", "")
    manifest[module_id] = blob.hex()

Path("build/encrypted_manifest.json").write_text(json.dumps(manifest))
print(f"Encrypted {len(TARGETS)} modules.")
```

### Generating C header from encrypted blobs

```python
# scripts/generate_encrypted_header.py  (runs after encrypt_modules.py)
import json
from pathlib import Path

manifest = json.loads(Path("build/encrypted_manifest.json").read_text())

lines = ["/* AUTO-GENERATED — DO NOT EDIT */\n",
         "#pragma once\n",
         "#include <stddef.h>\n\n"]

for module_id, hex_blob in manifest.items():
    data = bytes.fromhex(hex_blob)
    c_array = ", ".join(f"0x{b:02x}" for b in data)
    lines.append(f"/* {module_id} — {len(data)} bytes (12-byte nonce + ciphertext + 16-byte GCM tag) */\n")
    lines.append(f"static const unsigned char ENC_{module_id.upper()}[] = {{{c_array}}};\n")
    lines.append(f"static const size_t ENC_{module_id.upper()}_LEN = {len(data)};\n\n")

Path("build/arc_modules.h").write_text("".join(lines))
print("Generated build/arc_modules.h")
```

---

## Layer 2 — Nuitka C Compilation with Custom Decryption Stub

### The decryption stub

Nuitka supports **C-level plugins** and `--include-raw-dir`. We write a small C
module that:

1. Is linked into the final binary by Nuitka
2. At startup, decrypts each encrypted module blob into a `malloc`'d buffer
3. Calls `PyImport_AddModuleObject` + `PyMarshal_ReadObjectFromString` to load
   the decrypted bytecode into the CPython interpreter
4. Immediately calls `OPENSSL_cleanse` / `explicit_bzero` on the buffer and `free`s it

```c
/* arc_loader.c — compiled into the Nuitka binary */
#include "arc_modules.h"
#include <openssl/evp.h>
#include <string.h>

/* The AES key is split and reassembled at runtime to defeat simple string searches.
   Build system fills in the four 8-byte chunks via -DARC_KEY_A=... etc.          */
static void assemble_key(unsigned char *key) {
    const unsigned char a[8] = ARC_KEY_A;
    const unsigned char b[8] = ARC_KEY_B;
    const unsigned char c[8] = ARC_KEY_C;
    const unsigned char d[8] = ARC_KEY_D;
    memcpy(key,      a, 8);
    memcpy(key + 8,  b, 8);
    memcpy(key + 16, c, 8);
    memcpy(key + 24, d, 8);
}

/*
 * decrypt_module — AES-256-GCM decrypt a module blob.
 * blob layout: [12-byte nonce][ciphertext][16-byte GCM tag]
 * Returns heap-allocated plaintext. Caller must cleanse + free.
 */
static unsigned char *decrypt_module(
        const unsigned char *blob, size_t blob_len, size_t *out_len) {

    const size_t  NONCE_LEN   = 12;
    const size_t  TAG_LEN     = 16;
    size_t        ct_len      = blob_len - NONCE_LEN - TAG_LEN;
    unsigned char key[32];
    unsigned char *plaintext  = malloc(ct_len);

    assemble_key(key);

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    EVP_DecryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL);
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_IVLEN, NONCE_LEN, NULL);
    EVP_DecryptInit_ex(ctx, NULL, NULL, key, blob /* nonce */);

    int len = 0;
    EVP_DecryptUpdate(ctx, plaintext, &len,
                      blob + NONCE_LEN,      /* ciphertext */
                      (int)ct_len);
    *out_len = len;

    /* Set expected tag before finalise */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_TAG, TAG_LEN,
                         (void *)(blob + NONCE_LEN + ct_len));

    int ok = EVP_DecryptFinal_ex(ctx, plaintext + len, &len);
    EVP_CIPHER_CTX_free(ctx);

    /* Immediate key zeroisation */
    OPENSSL_cleanse(key, sizeof(key));

    if (ok <= 0) {
        /* GCM tag mismatch — binary has been tampered with */
        OPENSSL_cleanse(plaintext, ct_len);
        free(plaintext);
        return NULL;            /* caller must abort */
    }

    *out_len += len;
    return plaintext;
}
```

### Nuitka build command (with stub included)

```bash
python -m nuitka \
    --onefile \
    --standalone \
    --output-filename=arc \
    --include-package=app \
    --include-data-dir=docs=docs \
    --include-data-dir=config=config \
    --user-package-configuration-file=nuitka-pkg.yml \
    --clang \
    --lto=yes \
    --jobs=4 \
    --c-compiler-flags="-DARC_KEY_A={KEY_A} -DARC_KEY_B={KEY_B} -DARC_KEY_C={KEY_C} -DARC_KEY_D={KEY_D}" \
    --c-compiler-flags="-include build/arc_modules.h" \
    --link-with=arc_loader.o \
    run.py
```

`KEY_A`–`KEY_D` are injected by the CI pipeline from a vault secret — they never
appear in any committed file.

---

## Layer 3 — GCC / Clang Hardening Flags

These are passed to Nuitka via `--c-compiler-flags` and `--link-flags`.

### Compile-time flags

```makefile
CFLAGS = \
  -O2                          \  # optimise (also obscures control flow)
  -fstack-protector-all        \  # canary on every stack frame
  -fstack-clash-protection     \  # prevent stack-clash attacks
  -fcf-protection=full         \  # Intel CET: control-flow integrity (x86)
  -fPIE                        \  # position-independent executable
  -D_FORTIFY_SOURCE=3          \  # fortified libc wrappers (glibc 2.34+)
  -fvisibility=hidden          \  # hide all symbols by default
  -fno-plt                     \  # avoid PLT stubs (reduces ROP gadgets)
  -fstrict-aliasing            \  # strict aliasing for better optimisation
  -fno-asynchronous-unwind-tables \  # strip .eh_frame (reduces attack surface)
  -DNDEBUG                     \  # disable assert() in release
  -g0                             # no debug info in binary
```

### Link-time flags (Linux ELF)

```makefile
LDFLAGS = \
  -pie                         \  # ASLR-compatible
  -Wl,-z,relro                 \  # mark GOT read-only after relocations
  -Wl,-z,now                   \  # resolve all symbols at load (full RELRO)
  -Wl,-z,noexecstack           \  # non-executable stack
  -Wl,-z,separate-code         \  # code and data in separate segments
  -Wl,--strip-all              \  # remove all symbol table entries
  -Wl,--gc-sections            \  # dead-code elimination
  -Wl,-z,defs                     # no undefined symbols
```

### macOS equivalents

```makefile
LDFLAGS_MACOS = \
  -Wl,-pie \
  -Wl,-dead_strip \
  -Wl,-no_eh_labels \
  -Wl,-S                          # strip debug symbols
  # codesign --options runtime (required for Gatekeeper + notarisation)
```

### Post-link hardening steps

```bash
# Strip any remaining debug info (belt and suspenders after --strip-all)
strip --strip-all arc

# Verify hardening is in place (Linux)
checksec --file=arc
# Expected output:
#   RELRO:    Full RELRO
#   STACK:    Canary found
#   NX:       NX enabled
#   PIE:      PIE enabled
#   Symbols:  No symbols
```

### LTO (Link-Time Optimisation)

Pass `--lto=yes` to Nuitka (maps to `-flto` in GCC/Clang). LTO:
- Lets the compiler inline and eliminate code across translation units
- Significantly reduces the number of callable functions visible to ROP tooling
- Merges all C files before final optimisation — the output more closely resembles
  a single monolithic C program than a collection of linked objects

---

## Anti-Debug and Integrity Checks (Optional, C-level)

Add a small C module that is called from the Nuitka entry point before any Python
runs. These are defence-in-depth measures, not unbreakable, but they raise the cost.

```c
/* arc_hardening.c */

#include <sys/ptrace.h>
#include <stdlib.h>
#include <time.h>

/*
 * ptrace self-check — a debugger attaches via ptrace; calling ptrace(PTRACE_TRACEME)
 * from inside a debugged process returns -1.
 * Linux only; macOS equivalent uses sysctl(KERN_PROC).
 */
static void check_debugger(void) {
#ifdef __linux__
    if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
        _exit(1);   /* silent exit — don't reveal reason */
    }
#endif
}

/*
 * Timing check — debugger single-stepping inflates wall-clock time.
 * A 1 ms nop loop that takes > 500 ms wall-clock = likely being stepped.
 */
static void check_timing(void) {
    struct timespec start, end;
    volatile int x = 0;
    clock_gettime(CLOCK_MONOTONIC, &start);
    for (int i = 0; i < 1000000; i++) { x += i; }
    clock_gettime(CLOCK_MONOTONIC, &end);
    long elapsed_ms = (end.tv_sec - start.tv_sec) * 1000
                    + (end.tv_nsec - start.tv_nsec) / 1000000;
    if (elapsed_ms > 500) { _exit(1); }
    (void)x;
}

/*
 * Binary self-integrity check — hash the first N bytes of our own binary
 * and compare against a value embedded at compile time.
 * The expected hash is computed at build time and injected via -DARC_BINARY_HASH=...
 */
static void check_binary_integrity(const char *argv0) {
    /* Implementation reads /proc/self/exe (Linux) or argv[0] (macOS),
       computes SHA-256 of the first 1 MB, compares to ARC_BINARY_HASH constant. */
    /* ... */
}

void arc_security_checks(int argc, char **argv) {
    check_debugger();
    check_timing();
    check_binary_integrity(argv[0]);
}
```

---

## Full Build Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│  CI Pipeline (GitHub Actions, secrets injected at runtime)              │
│                                                                         │
│  1. checkout                                                            │
│  2. pip install nuitka cryptography pyarmor                            │
│                                                                         │
│  3. scripts/encrypt_modules.py                                          │
│        reads:  ARC_BUILD_SECRET (CI secret, never committed)           │
│        writes: build/encrypted_manifest.json                           │
│                                                                         │
│  4. scripts/generate_encrypted_header.py                               │
│        reads:  build/encrypted_manifest.json                           │
│        writes: build/arc_modules.h                                     │
│                                                                         │
│  5. scripts/split_key.py                                               │
│        splits AES key into ARC_KEY_A..D (passed as -D flags to GCC)   │
│                                                                         │
│  6. gcc -c arc_loader.c arc_hardening.c  (with hardening flags)        │
│        reads:  build/arc_modules.h, ARC_KEY_A..D                       │
│        writes: arc_loader.o, arc_hardening.o                           │
│                                                                         │
│  7. python -m nuitka --onefile --clang --lto=yes ...                   │
│        --link-with=arc_loader.o,arc_hardening.o                        │
│        --c-compiler-flags="(all hardening flags)"                      │
│        writes: arc (stripped native binary)                            │
│                                                                         │
│  8. checksec --file=arc  (verify hardening applied)                    │
│  9. strip --strip-all arc                                               │
│ 10. (macOS) codesign + notarytool                                       │
│ 11. upload-artifact → GitHub Release                                   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## What an Attacker Sees at Each Layer

| Layer | What they have | Required effort |
|-------|---------------|-----------------|
| Download `arc` binary | Stripped ELF/Mach-O, ASLR, full RELRO, no symbols | Need Ghidra/IDA Pro |
| Disassemble with Ghidra | Mangled Nuitka C symbols, LTO-inlined functions | Days of RE work |
| Find the AES decrypt call | Sees EVP_aes_256_gcm call, but the key assembly is split across 4 static arrays | Key is not contiguous in memory or binary |
| Dump process memory at decrypt moment | Gets AES key in RAM briefly, decrypted module bytecode | Requires a bypass of ptrace check + timing check AND correct timing |
| Decompile the `.pyc` bytecode dump | Gets Python bytecode (no source, no line info) | Days of manual bytecode reading |

Crucially, **there is no path from "download the binary" to "read the Python source"
without significant reverse-engineering effort and bypassing multiple active defences**.

---

## Integration with the License System

From `ideas/security_system.md`, the license check lives in `app/auth/license.py`.
That module is one of the AES-encrypted targets. This means:

- The license verification URL, the revocation logic, and the self-deletion code
  are inside the encrypted layer — not visible in the binary as plaintext strings
- The `build_secret` and the license server's public key (for JWT RS256 verification)
  are injected at build time via CI secrets, not stored in source
- Patching out the license check requires breaking Layer 3 + Layer 2 + Layer 1 first

```
grep -r "keys.arc-cli.io" arc    →  nothing (URL is AES-encrypted)
strings arc | grep -i license    →  nothing
strings arc | grep http          →  nothing (all sensitive strings encrypted)
```

---

## Toolchain Summary

| Tool | Role | License |
|------|------|---------|
| `cryptography` (Python) | AES-256-GCM encryption at build time | Apache 2.0 |
| `nuitka` | Python → C transpilation | Apache 2.0 |
| `openssl` / `libssl` | AES-GCM decryption in C stub | Apache 2.0 |
| `gcc` / `clang` | C compilation with hardening flags | GPL / Apache |
| `checksec` | Verify hardening flags post-build | Unknown/MIT |
| `strip` | Remove symbols from final binary | GPL (binutils) |
| `codesign` + `notarytool` | macOS Gatekeeper signing (requires Apple dev cert) | Proprietary |
| `signtool` | Windows Authenticode signing (requires EV cert) | Proprietary |

All tools in the build pipeline are open source except for platform code-signing, which
requires paid certificates ($99/year Apple Developer, ~$300/year Authenticode EV).

---

## Open Questions

- **Key rotation:** The AES encryption key is per-build. If a key is extracted, only
  that build is compromised — future releases use new keys. Should keys rotate per
  release tag or per platform?

- **macOS/Linux key split:** HKDF can derive platform-specific keys so the macOS
  binary cannot decrypt the Linux binary's modules and vice versa. Adds little
  security but raises the cost of porting an attack across platforms.

- **Memory protection after decryption:** After CPython loads a decrypted module,
  the plaintext bytecode is in CPython's memory pool. On Linux, `mprotect` can mark
  that region non-readable — but this requires knowing the exact allocation, which
  the Nuitka runtime does not expose easily.

- **Build secret management:** The `ARC_BUILD_SECRET` must never appear in CI logs.
  GitHub Actions encrypts CI secrets, but if the CI YAML itself is public, the secret
  access pattern is visible. Use an OIDC-based secrets vault (AWS Secrets Manager,
  HashiCorp Vault) rather than a static GitHub Actions secret for production.

- **Rust alternative:** Rewriting the sensitive core (license check, API client) in
  Rust and calling it from Python via PyO3 would produce native code without needing
  the AES encryption layer at all — the sensitive logic would never exist as Python.
  That is a larger investment but a cleaner long-term architecture.

---

## Summary

The design stacks three protections:

1. **AES-256-GCM** encrypts every sensitive Python module at build time using a key
   that is never committed and never present in the binary as a contiguous constant
2. **Nuitka** compiles the decryption stub and all Python to native C — there is no
   bytecode to decompile
3. **GCC/Clang hardening flags** (full RELRO, stack canaries, LTO, PIE, stripped
   symbols) make the binary difficult to analyse and exploit even at the C level

The result is a binary where:
- **No Python source is distributed**
- **No decryptable bytecode is on disk**
- **Sensitive strings (URLs, keys, algorithm names) are not findable with `strings`**
- **The license system lives inside the encrypted layer** — patching it out requires
  breaking all three layers before the first line of Python runs

