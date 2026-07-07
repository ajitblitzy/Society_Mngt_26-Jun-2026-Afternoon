# Overview

## What this is

This repository is a synthetic, roughly 300,000-line JavaScript *corpus* built
from one tiny, repeated building block: a deterministic arithmetic *helper*
named `mod_N_M(x)`. Because all 33,105 *helper* functions across the *corpus*
share a byte-identical body — only the `mod_N_M` name changes — a single
*canonical contract* describes the whole project. Reference: `[1.2 System Overview]`.

Every *helper* takes one argument `x` and deterministically returns a `Number`.
It is pure, deterministic, and O(1): it performs no input validation, never
throws, and has no side effects. The exact arithmetic — the *canonical
contract* — is defined once in the single source of truth,
[Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md),
which this overview links to rather than restating.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## What this is not

The folder names *suggest* a running society-management application, but no such
application exists behaviorally. Framed honestly:

- **Not an application, API, or website** — nothing serves requests or renders a page.
- **No database, persistence, or cache** — and no file or network I/O of any kind.
- **No entry point, server, or CLI** — there is no `index.js`, `server.js`, or `app.js` to start.
- **No framework and no runtime dependencies** — the code is plain, dependency-free JavaScript.
- **Nominal folder names only** — the nine layers (`controllers/`, `routes/`, `models/`, `repositories/`, `config/`, and the rest) are organizational labels with no routing, schema, persistence, or configuration behavior behind them. Reference: `[5.1 High-Level Architecture §5.1.1]`.

## How the corpus is organized

The code lives under `src/` in nine nominal namespaces, with fixtures under
`tests/`:

- `src/` holds the nine namespaces — `controllers`, `services`, `routes`, `models`, `domain`, `repositories`, `middleware`, `config`, and `utils` — each containing flat *module* files whose only content is identical `mod_N_M(x)` *helpers*, and at runtime the *modules* are self-contained with zero references between them. Reference: `[5.1 High-Level Architecture §5.1.1]`.
- `tests/` holds `unit/` and `integration/` fixtures — the same *helpers* with no assertions, no runner, and no imports — so they are **static fixtures**, not a runnable suite. Reference: `[4.1 System Workflows §4.1.2]`.
- `src/utils/filler.js` is **comment-only** sizing padding with zero function declarations. `Source: society_mgmt_300k/src/utils/filler.js`
- `src/middleware/file_27.js` is a smaller *module* with **705** *helpers*, versus roughly 1,200 in a full *module*. `Source: society_mgmt_300k/src/middleware/file_27.js`

## Where to go next

- [Invoking a Helper](invoking-a-helper.md) — the setup-free quick start: copy a *helper* and call it.
- [Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md) — the step-by-step *canonical contract*, including the single `r % 2 === 0` *critical path* decision.
- [Architecture Overview](../architecture/overview.md) — the nominal-vs-as-implemented picture and the module-isolation diagram.
- [Limitations and caveats](../limitations-and-caveats.md) — the honest inventory of what the *corpus* is not.

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical contract* *helper* body (`r = 6x`; `+10` when `6x` is even), byte-identical across all 33,105 functions.
- Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 — the *module* file structure and the verified absence of any `require`/`import`/`export`.
- Source: society_mgmt_300k/src/utils/filler.js — comment-only sizing padding with zero function declarations.
- Source: society_mgmt_300k/src/middleware/file_27.js — the smaller *module* holding 705 *helpers* rather than the usual ~1,200.
- `[1.2 System Overview]` — the synthetic-corpus framing and the 33,105-function count.
- `[5.1 High-Level Architecture §5.1.1]` — the nominal-vs-as-implemented layering and module isolation.
- `[4.1 System Workflows §4.1.2]` — the single-decision runtime flow and the static-fixture nature of `tests/`.
