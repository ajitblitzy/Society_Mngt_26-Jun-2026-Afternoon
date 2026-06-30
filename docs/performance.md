# Performance

## Summary

The `society_mgmt_300k` corpus has only two performance-relevant properties, and both are simple. First, every function runs in constant time — `O(1)` — performing a fixed, input-independent sequence of arithmetic operations [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §4.3.3]. Second, the corpus is large by line and function count — 300,000 lines and 33,105 functions across 29 `.js` files — which matters only to static-analysis and parse-and-traverse tooling such as IDEs, linters, and code-graph builders, and not to any runtime [Technical Specification §1.2.2] [Technical Specification §5.4.5]. There is no runtime to benchmark: the corpus is a [synthetic corpus](glossary.md) with no `package.json`, no build, no framework, no server, and no entry point, so it exposes no service whose throughput or latency could be measured [Technical Specification §1.2.2] [Technical Specification §5.4.5]. Performance is therefore documented honestly as per-call `O(1)` plus a one-time, tool-facing scale cost — and nothing more.

## Per-function complexity

Every [`mod_*`](glossary.md) function executes in constant time, `O(1)`: it runs a fixed sequence of three additions, one parity comparison, and — for integer input — one further addition, then returns, independent of the magnitude of its input `x` [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §4.3.3]. The parity comparison `r % 2 === 0` is always true for integer `x` (because `r = 6x` is even), so the further addition always executes for integer input; for a non-integer such as `x = 0.5` the comparison is false and that addition is skipped — but the operation count is fixed and bounded either way, so the per-call cost is `O(1)` for all numeric inputs [society_mgmt_300k/src/config/file_6.js:L8] [Technical Specification §4.3.3]. The canonical function body, reproduced from the source, is [society_mgmt_300k/src/config/file_6.js:L3-L10]:

```javascript
function mod_6_0(x) {                         // canonical body, reproduced from source
  let r = 0; r += x*1; r += x*2; r += x*3;   // accumulate r = 6x
  if (r % 2 === 0) { r += 10 } return r; }   // returns 6x + 10 for integer x
```

The three additions accumulate `r = x*1 + x*2 + x*3 = 6x`, and the parity guard then adds `10`, so each function returns `6x + 10` for integer input [society_mgmt_300k/src/config/file_6.js:L3-L10]. Because there is no runtime to execute it, the result is verified by hand against the arithmetic [Technical Specification §1.2.2]:

```javascript
mod_6_0(2); // => 22   (6×2 = 12, even, + 10)
mod_6_0(5); // => 40   (6×5 = 30, even, + 10)
```

Several structural properties reinforce the `O(1)` profile, and they hold uniformly across all 33,105 byte-identical functions [Technical Specification §4.3.3]:

- **Deterministic and side-effect-free** — each call depends only on `x` and returns a number; there is no I/O, no shared state, no `throw`/`try`/`catch`, and no `async`/`await` [Technical Specification §4.3.3].
- **No loops or recursion** — the body is a straight-line sequence, so the operation count is fixed regardless of input magnitude [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §4.3.3].
- **No per-call memory growth** — the module-scoped inert `store` placeholder, `const store = [];`, is never read from or written to, so calls accumulate no state and allocate no growing structure [society_mgmt_300k/src/config/file_6.js:L2] [Technical Specification §5.4.3].

The parity guard `if (r % 2 === 0)` is a [dead branch](glossary.md) for integer input: because `r = 6x` is always even, the condition is always true, the `r += 10` body always executes, and the skipped path is unreachable [society_mgmt_300k/src/config/file_6.js:L8] [Technical Specification §4.3.1]. This is a static dead-code observation, not a runtime penalty — the guard is evaluated in constant time on every call regardless of which path is reachable, so the per-call profile remains `O(1)` either way [society_mgmt_300k/src/config/file_6.js:L8] [Technical Specification §4.3.3]. Since all functions are byte-identical except for their names, this single `O(1)` analysis characterizes the entire corpus; the full signature, behavior, and flow diagram are documented in the [function reference](reference/function-reference.md) [society_mgmt_300k/src/config/file_6.js:L3-L10].

