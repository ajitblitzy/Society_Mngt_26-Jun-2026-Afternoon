# Overview

← Back to the [documentation hub](./README.md)

## Purpose

This document orients a reader to the synthetic `society_mgmt_300k` JavaScript
*corpus*: what it is, how it is structured, and — just as importantly — what it
is **not**. It uses an honest **verified-absence** framing: every capability the
code does not have is reported as a *verified absence* (confirmed by a first-hand
scan of the source) rather than implied. Every technical claim below carries a
source citation to a code `path:line`, a repository scan, or a Technical
Specification / Agent Action Plan (AAP) section, so any statement can be traced
back to verifiable evidence.

## What This Is

`society_mgmt_300k` is a **deterministically generated, synthetic JavaScript
corpus** — a body of code produced to a fixed size and shape, not a runnable
product:

- **A 300,000-line corpus.** The source totals exactly **300,000 lines** of
  JavaScript. Source: repository scan
  (`find . -name "*.js" -exec cat {} + | wc -l` = 300000); Tech Spec §1.2.
- **29 files defining 33,105 functions.** The corpus comprises **29 `.js` files**
  that together define **33,105 functions**. Source: first-hand repository scan;
  AAP §0.3.1.
- **Byte-identical arithmetic helpers.** Every function is **byte-identical** and
  computes **`6x + 10`** for an integer input `x`: the canonical body accumulates
  `r = x*1 + x*2 + x*3` (`= 6x`) and then adds `10`. One *representative function*
  therefore stands in for all 33,105 functions; they are never enumerated
  individually. Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`.

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

- **A nominal layered scaffold.** The files are arranged into a directory
  *scaffold* of **nine `src/` layers** (`config`, `controllers`, `domain`,
  `middleware`, `models`, `repositories`, `routes`, `services`, `utils`) plus a
  **`tests/`** tree of two layers (`unit`, `integration`). The layer names are
  organizational only and carry **no inter-layer wiring**. Source:
  `society_mgmt_300k/src/routes/file_3.js:L1-L11`; Tech Spec §1.2.2, §2.2.4.
- **License and documentation artifacts.** Alongside the source, the repository
  includes license files — an Apache 2.0 license at the repository root and an MIT
  license inside the project subfolder — and Markdown documentation: a top-level
  `README.md` and this `docs/` tree. These are the notable non-source artifacts,
  not an exhaustive inventory of every tracked file. Source: `/LICENSE:L1`;
  `society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3`; first-hand repository scan.

## What This Is NOT (Verified Absence)

Each of the following is **verified absent** — confirmed by a first-hand scan, not
merely undocumented or assumed:

- **Not a runnable application.** There is no entry point and no application
  wiring; nothing starts, listens, or runs. Source: first-hand repository scan;
  AAP §0.2.2; Tech Spec §1.2.
- **No exported or importable API.** The scan found **0** occurrences of
  `module.exports` and **0** of `require(` across `src/` and `tests/`, so nothing
  is exportable and no other code can import the corpus. Source: repository scan
  (0 exports / 0 imports); AAP §0.2.2.
- **No framework, server, database, network, or filesystem.** The corpus performs
  only in-memory integer arithmetic; there is no external input beyond the numeric
  argument `x`. Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`;
  first-hand repository scan.
- **No configuration values.** Despite its name, the `config/` layer holds the
  same arithmetic functions as every other layer — no credentials, connection
  strings, or tunable settings. Source:
  `society_mgmt_300k/src/config/file_6.js:L1`.
- **No functional tests or assertions.** The `tests/` files contain the same
  arithmetic functions and **no assertions**; they are not functional tests.
  Source: Tech Spec §1.2.2; AAP §0.3.1.
- **No dependencies or manifest.** There is **no `package.json`** or lockfile and
  **zero** third-party dependencies. Source: first-hand repository scan;
  AAP §0.2.1.
- **No build pipeline.** No build, bundling, or CI configuration exists; this
  documentation renders natively on GitHub with no build step. Source: first-hand
  repository scan; AAP §0.2.1.

## Key Facts

The table below summarizes the corpus at a glance. The figures are drawn from the
first-hand repository scan and AAP §0.3.1; the line total is from the source scan
(`wc -l` = 300000) and Tech Spec §1.2; the representative function is from
`society_mgmt_300k/src/controllers/file_0.js:L3-L11`.

| Property | Value |
| --- | --- |
| Total source lines | 300,000 |
| Source files (`.js`) | 29 |
| Functions defined | 33,105 |
| `src` layers | 9 |
| `tests` layers | 2 |
| Representative function | `mod_<fileId>_<k>(x) → 6x + 10` |
| Exported / importable API | None (0 `module.exports`, 0 `require(`) |
| Third-party dependencies | None (no `package.json`) |

## How To Read This Documentation

This document is the system overview. From here, follow the links below into the
rest of the documentation tree (every document also links back to the index):

- **[Architecture](./architecture.md)** — the nominal layered *scaffold* and an
  edge-less containment diagram showing the absence of inter-layer wiring.
- **[Functionality](./functionality/README.md)** — the index of functionality
  topics: the *representative function* contract, the symbol namespace, the
  per-layer module reference, the `store` placeholder, and corpus sizing.
- **[Performance](./performance.md)** — constant-time `O(1)` per call, the dead
  always-true parity branch, and corpus scale.
- **[Security](./security.md)** — the verified-absence security posture and an
  operational note on setup-instruction secrets.
- **[Licensing governance](./governance/licensing.md)** — the Apache-vs-MIT
  license inconsistency and a recommended single-license resolution.
- **[Documentation index](./README.md)** — the top-level navigation hub for all
  corpus documentation.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L3-L11` — the canonical,
  byte-identical function body computing `6x + 10`; the *representative function*
  for all 33,105 functions.
- `society_mgmt_300k/src/routes/file_3.js:L1-L11` — a representative layer file
  showing the self-contained, no-imports/no-exports file shape of the nominal
  layered scaffold.
- `society_mgmt_300k/src/config/file_6.js:L1` — the `config/` layer holds
  arithmetic functions, not configuration values.
- First-hand repository scan — 29 `.js` files, 33,105 functions, **0**
  `module.exports`, **0** `require(`, and no `package.json` or lockfile; the
  300,000-line total (`find . -name "*.js" -exec cat {} + | wc -l` = 300000).
- `/LICENSE:L1`; `society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3` — the Apache 2.0
  (root) vs MIT (project subfolder) license inconsistency; flagged only, see the
  [licensing governance](./governance/licensing.md) document.
- Tech Spec §1.2, §1.2.2, §2.2.4 — the synthetic corpus, its scale, and the
  nominal layered scaffold with no inter-layer wiring.
- AAP §0.2.1, §0.2.2, §0.3.1 — the documentation/dependency assessment and the
  per-layer file/function inventory.

---

← Back to the [documentation hub](./README.md)
