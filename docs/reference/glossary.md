# Glossary

← Back to the [documentation hub](../README.md)

## Overview

This glossary defines the vocabulary used across the **`society_mgmt_300k`**
documentation so that terminology stays consistent from one page to the next.
Every term below is drawn from the verified source *corpus* and is recorded with
its exact, code-confirmed meaning rather than any assumed domain definition.

## Terms

The terms are listed alphabetically. Each definition that asserts a code fact
carries an inline `Source:` citation. Single-function behavior is cited to the
canonical file `society_mgmt_300k/src/controllers/file_0.js`; corpus-wide facts
(counts, name uniqueness, `store` usage, and the module-keyword sweep) are cited
to the reproducible scans on the [corpus evidence](corpus-evidence.md) page.

- **dead (always-true) branch** — the conditional `if (r % 2 === 0) { r += 10 }`
  that appears inside every `mod_*` function. The accumulator `r` is built up as
  `r += x*1; r += x*2; r += x*3`, so it always equals `6x`, which is **always
  even**. The parity test is therefore **always true**, the `+ 10` is **always
  applied**, and the implicit false path is **unreachable** (dead). As a result,
  every function effectively returns `6x + 10`. The branch is shown in the
  canonical body (Source: `society_mgmt_300k/src/controllers/file_0.js:L4-L10`),
  and all 33,105 functions share that one byte-identical body
  (Source: `docs/reference/corpus-evidence.md:L67-L95`).
- **deterministic** — describes a function whose output is fully determined by its
  inputs: calling a `mod_*` function with the same `x` always yields the same
  result, with no dependence on time, randomness, or external state. Each function
  computes `6x + 10` from `x` alone
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`); because all
  33,105 bodies are byte-identical, this holds corpus-wide
  (Source: `docs/reference/corpus-evidence.md:L67-L95`).
- **filler** — comment-only padding lines of the form `// filler N` (where `N` is
  an incrementing number) used to pad a file toward the corpus's exact line
  target. The file `society_mgmt_300k/src/utils/filler.js` is composed
  **entirely** of filler: it defines **0 functions** across **1,999 lines** and
  declares no symbols at all. The motif of its lines is shown at
  (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`), and its full
  0-function / 1,999-line shape is confirmed corpus-wide
  (Source: `docs/reference/corpus-evidence.md:L217-L232`). For where it sits among
  the 29 files, see the [file inventory](file-inventory.md).
- **layer** — a nominal folder (`config`, `controllers`, `domain`, `middleware`,
  `models`, `repositories`, `routes`, `services`, `utils`, `tests/unit`, or
  `tests/integration`) whose conventional application-architecture name is only a
  label. Despite that name, each *layer* contains only `mod_*` arithmetic stubs
  and has **no inter-layer edges** — no layer imports from, requires, or calls
  another. A single layer's content is shown by the canonical motif
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`); the absence of
  any module keywords across the source corpus — and therefore of inter-layer
  edges — is confirmed by a corpus-wide sweep over `society_mgmt_300k/**/*.js`
  (Source: `docs/reference/corpus-evidence.md:L112-L151`).
- **`mod_`** — the function-name prefix shared by the whole *corpus*. A function
  is named `mod_<fileId>_<k>`, where `<fileId>` is the numeric id of its file and
  `<k>` is the function's **0-based** index within that file; for example,
  `mod_0_0` is the first function in `file_0.js`. The naming scheme is shown by
  the declaration on line 3 of the canonical file
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3`); that all **33,105**
  functions follow it and that all **33,105** names are distinct (collision-free)
  is verified corpus-wide (Source: `docs/reference/corpus-evidence.md:L47-L65`).
- **`O(1)`** — "constant time and space": the cost of an operation does not grow
  with the size or magnitude of its input. Each `mod_*` call performs a fixed
  number of arithmetic steps on a single scalar accumulator, so it runs in `O(1)`
  time and `O(1)` space regardless of the value of `x`
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`); the analysis
  applies to every function because all bodies are byte-identical
  (Source: `docs/reference/corpus-evidence.md:L67-L95`).
- **pure function** (also **pure**) — a function that (a) returns the same output
  for the same input and (b) has no observable side effects: no I/O and no
  mutation of external or shared state. Every `mod_*` function is pure — it reads
  only `x`, writes only a local accumulator `r`, and never reads or writes the
  inert module-scoped `store`
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L2-L10`); the
  never-read / never-written status of `store` is confirmed corpus-wide
  (Source: `docs/reference/corpus-evidence.md:L97-L110`).
- **referentially transparent** — a property that follows from purity: any call to
  a `mod_*` function may be replaced by its computed result without changing
  program behavior, precisely because the function is *pure* and *deterministic*
  and performs no I/O or external mutation
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L2-L10`;
  `docs/reference/corpus-evidence.md:L67-L95`).
- **short variant** — a `.js` file that contains **fewer than the standard 1,200
  functions**. The only short variant in the corpus is
  `society_mgmt_300k/src/middleware/file_27.js`, which defines **705 functions**
  across **6,347 lines**; it is otherwise structurally identical to a standard
  file. Its header and motif are shown at
  (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`), and its
  705-function / 6,347-line count is confirmed corpus-wide
  (Source: `docs/reference/corpus-evidence.md:L217-L232`). For the full per-file
  counts, see the [file inventory](file-inventory.md).
- **`store`** — an inert, module-scoped array declared as `const store = [];` at
  the top of a module (line 2, immediately after the header comment). It is a
  *placeholder*: the declaration is shown on line 2 of the canonical file
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L2`); it appears in **28**
  of the 29 `.js` files (every function-bearing file) yet is **never read and
  never written** by any function — confirmed corpus-wide — so removing it would
  change no result (Source: `docs/reference/corpus-evidence.md:L97-L110`).
- **synthetic corpus** — machine-generated code whose purpose is **scale and
  structure** (symbol density, a layered folder layout, and an exact line target)
  rather than real domain behavior. Here, *"society management"* is only a
  **nominal label** — the repository name and a per-file header comment (for
  example, `// mod_0 - society module`), not implemented functionality. The header
  is shown on line 1 of the canonical file
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`); that the "society"
  label appears only in module headers (28 files) and nowhere as behavior is
  confirmed by a corpus-wide header scan
  (Source: `docs/reference/corpus-evidence.md:L248-L262`).

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L2` — the canonical module
  header comment (line 1) and the inert `const store = [];` declaration (line 2);
  this file is also the basis for the `mod_` naming scheme declared on line 3.
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only `// filler N`
  padding motif that defines no functions.
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short-variant file's
  header and motif (the same `mod_*` motif).
- `docs/reference/corpus-evidence.md:L28-L262` — the reproducible scans backing
  the corpus-wide statements in these definitions: the 33,105 function count and
  name uniqueness (`mod_`), the byte-identical body (*deterministic*, *pure*,
  `O(1)`, *referentially transparent*), the 28-file `store` placeholder count and
  its never-read / never-written status, the module-keyword sweep behind the
  *layer* isolation claim, the file shapes (*short variant*, *filler*), and the
  header scan (*synthetic corpus*).

---

← Back to the [documentation hub](../README.md)
