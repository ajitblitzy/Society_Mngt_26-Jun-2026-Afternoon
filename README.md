# society_mgmt_300k

`society_mgmt_300k` is a deterministic, **synthetic JavaScript corpus** of exactly **300,000 lines** spread across **29 `.js` files** and holding **33,105 near-identical functions** [Technical Specification §1.2.2]. Despite its "Society Management" name, it contains **no society-management — or any other — business logic**: every function does the same thing, returning **`6x + 10`** for an integer input `x` [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §1.2.1]. The repository exists to be read, navigated, and statically analyzed at scale rather than executed — there is no entry point, runtime, or framework [Technical Specification §1.2.2]. Read the name as a label on a box of repeated arithmetic, and start at the [documentation home](docs/index.md).

## What this is / what this is not

### What it is

- A **deterministic arithmetic helper corpus**: every function computes `6x + 10` and is pure, side-effect-free, and `O(1)`, with no loops, recursion, `throw`/`try`/`catch`, or `async`/`await` [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §4.3.3].
- A **layered directory layout by name only**: nine `src/` layers plus a `tests/` tree, where the familiar layer names are nominal labels with no imports, exports, classes, shared state, or calls between files [Technical Specification §5.4.2].
- A set of **generated test fixtures**: the files under `tests/unit` and `tests/integration` hold the same `mod_*` functions with no assertions and no test-runner code [Technical Specification §1.2.2].

### What it is not

- **Not a runnable application** — there is no `index.js`/`app.js`/`server.js`/`main.js` entry point, no runtime, and no framework [Technical Specification §1.2.2].
- **Not a web or API service** — there are no HTTP endpoints, route definitions, or request handlers anywhere in the tree [Technical Specification §5.4.2].
- **Not a data layer** — there are no schemas, data fields, or database access; the `models/`, `repositories/`, and `domain/` layers hold only arithmetic helpers [Technical Specification §1.2.2].
- **No configuration and no dependencies** — there is no configuration object, no `package.json`, and zero third-party dependencies [Technical Specification §1.2.2].

## Structure at a glance

The corpus is organized into **11 directories** — nine nominal `src/` layers plus two `tests/` directories. The counts below reconcile to **29 files**, **33,105 functions**, and exactly **300,000 lines** [Technical Specification §1.2.2].

| Directory | Files | Functions |
| --- | --- | --- |
| `society_mgmt_300k/src/config` | 2 | 2,400 |
| `society_mgmt_300k/src/middleware` | 3 | 3,105 |
| `society_mgmt_300k/src/models` | 3 | 3,600 |
| `society_mgmt_300k/src/controllers` | 3 | 3,600 |
| `society_mgmt_300k/src/routes` | 3 | 3,600 |
| `society_mgmt_300k/src/domain` | 2 | 2,400 |
| `society_mgmt_300k/src/services` | 3 | 3,600 |
| `society_mgmt_300k/src/repositories` | 2 | 2,400 |
| `society_mgmt_300k/src/utils` | 3 + `filler.js` | 3,600 |
| `society_mgmt_300k/tests/unit` | 2 | 2,400 |
| `society_mgmt_300k/tests/integration` | 2 | 2,400 |
| **Total** | **29** | **33,105** |

The grand total is exactly **300,000 lines** of JavaScript [Technical Specification §1.2.2]. The extra file counted in `src/utils` is `filler.js`, a **comment-only** file with **0 functions** that pads the corpus to that exact line count [society_mgmt_300k/src/utils/filler.js]. A full per-layer inventory is in the [source layout](docs/reference/source-layout.md).

## The one behavior

Every non-filler file follows one canonical shape: a header comment `// mod_<fileId> - society module` on line 1, an inert `const store = [];` on line 2 (declared but never read or written), then a run of `mod_<fileId>_<k>(x)` functions [society_mgmt_300k/src/config/file_6.js:L1-L10]. All 33,105 functions are byte-for-byte identical except for their names, so the single example below is representative of every one of them [society_mgmt_300k/src/config/file_6.js:L3-L10]:

```javascript
// representative of all 33,105 functions; returns 6x + 10
mod_6_0(2);  // => 22   (6*2 + 10)
mod_6_0(5);  // => 40   (6*5 + 10)
```

Each function accumulates `r = x*1 + x*2 + x*3` (which equals `6x`), then runs `if (r % 2 === 0) { r += 10 }` before returning `r`. Because `6x` is always even for integer input, the parity check is **always true**, the `+= 10` runs unconditionally, and the `else` path is a **dead, unreachable branch** — so each function effectively returns `6x + 10` [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §4.3.1]. See the [function reference](docs/reference/function-reference.md) for the full signature and flow.

## Documentation

Full documentation lives under [`docs/`](docs/index.md); the index is the master navigation hub for the whole set.

- [Documentation home](docs/index.md)
- [Overview](docs/getting-started/overview.md) · [Repository tour](docs/getting-started/repository-tour.md)
- [Architecture overview](docs/architecture/overview.md) · [Module pattern](docs/architecture/module-pattern.md)
- [Function reference](docs/reference/function-reference.md) · [Source layout](docs/reference/source-layout.md)
- [Performance](docs/performance.md) · [Security](docs/security.md) · [Glossary](docs/glossary.md)

## No build, run, or test

There is **nothing to install, build, run, or test**. The repository has no `package.json`, no runtime or framework, no build or CI configuration, and no test runner; the `tests/` directories are fixtures without assertions [Technical Specification §1.2.2]. The files are meant to be opened and read or fed to static-analysis tooling — see the [repository tour](docs/getting-started/repository-tour.md) for guidance on navigating the tree.

## Licensing

This repository contains **two conflicting license files**: the root `LICENSE` is the **Apache License 2.0** [LICENSE:L1-L2], while `society_mgmt_300k/LICENSE/LICENSE.txt` is the **MIT License** (Copyright (c) 2026) [society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3]. This inconsistency is a known governance issue [Technical Specification §1.3.3]; it is **not resolved here** and is recorded as an open item in [security](docs/security.md).
