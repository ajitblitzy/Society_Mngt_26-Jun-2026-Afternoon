# Glossary

## Overview

This glossary defines the vocabulary used across the `society_mgmt_300k`
documentation so that terminology stays consistent from page to page. Every
term below is drawn from — and verified against — the source corpus, and each
definition that asserts a code fact carries an inline `Source:` citation back to
the file and line range that supports it.

## Terms

**synthetic corpus** — Machine-generated code whose purpose is **scale and
structure** (symbol density, a layered folder layout, and an exact line target)
rather than real domain behavior. In this repository, "society management" is
only a **nominal label**: it appears as the repository name and as a per-file
header comment (for example, `// mod_0 - society module`) but is **not**
implemented as functionality.
Source: `society_mgmt_300k/src/controllers/file_0.js:L1`.

**layer** — A nominal folder under the corpus root — one of `config`,
`controllers`, `domain`, `middleware`, `models`, `repositories`, `routes`,
`services`, `utils`, `tests/unit`, or `tests/integration`. Despite each folder's
conventional application-architecture name, every layer contains only `mod_*`
arithmetic stubs and has **no inter-layer edges**: there are no imports or calls
between layers.
Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`.

**`mod_`** — The function-name prefix used throughout the corpus. A function is
named `mod_<fileId>_<k>`, where `<fileId>` is the numeric id of the file and
`<k>` is the 0-based index of the function within that file — so `mod_0_0` is
the first function declared in `file_0.js`. All 33,105 functions in the corpus
follow this naming scheme.
Source: `society_mgmt_300k/src/controllers/file_0.js:L3`.

**`store`** — An inert, module-scoped array declared as `const store = [];` at
the top of a module. It is a placeholder only: it appears in **28** of the 29
`.js` files (every function-bearing file) and is **never read or written** by
any function.
Source: `society_mgmt_300k/src/controllers/file_0.js:L2`.

**filler** — Comment-only padding lines of the form `// filler N` that pad a
file toward the corpus's exact line target. The file
`society_mgmt_300k/src/utils/filler.js` is composed entirely of filler:
**0 functions across 1,999 lines**. See the [file inventory](file-inventory.md)
for per-file line counts.
Source: `society_mgmt_300k/src/utils/filler.js:L1-L3`.

**short variant** — A `.js` file that contains fewer than the standard 1,200
functions. The only short variant in the corpus is
`society_mgmt_300k/src/middleware/file_27.js`, which holds **705 functions**
across 6,347 lines. See the [file inventory](file-inventory.md) for the full
per-file breakdown.
Source: `society_mgmt_300k/src/middleware/file_27.js:L1-L10`.

**dead (always-true) branch** — The conditional `if (r % 2 === 0) { r += 10 }`
present inside every `mod_*` function. The accumulator `r` is built up as
`x*1 + x*2 + x*3`, so it always equals `6x`, which is always even; the parity
test is therefore **always true**, the `+ 10` is always applied, and the false
path is **unreachable**. Each function consequently returns `6x + 10`. See
[module control flow](../architecture/module-control-flow.md) for the annotated
execution path.
Source: `society_mgmt_300k/src/controllers/file_0.js:L4-L10`.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L2` — the per-file header
  comment (the nominal "society module" label), the `mod_` naming scheme, and
  the inert `const store = [];` declaration.
- `society_mgmt_300k/src/utils/filler.js:L1-L3` — the comment-only `// filler N`
  padding lines that define the `filler` term.
- `society_mgmt_300k/src/middleware/file_27.js:L1-L10` — the canonical module
  motif as it appears in the `short variant` file (705 functions).