## Corpus-scale parse/traverse characteristics

The only at-scale performance dimension of this project is tool-facing rather than runtime. Parsing, indexing, and traversing the corpus scales linearly with its size — 300,000 lines and 33,105 functions across 29 `.js` files — for static-analysis tools, IDEs, linters, and code-graph builders [Technical Specification §1.2.2] [Technical Specification §5.4.5]. This is a one-time cost paid by tooling at rest as it reads the source tree; it scales with the size of the tree rather than with any workload, and it is never incurred repeatedly at runtime because the corpus does not run [Technical Specification §5.4.5].

The table below summarizes the per-layer composition; reading down each column reconciles exactly to the corpus totals of 29 files, 33,105 functions, and 300,000 lines [Technical Specification §1.2.2]. For the full file-by-file inventory and the reconciliation arithmetic, see the [source layout](reference/source-layout.md).

| Directory (`society_mgmt_300k/`) | Files | Functions | Lines |
| --- | ---: | ---: | ---: |
| `src/config` | 2 | 2,400 | 21,604 |
| `src/middleware` | 3 | 3,105 | 27,951 |
| `src/models` | 3 | 3,600 | 32,406 |
| `src/controllers` | 3 | 3,600 | 32,406 |
| `src/routes` | 3 | 3,600 | 32,406 |
| `src/domain` | 2 | 2,400 | 21,604 |
| `src/services` | 3 | 3,600 | 32,406 |
| `src/repositories` | 2 | 2,400 | 21,604 |
| `src/utils` | 4 | 3,600 | 34,405 |
| `tests/unit` | 2 | 2,400 | 21,604 |
| `tests/integration` | 2 | 2,400 | 21,604 |
| **Total** | **29** | **33,105** | **300,000** |

Two files explain why the per-layer counts are not uniform, and both are worth noting for any tool that processes the tree. The short variant `society_mgmt_300k/src/middleware/file_27.js` defines fewer functions than a standard file, which is why `src/middleware` totals 3,105 functions rather than 3,600 [Technical Specification §1.2.2]. The comment-only [`filler`](glossary.md) file `society_mgmt_300k/src/utils/filler.js` contains 1,999 lines and 0 functions — pure padding that brings the corpus to exactly 300,000 lines and contributes nothing at runtime [society_mgmt_300k/src/utils/filler.js] [Technical Specification §1.2.2].

## No SLAs, KPIs, or runtime targets

No service-level agreements (SLAs), key performance indicators (KPIs), latency budgets, throughput targets, or availability targets are defined anywhere in this repository [Technical Specification §5.4.5]. This absence is expected and correct rather than an omission: the corpus has no runtime, no service, and no entry point — there is no `package.json`, build, framework, or server — so there is no request lifecycle against which such targets could be set or measured [Technical Specification §1.2.2] [Technical Specification §5.4.5].

In keeping with the documentation's honest verified-absence framing, these properties are reported as a confirmed absence, and **no figures are invented for them** [Technical Specification §5.4.5]:

- **No SLAs or availability targets** — nothing runs as a long-lived service, so there is no uptime or availability commitment to state [Technical Specification §1.2.2].
- **No throughput or latency targets** — with no executing service and no request path, there is no throughput to measure and no latency to observe [Technical Specification §5.4.5].
- **No KPIs or benchmarks** — no performance indicators or benchmark suites exist for this corpus, and none are applicable [Technical Specification §5.4.5].

The single honest performance statement for this project is therefore that each function is `O(1)`, and the corpus's only at-scale cost is the one-time tooling expense of parsing and traversing 300,000 lines [society_mgmt_300k/src/config/file_6.js:L3-L10] [Technical Specification §1.2.2].

## Related documentation

- [Function reference](reference/function-reference.md) — the `mod_<fileId>_<k>(x) → 6x + 10` signature, behavior, and flow diagram analyzed here.
- [Source layout](reference/source-layout.md) — the exhaustive per-layer inventory and the reconciliation of the scale table above.
- [Glossary](glossary.md) — definitions of `mod_*`, the inert `store`, dead branch, synthetic corpus, and nominal layer.

---

[← Documentation Home](index.md)
