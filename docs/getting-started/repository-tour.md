# Repository tour

This page is the navigation guide for `society_mgmt_300k`: it shows how to find your way around the folders, how to read a single file, why there is nothing to build or run, and how the line count adds up. If you have not yet read the [overview](overview.md), start there for the big picture, then come back here to learn the layout. Two things matter most for orientation: **there is nothing to execute — you open and read files** `[Technical Specification §1.2.2]`, and **the 300,000-line figure is real and reconciles exactly** `[Technical Specification §1.2.2]`.

## Directory map

The corpus lives entirely under `society_mgmt_300k/`, which splits into a `src/` tree of nine [nominal layers](../glossary.md), a `tests/` tree of two fixture directories, and a nested `LICENSE/` folder `[Technical Specification §1.2.2]`. The tree below lists each directory with its `.js` file count; the per-directory `.js` counts sum to the **29 `.js` files** in the corpus `[Technical Specification §1.2.2]`:

```text
society_mgmt_300k/
├── src/                 # nine nominal layers (naming convention only)
│   ├── config/          # 2 files
│   ├── controllers/     # 3 files
│   ├── domain/          # 2 files
│   ├── middleware/      # 3 files  (file_27.js is a short variant)
│   ├── models/          # 3 files
│   ├── repositories/    # 2 files
│   ├── routes/          # 3 files
│   ├── services/        # 3 files
│   └── utils/           # 4 files  (3 mod_* files + comment-only filler.js)
├── tests/               # fixtures, not an executable test suite
│   ├── unit/            # 2 files
│   └── integration/     # 2 files
└── LICENSE/             # nested LICENSE.txt
```

The nested `LICENSE/` folder contains an MIT `LICENSE.txt` and holds no `.js` files, so it is outside the 29-file tally `[society_mgmt_300k/LICENSE/LICENSE.txt]`. The directory names (`controllers`, `services`, `repositories`, and so on) are **nominal only**: they mirror the tiers of a conventional layered application but carry no runtime role, because the corpus has no imports, exports, classes, shared state, or calls between files — so there are **no runtime edges** between layers `[Technical Specification §5.4.2]`. Read a folder name as a label on a box of identical arithmetic helpers, not as a description of behavior `[Technical Specification §1.2.1]`. For the layering detail and a diagram of this verified absence of edges, see the [architecture overview](../architecture/overview.md) `[Technical Specification §5.4.2]`.

## How to read a single module

Every non-filler file follows one canonical shape, so once you can read one file you can read them all `[society_mgmt_300k/src/config/file_6.js:L1-L10]`. Open any `.js` file and you will find three parts:

- **Line 1 — header comment.** A single line of the form `// mod_<fileId> - society module` (for example, `// mod_6 - society module`) `[society_mgmt_300k/src/config/file_6.js:L1]`.
- **Line 2 — inert `store`.** The module-scoped declaration `const store = [];`, an inert [`store`](../glossary.md) placeholder that is **never read from or written to**, so it holds no state and affects no result `[society_mgmt_300k/src/config/file_6.js:L2]`.
- **Lines 3 onward — the `mod_*` functions.** A run of [`mod_*`](../glossary.md) functions written generally as `mod_<fileId>_<k>(x)`, each accumulating `r = x*1 + x*2 + x*3` (that is, `6x`) and returning `6x + 10` for integer input `[society_mgmt_300k/src/config/file_6.js:L3-L10]`.

The canonical function body looks like this; the worked calls are **representative of all 33,105 functions**, because every function is byte-for-byte identical apart from its name `[society_mgmt_300k/src/config/file_6.js:L3-L10]`:

```javascript
function mod_6_0(x){ let r=0; r+=x*1; r+=x*2; r+=x*3; if(r%2===0){r+=10} return r; }
// mod_6_0(2) === 22 and mod_6_0(5) === 40   (both equal 6x + 10)
```

