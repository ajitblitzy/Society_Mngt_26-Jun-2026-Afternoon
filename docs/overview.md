# Overview

← Back to the [documentation hub](./README.md)

## What this corpus is

`society_mgmt_300k` is a **synthetic, dependency-free JavaScript corpus** built
for static analysis and code traversal rather than execution. It comprises
**29 `.js` files** that together declare **33,105** functions named
`mod_<fileId>_<k>`, totaling **exactly 300,000 lines**, arranged as a layered
folder *scaffold*. There is no build step, no package manifest, and no
third-party dependency.
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (per-file motif);
docs/reference/corpus-evidence.md:L28-L54 (the 29-file / 33,105-function /
300,000-line counts); docs/reference/corpus-evidence.md:L234-L246 (no
package.json or lockfile)

Every **function-bearing** `.js` module follows one canonical motif — a header
comment, an inert module-scoped `const store = [];`, then a run of single-argument
arithmetic functions. The sole exception is the comment-only padding file
`society_mgmt_300k/src/utils/filler.js` (0 functions, no header or `store`)
(Source: society_mgmt_300k/src/utils/filler.js:L1-L3;
docs/reference/corpus-evidence.md:L217-L232):

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
Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (the body and dead
branch); docs/reference/corpus-evidence.md:L67-L95 confirms this body is
byte-identical across all 33,105 functions

## "Society management" is a label

The "society management" theme is **nominal only**. It appears in exactly two
places: the repository name (`society_mgmt_300k`) and a per-file header comment
such as `// mod_0 - society module`. There is no domain model, no entities, no
business rules, and no society-management behavior of any kind — only the
arithmetic helpers described above.
Source: society_mgmt_300k/src/controllers/file_0.js:L1 (per-file header comment);
docs/reference/corpus-evidence.md:L248-L262 (the corpus-wide header-comment scan
showing the label appears only in module headers) and
docs/reference/corpus-evidence.md:L67-L95 (byte-identical arithmetic bodies —
i.e. no domain logic)

## Capability summary

The corpus has a **single behavioral capability**: the arithmetic helper family
(feature **F-001**), in which every `mod_<fileId>_<k>(x)` computes `6x + 10`.
This one archetype is replicated uniformly across all layers, so a single worked
example documents the entire family. Alongside each helper sits an inert
placeholder — `const store = [];` (feature **F-004**) — present in **28** of the
29 files and never read or written.
Source: society_mgmt_300k/src/controllers/file_0.js:L2-L10 (per-file motif);
docs/reference/corpus-evidence.md:L67-L95 (the body byte-identical across all
33,105 functions) and docs/reference/corpus-evidence.md:L97-L110 (the inert
`store` declared in 28 files, never read or written)

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
  Source: society_mgmt_300k/src/controllers/file_0.js:L1 (per-file header
  comment); docs/reference/corpus-evidence.md:L248-L262 (corpus-wide
  header-comment scan) and docs/reference/corpus-evidence.md:L67-L95
  (byte-identical arithmetic bodies — i.e. no domain logic)
- **No user interface and no end-user workflow** — nothing renders, prompts, or
  drives an interactive flow; the sole external input is the numeric argument
  `x`. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (the
  single-argument body); docs/reference/corpus-evidence.md:L112-L151 (the
  source-corpus sweep finds zero `console`/`fetch`/`Promise`/`async`, so nothing
  renders or drives an interactive flow)
- **No REST API, routes, or endpoints** — the `controllers/` and `routes/`
  folders contain the same arithmetic stubs as every other layer.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (per-file motif);
  docs/reference/corpus-evidence.md:L177-L215 (the `controllers`/`routes` layers
  hold the same `mod_*` counts as every other layer) and
  docs/reference/corpus-evidence.md:L67-L95 (identical bodies)
- **No persistence, database, or ORM** — the `models/` and `repositories/`
  folders are arithmetic stubs, and the `store` placeholder is inert (never read
  or written). Source: society_mgmt_300k/src/controllers/file_0.js:L2 (the
  per-file `store` line); docs/reference/corpus-evidence.md:L97-L110 (`store`
  declared in 28 files and never read or written) and
  docs/reference/corpus-evidence.md:L67-L95 (identical arithmetic bodies)
- **No configuration, authentication, secrets, or cryptography** — the `config/`
  folder holds only arithmetic stubs, and a **source-corpus** keyword sweep over
  `society_mgmt_300k/**/*.js` returns zero occurrences of `password`, `token`,
  `jwt`, `auth`, `crypto`, or `encrypt`.
  Source: society_mgmt_300k/src/config/file_6.js:L1-L10 (a representative
  `config/` stub); docs/reference/corpus-evidence.md:L112-L151 (the source-corpus
  keyword sweep)
- **No module system** — a **source-corpus** sweep over
  `society_mgmt_300k/**/*.js` returns zero occurrences of `require`, `import`,
  `export`, or `module.exports`, so every symbol is file-local and nothing is
  externally importable.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (per-file motif);
  docs/reference/corpus-evidence.md:L112-L151 (the source-corpus sweep)

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
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (per-file motif);
docs/reference/corpus-evidence.md:L177-L215 (per-layer composition) and
docs/reference/corpus-evidence.md:L112-L151 (the zero `require`/`import`/`export`
sweep confirming no inter-layer edges)

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical module
  motif (header comment, inert `store`, and a `mod_<fileId>_<k>(x)` body). The
  generalization across all 33,105 functions is substantiated by
  `docs/reference/corpus-evidence.md:L28-L54` (counts) and
  `docs/reference/corpus-evidence.md:L67-L95` (byte-identical bodies); the
  no-module-system claim by `docs/reference/corpus-evidence.md:L112-L151`.
- `society_mgmt_300k/src/controllers/file_0.js:L1` — the header comment
  `// mod_0 - society module`; the per-file motif for the label. The corpus-wide
  "society management is only a label" claim is substantiated by
  `docs/reference/corpus-evidence.md:L248-L262`.
- `society_mgmt_300k/src/controllers/file_0.js:L2` — the inert
  `const store = [];` placeholder (feature F-004). That it is present in 28 of
  the 29 files and never read or written is substantiated by
  `docs/reference/corpus-evidence.md:L97-L110`.
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the `6x + 10`
  arithmetic body and the dead always-true parity branch (for example,
  `mod_0_0(4) === 34`).
- `society_mgmt_300k/src/config/file_6.js:L1-L10` — a representative `config/`
  layer file that holds only the arithmetic motif. The corpus-wide absence of
  configuration logic follows from `docs/reference/corpus-evidence.md:L67-L95`
  (byte-identical bodies) and `docs/reference/corpus-evidence.md:L112-L151` (the
  zero-keyword sweep).

---

← Back to the [documentation hub](./README.md)
