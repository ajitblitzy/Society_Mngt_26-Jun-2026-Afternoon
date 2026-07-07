# Expected Behavior (All Scenarios)

## Purpose

This page documents the complete input-to-output behavior envelope of the
*corpus*'s canonical *helper* `mod_N_M(x)` — every input scenario paired with
its exact, executed output. Because all 33,105 *helper* functions across the
*corpus* share a byte-identical body (only the `mod_N_M` name differs), these
scenarios describe the behavior of the whole *corpus*, not just one *module*.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

It complements the [Function contract](../reference/function-contract.md), with
which it shares the same scenario data, and is anchored in the
[Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md) —
the single source of truth for the *helper* body.

## How to read this

- Each row's `Output` is the **exact, executed** result produced by running
  the *canonical contract* body in Node.js — not an approximation or a rounded
  value. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`
- The *helper* is pure and deterministic, so the same input always yields the
  same output; there is no hidden state, randomness, or time dependence.
- The *helper* **never throws**. "Error-like" inputs (a non-numeric string or
  `undefined`) return `NaN` rather than raising an exception, because they flow
  through the exact same arithmetic path as valid input.
- In one line, each *helper* computes `r = 6x` and adds a fixed `10` when `6x`
  is even; the full derivation is not repeated here — see the
  [Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md).
  `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## Scenario table

The ten rows below were executed against the *canonical contract* body and
verified exactly; each pairs an input `x` with the *helper*'s returned value
and the scenario category it represents.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

| Input `x` | Output | Category |
| --- | --- | --- |
| `5` | `40` | positive integer (6x even → +10) |
| `1` | `16` | small integer |
| `0` | `10` | zero (0 is even → +10) |
| `-2` | `-2` | negative (−12 even → +10 → −2) |
| `0.5` | `3` | non-integer, 6x = 3 odd → no bonus |
| `"2"` | `22` | numeric string (coerces via `*`: r = 12 even → 22) |
| `"abc"` | `NaN` | non-numeric string → NaN |
| `undefined` | `NaN` | undefined → NaN |
| `2.5` | `15` | non-integer, 6x = 15 odd → no bonus |
| `10` | `70` | larger integer |

## Coercion notes

- Numeric strings coerce through the `*` operator: `"2"` becomes `r = 12`,
  which is even, so the fixed `+10` bonus applies and the result is `22`.
  `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`
- Non-numeric strings (for example `"abc"`) and `undefined` yield `NaN`,
  because the arithmetic `x*1`, `x*2`, and `x*3` produces `NaN` for these
  inputs. `Source: society_mgmt_300k/src/controllers/file_0.js:L4-L7`
- Since `NaN % 2` is not `=== 0`, the `+10` bonus is skipped for `NaN` inputs
  and the *helper* returns `NaN`.
  `Source: society_mgmt_300k/src/controllers/file_0.js:L8-L9`
- Every **integer** `x` yields `6x + 10`, because `6x` is always even for
  integer `x`. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## Edge and error scenarios

The scenarios below walk the full behavior envelope, grouped by input kind, so
every category the *corpus* can encounter is covered.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

- Integer — `1`, `5`, and `10` each return `6x + 10` (`16`, `40`, `70`),
  because `6x` is even for every integer.
- Zero — `0` is even, so it earns the bonus and returns `10`.
- Negative — `-2` gives `6x = −12` (even), so `−12 + 10 = −2`.
- Large magnitude — `10` returns `70`; the same `6x + 10` pattern generalizes
  to arbitrarily large integers, with no special casing or overflow handling.
- Non-integer — `0.5` gives `6x = 3` (odd → `3`) and `2.5` gives `6x = 15`
  (odd → `15`); when `6x` is odd the bonus is skipped.
- String-coercion — `"2"` coerces through `*` to `r = 12` (even) and returns
  `22`.
- Non-numeric — `"abc"` and `undefined` both return `NaN`.

There is **no thrown error and no error path** in the *corpus*. The single
`r % 2 === 0` decision — visualized in the
[Critical Path](../functional-flows/critical-path.md) — is the only branch, and
it has no error case. Non-numeric input is never rejected: it flows through the
same path as valid input and returns `NaN` instead of raising an exception, so
a caller never needs a `try`/`catch` around a *helper* call.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## Worked examples

The calls below were executed against the *canonical contract* body; each
`// =>` output matches the scenario table exactly.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

```javascript
mod_0_0(5);         // => 40   integer: 6x = 30 is even, +10 bonus
mod_0_0(0.5);       // => 3    non-integer: 6x = 3 is odd, no bonus
mod_0_0("2");       // => 22   numeric string: coerces to r = 12, even, +10
mod_0_0("abc");     // => NaN  non-numeric: arithmetic yields NaN
mod_0_0(undefined); // => NaN  undefined: arithmetic yields NaN
```

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L2 — the vestigial
  `const store = []` placeholder, never read or written.
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical
  contract* *helper* body whose executed outputs populate every scenario on
  this page.
- `[4.1 System Workflows §4.1.2]` — the single-decision (*critical path*)
  runtime flow this behavior envelope corresponds to.
