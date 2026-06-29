# File Inventory

## Overview

This page inventories all 29 `.js` files in the `society_mgmt_300k`
synthetic corpus, mapping each file to its nominal layer, its function
count, and its line count. Across the whole corpus the totals are
**29 files**, **33,105 functions**, and **300,000 lines**, verified by
direct line and function counting of the source branch.
Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — direct
full-corpus scan of all 29 `.js` files (reproducible commands in the
[Verification](#verification) section below).

Two files are structural exceptions to the standard module shape: the
short variant `file_27.js` (705 functions / 6,347 lines) and the
comment-only `filler.js` (0 functions / 1,999 lines). Every other file
is a "standard" module of 1,200 functions / 10,802 lines.
Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10,
society_mgmt_300k/src/utils/filler.js:L1-L3

For the per-layer roll-up and the line-target math narrative, see
[Corpus composition](../functionality/corpus-composition.md).

## Inventory table

The table below lists every `.js` file, ordered and grouped by nominal
layer. The Notes column flags the two structural exceptions; standard
files are marked with an em dash.

| Layer | File | Functions | Line count | Notes |
| --- | --- | ---: | ---: | --- |
| src/config | file_6.js | 1,200 | 10,802 | — |
| src/config | file_17.js | 1,200 | 10,802 | — |
| src/controllers | file_0.js | 1,200 | 10,802 | — |
| src/controllers | file_11.js | 1,200 | 10,802 | — |
| src/controllers | file_22.js | 1,200 | 10,802 | — |
| src/domain | file_8.js | 1,200 | 10,802 | — |
| src/domain | file_19.js | 1,200 | 10,802 | — |
| src/middleware | file_5.js | 1,200 | 10,802 | — |
| src/middleware | file_16.js | 1,200 | 10,802 | — |
| src/middleware | file_27.js | 705 | 6,347 | short variant |
| src/models | file_2.js | 1,200 | 10,802 | — |
| src/models | file_13.js | 1,200 | 10,802 | — |
| src/models | file_24.js | 1,200 | 10,802 | — |
| src/repositories | file_7.js | 1,200 | 10,802 | — |
| src/repositories | file_18.js | 1,200 | 10,802 | — |
| src/routes | file_3.js | 1,200 | 10,802 | — |
| src/routes | file_14.js | 1,200 | 10,802 | — |
| src/routes | file_25.js | 1,200 | 10,802 | — |
| src/services | file_1.js | 1,200 | 10,802 | — |
| src/services | file_12.js | 1,200 | 10,802 | — |
| src/services | file_23.js | 1,200 | 10,802 | — |
| src/utils | file_4.js | 1,200 | 10,802 | — |
| src/utils | file_15.js | 1,200 | 10,802 | — |
| src/utils | file_26.js | 1,200 | 10,802 | — |
| src/utils | filler.js | 0 | 1,999 | comment-only padding (no functions) |
| tests/integration | file_10.js | 1,200 | 10,802 | — |
| tests/integration | file_21.js | 1,200 | 10,802 | — |
| tests/unit | file_9.js | 1,200 | 10,802 | — |
| tests/unit | file_20.js | 1,200 | 10,802 | — |
| **Total** | 29 files | **33,105** | **300,000** | — |

Standard files share one 1,200-function module archetype; only the two
rows flagged in the Notes column deviate from it.
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 — the
canonical 1,200-function archetype. That 27 standard files each match it
is verified by the direct full-corpus scan ([Verification](#verification)).

## Structural exceptions

Two files deviate from the standard 1,200-function / 10,802-line module
shape:

- **`society_mgmt_300k/src/middleware/file_27.js`** — the only short
  variant: 705 functions / 6,347 lines (fewer than the standard
  1,200 / 10,802). It uses the same module motif as every other file,
  only with fewer functions.
  Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10
- **`society_mgmt_300k/src/utils/filler.js`** — the only comment-only
  file: 0 functions / 1,999 lines of `// filler N` padding, used to
  reach the exact 300,000-line corpus target.
  Source: society_mgmt_300k/src/utils/filler.js:L1-L3

## How the totals add up

The corpus totals are re-verifiable from three numbers: the standard
file size, the short variant, and the filler padding.

- **Functions:** 27 standard files × 1,200 = 32,400; then `file_27.js`
  and `filler.js` add 705 and 0, so
  32,400 + 705 + 0 = **33,105**.
- **Lines:** 27 standard files × 10,802 = 291,654; then `file_27.js`
  and `filler.js` add 6,347 and 1,999, so
  291,654 + 6,347 + 1,999 = **300,000**.
- **Files:** 27 standard + 2 exceptions = **29** `.js` files; 28 contain
  `mod_*` functions (27 standard + `file_27.js`) and 1 (`filler.js`)
  contains none.

Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (standard
archetype), society_mgmt_300k/src/middleware/file_27.js:L1-L10 (short
variant), society_mgmt_300k/src/utils/filler.js:L1-L3 (filler) — the
three module shapes. The 27 / 1 / 1 file split and the 29-file,
33,105-function, and 300,000-line totals come from the direct
full-corpus scan ([Verification](#verification)).

## Verification

The corpus-wide totals on this page are re-verifiable by a direct static
scan of the source branch. Run the following from the repository root
(the expected output is shown in each command's comment):

```bash
# .js file count -> 29
find society_mgmt_300k -name '*.js' | wc -l

# total lines across all .js files -> 300000
find society_mgmt_300k -name '*.js' -print0 | xargs -0 cat | wc -l

# total mod_<id>_<k> function declarations -> 33105
grep -rhoE 'function mod_[0-9]+_[0-9]+' \
  society_mgmt_300k --include='*.js' | wc -l

# files declaring const store = [] -> 28 (all but filler.js)
grep -rlE 'const store = \[\]' \
  society_mgmt_300k --include='*.js' | wc -l
```

These counts confirm the **29 files / 33,105 functions / 300,000 lines**
totals, the **27 standard** files (1,200 functions / 10,802 lines each),
the **short variant** `file_27.js` (705 / 6,347), and the comment-only
`filler.js` (0 / 1,999). Re-run after any corpus change to refresh the
inventory.
Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — direct
full-corpus static scan of all 29 `.js` files.

## Source Citations

The inventory counts are corpus-wide and were verified by the direct
full-corpus scan documented in the [Verification](#verification) section
(re-runnable counting commands). Primary sources:

- `society_mgmt_300k/src/` and `society_mgmt_300k/tests/` — the direct
  full-corpus scan of all 29 `.js` files that establishes the 29-file,
  33,105-function, and 300,000-line totals and the 27-standard-file
  count (see [Verification](#verification)).
- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — standard module
  archetype (the 1,200-function motif shared by 27 files).
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short
  variant (705 functions / 6,347 lines).
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — comment-only padding
  (0 functions / 1,999 lines).

For the per-layer roll-up and the 300,000-line target narrative, see
[Corpus composition](../functionality/corpus-composition.md).
