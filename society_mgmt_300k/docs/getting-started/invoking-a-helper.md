# Invoking a Helper

## Purpose

This page shows the fastest way to run a *helper* `mod_N_M(x)` and see its
result, with **no setup, no install, and no build**. Every *helper* in the
*corpus* is byte-identical — only the `mod_N_M` name changes — so the single
example on this page faithfully represents all 33,105 of them.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## The quick way (copy the helper)

Copy the *canonical contract* body from the single source of truth —
[Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md) —
into a Node.js session (or any `.js` file), then call it. That is the entire
quick start; the body is defined once on the canonical page and is not repeated
here. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

With the *helper* defined in scope, calling it produces:

```javascript
console.log(mod_0_0(5));    // => 40
console.log(mod_0_0(1));    // => 16
console.log(mod_0_0(0.5));  // => 3
```

Even results such as `5 -> 40` and `1 -> 16` earn the fixed bonus, while the
non-integer `0.5 -> 3` does not; see the
[canonical contract](../functional-flows/helper-computation.md) for the reason.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## Why you can't just require() it (no-exports caveat)

Copying the *helper* is not merely the easy path — it is the only path. Every
*module* file declares no `module.exports` and no `export`, so calling
`require('.../src/controllers/file_0.js')` returns an empty object `{}` and
exposes **none** of the helpers. To actually run a real *module*'s *helper*
you must either (a) copy the function — every body is identical, so any copy
is faithful — or (b) evaluate the file's contents in a Node REPL or via the
built-in `vm` module.
`Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10`

```javascript
// Module files have NO exports, so requiring one yields an empty object:
const mod = require('./src/controllers/file_0.js');
console.log(Object.keys(mod)); // => []  (no helpers exposed)

// Instead, copy the identical canonical helper (above) and call it,
// or evaluate the file's contents in a Node REPL / the `vm` module.
```

## Next steps

- [Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md) — the step-by-step *canonical contract*, including the single `r % 2 === 0` *critical path* decision.
- [Function contract](../reference/function-contract.md) — the signature, parameter, return type, and the executed input-to-output scenario table.
- [Expected behavior](../scenarios/expected-behavior.md) — the complete input-to-output envelope (integer, zero, negative, non-integer, string-coercion, and non-numeric).
- Contributors can lint every document from `society_mgmt_300k/` with `npm run docs:lint`.

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 — file structure (the `// mod_0` banner and the vestigial `const store = []`) and the verified no-exports behavior, where `require(...)` returns `{}`.
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical contract* *helper* body and its verified outputs (`5 -> 40`, `1 -> 16`, `0.5 -> 3`).
