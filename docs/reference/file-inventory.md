# File Inventory

← Back to the [documentation hub](../README.md)

## Overview

This page is the authoritative file-level inventory of the synthetic `society_mgmt_300k` JavaScript corpus. It maps every one of the **29 `.js` files** to its nominal layer, its function count, and its line count, so any structural claim about the corpus is traceable to a specific file. In total the corpus comprises **29 files**, **33,105 functions**, and **300,000 lines** — a deterministic, reproducible size rather than an incidental one.

Two files are structural exceptions to the otherwise uniform 1,200-function / 10,802-line standard module: `society_mgmt_300k/src/middleware/file_27.js` is a *short variant* with only 705 functions / 6,347 lines (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`), and `society_mgmt_300k/src/utils/filler.js` is *comment-only padding* with 0 functions / 1,999 lines (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`). For the per-layer roll-up and the line-target math narrative, see [Corpus sizing](../functionality/corpus-sizing.md).

## Inventory table

The table lists all 29 `.js` files grouped by nominal layer, with the function count and line count of each. Standard module files share an identical 1,200-function / 10,802-line shape; the two exceptions are flagged in the **Notes** column.

| Layer | File | Functions | Line count | Notes |
| --- | --- | --- | --- | --- |
| `src/config` | `file_6.js` | 1,200 | 10,802 | — |
| `src/config` | `file_17.js` | 1,200 | 10,802 | — |
| `src/controllers` | `file_0.js` | 1,200 | 10,802 | — |
| `src/controllers` | `file_11.js` | 1,200 | 10,802 | — |
| `src/controllers` | `file_22.js` | 1,200 | 10,802 | — |
| `src/domain` | `file_8.js` | 1,200 | 10,802 | — |
| `src/domain` | `file_19.js` | 1,200 | 10,802 | — |
| `src/middleware` | `file_5.js` | 1,200 | 10,802 | — |
| `src/middleware` | `file_16.js` | 1,200 | 10,802 | — |
| `src/middleware` | `file_27.js` | 705 | 6,347 | short variant |
| `src/models` | `file_2.js` | 1,200 | 10,802 | — |
| `src/models` | `file_13.js` | 1,200 | 10,802 | — |
| `src/models` | `file_24.js` | 1,200 | 10,802 | — |
| `src/repositories` | `file_7.js` | 1,200 | 10,802 | — |
| `src/repositories` | `file_18.js` | 1,200 | 10,802 | — |
| `src/routes` | `file_3.js` | 1,200 | 10,802 | — |
| `src/routes` | `file_14.js` | 1,200 | 10,802 | — |
| `src/routes` | `file_25.js` | 1,200 | 10,802 | — |
| `src/services` | `file_1.js` | 1,200 | 10,802 | — |
| `src/services` | `file_12.js` | 1,200 | 10,802 | — |
| `src/services` | `file_23.js` | 1,200 | 10,802 | — |
| `src/utils` | `file_4.js` | 1,200 | 10,802 | — |
| `src/utils` | `file_15.js` | 1,200 | 10,802 | — |
| `src/utils` | `file_26.js` | 1,200 | 10,802 | — |
| `src/utils` | `filler.js` | 0 | 1,999 | comment-only padding (no functions) |
| `tests/integration` | `file_10.js` | 1,200 | 10,802 | — |
| `tests/integration` | `file_21.js` | 1,200 | 10,802 | — |
| `tests/unit` | `file_9.js` | 1,200 | 10,802 | — |
| `tests/unit` | `file_20.js` | 1,200 | 10,802 | — |
| **Total** | **29 files** | **33,105** | **300,000** | — |

Every standard file shares the same 1,200-function / 10,802-line archetype, verified against the canonical module file (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`); the two exceptions are detailed in the next section.

## Structural exceptions

Only two files deviate from the standard 1,200-function / 10,802-line module shape:

- `society_mgmt_300k/src/middleware/file_27.js` — the only **short variant**: 705 functions / 6,347 lines (fewer than the standard 1,200 / 10,802). It is the sole reason the `middleware` layer totals 3,105 functions rather than 3,600. Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`
- `society_mgmt_300k/src/utils/filler.js` — the only **comment-only** file: 0 functions / 1,999 lines of `// filler N` padding used to reach the exact 300,000-line target. It is counted among the 29 `.js` files but contributes no functions. Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`

## How the totals add up

The inventory is re-verifiable from a small amount of arithmetic over the three file shapes:

- **Functions:** 27 standard files × 1,200 = 32,400; plus `file_27.js` 705 and `filler.js` 0 = **33,105 functions**.
- **Lines:** 27 standard files × 10,802 = 291,654; plus `file_27.js` 6,347 and `filler.js` 1,999 = **300,000 lines**.
- **Files:** 27 standard plus `file_27.js` plus `filler.js` = **29 `.js` files** — 28 of which contain `mod_*` functions, while `filler.js` contains none.

Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`, `society_mgmt_300k/src/middleware/file_27.js:L1-L10`, `society_mgmt_300k/src/utils/filler.js:L1-L3`

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the standard module archetype (header comment, the `const store = []` placeholder, and the `mod_<id>_<k>(x)` function block) defining the uniform 1,200-function / 10,802-line shape shared by 27 files.
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short variant (705 functions / 6,347 lines).
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only padding file (0 functions / 1,999 lines of `// filler N`).

All counts are corpus-wide and were verified by direct line and function counting of the source branch. For the per-layer roll-up and the deterministic line-target arithmetic, see [Corpus sizing](../functionality/corpus-sizing.md).

---

← Back to the [documentation hub](../README.md)
