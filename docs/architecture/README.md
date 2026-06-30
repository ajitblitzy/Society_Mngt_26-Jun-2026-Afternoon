# Architecture

← Back to the [documentation hub](../README.md)

## Overview

This is the **architecture area index** for the synthetic
[`society_mgmt_300k`](../overview.md) *corpus*. It documents the **structure** of
the corpus: its **11-layer nominal scaffold** (feature F-003) and the
**per-function control flow** of a single `mod_<id>_<k>(x)` helper, including the
dead always-true parity branch. The corpus is a **layered folder scaffold** whose
layer names are borrowed from conventional web-application architecture, yet every
folder holds **only arithmetic stubs** with no behavior specific to its nominal
role. *"Society management"* is a **label**: it appears solely as the repository
name and as a per-file header comment such as `// mod_0 - society module`
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).

The scaffold is **dependency-free**. There is **no module system** and there are
**no inter-layer edges**: no file imports, requires, or exports another, so every
symbol is file-local and no layer depends on any other
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). Terminology used
across this area — *layer*, *synthetic corpus*, *dead branch*, and *short variant*
— is defined once in the [glossary](../reference/glossary.md) and is not redefined
here.

## Scaffold at a glance

- **11 nominal layers** — nine under `src/` (config, middleware, models,
  controllers, routes, domain, services, repositories, utils) and two under
  `tests/` (unit, integration); the names are nominal and each layer contains only
  `mod_<id>_<k>(x)` arithmetic stubs
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).
- **29 `.js` files / 33,105 `mod_*` functions / 300,000 lines** in total; the
  authoritative per-layer file / function / line table lives in
  [Corpus composition](../functionality/corpus-composition.md), and every layer
  repeats the same single-file archetype
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- **No inter-layer dependencies and no module system** — zero
  `require` / `import` / `export` / `module.exports` occurrences across the corpus,
  so symbols are file-local and no layer imports another
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- **Every function returns `6x + 10`** — each `mod_<id>_<k>(x)` accumulates
  `x*1 + x*2 + x*3` (= `6x`) and adds `10` when the accumulator is even; because
  `6x` is always even the parity branch is a **dead always-true branch**, so, for
  example, `mod_0_0(4) === 34`
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).

## In this area

- **[Layered scaffold](layered-scaffold.md)** — F-003: the 11 nominal layers, the
  per-layer composition, and the layer-map diagram that renders the layers as
  isolated nodes with no inter-layer edges.
- **[Module control flow](module-control-flow.md)** — the step-by-step execution of
  any `mod_<id>_<k>(x)`, with the dead always-true parity branch annotated in a
  control-flow diagram.

## Related documentation

- [Overview](../overview.md) — the system overview: what the corpus is and what it
  is **not**.
- [Corpus composition](../functionality/corpus-composition.md) — the authoritative
  per-layer file / function / line counts and the deterministic 300,000-line math.
- [Functionality catalog](../functionality/README.md) — the F-001 through F-006
  feature catalog.
- [Glossary](../reference/glossary.md) — definitions of *layer*, *synthetic
  corpus*, *dead branch*, and *short variant*.
- [Documentation hub](../README.md) — the top-level documentation index.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1` — the canonical header comment
  `// mod_0 - society module`; the basis for the nominal-layer scaffold and the
  evidence that *"society management"* is a label rather than implemented
  functionality.
- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical module motif
  (header comment, inert `store`, and the `mod_<id>_<k>(x)` body); the single-file
  archetype from which the corpus-wide counts are composed and the basis for the
  no-module-system claim.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the `6x + 10` arithmetic
  body and the dead always-true parity branch (for example, `mod_0_0(4) === 34`).

---

← Back to the [documentation hub](../README.md)
