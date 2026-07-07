# society_mgmt_300k Documentation

## About this documentation

This set documents the *functional flows* of the **society_mgmt_300k** synthetic JavaScript *corpus*, whose behavior everywhere reduces to a single *canonical contract*: every *helper* computes `r = 6x` and, when `6x` is even, adds a fixed bonus of `10` before returning `r` (`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`). That behavior is pure, deterministic, `O(1)`, performs no input validation, never throws, and is identical across all 33,105 functions in the corpus. The documents are organized for progressive disclosure — start with a plain-language overview, move through the functional flows, and finish with the detailed reference — so a first-time reader can go from zero to a complete understanding without reading everything at once.

## Recommended reading order

New to the corpus? Read the documents in this order:

1. [Getting started — Overview](getting-started/overview.md) — what the corpus is, and what it is not.
2. [Invoking a helper (quick start)](getting-started/invoking-a-helper.md) — load a module and call a helper.
3. [Functional flows — Critical path](functional-flows/critical-path.md) — the single decision that shapes every result.
4. [Helper computation (canonical contract)](functional-flows/helper-computation.md) — the step-by-step behavior in detail.
5. [Reference — Function contract](reference/function-contract.md) and [Expected behavior (all scenarios)](scenarios/expected-behavior.md) — the input-to-output contract and every scenario.
6. [Architecture overview](architecture/overview.md) — the nominal layer names versus the as-implemented flat module set.
7. [Limitations and caveats](limitations-and-caveats.md) — what the corpus deliberately does not do.

## Table of contents

- **Getting started**
  - [Overview](getting-started/overview.md)
  - [Invoking a helper (quick start)](getting-started/invoking-a-helper.md)
- **Functional flows**
  - [Functional flows index](functional-flows/README.md)
  - [Critical path](functional-flows/critical-path.md)
  - [Helper computation (canonical contract)](functional-flows/helper-computation.md)
  - [Module invocation sequence](functional-flows/module-invocation-sequence.md)
- **Reference**
  - [Function contract](reference/function-contract.md)
  - [Module index](reference/module-index.md)
  - [Namespace: controllers](reference/namespaces/controllers.md)
  - [Namespace: services](reference/namespaces/services.md)
  - [Namespace: routes](reference/namespaces/routes.md)
  - [Namespace: models](reference/namespaces/models.md)
  - [Namespace: domain](reference/namespaces/domain.md)
  - [Namespace: repositories](reference/namespaces/repositories.md)
  - [Namespace: middleware](reference/namespaces/middleware.md)
  - [Namespace: config](reference/namespaces/config.md)
  - [Namespace: utils](reference/namespaces/utils.md)
- **Architecture**
  - [Architecture overview](architecture/overview.md)
  - [Data flow](architecture/data-flow.md)
- **Scenarios**
  - [Expected behavior (all scenarios)](scenarios/expected-behavior.md)
- **Limitations**
  - [Limitations and caveats](limitations-and-caveats.md)

## Glossary

- **Corpus** — the complete society_mgmt_300k source tree (all `src/` and `tests/` files taken together).
- **Module** — a single `mod_N` file (for example, `src/controllers/file_0.js`) that contains many top-level helpers.
- **Helper** — one `mod_N_M(x)` function; the smallest unit of behavior and the subject of the canonical contract.
- **Critical path** — the one decision point (`r % 2 === 0`) that determines whether the fixed bonus of `10` is added.
- **Canonical contract** — the single input-to-output behavior shared by every helper: `r = 6x`, plus `10` when `6x` is even.

## How to validate these docs

From `society_mgmt_300k/`, run `npm run docs:lint` to check Markdown style and `npm run docs:linkcheck` to verify that every internal link resolves.
