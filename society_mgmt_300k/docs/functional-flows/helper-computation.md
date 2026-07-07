# Helper Computation (Canonical Contract)

## Purpose

Every runtime behavior in this *corpus* comes from one tiny building block:
a *helper* named `mod_N_M(x)` — for example `mod_0_0`, `mod_0_1`, and so on
inside the `controllers` *module*. A *helper* takes a single argument `x`,
runs a fixed sequence of arithmetic steps, and returns a `Number`. There is
no other logic anywhere in the code: no input/output, no shared state, and
no branching beyond a single parity check.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

Because all 33,105 *helper* functions across the *corpus* share a
byte-identical body (only the `mod_N_M` name changes), documenting one
function documents them all. This page is therefore the *canonical
contract* — the single source of truth for what any *helper* does — and
every other document in this set links back here instead of repeating the
behavior. Reference: `[1.2 System Overview §1.2.2]`.

## Signature

```text
mod_N_M(x) -> Number
```

- `x` — any JavaScript value. The *helper* performs no input validation,
  so `x` may be a number, a numeric string such as `"2"`, a non-numeric
  string, `undefined`, or anything else.
  `Source: society_mgmt_300k/src/controllers/file_0.js:L3`
- Return — a `Number`. For numeric (or numeric-coercible) input the result
  is a finite number; for non-numeric input the result is `NaN`, which is
  still of type `Number`.
  `Source: society_mgmt_300k/src/controllers/file_0.js:L9`

## Step-by-step

The *helper* body runs top to bottom with no early returns. The walkthrough
below shows the running value of the accumulator `r` after each statement,
treating `x` as the input.
`Source: society_mgmt_300k/src/controllers/file_0.js:L4-L9`

- `let r = 0;` — start the accumulator at zero, so `r = 0`.
- `r += x*1;` — add one times `x`, so now `r = x`.
- `r += x*2;` — add two times `x`, so now `r = 3x`.
- `r += x*3;` — add three times `x`, so now `r = 6x` (the three additions
  always sum to `6x`).
- `if (r % 2 === 0) { r += 10 }` — the single *critical path* decision:
  when `6x` is even, add a fixed `+10` bonus; otherwise leave `r` unchanged.
- `return r;` — return the final accumulator.

The verbatim body, exactly as it appears in the source, is:

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

`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

- See the [critical path flowchart](critical-path.md) for the visual
  decision flow.

## Canonical contract

The input-to-output rule is small enough to state completely:

- For any integer `x`, `6x` is always even (because `6` is even), so the
  parity check succeeds and the result is `6x + 10`.
  Example: `mod(5) = 30 + 10 = 40`.
- For a non-integer `x` whose `6x` is odd — for instance `x = 0.5`, where
  `6x = 3` — the parity check fails and the result is exactly `6x` with no
  bonus. Example: `mod(0.5) = 3`.
- Parity is tested with the `%` operator. For non-numeric input the
  arithmetic produces `NaN`, and `NaN % 2 === 0` evaluates to `false`, so
  no bonus is added and the *helper* returns `NaN`.
  Example: `mod("abc") = NaN`.

The *canonical contract* also fixes these properties, which hold for every
*helper* in the *corpus*:

- Pure — the return value depends only on `x`; nothing outside the function
  is read.
- Deterministic — the same `x` always produces the same result.
- O(1) time and space — a fixed number of arithmetic operations, no loops,
  and no allocation that grows with the input.
- No input validation — `x` is never checked or defensively coerced.
- Never throws — there is no code path that raises an error; invalid input
  yields `NaN`, not an exception.
- No side effects — the module-level `const store = []` declared just above
  the *helper* is never read or written; it is a vestigial, dead
  placeholder. `Source: society_mgmt_300k/src/controllers/file_0.js:L2`

## Worked examples

The results below were executed against the *canonical contract* body and
verified. Each row shows an input `x` and the exact value returned by
`mod_N_M(x)`. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

| Input `x` | Result | Why |
| --- | --- | --- |
| `5` | `40` | integer, `6x = 30` even, `+10` |
| `1` | `16` | integer, `6x = 6` even, `+10` |
| `0` | `10` | integer, `6x = 0` even, `+10` |
| `-2` | `-2` | integer, `6x = -12` even, `+10` |
| `0.5` | `3` | non-integer, `6x = 3` odd, no bonus |
| `2.5` | `15` | non-integer, `6x = 15` odd, no bonus |
| `"2"` | `22` | numeric string, `6x = 12` even, `+10` |
| `"abc"` | `NaN` | non-numeric, arithmetic is `NaN` |

To reproduce these results, paste the *canonical contract* body into Node
and call it directly:

```javascript
function mod_0_0(x){
 let r=0;
 r+=x*1;
 r+=x*2;
 r+=x*3;
 if(r%2===0){r+=10}
 return r;
}

mod_0_0(5);     // => 40
mod_0_0(0.5);   // => 3
mod_0_0("abc"); // => NaN
```

For the complete input envelope — including large magnitudes, additional
string-coercion cases, and `undefined` — see the
[Expected behavior scenarios](../scenarios/expected-behavior.md).

## See also

- [Critical path flowchart](critical-path.md) — the visual decision flow
  for the single `r % 2 === 0` branch.
- [Function contract](../reference/function-contract.md) — the same
  behavior as a formal signature and scenario reference.
- [Expected behavior scenarios](../scenarios/expected-behavior.md) — the
  exhaustive input-to-output table.

## Source Citations

- Source: society_mgmt_300k/src/controllers/file_0.js:L2 — the vestigial
  `const store = []` placeholder, never read or written.
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the *canonical
  contract* *helper* body documented on this page.
- `[4.1 System Workflows §4.1.2]` — the single-decision runtime flow this
  contract corresponds to.
