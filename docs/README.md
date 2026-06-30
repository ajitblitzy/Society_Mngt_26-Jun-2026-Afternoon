# society_mgmt_300k — Documentation

This page is the documentation hub and navigation entry point for everything
under `docs/`. Start here, then follow the links below to the topic you need;
the repository's root [`README.md`](../README.md) links here as the
documentation entry point.

## Overview

`society_mgmt_300k` is a **synthetic, dependency-free JavaScript corpus** — a
deterministically generated body of code intended for static analysis and code
traversal rather than execution. It comprises **29 `.js` files** totaling
**exactly 300,000 lines** and defining **33,105 functions** named
`mod_<fileId>_<k>`, every one of which computes the same expression, `6x + 10`,
for a numeric input `x`
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).

The files are arranged as a **layered scaffold of 11 nominal layers** under
`src/` and `tests/`, with **no inter-layer dependencies** and no module system.
The name "society management" is a **nominal label only** — it appears as the
repository name and a per-file header comment, and is **not** implemented
domain functionality
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1`). These documents are
plain Markdown with any diagrams embedded as fenced `mermaid` blocks that render
natively on GitHub, so **no build step** is required to read them.

## How to read these docs

The documentation is arranged for **progressive disclosure** — start broad,
then drill into detail. Read in the order below, then use the Reference
material for targeted lookups:

1. [Overview](overview.md) — what the corpus is (and is not).
2. [Functionality](functionality/README.md) — what the code does.
3. [Architecture](architecture/README.md) — how the code is laid out, plus
   control flow.
4. [Performance](performance/README.md) — runtime characteristics.
5. [Security](security/README.md) — security posture and governance.
6. [Reference](reference/file-inventory.md) — inventory, code reference, and
   glossary for targeted lookups.

## Documentation map

Every documentation page is indexed below, grouped by area.

- **[Overview](overview.md)** — system overview; synthetic-corpus nature;
  "society management" as a label; what the system is **not**.
- **Functionality**
  - [Functionality catalog](functionality/README.md) — features F-001..F-006
    summary plus a feature-relationship diagram.
  - [Arithmetic helpers](functionality/arithmetic-helpers.md) — F-001 core
    behavior (`6x + 10`, dead branch) and F-002 symbol namespace.
  - [Module anatomy](functionality/module-anatomy.md) — header comment, the
    F-004 inert `store`, and the comment-only `filler.js` variant.
  - [Corpus composition](functionality/corpus-composition.md) — F-005 sizing;
    per-layer file/function/line table.
- **Architecture**
  - [Architecture index](architecture/README.md) — scaffold summary and links.
  - [Layered scaffold](architecture/layered-scaffold.md) — F-003, the 11
    nominal layers; layer-map diagram (no inter-layer edges).
  - [Module control flow](architecture/module-control-flow.md) — control-flow
    diagram annotating the dead always-true branch.
- **[Performance](performance/README.md)** — O(1) per-call time and space,
  determinism, and the explicit absence of SLAs.
- **[Security](security/README.md)** — verified-absence posture; attack
  surface; F-006 dual-license governance.
- **Reference**
  - [File inventory](reference/file-inventory.md) — all 29 `.js` files mapped
    to layer / function count / line count.
  - [Code reference](reference/code-reference.md) — the `mod_*` archetype
    (file-local, not a public API).
  - [Glossary](reference/glossary.md) — terminology (`mod_`, `store`,
    `filler`, layer, short variant, synthetic corpus, dead branch).

## Key facts at a glance

- **Scale:** 29 `.js` files, 33,105 functions, exactly 300,000 lines
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- **Behavior:** every `mod_<fileId>_<k>(x)` returns `6x + 10`; for example,
  `mod_0_0(4)` = `6*4 + 10` = `34`. The parity branch (`if (r % 2 === 0)`) is a
  **dead always-true branch** because `6x` is always even
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).
- **Structure:** 11 nominal layers under `src/` and `tests/` with **no
  inter-layer edges**
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).
- **Dependencies:** zero — there is no module system, package manifest, or
  external dependency
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- **Naming:** "society management" is a **nominal label**, not implemented
  functionality
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).
- **Licensing:** a **dual-license conflict (F-006)** exists — the root
  `LICENSE` is Apache-2.0 while `society_mgmt_300k/LICENSE/LICENSE.txt` is MIT;
  it is documented (not resolved) in [Security](security/README.md)
  (Source: LICENSE; `society_mgmt_300k/LICENSE/LICENSE.txt:L1`).

## Conventions

Every page in this tree follows the same conventions so they are predictable:

- **One H1 per page** — a single `#` title; all other headings use `##`/`###`.
- **Source citations on every claim** — each technical statement carries an
  inline `Source: society_mgmt_300k/<path>:Lx-Ly` citation (or `Source: LICENSE`
  for the root license) so any reader can trace it to the code.
- **Mermaid diagrams as fenced code blocks** — diagrams are written as fenced
  `mermaid` blocks that render natively on GitHub; no build step is required.
- **Consistent terminology** — terms are defined once in the
  [Glossary](reference/glossary.md); other pages defer to it rather than
  redefining them.

## Source Citations

- Canonical module motif and corpus counts (the `// mod_0 - society module`
  header, the inert `const store = []`, and the `6x + 10` function body that is
  byte-identical across all 33,105 functions) — Source:
  `society_mgmt_300k/src/controllers/file_0.js:L1-L10`.
- Dual-license conflict (F-006) — Source: `LICENSE` (Apache-2.0) and
  `society_mgmt_300k/LICENSE/LICENSE.txt:L1` (MIT).
- Project identity and documentation entry point — Source: `README.md`.
