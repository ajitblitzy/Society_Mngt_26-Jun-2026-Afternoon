# Function Contract

## Purpose

This page is the input/output contract for the *corpus*'s single canonical
*helper*, `mod_N_M(x)`. Because all 33,105 *helper* functions across the
*corpus* share a byte-identical body — only the `mod_N_M` name differs — this
one *canonical contract* governs the behavior of every *module* in the
project. For the full step-by-step derivation of the body, see
[Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md).
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`. Reference:
`[1.2 System Overview §1.2.2]`.

## Signature

```text
mod_N_M(x) -> Number
```

The single argument `x` may be any JavaScript value — the *helper* performs no
input validation — and the return is always a `Number` (which may be `NaN`).
For the complete, annotated body behind this signature, see
[Helper Computation (Canonical Contract)](../functional-flows/helper-computation.md).
`Source: society_mgmt_300k/src/controllers/file_0.js:L3`

## Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x` | `Number` (any value accepted; coerced via `*`) | yes | the single operand; multiplied and summed to `6x` |

`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L7`

## Return

The *helper* returns a `Number`. For any integer `x` the result is `6x + 10`;
when `6x` is odd — which can only happen for a non-integer `x` — the result is
exactly `6x` with no bonus; and for non-numeric input the result is `NaN`.
`Source: society_mgmt_300k/src/controllers/file_0.js:L8-L9`

## Behavior contract

The *canonical contract* guarantees the following properties for every *helper*
in the *corpus*:

- Pure — the return value depends only on `x`, and the *helper* has no side
  effects; the module-level `const store = []` is never read or written.
  `Source: society_mgmt_300k/src/controllers/file_0.js:L2`
- Deterministic — the same input always produces the same output.
- O(1) time and space — a fixed number of arithmetic operations, no loops, and
  no input-dependent allocation.
- No input validation — `x` is never type-checked or defensively coerced.
- Never throws — there is no error branch; invalid input yields `NaN`, not an
  exception.

Reference: `[4.1 System Workflows §4.1.2]`.

## Scenario table

The following input-to-output pairs were executed against the *canonical
contract* body and verified exactly.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

| Input `x` | Output |
| --- | --- |
| `5` | `40` |
| `1` | `16` |
| `0` | `10` |
| `-2` | `-2` |
| `0.5` | `3` |
| `"2"` (numeric string) | `22` |
| `"abc"` (non-numeric) | `NaN` |
| `undefined` | `NaN` |
| `2.5` | `15` |
| `10` | `70` |

Coercion notes:

- Numeric strings coerce through the `*` operator (for example `"2"` becomes
  `r = 12`, which is even, so the result is `22`).
- Non-numeric input and `undefined` produce `NaN`; because `NaN % 2` is not
  `=== 0`, the fixed `+10` bonus is skipped and the *helper* returns `NaN`.
- Every integer yields `6x + 10`, since `6x` is always even for integer `x`.

## Worked examples

The three cases below span the behavior envelope — an even/integer input that
earns the `+10` bonus, a non-integer input whose `6x` is odd (no bonus), and a
non-numeric input that yields `NaN`. Each output matches the scenario table
above. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

```javascript
mod_N_M(10);    // => 70   integer: 6x = 60 is even, +10 bonus
mod_N_M(0.5);   // => 3    non-integer: 6x = 3 is odd, no bonus
mod_N_M("abc"); // => NaN  non-numeric: arithmetic yields NaN
```

- For the complete scenario envelope, see the Expected behavior scenarios reference (planned in a later documentation checkpoint).

## No-validation / no-throw note

The *helper* performs no type checking and contains no error branch. Invalid,
missing, or non-numeric input flows through exactly the same arithmetic path as
valid input and yields `NaN` rather than raising an exception, so a caller never
needs a `try`/`catch` around a *helper* call.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L2 — the vestigial
  `const store = []` placeholder, never read or written.
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical
  contract* *helper* body documented on this page.
- `[4.1 System Workflows §4.1.2]` — the single-decision (*critical path*)
  runtime flow this contract corresponds to.
