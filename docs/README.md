# society_mgmt_300k — Documentation

## Overview

This is the navigation hub for the **`society_mgmt_300k`**
documentation. The repository is a **synthetic, dependency-free**
JavaScript corpus: **29** `.js` files holding **33,105** functions
named `mod_<fileId>_<k>`, totalling **exactly 300,000** lines.
Source: docs/reference/file-inventory.md#verification

The corpus is organized as a layered scaffold of
**11 nominal layers** under `src/` and `tests/`, with no inter-layer
dependencies. These docs are **plain Markdown**, with any diagrams
embedded as fenced `mermaid` code blocks that render natively on
GitHub — there is no build step, generator, or package manifest. Note
that "society management" is a **nominal label** (the repository name
plus a per-file header comment), not implemented domain functionality.
Source: docs/architecture/layered-scaffold.md (the 11 nominal layers
with no inter-layer dependencies); docs/security/README.md#supply-chain
(no build step, generator, or package manifest);
society_mgmt_300k/src/controllers/file_0.js:L1 (the `// mod_0 - society
module` header label)

## How to read these docs

The documentation follows a **progressive-disclosure** path: start with
the high-level overview, learn *what* the code does, then *how* it is
laid out, review its performance and security characteristics, and keep
the reference material for lookups.

1. **[Overview](overview.md)** — what the corpus is and what it is not.
2. **[Functionality](functionality/README.md)** — *what* the code does.
3. **[Architecture](architecture/README.md)** — *how* the corpus is
   laid out, plus the per-function control flow.
4. **[Performance](performance/README.md)** — runtime characteristics.
5. **[Security](security/README.md)** — security posture and licensing.
6. **Reference** — the [file inventory](reference/file-inventory.md),
   [code reference](reference/code-reference.md), and
   [glossary](reference/glossary.md) for lookups.

## Documentation map

Every documentation area and page, with a one-line description of each:

- **[Overview](overview.md)** — system overview; the synthetic-corpus
  nature; "society management" as a label; and what the system is
  **not**.
- **Functionality** — what the code does:
  - **[Functionality catalog](functionality/README.md)** — features
    F-001..F-006 summary and the feature-relationship diagram.
  - **[Arithmetic helpers](functionality/arithmetic-helpers.md)** —
    F-001 core behavior (`6x + 10`, dead branch) and the F-002
    namespace.
  - **[Module anatomy](functionality/module-anatomy.md)** — the header
    comment, the F-004 inert `store`, and the comment-only `filler.js`
    variant.
  - **[Corpus composition](functionality/corpus-composition.md)** —
    F-005 sizing and the per-layer file/function/line table.
- **Architecture** — how it is laid out:
  - **[Architecture index](architecture/README.md)** — scaffold summary
    and links.
  - **[Layered scaffold](architecture/layered-scaffold.md)** — F-003,
    the 11 nominal layers and the layer-map diagram (no inter-layer
    edges).
  - **[Module control flow](architecture/module-control-flow.md)** —
    control-flow diagram annotating the dead always-true branch.
- **[Performance](performance/README.md)** — O(1) per-call time and
  space, determinism, and the explicit absence of SLAs.
- **[Security](security/README.md)** — the verified-absence posture, the
  attack surface, and the F-006 dual-license governance item.
- **Reference** — material for lookups:
  - **[File inventory](reference/file-inventory.md)** — all 29 `.js`
    files mapped to layer, function count, and line count.
  - **[Code reference](reference/code-reference.md)** — the `mod_*`
    archetype (file-local, not a public API).
  - **[Glossary](reference/glossary.md)** — terminology (`mod_`,
    `store`, `filler`, *layer*, *short variant*, *synthetic corpus*,
    *dead branch*).

## Key facts at a glance

- **Size:** 29 `.js` files, 33,105 `mod_<fileId>_<k>` functions, and
  exactly 300,000 lines.
  Source: docs/reference/file-inventory.md#verification
- **Behavior:** every function effectively returns `6x + 10` — it sums
  `x*1 + x*2 + x*3` (= `6x`), then adds `10` on the always-true even
  branch; for example, `mod_0_0(4) === 34`.
  Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
- **Structure:** 11 nominal layers under `src/` and `tests/` with no
  inter-layer edges.
  Source: docs/architecture/layered-scaffold.md
- **No dependencies, no module system:** there is no `package.json` or
  other manifest, and no `require`/`import`/`export`, so every symbol is
  file-local and not externally importable.
  Source: docs/security/README.md#supply-chain (no `package.json` or
  other manifest); docs/security/README.md#verified-absences-keyword-sweep
  (no `require`/`import`/`export` — symbols are file-local)
- **Inert placeholder:** a module-scoped `const store = [];` appears in
  28 of the 29 files and is never read or written.
  Source: docs/functionality/module-anatomy.md (the inert `store`, never
  read or written, in 28 of the 29 files);
  society_mgmt_300k/src/controllers/file_0.js:L2 (the representative
  declaration)
- **Licensing (F-006):** a dual-license conflict — the root `LICENSE` is
  Apache-2.0 while `society_mgmt_300k/LICENSE/LICENSE.txt` is MIT —
  documented (not resolved) in [Security](security/README.md).
  Source: LICENSE; society_mgmt_300k/LICENSE/LICENSE.txt:L1

## Conventions

To keep the child pages predictable, every documentation page follows
the same conventions:

- **One H1 per page** — each page has a single top-level heading; all
  other headings are `##`/`###`.
- **Inline source citations** — every technical claim is followed by a
  `Source:` reference: a `society_mgmt_300k/...:Lx-Ly` source line for
  line-supported claims (or `Source: LICENSE`), or the authoritative
  documentation page (for example
  `docs/reference/file-inventory.md#verification`) for corpus-wide
  facts, so it can be re-verified against the code.
- **Mermaid diagrams** are embedded as fenced `mermaid` code blocks that
  render natively on GitHub; no build step or image assets are used.
- **Terminology** is defined once in the
  [Glossary](reference/glossary.md); pages link to it rather than
  redefining terms.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical
  module motif (header comment, inert `store`, and a `mod_*` function);
  the representative archetype only.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the function
  body that yields the `6x + 10` behavior, including the dead
  always-true parity branch.
- `docs/reference/file-inventory.md#verification` — the authoritative,
  reproducible scan establishing the 29-file / 33,105-function /
  300,000-line counts.
- `docs/architecture/layered-scaffold.md` — the authoritative source for
  the 11 nominal layers and the absence of inter-layer edges.
- `docs/security/README.md#supply-chain` — the dependency-free
  supply-chain posture (no `package.json`, lockfile, generator, or build
  step).
- `docs/security/README.md#verified-absences-keyword-sweep` — the
  authoritative keyword sweep establishing that no module system is
  present (zero `require`/`import`/`export`), so every symbol is
  file-local.
- `docs/functionality/module-anatomy.md` — the authoritative source for
  the inert `store` placeholder (F-004), present in 28 of the 29 files.
- `LICENSE` — the root **Apache-2.0** license (F-006).
- `society_mgmt_300k/LICENSE/LICENSE.txt:L1` — the inner **MIT** license
  that conflicts with the root Apache-2.0 license (F-006).
- `README.md` — the repository's root readme (a placeholder at this
  checkpoint), to be updated at the final checkpoint to link into this
  documentation hub as its entry point.
