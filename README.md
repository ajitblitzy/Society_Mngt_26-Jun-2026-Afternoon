# society_mgmt_300k

`society_mgmt_300k` is a **synthetic, dependency-free JavaScript corpus** built
for static analysis and code traversal rather than execution. It comprises
**29 `.js` files** that declare **33,105 functions** named `mod_<fileId>_<k>`
and total **exactly 300,000 lines**, arranged as a layered scaffold of **11
nominal layers** — nine under `src/` (`config`, `controllers`, `domain`,
`middleware`, `models`, `repositories`, `routes`, `services`, `utils`) and two
under `tests/` (`unit`, `integration`). There is no build step, no package
manifest, and no third-party dependency.
Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 (per-file motif);
counts verified corpus-wide over society_mgmt_300k/**/*.js (29 files, 33,105
functions, 300,000 lines).

## What this is / is not

### What it is

- A **synthetic, static-analysis-oriented corpus** of pure arithmetic helper
  functions: every `mod_<fileId>_<k>(x)` deterministically computes `6x + 10`
  with no side effects.
  Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
- A **layered folder scaffold** of 11 nominal layers under `src/` and `tests/`,
  named after conventional web-application tiers but holding only the same
  arithmetic stubs in every layer.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10
- **Dependency-free with no build step** — plain `.js` source with no module
  system (`require`/`import`/`export`/`module.exports`), no package manifest,
  and no runtime dependency.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

### What it is not

- **Not a runnable society-management application.** "Society management" is a
  **nominal label only** — it appears as the repository name and a per-file
  header comment (e.g. `// mod_0 - society module`); there is no implemented
  domain logic, no entities, and no business rules.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1
- **Not a REST API or service.** The `controllers/` and `routes/` layers hold
  the same arithmetic stubs as every other layer — there are no endpoints,
  routes, or request/response handlers.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10
- **No persistence, I/O, configuration, or authentication.** The module-scoped
  `const store = [];` is inert (never read or written), and the sole external
  input is the numeric argument `x` — there is no database, file/network I/O,
  configuration object, or auth/crypto anywhere in the source.
  Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

## The `mod_*` archetype

Every `.js` file in the corpus follows one canonical motif: a header comment, an
inert module-scoped `const store = [];`, then a run of single-argument
arithmetic functions. The first function of the first file is representative of
all 33,105:

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

Each `mod_<fileId>_<k>(x)` accumulates `x*1 + x*2 + x*3` (= `6x`) and then adds
`10` when the accumulator is even. Because `6x` is always even, the
`if (r % 2 === 0)` test is **always true** — a *dead always-true branch* — so
every function effectively returns **`6x + 10`**. For example, `mod_0_0(4)`
returns `6*4 + 10`, that is **`34`** (`mod_0_0(4) === 34`).
Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## Documentation

Full documentation lives under [`docs/`](docs/README.md). Start at
[docs/README.md](docs/README.md) and follow the topic links below:

- [docs/README.md](docs/README.md) — documentation index / navigation hub.
- [docs/overview.md](docs/overview.md) — system overview (synthetic-corpus
  nature; "society management" as a label).
- [docs/functionality/README.md](docs/functionality/README.md) — functionality
  catalog (features F-001..F-006).
- [docs/architecture/README.md](docs/architecture/README.md) — layered scaffold
  plus control-flow diagrams.
- [docs/performance/README.md](docs/performance/README.md) — O(1) complexity,
  determinism, and the explicit absence of SLAs.
- [docs/security/README.md](docs/security/README.md) — verified-absence security
  posture plus the F-006 dual-license discussion.
- [docs/reference/file-inventory.md](docs/reference/file-inventory.md) — full
  inventory of all 29 `.js` files.
- [docs/reference/code-reference.md](docs/reference/code-reference.md) — code
  reference for the `mod_*` family.
- [docs/reference/glossary.md](docs/reference/glossary.md) — terminology.

## License

This repository currently carries **two conflicting licenses** with no statement
of precedence (governance item **F-006**): the root [`LICENSE`](LICENSE) is the
**Apache License 2.0**, while the inner
[`society_mgmt_300k/LICENSE/LICENSE.txt`](society_mgmt_300k/LICENSE/LICENSE.txt)
is the **MIT License**. This unresolved conflict is **documented, not resolved
here** — see [docs/security/README.md](docs/security/README.md) for the full
F-006 discussion and recommended resolution paths.
Source: LICENSE; Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1
