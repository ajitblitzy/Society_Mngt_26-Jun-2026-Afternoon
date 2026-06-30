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
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1` for the per-file header
comment; `docs/reference/corpus-evidence.md:L248-L262` for the corpus-wide
header-comment scan showing the label appears only in module headers).

The scaffold is **dependency-free**. There is **no module system** and there are
**no inter-layer edges**: no file imports, requires, or exports another, so every
symbol is file-local and no layer depends on any other
(Source: `docs/reference/corpus-evidence.md:L112-L151` for the zero
`require`/`import`/`export`/`module.exports` sweep that confirms no module system
and no inter-layer edges, and `docs/reference/corpus-evidence.md:L234-L246` for
the absence of any package manifest that makes the scaffold dependency-free).
Terminology used
across this area — *layer*, *synthetic corpus*, *dead branch*, and *short variant*
— is defined once in the [glossary](../reference/glossary.md) and is not redefined
here.

## Scaffold at a glance

- **11 nominal layers** — nine under `src/` (config, middleware, models,
  controllers, routes, domain, services, repositories, utils) and two under
  `tests/` (unit, integration); the names are nominal and each layer contains only
  `mod_<id>_<k>(x)` arithmetic stubs
  (Source: `docs/reference/corpus-evidence.md:L177-L215` for the per-layer
  composition of all 11 layers and `docs/reference/corpus-evidence.md:L67-L95`
  for the byte-identical arithmetic bodies; per-file header motif:
  `society_mgmt_300k/src/controllers/file_0.js:L1`).
- **29 `.js` files / 33,105 `mod_*` functions / 300,000 lines** in total; the
  authoritative per-layer file / function / line table lives in
  [Corpus composition](../functionality/corpus-composition.md), and every layer
  repeats the same single-file archetype
  (Source: `docs/reference/corpus-evidence.md:L28-L54` for the 29-file /
  33,105-function / 300,000-line totals and
  `docs/reference/corpus-evidence.md:L177-L215` for the per-layer roll-up;
  `society_mgmt_300k/src/controllers/file_0.js:L1-L10` for the single-file
  archetype).
- **No inter-layer dependencies and no module system** — zero
  `require` / `import` / `export` / `module.exports` occurrences across the corpus,
  so symbols are file-local and no layer imports another
  (Source: `docs/reference/corpus-evidence.md:L112-L151`).
- **Every function returns `6x + 10`** — each `mod_<id>_<k>(x)` accumulates
  `x*1 + x*2 + x*3` (= `6x`) and adds `10` when the accumulator is even; because
  `6x` is always even the parity branch is a **dead always-true branch**, so, for
  example, `mod_0_0(4) === 34`
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10` for the body and
  dead branch; `docs/reference/corpus-evidence.md:L67-L95` confirms this body is
  byte-identical across all 33,105 functions).

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
  `// mod_0 - society module` (per-file motif). The corpus-wide nominal-layer
  scaffold and the claim that *"society management"* is a label rather than
  implemented functionality are substantiated by
  `docs/reference/corpus-evidence.md:L177-L215` (per-layer composition) and
  `docs/reference/corpus-evidence.md:L248-L262` (header-comment scan).
- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical module motif
  (header comment, inert `store`, and the `mod_<id>_<k>(x)` body). The corpus-wide
  counts are substantiated by `docs/reference/corpus-evidence.md:L28-L54` and the
  per-layer roll-up by `docs/reference/corpus-evidence.md:L177-L215`; the
  no-module-system claim by `docs/reference/corpus-evidence.md:L112-L151`.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the `6x + 10` arithmetic
  body and the dead always-true parity branch (for example, `mod_0_0(4) === 34`).

---

← Back to the [documentation hub](../README.md)
