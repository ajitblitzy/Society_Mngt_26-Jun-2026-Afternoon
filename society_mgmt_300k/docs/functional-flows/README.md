# Functional Flows

## Overview

This subtree documents the single genuine runtime process of the *corpus*: a
Host loads a *module*, calls a *helper* named `mod_N_M(x)`, the *helper*
computes `r = 6x`, performs one parity check, and returns `r`. Because every
*helper* is byte-identical across all 33,105 functions, this one flow
describes the entire runtime behavior of the system.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`. Together these
pages hold the *canonical contract* — what a *helper* computes — and highlight
the *critical path*, the single `r % 2 === 0` decision that shapes every
result. Reference: `[4.1 System Workflows §4.1.1]`.

## Recommended reading order

1. [Helper Computation (Canonical Contract)](helper-computation.md) — start here; the *canonical contract* and a step-by-step walkthrough of what every *helper* computes.
2. [Critical Path](critical-path.md) — the single `r % 2 === 0` decision that determines each output, illustrated with a flowchart.
3. [Module Invocation Sequence](module-invocation-sequence.md) — how a Host loads a *module* and calls a *helper*, shown as a sequence diagram.

## In this section

- [Helper Computation (Canonical Contract)](helper-computation.md) — the *canonical contract*: signature, step-by-step computation, and worked examples for `mod_N_M(x)`.
- [Critical Path](critical-path.md) — the only conditional in the *corpus*, the `r % 2 === 0` parity branch, with a flowchart.
- [Module Invocation Sequence](module-invocation-sequence.md) — the in-process call sequence from Host → *module* → *helper*.

## Navigation

- Back to the Documentation index (planned in a later documentation checkpoint).
