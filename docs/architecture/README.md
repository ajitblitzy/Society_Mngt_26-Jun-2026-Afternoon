# Architecture

## Overview

This area documents the **structure** of the `society_mgmt_300k`
corpus: its 11-layer nominal scaffold (feature **F-003**) and the
per-function control flow that every `mod_<id>_<k>(x)` follows,
including its dead always-true parity branch. The codebase is a
**synthetic, dependency-free** JavaScript scaffold — its folders are
named after conventional application tiers (config, middleware,
models, controllers, routes, domain, services, repositories, utils,
plus `tests/unit` and `tests/integration`), yet each layer holds
nothing but single-argument arithmetic stubs. The layers are therefore
**nominal only**, and "society management" is likewise a **label**: it
appears solely as the repository name and a per-file header comment
such as `// mod_0 - society module`, never as implemented domain
functionality.
Source: society_mgmt_300k/src/controllers/file_0.js:L1

The scaffold has **no inter-layer edges and no module system**: a
whole-tree sweep finds zero `require`, `import`, `export`, and
`module.exports`, so every symbol is file-local and no layer imports
another. There is no request pipeline, dependency injection, routing
table, or persistence to document — only the uniform `mod_*` archetype
replicated across all layers. This area is intentionally faithful: it
describes the structure exactly as it exists and does **not** infer or
fabricate relationships, pipelines, services, or service levels that
the code does not contain.
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

## Scaffold at a glance

- **11 nominal layers** — nine under `src/` (config, middleware,
  models, controllers, routes, domain, services, repositories, utils)
  and two under `tests/` (unit, integration), each named like an
  application tier but containing only arithmetic stubs.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1
- **29 `.js` files / 33,105 `mod_<fileId>_<k>` functions / exactly
  300,000 lines** across the whole corpus. See
  [Corpus composition](../functionality/corpus-composition.md) for the
  authoritative per-layer file/function/line table.
  Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — direct
  full-corpus scan of all 29 `.js` files.
- **No inter-layer dependencies** — with no module system anywhere in
  the corpus, no file imports or references another, so the layer map
  renders as isolated nodes with no connecting edges.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10
- **Every function returns `6x + 10`** — each `mod_<id>_<k>(x)`
  accumulates `x*1 + x*2 + x*3` (= `6x`) and then adds `10` on an
  always-true parity test, so for example `mod_0_0(4) === 34`.
  Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## In this area

- **[Layered scaffold](layered-scaffold.md)** — F-003: the 11 nominal
  layers, each layer's nominal role versus its stub-only actual
  content, and the layer-map diagram rendered as isolated nodes with
  no inter-layer edges.
- **[Module control flow](module-control-flow.md)** — the step-by-step
  execution of any `mod_<id>_<k>(x)`, with the dead always-true parity
  branch annotated and a control-flow diagram.

## Related documentation

- [Overview](../overview.md) — the system overview and what this
  corpus is and is **not**.
- [Corpus composition](../functionality/corpus-composition.md) — the
  per-layer file/function/line counts and the 300,000-line math.
- [Functionality catalog](../functionality/README.md) — the F-001
  through F-006 feature index.
- [Glossary](../reference/glossary.md) — definitions of *layer*,
  *synthetic corpus*, *short variant*, *dead always-true branch*, and
  the other terminology used here.
- [Documentation home](../README.md) — the top-level documentation hub.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1` — the per-file
  header comment (the nominal "society module" label) that establishes
  the layered scaffold's naming.
- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical
  module motif (header comment, inert `store`, and a `mod_*` function)
  reproduced uniformly across every layer; the counts archetype and the
  evidence that no module system is present.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the function
  body that yields the `6x + 10` behavior shared by all 33,105
  functions.
- `society_mgmt_300k/src/` and `society_mgmt_300k/tests/` — the direct
  full-corpus scan establishing the 29-file / 33,105-function /
  300,000-line totals; the authoritative per-layer breakdown lives in
  [Corpus composition](../functionality/corpus-composition.md).
