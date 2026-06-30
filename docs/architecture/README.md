# Architecture

← Back to the [documentation hub](../README.md)

## Overview

This is the **architecture index** for the synthetic
[`society_mgmt_300k`](../overview.md) *corpus*. The corpus is organized as a
**layered folder scaffold** of **11 nominal layers** — nine under `src/` (config,
middleware, models, controllers, routes, domain, services, repositories, utils)
and two under `tests/` (unit, integration) — holding **29 `.js` files**,
**33,105** `mod_*` functions, and **300,000 lines** in total
(Source: `docs/reference/corpus-evidence.md:L28-L54`). Every file follows a single
canonical module motif (Source:
`society_mgmt_300k/src/controllers/file_0.js:L1-L10`), and the layers carry **no
inter-layer edges**: a source-corpus keyword sweep over `society_mgmt_300k/**/*.js`
finds zero `require`/`import`/`export`/`module.exports` occurrences
(Source: `docs/reference/corpus-evidence.md:L112-L151`).

## Pages in this area

- [Layered scaffold (F-003)](layered-scaffold.md) — the 11 nominal layers, the
  per-layer file / function / line composition, the deliberate absence of
  inter-layer edges, and the layer-map Mermaid diagram.
- [Module control flow](module-control-flow.md) — the step-by-step execution of a
  single `mod_<id>_<k>(x)` function, the dead always-true parity branch, and the
  control-flow Mermaid diagram.

## See also

- [Overview](../overview.md) — what the corpus is and what it is not.
- [Corpus composition](../functionality/corpus-composition.md) — the per-layer
  sizing roll-up and the deterministic 300,000-line arithmetic.
- [File inventory](../reference/file-inventory.md) — the per-file table.
- [Corpus evidence](../reference/corpus-evidence.md) — the reproducible scans
  behind the corpus-wide counts and the keyword sweep cited above.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical module
  motif (header comment, inert `store`, and the `mod_<id>_<k>(x)` body); the
  single-file archetype shared across the scaffold.
- `docs/reference/corpus-evidence.md:L28-L262` — the reproducible scans behind the
  29-file / 33,105-function / 300,000-line counts, the per-layer roll-up, and the
  source-corpus keyword sweep confirming no module system and no inter-layer edges.

---

← Back to the [documentation hub](../README.md)
