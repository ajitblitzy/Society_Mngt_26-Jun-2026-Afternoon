# Overview

← Back to the [documentation hub](./README.md)

## What this corpus is

`society_mgmt_300k` is a **synthetic, dependency-free JavaScript corpus** built
for static analysis and code traversal rather than execution. It comprises
**29 `.js` files** that together declare **33,105** functions named
`mod_<fileId>_<k>`, totaling **exactly 300,000 lines**, arranged as a layered
folder *scaffold*. There is no build step, no package manifest, and no
third-party dependency.
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

Every `.js` module follows one canonical motif — a header comment, an inert
module-scoped `const store = [];`, then a run of single-argument arithmetic
functions:

```javascript
// mod_0 - society module
const store = [];
function mod_0_0(x){
 let r=0;
 r+=x*1;
 r+=x*2;
 r+=x*3;
 if(r%2===0){r+=10}
 return r;
}
```

Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

Each `mod_<fileId>_<k>(x)` accumulates `x*1 + x*2 + x*3` (= `6x`) and then adds
`10` whenever the accumulator is even. Because `6x` is always even, the
`if (r % 2 === 0)` test is always true — a **dead always-true branch** — so
every function effectively returns **`6x + 10`**. For example, `mod_0_0(4)`
returns `6*4 + 10`, that is **`34`**.
Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## "Society management" is a label

The "society management" theme is **nominal only**. It appears in exactly two
places: the repository name (`society_mgmt_300k`) and a per-file header comment
such as `// mod_0 - society module`. There is no domain model, no entities, no
business rules, and no society-management behavior of any kind — only the
arithmetic helpers described above.
Source: society_mgmt_300k/src/controllers/file_0.js:L1

## Capability summary

The corpus has a **single behavioral capability**: the arithmetic helper family
(feature **F-001**), in which every `mod_<fileId>_<k>(x)` computes `6x + 10`.
This one archetype is replicated uniformly across all layers, so a single worked
example documents the entire family. Alongside each helper sits an inert
placeholder — `const store = [];` (feature **F-004**) — present in **28** of the
29 files and never read or written.
Source: society_mgmt_300k/src/controllers/file_0.js:L2-L10

For the full treatment, see the
[Functionality catalog](functionality/README.md) and, in particular, the
[Arithmetic helpers](functionality/arithmetic-helpers.md) page. Corpus-specific
terminology (for example *synthetic corpus*, *dead branch*, and *short variant*)
is defined once in the [glossary](reference/glossary.md) and is not redefined
here.

## What this system is NOT

To keep this documentation faithful, the following capabilities are reported as
**verified absences** — each confirmed by a first-hand scan of the source rather
than merely left undocumented:

- **Not a runnable society-management application** — there is no domain logic;
  "society management" is only a label.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1
- **No user interface and no end-user workflow** — nothing renders, prompts, or
  drives an interactive flow; the sole external input is the numeric argument
  `x`. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
- **No REST API, routes, or endpoints** — the `controllers/` and `routes/`
  folders contain the same arithmetic stubs as every other layer.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10
- **No persistence, database, or ORM** — the `models/` and `repositories/`
  folders are arithmetic stubs, and the `store` placeholder is inert (never read
  or written). Source: society_mgmt_300k/src/controllers/file_0.js:L2
- **No configuration, authentication, secrets, or cryptography** — the `config/`
  folder holds only arithmetic stubs, and a whole-tree keyword sweep returns
  zero occurrences of `password`, `token`, `jwt`, `auth`, `crypto`, or
  `encrypt`. Source: society_mgmt_300k/src/config/file_6.js:L1-L10
- **No module system** — a whole-tree sweep returns zero occurrences of
  `require`, `import`, `export`, or `module.exports`, so every symbol is
  file-local and nothing is externally importable.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

## How it is organized

The corpus is an **11-layer nominal scaffold**: nine layers under `src/`
(`config`, `middleware`, `models`, `controllers`, `routes`, `domain`,
`services`, `repositories`, `utils`) and two under `tests/` (`unit`,
`integration`). The layer names are borrowed from conventional web-application
architecture, but each folder holds only `mod_*` arithmetic stubs and there are
**no inter-layer edges**. For the layer map, see the
[Architecture](architecture/README.md) area and specifically the
[layered scaffold](architecture/layered-scaffold.md); for the authoritative
per-layer file, function, and line counts, see
[Corpus composition](functionality/corpus-composition.md).
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical module
  motif (header comment, inert `store`, and a `mod_<fileId>_<k>(x)` body); the
  single-file archetype generalized across all 33,105 functions and the basis
  for the no-module-system claim.
- `society_mgmt_300k/src/controllers/file_0.js:L1` — the header comment
  `// mod_0 - society module`; evidence that "society management" is a label,
  not implemented functionality.
- `society_mgmt_300k/src/controllers/file_0.js:L2` — the inert
  `const store = [];` placeholder (feature F-004), present in 28 of the 29 files
  and never read or written.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the `6x + 10`
  arithmetic body and the dead always-true parity branch (for example,
  `mod_0_0(4) === 34`).
- `society_mgmt_300k/src/config/file_6.js:L1-L10` — a `config/` layer file that
  holds only arithmetic stubs, evidencing the absence of configuration values.

---

← Back to the [documentation hub](./README.md)
