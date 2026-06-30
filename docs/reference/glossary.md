# Glossary

← Back to the [documentation hub](../README.md)

## Overview

This glossary defines the vocabulary used across the **`society_mgmt_300k`**
documentation so that terminology stays consistent from one page to the next.
Every term below is drawn from the verified source *corpus* and is recorded with
its exact, code-confirmed meaning rather than any assumed domain definition.

## Terms

The terms are listed alphabetically. Each definition that asserts a code fact
carries an inline `Source:` citation pointing to the verifiable line(s) in the
corpus.

- **dead (always-true) branch** — the conditional `if (r % 2 === 0) { r += 10 }`
  that appears inside every `mod_*` function. The accumulator `r` is built up as
  `r += x*1; r += x*2; r += x*3`, so it always equals `6x`, which is **always
  even**. The parity test is therefore **always true**, the `+ 10` is **always
  applied**, and the implicit false path is **unreachable** (dead). As a result,
  every function effectively returns `6x + 10`
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L4-L10`).
- **filler** — comment-only padding lines of the form `// filler N` (where `N` is
  an incrementing number) used to pad a file toward the corpus's exact line
  target. The file `society_mgmt_300k/src/utils/filler.js` is composed
  **entirely** of filler: it defines **0 functions** across **1,999 lines** and
  declares no symbols at all. For where it sits among the 29 files, see the
  [file inventory](file-inventory.md)
  (Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`).
- **layer** — a nominal folder (`config`, `controllers`, `domain`, `middleware`,
  `models`, `repositories`, `routes`, `services`, `utils`, `tests/unit`, or
  `tests/integration`) whose conventional application-architecture name is only a
  label. Despite that name, each *layer* contains only `mod_*` arithmetic stubs
  and has **no inter-layer edges** — no layer imports from, requires, or calls
  another (Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`).
- **`mod_`** — the function-name prefix shared by the whole *corpus*. A function
  is named `mod_<fileId>_<k>`, where `<fileId>` is the numeric id of its file and
  `<k>` is the function's **0-based** index within that file; for example,
  `mod_0_0` is the first function in `file_0.js`. All **33,105** functions in the
  corpus follow this naming scheme
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3`).
- **short variant** — a `.js` file that contains **fewer than the standard 1,200
  functions**. The only short variant in the corpus is
  `society_mgmt_300k/src/middleware/file_27.js`, which defines **705 functions**
  across **6,347 lines**; it is otherwise structurally identical to a standard
  file. For the full per-file counts, see the [file inventory](file-inventory.md)
  (Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`).
- **`store`** — an inert, module-scoped array declared as `const store = [];` at
  the top of a module (line 2, immediately after the header comment). It is a
  *placeholder*: it appears in **28** of the 29 `.js` files (every
  function-bearing file) yet is **never read and never written** by any function,
  so removing it would change no result
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L2`).
- **synthetic corpus** — machine-generated code whose purpose is **scale and
  structure** (symbol density, a layered folder layout, and an exact line target)
  rather than real domain behavior. Here, *"society management"* is only a
  **nominal label** — the repository name and a per-file header comment (for
  example, `// mod_0 - society module`), not implemented functionality
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L2` — the canonical module
  header comment (line 1) and the inert `const store = [];` declaration (line 2);
  this file is also the basis for the `mod_` naming scheme declared on line 3.
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only `// filler N`
  padding that defines no functions.
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the short-variant file
  (705 functions) sharing the same `mod_*` motif.

---

← Back to the [documentation hub](../README.md)
