# Performance

← Back to the [documentation hub](../README.md)

## Overview

The runtime cost of the synthetic `society_mgmt_300k` corpus is dominated by
trivial, constant-time scalar arithmetic. Every callable in the corpus is one of
the **33,105** byte-identical `mod_<fileId>_<k>(x)` functions, each of which
performs a fixed handful of operations on a single local accumulator and returns
immediately (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).
There is **no measured performance program** anywhere in the repository — no
benchmark suite, no load test, no performance CI, and no service-level
objectives — so this document reports the performance surface **faithfully from
the code** and never asserts a figure the project does not define
(Source: Technical Specification §2.5.2). Where a conventional performance
surface is absent, that absence is stated explicitly rather than implied.

## Time & space complexity

Every `mod_*` call runs in **`O(1)` time** and **`O(1)` space**. The analysis
rests entirely on the canonical function body, which is byte-identical across
all 33,105 functions and is reproduced here verbatim from the source
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`):

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

- **`O(1)` time.** The operation count per call is fixed and independent of the
  magnitude of `x`: one initialisation (`let r=0`), three multiply-add
  accumulations (`x*1`, `x*2`, `x*3`), one parity test (`r%2===0`), one
  conditional add (`r+=10`), and one `return`. No step repeats and none scales
  with the input, so the work performed is constant
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).
- **`O(1)` space.** The only working state is the single scalar accumulator `r`;
  no array, object, or string is created or grown during a call. The
  module-scoped `const store = [];` is declared once but is never read or
  written, so it contributes no per-call allocation
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L2`).

For definitions of the terminology used across these documents — including
*`O(1)`*, *pure*, and *deterministic* — see the
[glossary](../reference/glossary.md).

## Determinism & purity

Each `mod_*` function is [*pure*](../reference/glossary.md) and
[*deterministic*](../reference/glossary.md): the same input `x` always produces
the same output, and the call has no side effects. The three accumulations build
`r = x*1 + x*2 + x*3 = 6x`; because `6x` is always even, the parity guard is a
[dead, always-true branch](../reference/glossary.md) and the `+ 10` always
applies, so every function effectively returns **`6x + 10`**
(Source: `society_mgmt_300k/src/controllers/file_0.js:L4-L9`). The worked example
is exact and verifiable by inspection: **`mod_0_0(4) === 34`** (that is,
`6*4 + 10`).

Because there is no I/O and no mutation of external or module-level state — the
`store` array is never written — the functions are
[*referentially transparent*](../reference/glossary.md): any call may be replaced
by its computed result without changing program behaviour
(Source: `society_mgmt_300k/src/controllers/file_0.js:L2-L10`).

## No loops, recursion, or allocation-in-loops

The corpus contains **none** of the classic per-call performance hazards. Each
function body is straight-line code with a single forward conditional branch:

- **No loops.** There are no `for`, `while`, or `do` constructs, so no work is
  repeated and per-call cost cannot grow with the input
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).
- **No recursion.** No `mod_*` body calls another function, so there is no call
  stack growth and no recursive expansion
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`).
- **No allocation-in-loops.** There are no loops, and there is no allocation at
  all within a call beyond the inert top-level `store`, so there is no place for
  repeated allocation to accumulate cost
  (Source: `society_mgmt_300k/src/controllers/file_0.js:L2-L10`).

These absences are why per-call cost is fixed; they are documented as verified
absences rather than as measured optimisations.

## Corpus scale vs. runtime throughput

The corpus's **generation-time scale** is large — **29** `.js` files,
**33,105** `mod_*` functions, and exactly **300,000** lines — but this describes
the size of the static artefact, **not** a runtime cost
(Source: `society_mgmt_300k/src/controllers/file_0.js:L1-L10`). Any single
invocation touches only one function's `O(1)` body; the number of other files or
functions in the tree does not change a call's latency or memory use. There is
also **no aggregate runtime workload** — no orchestrator, server, or harness
calls these functions in bulk — so there is no throughput figure to report.
These counts are corpus facts, kept deliberately separate from any notion of
throughput. For the authoritative per-layer file / function / line breakdown,
see [Corpus composition](../functionality/corpus-composition.md).

## Service levels (SLAs / KPIs)

**No service levels are defined** for this corpus. There are no latency budgets,
no throughput or QPS/RPS targets, no error-rate objectives, no benchmark suites,
and no performance CI or monitoring anywhere in the repository
(Source: Technical Specification §2.5.2). This is reported as a faithful
**absence**: no placeholder targets, percentiles, or measured metrics are
invented here, because none exist in the source. (If a future workload were ever
to require performance guarantees, they would need to be defined and measured
first — they are **not** present today.)

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1-L10` — the canonical,
  byte-identical function motif (header comment, inert `store`, and
  fixed-operation body) that establishes the `O(1)` time and space complexity,
  the determinism, and the absence of loops and recursion.
- `society_mgmt_300k/src/controllers/file_0.js:L2` — the inert module-scoped
  `const store = [];` placeholder, never read or written (`O(1)` space, no side
  effects).
- `society_mgmt_300k/src/controllers/file_0.js:L4-L9` — the `6x` accumulation
  and always-true parity branch yielding the effective result `6x + 10` (worked
  example `mod_0_0(4) === 34`).
- `Technical Specification §2.5.2` — the explicit absence of SLAs, KPIs,
  benchmarks, and performance targets for the corpus.
- [Corpus composition](../functionality/corpus-composition.md) — the per-layer
  file / function / line figures cited here as generation-time scale.

---

← Back to the [documentation hub](../README.md)