The `+ 10` comes from the parity guard `if (r % 2 === 0)`, which is an always-true [dead branch](../glossary.md) for integer input because `6x` is always even `[society_mgmt_300k/src/config/file_6.js:L8]`. The files under `tests/` use this same shape — for example, `mod_9_0` in `tests/unit/file_9.js` `[society_mgmt_300k/tests/unit/file_9.js:L1-L10]`. For the full signature, the parameter and return detail, and a flow diagram, see the [function reference](../reference/function-reference.md); for the exhaustive per-file inventory, see the [source layout](../reference/source-layout.md) `[society_mgmt_300k/src/config/file_6.js:L3-L10]`.

## No build, run, or test runner

There is **nothing to install, build, run, or serve** `[Technical Specification §1.2.2]`. The corpus has **no `package.json`**, no scripts, no entry point (`index.js`, `app.js`, `server.js`, or `main.js`), no CI, no container configuration, and **zero third-party dependencies** — all verified absent `[Technical Specification §1.2.2]`. Because the layers have no runtime edges, nothing wires the files together into a running system `[Technical Specification §5.4.2]`.

The directories under `tests/` are **not an executable test suite**: `tests/unit` and `tests/integration` hold the same [`mod_*`](../glossary.md) functions as the `src` layers, with **no assertions and no test-runner hooks**, so they are generated [fixtures](../glossary.md) rather than runnable tests — do not expect `npm test` to work `[Technical Specification §1.2.2]`.

The only workflow, therefore, is to **open and read** the `.js` files in a text editor `[Technical Specification §1.2.2]`. Pick any file, recognize the three-part shape described above, and you have understood it `[society_mgmt_300k/src/config/file_6.js:L1-L10]`.

## Where the 300,000 lines come from

The corpus is **exactly 300,000 lines** across its 29 `.js` files, and the figure reconciles precisely `[Technical Specification §1.2.2]`. Of the 29 files, **28 contain `mod_*` functions** (contributing all **33,105** functions) and one — `filler.js` — contains none `[Technical Specification §1.2.2]`. Two files deviate from the standard size:

- **`society_mgmt_300k/src/utils/filler.js`** is **comment-only padding**: **1,999 lines** of the form `// filler NNNNNN` (spanning `// filler 298001` through `// filler 299999`) and **0 functions**, whose sole purpose is to pad the corpus to exactly 300,000 lines `[society_mgmt_300k/src/utils/filler.js]`.
- **`society_mgmt_300k/src/middleware/file_27.js`** is a **short variant**: **6,347 lines** with **705 functions**, instead of the standard 10,802 lines with 1,200 functions `[society_mgmt_300k/src/middleware/file_27.js]`.

The remaining 27 files are standard — each following the canonical file shape `[society_mgmt_300k/src/config/file_6.js:L1-L10]` — with 1,200 functions and 10,802 lines apiece `[Technical Specification §1.2.2]` (the per-file inventory is owned by the [source layout](../reference/source-layout.md)). The functions therefore reconcile as `27 × 1,200 + 705 = 33,105`, and the lines reconcile to exactly 300,000 `[Technical Specification §1.2.2]`:

```text
27 standard files × 10,802 lines = 291,654
src/middleware/file_27.js        =   6,347   (short variant, 705 functions)
src/utils/filler.js              =   1,999   (comment-only, 0 functions)
                                   ---------
total                            = 300,000
```

For the full per-layer breakdown — every directory's file, function, and line counts — see the [source layout](../reference/source-layout.md), which owns the exhaustive inventory table `[Technical Specification §1.2.2]`.

## Where to go next

- [Overview](overview.md) — what this repository actually is versus its misleading name.
- [Source layout](../reference/source-layout.md) — the exhaustive per-layer file, function, and line inventory `[Technical Specification §1.2.2]`.
- [Function reference](../reference/function-reference.md) — the full signature, integer-input `6x + 10` behavior, and flow diagram `[society_mgmt_300k/src/config/file_6.js:L3-L10]`.
- [Architecture overview](../architecture/overview.md) — the layered layout and why the layers have no runtime edges `[Technical Specification §5.4.2]`.
- [Glossary](../glossary.md) — definitions of the corpus-specific terminology used throughout this documentation.

---

[← Documentation Home](../index.md)
