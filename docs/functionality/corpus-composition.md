# Corpus Composition (F-005)

← Back to the [documentation hub](../README.md)

## Overview

The `society_mgmt_300k` corpus is sized to an **exact, deterministic target of 300,000 lines** spread across **29 `.js` files** that together declare **33,105** `mod_*` arithmetic functions, organised into 11 nominal layers; these corpus-wide totals were verified by direct, reproducible file/line/function scans (Source: `docs/reference/corpus-evidence.md:L28-L54`) and rolled up per layer (Source: `docs/reference/corpus-evidence.md:L177-L215`). This page is the per-layer roll-up of that total; for the authoritative per-file breakdown see the [file inventory](../reference/file-inventory.md), and for the layer map see the [layered scaffold](../architecture/layered-scaffold.md).

The target is hit precisely because of **two structural exceptions** to the otherwise uniform 1,200-function / 10,802-line standard module: a single *short variant*, `society_mgmt_300k/src/middleware/file_27.js` (705 functions / 6,347 lines), and a single comment-only padding file, `society_mgmt_300k/src/utils/filler.js` (0 functions / 1,999 lines). All three file shapes — the 27 standard files, the short variant, and the comment-only padding file — are confirmed corpus-wide (Source: `docs/reference/corpus-evidence.md:L217-L232`); each exception file's own motif is also shown directly (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`, `society_mgmt_300k/src/utils/filler.js:L1-L3`). Every count on this page is a **generation-time scale fact** — it describes the size and shape of the synthetic artefact, not any runtime behaviour, throughput, or performance metric. "Society management" is only a nominal label (the repository name and a per-file header comment), not implemented domain functionality (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`). For the meaning of *short variant*, *filler*, *layer*, and *synthetic corpus*, see the [glossary](../reference/glossary.md).

## Per-layer composition

The table below rolls every one of the 29 `.js` files up to its nominal layer, with the function count and line count of each layer. All values were verified by a direct, full-corpus per-layer scan of the source branch (Source: `docs/reference/corpus-evidence.md:L177-L215`). The `src/utils` row includes the comment-only `filler.js`, and the `src/middleware` row includes the short variant `file_27.js`; both are the reason their layers deviate from a clean multiple of the 1,200-function standard.

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

The per-layer line counts sum to exactly 300,000 and the per-layer function counts to exactly 33,105 (Source: `docs/reference/corpus-evidence.md:L37-L54` for the corpus totals, `docs/reference/corpus-evidence.md:L177-L215` for the per-layer roll-up). The `src/middleware` layer holds 3,105 functions rather than 3,600 solely because of the short variant `file_27.js`, and the `src/utils` layer holds 4 files rather than 3 because of the function-free `filler.js`; both file shapes are confirmed corpus-wide (Source: `docs/reference/corpus-evidence.md:L217-L232`) and shown directly in each file's motif (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`, `society_mgmt_300k/src/utils/filler.js:L1-L3`).

## How the 300,000-line target is met exactly

The corpus is built from just three file shapes, which makes the exact line target re-verifiable by hand. A **standard module file** contains 1,200 functions across 10,802 lines, and there are **27** such files; the standard shape, the short variant, and the comment-only file — together with their exact counts — are confirmed corpus-wide (Source: `docs/reference/corpus-evidence.md:L217-L232`). The single-file motif of a standard module is shown directly (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). Adding the two exceptions to the 27 standard files closes the gap to 300,000 precisely:

