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
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10` for the per-file
motif and the `6x + 10` body; `docs/reference/corpus-evidence.md:L28-L54` for the
verified 29-file / 33,105-function / 300,000-line counts and
`docs/reference/corpus-evidence.md:L67-L95` for the body being byte-identical
across all 33,105 functions).

The files are arranged as a **layered scaffold of 11 nominal layers** under
`src/` and `tests/`, with **no inter-layer dependencies** and no module system.
The name "society management" is a **nominal label only** — it appears as the
repository name and a per-file header comment, and is **not** implemented
domain functionality
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1` for the per-file header
comment; `docs/reference/corpus-evidence.md:L177-L215` for the 11-layer
composition, `docs/reference/corpus-evidence.md:L112-L151` for the zero
`require`/`import`/`export`/`module.exports` sweep that confirms no module system
and no inter-layer edges, and `docs/reference/corpus-evidence.md:L248-L262` for
the evidence that "society management" is only a label). These documents are
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

Every Markdown page in the `docs/` tree is indexed below. The **current
documentation set** is grouped by area first; an earlier flat documentation set
is listed afterwards under **Legacy / superseded pages**, so that no page is
left unindexed.

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
  - [Corpus evidence](reference/corpus-evidence.md) — the reproducible scans
    (E1–E12) that substantiate every corpus-wide count and absence claim.
  - [Glossary](reference/glossary.md) — terminology (`mod_`, `store`,
    `filler`, layer, short variant, synthetic corpus, dead branch).

### Legacy / superseded pages

The pages below are an **earlier, flat documentation set** that predates the
structured tree above. They are retained for history but are **superseded** by
the current documentation set; prefer the pages above. They are indexed here so
this hub remains a complete index of every page under `docs/`.

- [Architecture (legacy)](architecture.md) — superseded by the
  [Architecture index](architecture/README.md) and
  [Layered scaffold](architecture/layered-scaffold.md).
- [Performance (legacy)](performance.md) — superseded by
  [Performance](performance/README.md).
- [Security (legacy)](security.md) — superseded by
  [Security](security/README.md).
- [Licensing governance (legacy)](governance/licensing.md) — superseded by the
  F-006 section of [Security](security/README.md).
- [Corpus sizing (legacy)](functionality/corpus-sizing.md) — superseded by
  [Corpus composition](functionality/corpus-composition.md).
- [Module reference (legacy)](functionality/module-reference.md) — superseded by
  the [Code reference](reference/code-reference.md).
- [Store placeholder (legacy)](functionality/store-placeholder.md) — superseded
  by [Module anatomy](functionality/module-anatomy.md).
- [Symbol namespace (legacy)](functionality/symbol-namespace.md) — superseded by
  [Arithmetic helpers](functionality/arithmetic-helpers.md).

## Key facts at a glance

- **Scale:** 29 `.js` files, 33,105 functions, exactly 300,000 lines
  (Source: `docs/reference/corpus-evidence.md:L28-L54`; per-file motif:
  `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- **Behavior:** every `mod_<fileId>_<k>(x)` returns `6x + 10`; for example,
  `mod_0_0(4)` = `6*4 + 10` = `34`. The parity branch (`if (r % 2 === 0)`) is a
  **dead always-true branch** because `6x` is always even
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10` for the body and
  dead branch; `docs/reference/corpus-evidence.md:L67-L95` confirms this body is
  byte-identical across all 33,105 functions).
- **Structure:** 11 nominal layers under `src/` and `tests/` with **no
  inter-layer edges**
  (Source: `docs/reference/corpus-evidence.md:L177-L215` for the per-layer
  roll-up and `docs/reference/corpus-evidence.md:L112-L151` for the zero
  `require`/`import`/`export` sweep that confirms no inter-layer edges).
- **Dependencies:** zero — there is no module system, package manifest, or
  external dependency
  (Source: `docs/reference/corpus-evidence.md:L112-L151` for the zero-module
  sweep and `docs/reference/corpus-evidence.md:L234-L246` for the absence of any
  `package.json` or lockfile).
- **Naming:** "society management" is a **nominal label**, not implemented
  functionality
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1` for the per-file
  header comment; `docs/reference/corpus-evidence.md:L248-L262` for the
  corpus-wide header-comment scan).
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

- Canonical module motif (the `// mod_0 - society module` header, the inert
  `const store = []`, and the `6x + 10` function body) — Source:
  `society_mgmt_300k/src/controllers/file_0.js:L1-L10`.
- Corpus-wide counts (29 `.js` files, 33,105 functions, 300,000 lines) and the
  function body being byte-identical across all 33,105 functions — Source:
  `docs/reference/corpus-evidence.md:L28-L54` (counts) and
  `docs/reference/corpus-evidence.md:L67-L95` (body uniformity).
- Dual-license conflict (F-006) — Source: `LICENSE` (Apache-2.0) and
  `society_mgmt_300k/LICENSE/LICENSE.txt:L1` (MIT).
- Project identity and documentation entry point — Source: `README.md`.
