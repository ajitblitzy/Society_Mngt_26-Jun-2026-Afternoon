# Society Management 300k Corpus

A deterministic, **synthetic JavaScript corpus** (`society_mgmt_300k`)
deliberately sized to exactly **300,000 lines** across **29 `.js` files** and
**33,105 functions**, organized into a nominal layered scaffold. It exists for
static analysis and code traversal rather than execution — there is no runnable
application.
(Source: `society_mgmt_300k/**/*.js`; AAP §0.3.1, §1.2)

## What This Is / What This Is Not

### What it is

- A **deterministic, synthetic JavaScript corpus** of exactly 300,000 lines
  spread across 29 `.js` files and 33,105 functions.
  (Source: `society_mgmt_300k/**/*.js`; AAP §0.3.1)
- A collection of **byte-identical arithmetic helper functions**: every
  function is the same representative function, which computes `6x + 10` for an
  integer input `x`.
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`)
- A **nominal layered directory scaffold** — nine `src/` layers (`config`,
  `controllers`, `domain`, `middleware`, `models`, `repositories`, `routes`,
  `services`, `utils`) plus a `tests/` tree (`unit`, `integration`).
  (Source: `society_mgmt_300k/src/**`; AAP §0.3.1)
- A set of **license and documentation artifacts** (see
  [Documentation](#documentation) and [Licensing](#licensing) below).
  (Source: `/LICENSE`, `society_mgmt_300k/LICENSE/LICENSE.txt`)

The single representative function — identical across all 33,105 occurrences —
is:

```javascript
function mod_0_0(x) {
  let r = 0;
  r += x * 1;
  r += x * 2;
  r += x * 3;
  if (r % 2 === 0) { r += 10; }
  return r;
}
```

(Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`)

### What it is not

- **Not a runnable application** — there is no entry point, framework, server,
  or inter-module wiring.
  (Source: `society_mgmt_300k/**/*.js`; AAP §0.2.2, §1.2)
- **No exported or importable API** — there are zero `module.exports` and zero
  `require(...)` occurrences across the corpus; every symbol is module-local.
  (Source: `society_mgmt_300k/**/*.js`; AAP §0.2.2)
- **No framework, server, database, network, or external input** beyond the
  single numeric argument `x`. (Source: `society_mgmt_300k/**/*.js`; AAP §1.2)
- **No configuration values** — the `config/` layer holds arithmetic
  functions, not configuration.
  (Source: `society_mgmt_300k/src/config/file_6.js:L1-L11`; AAP §0.2.2)
- **No functional tests** — the files under `tests/` contain no assertions.
  (Source: `society_mgmt_300k/tests/**`; AAP §0.3.1)
- **No dependency manifest** — there is no `package.json` or lockfile.
  (Source: AAP §0.2.1)

This README uses an honest **verified-absence** framing: it documents only what
a first-hand scan of the corpus confirms and does not imply capabilities the
code does not have.

## Documentation

Full documentation lives under [`docs/`](docs/README.md). Begin at the index
and follow the topic links below:

- [Documentation index / navigation hub](docs/README.md)
- [System overview](docs/overview.md)
- [Layered scaffold & architecture](docs/architecture.md)
- [Functionality reference](docs/functionality/README.md) — arithmetic
  helpers, symbol namespace, module reference, store placeholder, and corpus
  sizing
- [Performance characteristics](docs/performance.md)
- [Security posture](docs/security.md)
- [Licensing governance](docs/governance/licensing.md) — the Apache-vs-MIT
  inconsistency

## Licensing

This repository contains license artifacts in two locations, and they are
currently **inconsistent**: the root [`LICENSE`](LICENSE) is the **Apache
License 2.0**, while the project copy
[`society_mgmt_300k/LICENSE/LICENSE.txt`](society_mgmt_300k/LICENSE/LICENSE.txt)
is the **MIT License**. This discrepancy is documented — not resolved here —
in [Licensing governance](docs/governance/licensing.md).
(Source: `/LICENSE:L1`, `society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3`)
