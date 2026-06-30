# Arithmetic Helpers (F-001 & F-002)

← Back to the [functionality index](README.md) · [documentation hub](../README.md)

## Overview

This page documents the corpus's **only** behavioral capability: the `mod_*`
arithmetic helper family. The family spans all **33,105** functions of the
synthetic [`society_mgmt_300k`](../overview.md) JavaScript *corpus*, and every one
of them effectively returns **`6x + 10`** for a numeric input `x`
(Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`). These functions
are *pure*, *deterministic*, single-argument, and structurally identical —
differing only in their `mod_<fileId>_<k>` name — so this single page documents
the entire family. (The terms *pure*, *deterministic*, *dead (always-true)
branch*, and *synthetic corpus* are defined in the
[glossary](../reference/glossary.md); this page does not redefine them.)

"Society management" is a **nominal label** only: it appears solely as the
repository name and a per-file header comment (`// mod_0 - society module`), not
as implemented domain behavior
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1`). For the step-by-step
execution diagram of a single call, see
[Module control flow](../architecture/module-control-flow.md); for the API-style
archetype (signature and parameter/return table), see
[Code reference](../reference/code-reference.md).

## Purpose

Each `mod_*` function is a deterministic numeric helper: given a single number
`x`, it returns a single number. There is no domain logic of any kind — the
`// mod_0 - society module` header comment is nominal, a label rather than a
description of behavior
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).

## Signature

Every function shares the signature `mod_<fileId>_<k>(x)`: it takes a single
numeric parameter `x`, runs synchronously, and returns a number
(Source: `society_mgmt_300k/src/controllers/file_0.js:L3`).

## The computation

The function body accumulates three products into a local variable `r`: starting
from `let r = 0`, it runs `r += x*1`, then `r += x*2`, then `r += x*3`. After the
three additions, `r = x*1 + x*2 + x*3`, i.e. **`r = 6x`**
(Source: `society_mgmt_300k/src/controllers/file_0.js:L4-L7`).

## The conditional `+10` (dead always-true branch)

After the accumulation, the body runs `if (r % 2 === 0) { r += 10 }`. Because
`r = 6x` is a multiple of `6` (hence a multiple of `2`), it is **always even**,
so the parity test `r % 2 === 0` is **always true** and the `r += 10` **always
executes**. The implicit `false`/`else` path — the case where the `+ 10` is
skipped — is therefore **unreachable (dead code)**
(Source: `society_mgmt_300k/src/controllers/file_0.js:L8`). This *dead
(always-true) branch* (defined in the [glossary](../reference/glossary.md)) is
documented **faithfully**, exactly as it executes; it is **not** "fixed",
simplified, or removed, because altering the source would be a code change and is
out of scope. For the annotated control-flow diagram, see
[Module control flow](../architecture/module-control-flow.md)
(Source: `society_mgmt_300k/src/controllers/file_0.js:L8`).

## Return value

The function returns the accumulator `r`. Because the `+ 10` always runs, the
returned value always equals **`6x + 10`**
(Source: `society_mgmt_300k/src/controllers/file_0.js:L9-L10`).

## Worked example

The canonical function body below is reproduced exactly as it appears in the
source. The inert `const store = [];` declaration is intentionally omitted here
(it is covered in [Module anatomy](module-anatomy.md)), and the computed result
is appended as a trailing comment
(Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`):

```javascript
// mod_0 - society module
function mod_0_0(x){
 let r=0;
 r+=x*1;
 r+=x*2;
 r+=x*3;
 if(r%2===0){r+=10}
 return r;
}
// mod_0_0(4) === 34   (6*4 + 10)
```

Because the function is pure and deterministic, `mod_0_0(4)` is exactly `34`
(that is, `6*4 + 10 = 34`)
(Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).

## Formula table

A few sample inputs and their exact return values, all following the `6x + 10`
rule (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`):

| x  | 6x | returns 6x + 10 |
|----|----|-----------------|
| 1  | 6  | 16              |
| 2  | 12 | 22              |
| 4  | 24 | 34              |
| 10 | 60 | 70              |

## Naming rules (F-002)

Functions are named with the scheme `mod_<fileId>_<k>`, where `<fileId>` is the
file's numeric id and `<k>` is the function's **0-based** index within that file
— so `mod_0_0` is the first function declared in `file_0.js`, `mod_0_1` the
second, and so on
(Source: `society_mgmt_300k/src/controllers/file_0.js:L3`). Because each name
combines the file id with the position, the **33,105** names are
**collision-free**: the file id plus the index uniquely identifies every
function. The symbols are **file-local** and **not importable** — the corpus has
no module system, so a whole-tree keyword sweep finds zero occurrences of
`require`, `import`, `export`, or `module.exports`, and no `mod_*` symbol can be
referenced from another file
(Source: `society_mgmt_300k/src/controllers/file_0.js:L3`). The `mod_` prefix
itself is defined in the [glossary](../reference/glossary.md).

## See also

- [Module control flow](../architecture/module-control-flow.md) — the
  step-by-step execution of a `mod_*` function, with the dead always-true branch
  annotated in a flowchart.
- [Code reference](../reference/code-reference.md) — the API-style archetype for
  the `mod_*` family (signature and parameter/return table).
- [Module anatomy](module-anatomy.md) — the anatomy of a module file, including
  the inert `store` placeholder omitted from the worked example above.
- [Corpus composition](corpus-composition.md) — the per-layer file, function, and
  line composition of the corpus.
- [Glossary](../reference/glossary.md) — definitions of `mod_`, *pure*,
  *deterministic*, *dead (always-true) branch*, and *synthetic corpus*.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1` — the nominal
  `// mod_0 - society module` header comment (the "society management" label) and
  the basis of the `mod_<fileId>_<k>` naming scheme.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the canonical function
  body that accumulates `6x` and returns `6x + 10`, including the dead
  always-true parity branch on line 8.
- The `mod_*` family documented here covers all **33,105** functions in the
  corpus, verified corpus-wide to be byte-identical apart from their names.

---

← Back to the [functionality index](README.md) · [documentation hub](../README.md)
