# Source layout

This page is the exhaustive structural inventory of the repository — the map
that enumerates every directory, file, function, and line, and shows how the
per-layer counts reconcile to the corpus totals. For terminology, see the
[glossary](../glossary.md); for the behavior of the functions listed here, see
the [function reference](function-reference.md).

## Overview

The repository is a [synthetic corpus](../glossary.md) of **29 files**,
**33,105 functions**, and **exactly 300,000 lines** of plain JavaScript,
organized into nine [nominal](../glossary.md) `src` layers plus two `tests`
directories `[Technical Specification §1.2.2]`. The layer names (`controllers`,
`services`, `repositories`, and so on) are a naming convention only: there is
no business logic behind them, and every file contains the same family of
[`mod_*`](../glossary.md) arithmetic helpers, built from one canonical pattern —
a header comment on line 1, an inert `const store = [];` on line 2, and a
sequence of `mod_<fileId>_<k>(x)` functions thereafter
`[society_mgmt_300k/src/config/file_6.js:L1-L10]`. Because the layering is
nominal, no module imports, exports, or calls another, and the `tests`
directories hold the same helpers rather than executable tests
`[Technical Specification §1.2.2]`.

## Inventory by layer

The table below lists every directory under `society_mgmt_300k/` with its file,
function, and line counts. The **Total** row reconciles exactly to
**29 files / 33,105 functions / 300,000 lines**
`[Technical Specification §1.2.2]`.

| Directory (`society_mgmt_300k/`) | Files | Functions | Lines |
| --- | ---: | ---: | ---: |
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
| **Total** | **29** | **33,105** | **300,000** |

Every `src` directory shares the identical canonical module pattern, documented
in the [module pattern](../architecture.md#layered-scaffold) page; only the two
anomalies described under [Special cases](#special-cases) — `file_27.js` and
`filler.js` — deviate from it, which is why a naive "every file has 1,200
functions" estimate would not reconcile `[Technical Specification §1.2.2]`.

## File listing

The map below names each file in each directory; all files are `.js`. Two files
are flagged because they break the standard shape: the short variant
`file_27.js` and the comment-only padding file `filler.js`, both detailed under
[Special cases](#special-cases).

| Directory (`society_mgmt_300k/`) | Files |
| --- | --- |
| `src/config` | `file_6.js`, `file_17.js` |
| `src/middleware` | `file_5.js`, `file_16.js`, `file_27.js` (short variant) |
| `src/models` | `file_2.js`, `file_13.js`, `file_24.js` |
| `src/controllers` | `file_0.js`, `file_11.js`, `file_22.js` |
| `src/routes` | `file_3.js`, `file_14.js`, `file_25.js` |
| `src/domain` | `file_8.js`, `file_19.js` |
| `src/services` | `file_1.js`, `file_12.js`, `file_23.js` |
| `src/repositories` | `file_7.js`, `file_18.js` |
| `src/utils` | `file_4.js`, `file_15.js`, `file_26.js`, `filler.js` (comment-only) |
| `tests/unit` | `file_9.js`, `file_20.js` |
| `tests/integration` | `file_10.js`, `file_21.js` |

This file-to-directory mapping was confirmed by a first-hand scan of the
repository tree `[Technical Specification §1.2.2]`.

## Special cases

Four observations explain why the per-layer numbers in the inventory are not
uniform, and one records an expected-but-absent artifact. Each is cited to its
source.

### Short variant: file_27.js

`society_mgmt_300k/src/middleware/file_27.js` follows the same canonical pattern
(header comment, inert `const store = [];`, and `mod_27_*` functions) but
defines only **705 functions** across **6,347 lines**, rather than the usual
1,200 functions / 10,802 lines. This single short file is why `src/middleware`
totals **3,105 functions** — that is, `2 × 1,200 + 705` — instead of 3,600
`[society_mgmt_300k/src/middleware/file_27.js]` `[Technical Specification §1.2.2]`.

### Comment-only padding: filler.js

`society_mgmt_300k/src/utils/filler.js` is comment-only padding: it contains
**0 functions** and **1,999 lines**, every line of the form `// filler NNNNNN`,
spanning `// filler 298001` through `// filler 299999`. Its sole purpose is to
pad the corpus to exactly 300,000 lines. This is why `src/utils` lists **4
files** yet contributes the same **3,600 functions** as a three-file layer, and
why its line total (**34,405**) sits exactly **1,999** above a standard
three-file layer's 32,406 `[society_mgmt_300k/src/utils/filler.js]`
`[Technical Specification §1.2.2]`.

### Standard file size

A typical full file holds **1,200 functions** and **10,802 lines**: two prefix
lines (the header comment on line 1 and `const store = [];` on line 2) followed
by 1,200 nine-line function blocks, i.e. `2 + 9 × 1,200 = 10,802`
`[society_mgmt_300k/src/config/file_6.js:L1-L10]`. The same formula gives the
short variant's size, `2 + 9 × 705 = 6,347`
`[society_mgmt_300k/src/middleware/file_27.js]`.

### Test directories are fixtures, not executable tests

`tests/unit` and `tests/integration` contain the same `mod_*` functions as the
`src` layers, with no assertions and no test-runner hooks — they are generated
fixtures, not runnable tests `[Technical Specification §1.2.2]`.

### No configuration object in src/config

Despite its name, `src/config` contains only `mod_*` helpers; there is no
configuration file, settings object, or environment schema to document
`[Technical Specification §1.2.2]`.

## How the totals reconcile

Reading down each column of the inventory confirms the corpus totals. The 29
files split into 27 standard files (1,200 functions / 10,802 lines each), the
short variant `file_27.js` (705 functions / 6,347 lines), and the comment-only
`filler.js` (0 functions / 1,999 lines):

```text
Files:      2 + 3 + 3 + 3 + 3 + 2 + 3 + 2 + 4 + 2 + 2              =      29
Functions:  27 standard × 1,200  +  file_27.js (705)  +  filler.js (0)   =  33,105
Lines:      27 standard × 10,802 +  filler.js (1,999) +  file_27.js (6,347) = 300,000
```

That is, `27 × 1,200 + 705 = 33,105` functions and
`27 × 10,802 + 1,999 + 6,347 = 300,000` lines across all 29 files. Every count
above is reproducible with `wc -l` and a function-signature scan, so the
inventory can be trusted exactly `[Technical Specification §1.2.2]`.

## Related documentation

- [← Documentation Home](../README.md)
- [Function reference](function-reference.md) — the behavior of the `mod_*` functions inventoried here.
- [Architecture overview](../architecture.md) — how the layers relate, and why there are no runtime edges between them.
- [Module pattern](../architecture.md#layered-scaffold) — the canonical file shape shared by every module.
- [Glossary](../glossary.md) — definitions of `mod_*`, `store`, `filler`, synthetic corpus, and nominal layer.
