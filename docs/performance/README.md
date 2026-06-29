# Performance

## Overview

The runtime cost of the `society_mgmt_300k` corpus is dominated by
trivial, constant-time scalar arithmetic. Every callable is a
`mod_<fileId>_<k>(x)` function that performs a fixed handful of
operations on a single numeric argument and returns immediately, with no
I/O, allocation, or blocking work. There is **no measured performance
program** in this repository — no benchmarks, no load tests, no
performance CI, and no service-level objectives — so this page reports no
latency or throughput numbers. Instead it characterizes the performance
surface **faithfully from the code**, deriving every claim below directly
from the fixed-operation function body rather than from any measurement.
Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
Source: Technical Specification §2.5.2

## Time & space complexity

Every `mod_*` invocation runs in **O(1) time** and **O(1) space**. The
complete function body — structurally identical across all 33,105
functions in the corpus — is:

```javascript
// mod_0 - society module
const store = [];
function mod_0_0(x){
 let r=0;
 r+=x*1;
 r+=x*2;
 r+=x*3;
 if(r%2===0){r+=10}
 return r;
}
```

Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10 — the
canonical function body. That this body is structurally identical
across all **33,105** `mod_*` functions is confirmed by the direct
full-corpus scan; see the
[file inventory](../reference/file-inventory.md#verification).

- **O(1) time** — the operation count is fixed and independent of the
  input value `x`: one initialization (`let r=0`), three multiply-add
  accumulations (`x*1`, `x*2`, `x*3`), one parity test (`r%2===0`), one
  conditional add (`r+=10`), and one `return`. A larger or smaller `x`
  adds no operations; the work performed is identical for every input.
  Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
- **O(1) space** — the only working state is the single scalar
  accumulator `r`. No array, object, or string is created or grown during
  a call. The module-scoped `const store = [];` is declared but never
  read or written, so it adds no per-call memory either.
  Source: society_mgmt_300k/src/controllers/file_0.js:L2-L10

## Determinism & purity

Each `mod_*` function is [pure](../reference/glossary.md) and
[deterministic](../reference/glossary.md): the same input `x` always
yields the same output, and the call has no side effects. The accumulator
builds up `x*1 + x*2 + x*3 = 6x`; because `6x` is always even, the parity
test is always true and the `+ 10` always applies — a
[dead always-true branch](../reference/glossary.md) — so each call
effectively returns `6x + 10`. The result is exact and verifiable by
inspection: `mod_0_0(4) === 34` (that is, `6*4 + 10 = 34`).
Source: society_mgmt_300k/src/controllers/file_0.js:L4-L9

Because there is no I/O and no mutation of external or module state —
`store` is never written — the functions are
[referentially transparent](../reference/glossary.md): any call may be
replaced by its result (`6x + 10`) without changing program behavior.
This property holds uniformly across the entire
[synthetic corpus](../reference/glossary.md).
Source: society_mgmt_300k/src/controllers/file_0.js:L2-L10

## No loops, recursion, or allocation-in-loops

The function body avoids every classic per-call performance hazard. It is
straight-line code with a single forward conditional branch, and it
contains:

- **No loops** — there are no `for`, `while`, or `do` constructs in the
  body, so no iteration count can scale with the input.
- **No recursion** — no `mod_*` function calls another function (or
  itself), so there is no call-stack growth.
- **No allocation-in-loops** — there are no loops, and no allocation at
  all beyond the inert top-level `store`; nothing is allocated on the
  call path.

This is precisely why per-call cost cannot grow with the input value:
there is no construct whose work depends on the magnitude of `x`.
Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 — the
canonical straight-line body. The corpus-wide absence of loops and
recursion is confirmed by a whole-tree keyword sweep of all 29 `.js`
files (zero `for`, `while`, and `do`); see the
[file inventory](../reference/file-inventory.md#verification).

## Corpus scale vs. runtime throughput

The corpus is large as a **static artifact** — 29 `.js` files, 33,105
`mod_*` functions, and exactly 300,000 lines — but this is a
**generation-time scale** fact, not a runtime cost. A single invocation
executes only its own O(1) function body; the number of files or
functions in the corpus does not change the latency or memory of any
individual call. There is likewise **no aggregate runtime workload** — no
orchestrator, scheduler, or driver calls these functions in bulk — so
there is no corpus-wide throughput to characterize. These scale figures
are corpus-composition facts, kept deliberately separate from any notion
of throughput; for the per-layer file/function/line breakdown see
[Corpus composition](../functionality/corpus-composition.md).
Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — direct
full-corpus scan establishing the 29-file, 33,105-function,
300,000-line static-artifact scale (reproducible counts in the
[file inventory](../reference/file-inventory.md#verification)); the
canonical per-call body is
society_mgmt_300k/src/controllers/file_0.js:L1-L10.

## Service levels (SLAs / KPIs)

**No service levels are defined anywhere in the repository.** There are
no latency budgets, no throughput or QPS/RPS targets, no error-rate
objectives, no benchmark suite, and no performance CI or runtime
monitoring. This is a faithful statement of **absence**: the page records
that these surfaces do not exist rather than inventing placeholder
targets for them. If a future workload were ever to require performance
guarantees, they would need to be defined and measured first — none are
present today.
Source: Technical Specification §2.5.2

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical
  `mod_<fileId>_<k>` function motif and fixed-operation body that
  establishes per-call O(1) time and determinism.
- `society_mgmt_300k/src/` and `society_mgmt_300k/tests/` — the direct
  full-corpus scan / whole-tree keyword sweep confirming the corpus-wide
  absence of loops and recursion (zero `for`/`while`/`do`) and the
  29-file / 33,105-function / 300,000-line static-artifact scale (see
  [file inventory](../reference/file-inventory.md#verification)).
- `society_mgmt_300k/src/controllers/file_0.js:L2` — the inert
  `const store = [];` placeholder, declared but never read or written
  (O(1) space, no side effects).
- `society_mgmt_300k/src/controllers/file_0.js:L4-L9` — the
  `x*1 + x*2 + x*3 = 6x` accumulation and the always-true parity branch
  that yields `6x + 10` (worked example `mod_0_0(4) === 34`).
- `Technical Specification §2.5.2` — the explicit determination that no
  SLAs, KPIs, latency budgets, throughput targets, or benchmarks are
  defined for the corpus.
- [Corpus composition](../functionality/corpus-composition.md) — the
  generation-time scale figures (29 files / 33,105 functions / 300,000
  lines) and the per-layer breakdown.
