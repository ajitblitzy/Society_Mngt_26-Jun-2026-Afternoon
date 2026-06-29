# Arithmetic Helpers (F-001 & F-002)

## Overview

This page documents the corpus's only behavioral capability: the `mod_*`
arithmetic helper family. The capability spans all **33,105** functions in
`society_mgmt_300k`, and every one of them effectively returns `6x + 10` for a
single numeric input `x`. The functions are pure, deterministic,
single-argument, and structurally identical — byte-for-byte the same apart from
their names — so this single page documents the entire family.
Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the
canonical example. That the family spans all **33,105** functions, each
byte-identical to this apart from its name, is confirmed by a direct
full-corpus scan; see the
[file inventory](../reference/file-inventory.md#verification).

"Society management" is a **nominal label** only: it appears as the repository
name and as a per-file header comment (for example, `// mod_0 - society
module`) and implements no domain functionality. For the step-by-step execution
diagram, see [Module control flow](../architecture/module-control-flow.md); for
the API-style archetype with a parameter/return table, see
[Code reference](../reference/code-reference.md).
Source: `society_mgmt_300k/src/controllers/file_0.js:L1`.

## Purpose

Each `mod_*` function is a deterministic numeric helper: given a single number
`x`, it returns a single number. There is no domain logic behind the name — the
`// mod_0 - society module` header is nominal and does not describe any
implemented behavior.
Source: `society_mgmt_300k/src/controllers/file_0.js:L1`.

## Signature

Every function in the family shares one signature:

```text
mod_<fileId>_<k>(x)
```

It takes a single numeric parameter `x`, runs synchronously, and returns a
number. There are no other parameters, no overloads, and no options object.
Source: `society_mgmt_300k/src/controllers/file_0.js:L3`.

## The computation

The body initialises an accumulator `r` to `0` and then adds three multiples of
the input: `r += x*1`, `r += x*2`, and `r += x*3`. The accumulator therefore
builds up to `r = x*1 + x*2 + x*3`, which equals `6x`.
Source: `society_mgmt_300k/src/controllers/file_0.js:L4-L7`.

## The conditional `+10` (dead always-true branch)

After the accumulation, the body runs `if (r % 2 === 0) { r += 10 }`. Because
`r` always equals `6x`, and `6x` is always even, the parity test `r % 2 === 0`
is **always true**: the `+ 10` is applied on every call, and the implicit
false / `else` path is **unreachable**. This is a dead always-true branch,
documented here faithfully — exactly as it executes. The source is **not**
modified: "fixing" or removing the always-true test would be a code change and
is out of scope for documentation. For the formal definition of this term, see
the [Glossary](../reference/glossary.md); for the annotated execution diagram,
see [Module control flow](../architecture/module-control-flow.md).
Source: `society_mgmt_300k/src/controllers/file_0.js:L8`.

## Return value

The function returns the accumulator `r`. Since `6x` is always even and the
`+ 10` always runs, the returned value is always `6x + 10`.
Source: `society_mgmt_300k/src/controllers/file_0.js:L9-L10`.

## Worked example

The canonical archetype is the first function in the first file. The block below
reproduces it — omitting the module-scoped `store`, which is covered in
[Module anatomy](module-anatomy.md) — and annotates the result:

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

Because the function is pure and deterministic, `mod_0_0(4)` is exactly `34`.
Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`.

## Formula table

The table below maps sample inputs to their exact returned values, each computed
as `6x + 10`:

| x  | 6x | returns 6x + 10 |
|----|----|-----------------|
| 1  | 6  | 16              |
| 2  | 12 | 22              |
| 4  | 24 | 34              |
| 10 | 60 | 70              |

Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`.

## Naming rules (F-002)

Functions follow the scheme `mod_<fileId>_<k>`, where `<fileId>` is the file's
numeric id (for example, `0` for `file_0.js`) and `<k>` is the function's
0-based index within that file — so `mod_0_0` is the first function in
`file_0.js`, `mod_0_1` is the second, and so on. The scheme is
**collision-free**: the file id plus the index uniquely identify each of the
**33,105** functions. The names are **file-local** and **not importable** — the
corpus has no module system, with zero occurrences of `require`, `import`,
`export`, or `module.exports` anywhere in the source tree. For the prefix
definition, see the [Glossary](../reference/glossary.md).
Source: `society_mgmt_300k/src/controllers/file_0.js:L3` — a
representative `mod_<fileId>_<k>` declaration. The **33,105**-function
count is from the direct full-corpus scan, and the **no module system**
claim (zero `require`/`import`/`export`/`module.exports`) is from the
whole-tree keyword sweep; see the
[file inventory](../reference/file-inventory.md#verification).

## See also

- [Module control flow](../architecture/module-control-flow.md) — the
  step-by-step execution path with the dead branch annotated.
- [Code reference](../reference/code-reference.md) — the API-style archetype and
  the parameter/return table.
- [Module anatomy](module-anatomy.md) — the header comment, the inert `store`
  placeholder, and the comment-only `filler.js` variant.
- [Corpus composition](corpus-composition.md) — per-layer file, function, and
  line counts.
- [Glossary](../reference/glossary.md) — definitions of `mod_`, `store`, the
  dead (always-true) branch, and other corpus terms.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1` — the per-file header comment
  (the nominal "society module" label) that underpins the `mod_*` naming scheme.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the function body: the
  `6x` accumulation, the dead always-true `+ 10` branch, and the `6x + 10`
  return value.
- `society_mgmt_300k/src/` and `society_mgmt_300k/tests/` — the direct
  full-corpus scan / whole-tree keyword sweep confirming the `mod_*`
  family spans all **33,105** functions, each identical to this archetype
  apart from its name, with no module system anywhere in the tree. See
  [file inventory](../reference/file-inventory.md#verification).