- A standard file is 10,802 lines, so 27 standard files contribute 27 × 10,802 = **291,654** lines (Source: `docs/reference/corpus-evidence.md:L217-L232`).
- Adding `file_27.js` (6,347 lines) brings the running total to **298,001** lines (Source: `docs/reference/corpus-evidence.md:L217-L232`; file motif: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`).
- Adding `filler.js` (1,999 lines) reaches exactly **300,000** lines — the F-005 target (Source: `docs/reference/corpus-evidence.md:L217-L232`; file motif: `society_mgmt_300k/src/utils/filler.js:L1-L3`).

In a single expression, 291,654 + 6,347 + 1,999 = 300,000 lines, matching the verified corpus line total (Source: `docs/reference/corpus-evidence.md:L37-L45`). The function total follows the same pattern: 27 standard files × 1,200 functions = 32,400, plus 705 from `file_27.js` and 0 from `filler.js`, for a total of **33,105** functions (Source: `docs/reference/corpus-evidence.md:L217-L232` for the per-file counts, `docs/reference/corpus-evidence.md:L47-L54` for the verified corpus function total). Hitting 300,000 lines exactly — neither 299,999 nor 300,001 — is feature **F-005**, the deterministic line-sizing of the synthetic corpus.

## The `file_27.js` short variant

`society_mgmt_300k/src/middleware/file_27.js` is the corpus's only *short variant*: it declares **705 functions across 6,347 lines**, fewer than the standard 1,200 functions / 10,802 lines, while otherwise following the identical module motif — the same `// mod_27 - society module` header comment, the same inert `const store = [];`, and the same `mod_<id>_<k>(x)` function shape. Its own header and motif are shown directly (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`), while the 705-function / 6,347-line count and its status as the sole short variant are confirmed by the corpus-wide file-shape scan (Source: `docs/reference/corpus-evidence.md:L217-L232`). It is the sole reason the `src/middleware` layer totals 3,105 functions (1,200 + 1,200 + 705) rather than 3,600 (Source: `docs/reference/corpus-evidence.md:L177-L215`). For the precise definition of the term, see *short variant* in the [glossary](../reference/glossary.md).

## The comment-only `filler.js`

`society_mgmt_300k/src/utils/filler.js` contains **0 functions across 1,999 lines**, each of which is a `// filler N` comment (where `N` is an incrementing number), and it declares no symbols at all. A representative window of the `// filler N` motif is shown directly (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`), while its full-file shape — 1,999 lines, 0 functions, and no `// mod_N - society module` header — is confirmed by the corpus-wide file-shape and header scans (Source: `docs/reference/corpus-evidence.md:L217-L232`, `docs/reference/corpus-evidence.md:L248-L262`). It is the line-padding file that closes the final gap to the 300,000-line target, and it is the reason the `src/utils` layer contains 4 files yet still only 3,600 functions (Source: `docs/reference/corpus-evidence.md:L177-L215`). For the anatomy of a module file and how `filler.js` differs from a function-bearing module, see [module anatomy](module-anatomy.md); for the term itself, see *filler* in the [glossary](../reference/glossary.md).

## See also

- [File inventory](../reference/file-inventory.md) — the authoritative per-file table (file → layer / function count / line count).
- [Layered scaffold](../architecture/layered-scaffold.md) — the 11-layer map and the absence of inter-layer edges.
- [Module anatomy](module-anatomy.md) — the structure of a standard module file and the `filler.js` variant.
- [Arithmetic helpers](arithmetic-helpers.md) — what each of the 33,105 `mod_*` functions computes.
- [Glossary](../reference/glossary.md) — definitions of *short variant*, *filler*, *layer*, and *synthetic corpus*.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the standard module archetype (the single-file **motif**: header comment, `const store = []`, and a `mod_<id>_<k>(x)` block). That this 1,200-function / 10,802-line shape is shared by **27 standard files** is established corpus-wide by `docs/reference/corpus-evidence.md:L217-L232`, not by this one file alone.
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short variant's header and motif; its 705-function / 6,347-line count is confirmed corpus-wide in `docs/reference/corpus-evidence.md:L217-L232`.
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only padding motif (`// filler N`); its 0-function / 1,999-line count is confirmed corpus-wide in `docs/reference/corpus-evidence.md:L217-L232`.
- `docs/reference/corpus-evidence.md:L28-L262` — the reproducible scans (file/line/function counts, per-layer roll-up, file shapes, and the header scan) that substantiate every corpus-wide count and the 300,000-line arithmetic on this page.

All counts are corpus-wide and were verified by direct, reproducible line and function scans recorded on the [corpus evidence](../reference/corpus-evidence.md) page (Source: `docs/reference/corpus-evidence.md:L28-L262`). For the per-file breakdown behind this per-layer roll-up, see the [file inventory](../reference/file-inventory.md).

---

← Back to the [documentation hub](../README.md)
