# Limitations and Caveats

## Purpose

This page states plainly what the `society_mgmt_300k` *corpus* is **not**, so
that its nominal folder taxonomy (`controllers/`, `services/`, `routes/`, and
the rest) is never misread as a running application. The *corpus* is a
synthetic, dependency-free JavaScript project whose only real behavior is a
single arithmetic *helper* — `mod_N_M(x)` — repeated, byte-for-byte identical,
across every file. Everything below is framed as an honest absence: each
"no X" note reflects a verified source fact, not a missing feature waiting to be
built. `Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`

For the complete enumeration of files this page refers to, see the
[module index](reference/module-index.md).

## No entry point

There is no runnable entry point anywhere in the *corpus*: no `index.js`,
`server.js`, or `app.js`, no `cmd/` directory, and no `package.json` `main`
field for the code. Nothing "starts" the *corpus* — there is no process to
launch, no server to bind, and no CLI to invoke. The only `package.json` in the
tree is the documentation-tooling manifest at `../package.json`, which declares
no `main` and no runtime dependencies.
`Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`
`[4.1 System Workflows §4.1.1]`

## No module wiring or exports

No *module* imports, requires, or exports anything. A repository-wide search
finds zero `require(`, zero `import`, zero `export`, and zero `module.exports`
statements across all of `../src/**` and `../tests/**`. Each `mod_N_M(x)`
*helper* is a top-level function symbol that becomes reachable only when a host
parses the file directly; it is never published through the module system.
`Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`

As a direct consequence, calling `require('../src/controllers/file_0.js')` from
Node returns an empty object `{}` and exposes none of the helpers. To run a
*helper*, copy its body (every *helper* corpus-wide is identical) or evaluate
the file in a REPL or a `vm` context.
`Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`

## No framework and no runtime dependencies

The *corpus* uses no web, CLI, or test framework and pulls in no runtime
libraries — it is entirely dependency-free. The nine `src/` namespaces contain
nothing but plain arithmetic *helpers*. The only dependencies declared anywhere
in the repository are documentation `devDependencies` (for Markdown linting,
link checking, and Mermaid rendering) in `../package.json`; these support the
docs only and never touch the code.
`Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`
`[3.1 Programming Languages]` `[5.1 High-Level Architecture §5.1.1]`

## No persistence, database, or cache

The *corpus* performs no persistence and no I/O: there is no database, no cache,
no file store, and no network access. Every *module* declares a module-scoped
`const store = [];` on its second line, but that array is a **dead placeholder**
— it is never read from and never written to by any *helper*. It exists only as
part of the uniform *module* template and has no runtime effect.
`Source: society_mgmt_300k/src/controllers/file_0.js:L2`

## Nominal layer names are organizational only

The nine `src/` folder names imply a conventional layered / MVC application, but
that structure is nominal only. At runtime every *module* is a flat, isolated,
import-free collection of identical arithmetic *helpers* with zero edges between
modules. The table below maps each nominal layer to its as-implemented reality.
`[5.1 High-Level Architecture §5.1.1]`

| Nominal layer | Implied role | As-implemented reality |
| --- | --- | --- |
| `controllers/`, `services/`, `domain/` | app/business logic | identical arithmetic helpers only |
| `routes/` | HTTP routing | **no HTTP routing exists** |
| `models/` | data schema | **no data schema exists** |
| `repositories/` | persistence access | **no persistence access exists** |
| `config/` | configuration values | **no configuration values exist** |
| `middleware/` | request middleware | identical helpers; `file_27.js` has 705 (smaller) |
| `utils/` | utilities | identical helpers + `filler.js` (comment-only padding) |

The two size notes above are verified directly against source: `file_27.js`
holds 705 *helpers* rather than the usual ~1,200, and `filler.js` contains only
`// filler` comment lines with zero function declarations.
`Source: society_mgmt_300k/src/middleware/file_27.js`
`Source: society_mgmt_300k/src/utils/filler.js`

## Tests are static fixtures, not an executable suite

The files under `../tests/unit/**` and `../tests/integration/**` are **static
fixtures**, not a runnable test suite. `tests/unit/file_9.js`,
`tests/unit/file_20.js`, `tests/integration/file_10.js`, and
`tests/integration/file_21.js` each contain the same `mod_N_M(x)` *helpers* as
the `src/` modules, with **no assertions, no test runner, no imports, and no**
`expect` / `describe` / `it` calls. Executing them runs nothing meaningful —
they define functions and never invoke them.
`Source: society_mgmt_300k/tests/unit/file_9.js:L1-L10`
`[4.1 System Workflows §4.1.2]`

## What IS guaranteed

Exactly one real behavior is guaranteed, and it is uniform across all 33,105
functions in the *corpus*: every *helper* shares one byte-identical body. That
body — the *canonical contract* — is defined once in the single source of
truth, [Helper Computation (Canonical Contract)](functional-flows/helper-computation.md),
and is intentionally not restated here.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

Stated as properties rather than code, every *helper* is **pure, deterministic,
and O(1)**, performs no input validation, has no side effects, and never throws.
For any input it returns a `Number` — which is `NaN` when `x` cannot be coerced
to a number. This single behavior is also the *corpus*'s only *critical path*.
See the [canonical contract](functional-flows/helper-computation.md) for the
full signature, the step-by-step derivation, worked examples, and the complete
input-to-output scenario table.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## See also

- [Canonical contract](functional-flows/helper-computation.md) — the single guaranteed *helper* behavior in full detail.
- [Architecture overview](architecture/overview.md) — the nominal-versus-actual layering and the module-isolation picture.
- [Data flow](architecture/data-flow.md) — the single in-process flow and the absence of any data store.
- [Module index](reference/module-index.md) — the full enumeration of all 28 `mod_*` modules by namespace.
- Back to the [Documentation index](README.md).

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L1 — the `// mod_N` module banner comment that heads every *module*.
- Source: society_mgmt_300k/src/controllers/file_0.js:L2 — the vestigial `const store = []` placeholder, never read or written.
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical contract* *helper* body (`r = 6x`; `+10` when `6x` is even) guaranteed corpus-wide.
- Source: society_mgmt_300k/src/middleware/file_27.js — the smaller *module* with 705 *helpers* rather than the usual ~1,200.
- Source: society_mgmt_300k/src/utils/filler.js — comment-only sizing padding with zero function declarations.
- Source: society_mgmt_300k/tests/unit/file_9.js:L1-L10 — a representative test *fixture*: the same *helpers* with no assertions, runner, or imports.
- `[4.1 System Workflows §4.1.1-§4.1.2]` — the single-decision runtime flow and the fixture nature of `tests/`.
- `[5.1 High-Level Architecture §5.1.1]` — the nominal-versus-actual layering and module isolation.
- `[3.1 Programming Languages]` — the dependency-free, framework-free baseline.
