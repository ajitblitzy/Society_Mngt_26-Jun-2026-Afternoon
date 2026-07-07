# society_mgmt_300k

## What this is

`society_mgmt_300k` is a synthetic, roughly 300,000-line JavaScript *corpus* built
from a single repeated building block: a small, deterministic arithmetic *helper*
named `mod_N_M(x)`. Every *helper* takes one number `x` and returns a computed
`Number`. This behavior is the project's *canonical contract*, and it is
byte-identical across all 33,105 *helper* functions in the *corpus* — only the
`mod_N_M` name changes. The verbatim body and its step-by-step derivation are
defined once, in the single source of truth —
[Helper Computation (Canonical Contract)](docs/functional-flows/helper-computation.md) —
which this README links to rather than restating.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`. `Reference: [1.2 System Overview]`.

Each *helper* is pure, deterministic, and runs in `O(1)`: it performs no input
validation, never throws, and has no side effects. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`.

## What this is NOT

The folder names *suggest* a running society-management application, but no such
application exists behaviorally. To set expectations honestly:

- **Not an application, API, or website** — nothing serves HTTP requests, renders a page, or exposes an interface. `Reference: [5.1 High-Level Architecture]`.
- **No database, persistence, or cache** — there is no data store, and no file, network, or queue I/O of any kind. Each *module* even declares a `const store = [];` that is never read or written. `Source: society_mgmt_300k/src/controllers/file_0.js:L2`.
- **No entry point** — there is no `index.js`, `server.js`, or `app.js` to start. `Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`.
- **No framework and no runtime dependencies** — the code is plain, dependency-free JavaScript. `Reference: [5.1 High-Level Architecture]`.
- **No module wiring** — there is not a single `require`, `import`, `export`, or `module.exports` anywhere; every *module* is self-contained with zero references to any other. `Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`.
- **Nominal folder names only** — the nine `src/` layers (`controllers/`, `services/`, `routes/`, `models/`, `domain/`, `repositories/`, `middleware/`, `config/`, `utils/`) are organizational labels that imply an MVC application which does not exist; there is no routing, schema, persistence, or configuration behavior behind them. `Reference: [5.1 High-Level Architecture]`.

## Repository layout

The code lives under `src/` in nine nominal namespaces, with static fixtures under `tests/`:

```text
society_mgmt_300k/
├── src/                  # nine nominal namespaces (organizational labels only)
│   ├── controllers/
│   ├── services/
│   ├── routes/
│   ├── models/
│   ├── domain/
│   ├── repositories/
│   ├── middleware/       # file_27.js is smaller (705 helpers)
│   ├── config/
│   └── utils/            # includes filler.js (comment-only padding)
├── tests/                # static fixtures — no runner, no assertions, no imports
│   ├── unit/
│   └── integration/
├── docs/                 # the documentation set (start at docs/README.md)
├── LICENSE/              # MIT license text
└── README.md             # you are here
```

- The *corpus* contains **28** `mod_*` *modules* in total — 24 under `src/` and 4 under `tests/` — plus `src/utils/filler.js`. `Reference: [1.2 System Overview]`.
- A full *module* holds roughly **1,200** *helpers*; `src/middleware/file_27.js` is smaller, with **705**. `Source: society_mgmt_300k/src/middleware/file_27.js`.
- `src/utils/filler.js` is **comment-only** sizing padding with zero function declarations. `Source: society_mgmt_300k/src/utils/filler.js`.
- `tests/unit/` and `tests/integration/` contain the same *helpers* as **static fixtures** — no assertions, no test runner, and no imports. `Reference: [4.1 System Workflows §4.1.2]`.

## Quick start (no setup required)

You do not need to install or build anything to see what a *helper* does. Because
every *helper* shares the same *canonical contract*, copy the verbatim body from
the single source of truth —
[Helper Computation (Canonical Contract)](docs/functional-flows/helper-computation.md) —
into any JavaScript environment (for example, `node -e` or the browser console),
then call it. The canonical page holds the body, so it is not repeated here.

With the *helper* defined in scope, calling it produces:

```javascript
console.log(mod_0_0(5));    // => 40
console.log(mod_0_0(1));    // => 16
console.log(mod_0_0(0.5));  // => 3
```

**Honest caveat:** you cannot `require()` the *helpers* directly. The *module*
files declare no `module.exports` or `export`, so
`require('./src/controllers/file_0.js')` returns an empty object `{}`. To exercise
a real *module*'s *helper*, copy the function (they are all identical) or evaluate
the file's contents inside a Node REPL or `vm` context. `Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`. For a step-by-step walkthrough, see [Invoking a helper](docs/getting-started/invoking-a-helper.md).

## Documentation

Full documentation lives in [`docs/`](docs/README.md) and is organized for
progressive disclosure — start with the overview, then the functional flows, then
the reference:

- [Documentation index](docs/README.md) — the complete table of contents.
- [Getting started: overview](docs/getting-started/overview.md) — what the *corpus* is and is not.
- [Functional flows (incl. critical path)](docs/functional-flows/README.md) — the runtime flow and the single `r % 2 === 0` *critical path* decision.
- [Function contract & scenarios](docs/reference/function-contract.md) — the input-to-output *canonical contract*.
- [Module index](docs/reference/module-index.md) — every *module* mapped by namespace.
- [Architecture overview](docs/architecture/overview.md) — nominal layers versus the as-implemented flat *module* set.
- [Expected behavior scenarios](docs/scenarios/expected-behavior.md) — the full input envelope, including edge and error cases.
- [Limitations & caveats](docs/limitations-and-caveats.md) — what the *corpus* deliberately does not do.

## Contributing to the docs

The documentation is Markdown with embedded Mermaid diagrams and is validated with
lightweight tooling. From `society_mgmt_300k/`, install the documentation tooling
and run the checks:

```text
npm install
npm run docs:lint        # Markdown style (markdownlint-cli2)
npm run docs:linkcheck   # internal link integrity (markdown-link-check)
```

These scripts and their pinned `devDependencies` are declared in
[`package.json`](package.json); no application or runtime dependencies are added.

## License

Released under the MIT License — see [`LICENSE/LICENSE.txt`](LICENSE/LICENSE.txt).

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical contract* body (`r = 6x`; `+10` when `6x` is even), byte-identical across all 33,105 functions.
- Source: society_mgmt_300k/src/controllers/file_0.js:L2 — the vestigial `const store = [];`, never read or written.
- Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 — the *module* file structure and the verified absence of any `require`/`import`/`export`/`module.exports`.
- Source: society_mgmt_300k/src/middleware/file_27.js — the smaller *module* holding 705 *helpers* rather than the usual ~1,200.
- Source: society_mgmt_300k/src/utils/filler.js — comment-only sizing padding with zero function declarations.
- `[1.2 System Overview]` — the synthetic-corpus framing, the 33,105-function count, and the module inventory.
- `[5.1 High-Level Architecture]` — the nominal-vs-as-implemented layering and module isolation.
- `[4.1 System Workflows §4.1.2]` — the static-fixture nature of `tests/`.
