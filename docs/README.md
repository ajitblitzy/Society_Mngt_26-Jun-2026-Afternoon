# Documentation

This is the documentation index for the **`society_mgmt_300k`** corpus and the
navigation hub for everything under `docs/`. Start here and follow the links
below to the topic you need; every other document links back to this index.

## What this corpus is

`society_mgmt_300k` is a **synthetic JavaScript corpus** — a deterministically
generated body of code rather than a runnable product. It comprises
**300,000 lines** across **29 `.js` files** that together define
**33,105 functions**, where every function is byte-identical and computes the
same expression, **`6x + 10`**, for an integer input `x`. The files are arranged
into a nominal layered *scaffold* (nine `src` layers plus `tests`), but the
corpus is **not a runnable application**: it exports no public API (zero
`module.exports` / `require` occurrences), and there is no framework, server,
database, network access, or external dependency. This documentation uses an
honest **verified-absence** framing — capabilities the code does not have are
reported as verified absences rather than implied. For the full narrative, see
the [System overview](./overview.md).

## Documentation map

Begin with the overview, then open the area you need. All fourteen documents are
listed below.

### Overview & architecture

- [System overview](./overview.md) — what this corpus is and what it is not.
- [Architecture](./architecture.md) — the nominal layered *scaffold* and an
  edge-less containment diagram showing the absence of inter-layer wiring.

### Functionality

- [Functionality index](./functionality/README.md) — entry point for the
  functionality topics below.
- [Arithmetic helpers (F-001)](./functionality/arithmetic-helpers.md) — the
  *representative function* contract `mod_<fileId>_<k>(x) → 6x + 10`.
- [Symbol namespace (F-002)](./functionality/symbol-namespace.md) — the
  `mod_<fileId>_<k>` naming scheme and its uniqueness.
- [Module reference](./functionality/module-reference.md) — the per-layer
  inventory of all 29 files and their function counts.
- [Store placeholder (F-004)](./functionality/store-placeholder.md) — the unused
  module-scoped `const store = []` declaration.
- [Corpus sizing (F-005)](./functionality/corpus-sizing.md) — the deterministic
  300,000-line composition.

### Reference

- [Function reference](./reference/function-reference.md) — the authoritative
  `mod_<fileId>_<k>(x) → 6x + 10` signature, behavior, parameters/return, and
  the dead always-true parity branch.
- [Source layout](./reference/source-layout.md) — the exhaustive per-layer
  inventory of all 29 files, 33,105 functions, and exactly 300,000 lines.
- [Glossary](./glossary.md) — definitions of `mod_*`, `store`, `filler`,
  synthetic corpus, dead branch, and nominal layer.

### Performance & security

- [Performance](./performance.md) — constant-time `O(1)` per call, the dead
  always-true parity branch, and corpus scale.
- [Security](./security.md) — the verified-absence security posture and an
  operational note on setup-instruction secrets.

### Governance

- [Licensing (F-006)](./governance/licensing.md) — the Apache-vs-MIT license
  inconsistency and a recommended single-license resolution.

## Documentation conventions

Every document in this tree follows the same conventions:

- **Source citations on every claim** — each technical statement cites a code
  `path:line` or a Technical Specification section, so any reader can trace it
  back to verifiable evidence.
- **Honest verified-absence framing** — features the corpus does not have are
  reported as verified absences; no capabilities, SLAs, or dependencies are
  implied or fabricated.
- **Mermaid diagrams** — diagrams are written as fenced `mermaid` blocks and
  render natively on GitHub, so **no build step is required** to read this
  documentation.

## Source citations

- Representative function body computing `6x + 10` (byte-identical across the
  corpus) — Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`;
  AAP §0.3.1.
- 300,000 lines / 29 `.js` files / 33,105 functions, arranged in the layered
  *scaffold* — Source: first-hand repository scan; AAP §0.3.1.
- Not a runnable application — no exported API (0 `module.exports` / `require`),
  no framework, server, database, or network, and no dependencies — Source:
  first-hand repository scan; AAP §0.2.2.
