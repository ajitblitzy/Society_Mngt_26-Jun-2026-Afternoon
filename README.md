# Society Management 300k Corpus

`society_mgmt_300k` is a **deterministically generated, synthetic JavaScript
corpus** — exactly **300,000 lines** across **29 `.js` files** that together
define **33,105 functions**, arranged in a nominal layered *scaffold* and
intended for **static analysis and traversal rather than execution** (Source:
first-hand repository scan `find . -name "*.js" -exec cat {} + | wc -l` = 300000;
AAP §0.3.1). It is not a runnable product: there is no entry point, framework, or
inter-module wiring (Source: first-hand repository scan; AAP §0.2.2, §1.2).

## What This Is / What This Is Not

This README uses an honest **verified-absence** framing: capabilities the code
does not have are reported as verified absences — confirmed by a first-hand scan
— rather than implied. Every technical claim below carries a source citation.

### What it is

- A **deterministic, synthetic JavaScript corpus** totaling exactly
  **300,000 lines** across **29 `.js` files** (Source: first-hand repository scan
  `find . -name "*.js" -exec cat {} + | wc -l` = 300000; AAP §0.3.1).
- **33,105 byte-identical arithmetic helper functions**, each computing
  **`6x + 10`** for an integer input `x` (Source:
  `society_mgmt_300k/src/controllers/file_0.js:L3-L11`).
- A **nominal layered directory *scaffold*** — nine `src/` layers (`config`,
  `controllers`, `domain`, `middleware`, `models`, `repositories`, `routes`,
  `services`, `utils`) plus a `tests/` tree (`unit`, `integration`) (Source:
  `society_mgmt_300k/src/**`; AAP §0.3.1).
- **License and documentation artifacts** — license files plus this `README.md`
  and the `docs/` documentation tree (Source: `/LICENSE:L1`;
  `society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3`).

A single *representative function* stands in for all 33,105 byte-identical
functions (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`):

```javascript
function mod_0_0(x){
 let r=0;
 r+=x*1;
 r+=x*2;
 r+=x*3;
 if(r%2===0){r+=10}
 return r;
}
```

### What it is not

- **Not a runnable application** — no entry point, framework, server, or wiring;
  nothing starts, listens, or runs (Source: first-hand repository scan;
  AAP §0.2.2, §1.2).
- **No exported or importable API** — the scan found **0** `module.exports` and
  **0** `require(` occurrences across `src/` and `tests/` (Source: first-hand
  repository scan; AAP §0.2.2).
- **No framework, server, database, network, or external input** beyond the
  numeric argument `x` (Source:
  `society_mgmt_300k/src/controllers/file_0.js:L3-L11`).
- **No configuration values** — despite its name, the `config/` layer holds the
  same arithmetic functions as every other layer (Source:
  `society_mgmt_300k/src/config/file_6.js:L1`).
- **No functional tests** — the `tests/` files contain the same arithmetic and
  **no assertions** (Source: AAP §0.3.1).
- **No dependencies or manifest** — there is **no `package.json`** or lockfile
  and zero third-party dependencies (Source: first-hand repository scan;
  AAP §0.2.1).

## Documentation

Full documentation lives under [`docs/`](docs/README.md). Start at the index
and follow the links to the topic you need:

- [Documentation index](docs/README.md) — navigation hub for all corpus
  documentation.
- [System overview](docs/overview.md) — what this corpus is and what it is not.
- [Architecture](docs/architecture.md) — the nominal layered *scaffold* and its
  edge-less containment diagram.
- [Functionality reference](docs/functionality/README.md) — arithmetic helpers,
  symbol namespace, module reference, store placeholder, and corpus sizing.
- [Performance](docs/performance.md) — constant-time `O(1)` per call, the dead
  always-true parity branch, and corpus scale.
- [Security](docs/security.md) — the verified-absence security posture and an
  operational note on setup-instruction secrets.
- [Licensing governance](docs/governance/licensing.md) — the Apache-vs-MIT
  license inconsistency and a recommended single-license resolution.

## Licensing

The repository contains two license files — an Apache License 2.0 at the root and
an MIT License inside the project subfolder (Source: `/LICENSE:L1`;
`society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3`). This **Apache-vs-MIT
inconsistency** is documented, and a single-license resolution is recommended, in
[`docs/governance/licensing.md`](docs/governance/licensing.md); it is flagged
only and not resolved here.

## Source citations

- **300,000 lines / 29 `.js` files / 33,105 functions**, arranged in the nominal
  layered *scaffold* — Source: first-hand repository scan
  (`find . -name "*.js" -exec cat {} + | wc -l` = 300000); AAP §0.3.1.
- **Representative function** computing **`6x + 10`**, byte-identical across the
  corpus — Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`.
- **No exported or importable API** (**0** `module.exports`, **0** `require(`),
  and no framework, server, database, network, dependencies, or manifest —
  Source: first-hand repository scan; AAP §0.2.1, §0.2.2.
- **The `config/` layer holds arithmetic, not configuration values** — Source:
  `society_mgmt_300k/src/config/file_6.js:L1`.
- **Apache 2.0 (repository root) vs MIT (project subfolder) license
  inconsistency** — Source: `/LICENSE:L1`;
  `society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3`.
