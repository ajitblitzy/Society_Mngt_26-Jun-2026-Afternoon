# Corpus Composition (F-005)

## Overview

The `society_mgmt_300k` codebase is a **synthetic corpus** sized to an
*exact*, deterministic target of **300,000 lines** spread across
**29** `.js` files that together declare **33,105** `mod_*` functions,
arranged in **11 nominal layers**. Hitting the line count precisely is
documented feature **F-005**: the corpus is generated so that its total
lands on 300,000 lines with no slack.
Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — direct
full-corpus scan of all 29 `.js` files establishing the 29-file,
33,105-function, 300,000-line, 11-layer totals
([file inventory](../reference/file-inventory.md#verification)); canonical
module example: society_mgmt_300k/src/controllers/file_0.js:L1-L10.

Two files are deliberate structural exceptions that make the exact
target reachable: the [short variant](../reference/glossary.md)
`file_27.js` (705 functions / 6,347 lines) and the comment-only
[filler](../reference/glossary.md) `filler.js` (0 functions /
1,999 lines). Every other file is a "standard" module of 1,200
functions / 10,802 lines.
Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10 (short
variant, 705 functions / 6,347 lines),
society_mgmt_300k/src/utils/filler.js:L1-L3 (filler, 0 functions /
1,999 lines); the 27 standard 1,200-function / 10,802-line files are
confirmed by the direct full-corpus scan
([file inventory](../reference/file-inventory.md#verification)).

These are **generation-time scale facts** — they describe the size and
shape of the artifact, not runtime behavior, throughput, or any
performance metric. For the full per-file table see
[File inventory](../reference/file-inventory.md); for the layer map see
[Layered scaffold](../architecture/layered-scaffold.md).

## Per-layer composition

The table below rolls the 29 files up by nominal layer, giving the file,
function, and line counts for each. All numbers were verified by a
direct full-corpus scan (line counting and `mod_*` function counting) of
the source branch.
Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — direct
full-corpus scan producing the per-layer file/function/line counts
([file inventory](../reference/file-inventory.md#verification)).

| Layer | Files | Functions | Lines |
| --- | ---: | ---: | ---: |
| src/config | 2 | 2,400 | 21,604 |
| src/middleware | 3 | 3,105 | 27,951 |
| src/models | 3 | 3,600 | 32,406 |
| src/controllers | 3 | 3,600 | 32,406 |
| src/routes | 3 | 3,600 | 32,406 |
| src/domain | 2 | 2,400 | 21,604 |
| src/services | 3 | 3,600 | 32,406 |
| src/repositories | 2 | 2,400 | 21,604 |
| src/utils | 4 | 3,600 | 34,405 |
| tests/unit | 2 | 2,400 | 21,604 |
| tests/integration | 2 | 2,400 | 21,604 |
| **Totals** | **29** | **33,105** | **300,000** |

Two layer rows reflect the structural exceptions: `src/utils` counts
**4** files because it includes the comment-only `filler.js` (which adds
lines but no functions), and `src/middleware` reports **3,105** rather
than 3,600 functions because its third file, `file_27.js`, is the short
variant.
Source: society_mgmt_300k/src/utils/filler.js:L1-L3,
society_mgmt_300k/src/middleware/file_27.js:L1-L10

## How the 300,000-line target is met exactly

The exact 300,000-line total (feature F-005) is the sum of three
verifiable parts — the standard files, the short variant, and the
comment-only filler:

- A **standard file** holds 1,200 functions across **10,802** lines, and
  there are **27** such files.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 — the
  canonical 1,200-function / 10,802-line standard file; the **27**-file
  count is from the direct full-corpus scan
  ([file inventory](../reference/file-inventory.md#verification)).
- 27 standard files × 10,802 lines = **291,654** lines.
- Add the short variant `file_27.js` (6,347 lines):
  291,654 + 6,347 = **298,001** lines.
  Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10
- Add the comment-only `filler.js` (1,999 lines):
  298,001 + 1,999 = **300,000** lines — the target met exactly.
  Source: society_mgmt_300k/src/utils/filler.js:L1-L3

The function total reconciles the same way: 27 standard files ×
1,200 = 32,400 functions; plus 705 from `file_27.js` and 0 from
`filler.js` gives **33,105** functions in total.
Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10,
society_mgmt_300k/src/utils/filler.js:L1-L3

## The `file_27.js` short variant

`society_mgmt_300k/src/middleware/file_27.js` is the corpus's only
[short variant](../reference/glossary.md): it declares **705 functions**
across **6,347 lines**, fewer than the standard 1,200 functions /
10,802 lines. It otherwise follows the same module motif as every other
file, opening with the header comment `// mod_27 - society module` and
the same `mod_<fileId>_<k>` arithmetic functions.
Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10

Because it is one of the three files in `src/middleware`, the short
variant is why that layer totals **3,105** functions
(1,200 + 1,200 + 705) rather than the 3,600 a layer of three standard
files would hold.
Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10

## The comment-only `filler.js`

`society_mgmt_300k/src/utils/filler.js` contains **0 functions** across
**1,999 lines**, every one of which is a `// filler N` comment. It is
pure line padding: it carries no `mod_*` functions and exists only to
close the final gap to the exact 300,000-line target. Its presence is
why `src/utils` holds **4** files yet still only 3,600 functions. For
the anatomy of this file see [Module anatomy](module-anatomy.md).
Source: society_mgmt_300k/src/utils/filler.js:L1-L3

## See also

- [File inventory](../reference/file-inventory.md) — the full per-file
  table (file → layer / function count / line count).
- [Layered scaffold](../architecture/layered-scaffold.md) — the layer
  map and the deliberate absence of inter-layer edges.
- [Module anatomy](module-anatomy.md) — the structure of a single module
  file, including `filler.js`.
- [Arithmetic helpers](arithmetic-helpers.md) — what each `mod_*`
  function computes.
- [Glossary](../reference/glossary.md) — definitions of *short variant*,
  *filler*, *layer*, and *synthetic corpus*.

## Source Citations

The counts on this page were verified by direct line and function
counting of the source branch. The primary sources are:

- `society_mgmt_300k/src/` and `society_mgmt_300k/tests/` — the direct
  full-corpus scan establishing the 29-file, 33,105-function,
  300,000-line totals, the per-layer composition, and the 27-standard /
  1-short / 1-filler split (see
  [file inventory](../reference/file-inventory.md#verification)).
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short
  variant (705 functions / 6,347 lines).
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only
  padding (0 functions / 1,999 lines).
- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the standard
  1,200-function / 10,802-line module archetype shared by 27 files.
