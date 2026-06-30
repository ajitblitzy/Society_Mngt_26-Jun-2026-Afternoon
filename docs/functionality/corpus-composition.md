# Corpus Composition (F-005)

← Back to the [documentation hub](../README.md)

## Overview

The `society_mgmt_300k` corpus is sized to an **exact, deterministic target of 300,000 lines** spread across **29 `.js` files** that together declare **33,105** `mod_*` arithmetic functions, organised into 11 nominal layers (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). This page is the per-layer roll-up of that total; for the authoritative per-file breakdown see the [file inventory](../reference/file-inventory.md), and for the layer map see the [layered scaffold](../architecture/layered-scaffold.md).

The target is hit precisely because of **two structural exceptions** to the otherwise uniform 1,200-function / 10,802-line standard module: a single *short variant*, `society_mgmt_300k/src/middleware/file_27.js` (705 functions / 6,347 lines), and a single comment-only padding file, `society_mgmt_300k/src/utils/filler.js` (0 functions / 1,999 lines) (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`). Every count on this page is a **generation-time scale fact** — it describes the size and shape of the synthetic artefact, not any runtime behaviour, throughput, or performance metric. "Society management" is only a nominal label (the repository name and a per-file header comment), not implemented domain functionality (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`). For the meaning of *short variant*, *filler*, *layer*, and *synthetic corpus*, see the [glossary](../reference/glossary.md).

## Per-layer composition

The table below rolls every one of the 29 `.js` files up to its nominal layer, with the function count and line count of each layer. All values were verified by a direct, full-corpus scan of the source branch (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). The `src/utils` row includes the comment-only `filler.js`, and the `src/middleware` row includes the short variant `file_27.js`; both are the reason their layers deviate from a clean multiple of the 1,200-function standard.

| Layer | Files | Functions | Lines |
| --- | --- | --- | --- |
| `src/config` | 2 | 2,400 | 21,604 |
| `src/middleware` | 3 | 3,105 | 27,951 |
| `src/models` | 3 | 3,600 | 32,406 |
| `src/controllers` | 3 | 3,600 | 32,406 |
| `src/routes` | 3 | 3,600 | 32,406 |
| `src/domain` | 2 | 2,400 | 21,604 |
| `src/services` | 3 | 3,600 | 32,406 |
| `src/repositories` | 2 | 2,400 | 21,604 |
| `src/utils` | 4 | 3,600 | 34,405 |
| `tests/unit` | 2 | 2,400 | 21,604 |
| `tests/integration` | 2 | 2,400 | 21,604 |
| **Totals** | **29** | **33,105** | **300,000** |

The per-layer line counts sum to exactly 300,000 and the per-layer function counts to exactly 33,105 (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). The `src/middleware` layer holds 3,105 functions rather than 3,600 solely because of the short variant `file_27.js`, and the `src/utils` layer holds 4 files rather than 3 because of the function-free `filler.js` (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`, `society_mgmt_300k/src/utils/filler.js:L1-L3`).

## How the 300,000-line target is met exactly

The corpus is built from just three file shapes, which makes the exact line target re-verifiable by hand. A **standard module file** contains 1,200 functions across 10,802 lines, and there are **27** such files (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). Adding the two exceptions to the 27 standard files closes the gap to 300,000 precisely:

- A standard file is 10,802 lines, so 27 standard files contribute 27 × 10,802 = **291,654** lines (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- Adding `file_27.js` (6,347 lines) brings the running total to **298,001** lines (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`).
- Adding `filler.js` (1,999 lines) reaches exactly **300,000** lines — the F-005 target (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`).

In a single expression, 291,654 + 6,347 + 1,999 = 300,000 lines. The function total follows the same pattern: 27 standard files × 1,200 functions = 32,400, plus 705 from `file_27.js` and 0 from `filler.js`, for a total of **33,105** functions (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`, `society_mgmt_300k/src/utils/filler.js:L1-L3`). Hitting 300,000 lines exactly — neither 299,999 nor 300,001 — is feature **F-005**, the deterministic line-sizing of the synthetic corpus.

## The `file_27.js` short variant

`society_mgmt_300k/src/middleware/file_27.js` is the corpus's only *short variant*: it declares **705 functions across 6,347 lines**, fewer than the standard 1,200 functions / 10,802 lines, while otherwise following the identical module motif — the same `// mod_27 - society module` header comment, the same inert `const store = [];`, and the same `mod_<id>_<k>(x)` function shape (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`). It is the sole reason the `src/middleware` layer totals 3,105 functions (1,200 + 1,200 + 705) rather than 3,600 (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`). For the precise definition of the term, see *short variant* in the [glossary](../reference/glossary.md).

## The comment-only `filler.js`

`society_mgmt_300k/src/utils/filler.js` contains **0 functions across 1,999 lines**, each of which is a `// filler N` comment (where `N` is an incrementing number), and it declares no symbols at all (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`). It is the line-padding file that closes the final gap to the 300,000-line target, and it is the reason the `src/utils` layer contains 4 files yet still only 3,600 functions (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`). For the anatomy of a module file and how `filler.js` differs from a function-bearing module, see [module anatomy](module-anatomy.md); for the term itself, see *filler* in the [glossary](../reference/glossary.md).

## See also

- [File inventory](../reference/file-inventory.md) — the authoritative per-file table (file → layer / function count / line count).
- [Layered scaffold](../architecture/layered-scaffold.md) — the 11-layer map and the absence of inter-layer edges.
- [Module anatomy](module-anatomy.md) — the structure of a standard module file and the `filler.js` variant.
- [Arithmetic helpers](arithmetic-helpers.md) — what each of the 33,105 `mod_*` functions computes.
- [Glossary](../reference/glossary.md) — definitions of *short variant*, *filler*, *layer*, and *synthetic corpus*.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the standard module archetype (1,200 functions / 10,802 lines) shared by 27 files; the basis for the per-layer roll-up.
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short variant (705 functions / 6,347 lines) that gives the `src/middleware` layer 3,105 functions.
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only padding file (0 functions / 1,999 lines of `// filler N`) that brings the total to exactly 300,000 lines.

All counts are corpus-wide and were verified by direct line and function counting of the source branch. For the per-file breakdown behind this per-layer roll-up, see the [file inventory](../reference/file-inventory.md).

---

← Back to the [documentation hub](../README.md)
