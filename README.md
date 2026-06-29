# society_mgmt_300k

`society_mgmt_300k` is a **synthetic, dependency-free JavaScript corpus**:
**29** `.js` files holding **33,105** functions named `mod_<fileId>_<k>`,
totalling **exactly 300,000** lines, arranged as a layered folder scaffold
of **11 nominal layers** under `src/` (`config`, `middleware`, `models`,
`controllers`, `routes`, `domain`, `services`, `repositories`, `utils`) and
`tests/` (`unit`, `integration`). It has no `package.json`, lockfile, or any
other manifest and requires no build step; the files exist to be read and
statically scanned rather than executed as an application.
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (the archetype
every file follows); docs/reference/file-inventory.md#verification (the
re-verifiable corpus-wide 29-file / 33,105-function / 300,000-line counts)

## What this is / is not

This repository **is**:

- A **synthetic, static-analysis-oriented corpus** of pure arithmetic
  helper functions — every function is single-argument, synchronous,
  side-effect-free, and deterministic.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10
- A **layered folder scaffold** of 11 nominal layers with no inter-layer
  dependencies.
  Source: docs/architecture/layered-scaffold.md
- **Dependency-free with no build step** — plain `.js` source, no manifest,
  no tooling.
  Source: docs/security/README.md#supply-chain

This repository **is not**:

- **Not a runnable society-management application.** "Society management"
  is a **nominal label only**: it appears as the repository name and as a
  per-file header comment (e.g., `// mod_0 - society module`); there is no
  domain model, no entities, and no business rules behind the name.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1
- **Not a REST API or service** — the `controllers/` and `routes/` folders
  hold the same arithmetic stubs as every other layer, not request handlers
  or a route table.
  Source: docs/security/README.md#verified-absences-keyword-sweep
- **Not a system with persistence, I/O, configuration, or authentication** —
  a whole-tree keyword sweep returns zero matches for any module-system,
  I/O, or security construct (`require`/`import`/`export`, `eval`, `fetch`,
  `crypto`, `auth`, secrets), and the module-scoped `store` array is inert.
  Source: docs/security/README.md#verified-absences-keyword-sweep

## The `mod_*` archetype

Every `.js` module follows one canonical motif: a header comment, an inert
module-scoped `const store = [];` placeholder, and then a run of
single-argument arithmetic functions. The archetype is:

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

Each `mod_<fileId>_<k>(x)` accumulates `x*1 + x*2 + x*3` (which equals `6x`)
and then adds `10` whenever the running total is even. Because `6x` is always
even, the `if (r % 2 === 0)` test is **always true** — it is a dead
always-true branch — so every function effectively returns **`6x + 10`**. The
result is exact and verifiable by inspection: `mod_0_0(4)` computes
`6 * 4 + 10`, so `mod_0_0(4) === 34`.
Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## Documentation

The full documentation lives under [`docs/`](docs/README.md). Start at the
navigation hub and follow the progressive-disclosure path (overview →
functionality → architecture → performance → security → reference):

- [`docs/README.md`](docs/README.md) — documentation index / navigation hub.
- [`docs/overview.md`](docs/overview.md) — system overview (the
  synthetic-corpus nature; "society management" as a label; what the system
  is not).
- [`docs/functionality/README.md`](docs/functionality/README.md) —
  functionality catalog (features F-001..F-006).
- [`docs/architecture/README.md`](docs/architecture/README.md) — layered
  scaffold and per-function control-flow diagrams.
- [`docs/performance/README.md`](docs/performance/README.md) — O(1) per-call
  complexity, determinism, and the explicit absence of SLAs.
- [`docs/security/README.md`](docs/security/README.md) — the
  verified-absence security posture and the F-006 dual-license discussion.
- [`docs/reference/file-inventory.md`](docs/reference/file-inventory.md) —
  full inventory of all 29 `.js` files (layer, function count, line count).
- [`docs/reference/code-reference.md`](docs/reference/code-reference.md) —
  code reference for the `mod_*` family.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — terminology.

Start at [docs/README.md](docs/README.md).

## License

This repository currently carries **two conflicting licenses with no
statement of precedence**:

- Root [`LICENSE`](LICENSE) — **Apache License, Version 2.0**.
  Source: LICENSE
- Inner [`society_mgmt_300k/LICENSE/LICENSE.txt`](society_mgmt_300k/LICENSE/LICENSE.txt)
  — **MIT License**.
  Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1

This unresolved dual-license conflict is tracked as governance item
**F-006** and is documented — but intentionally **not resolved** — in
[`docs/security/README.md`](docs/security/README.md#f-006--dual-license-conflict).
Editing the license files is out of scope for this documentation effort;
refer to the security document for the risk analysis and recommended
resolution paths.
