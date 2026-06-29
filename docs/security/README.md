# Security

## Overview

The `society_mgmt_300k` corpus presents a **minimal, verified-absent runtime attack surface** and exactly **one live governance item** — a dual-license conflict (feature F-006). Every function in the corpus is a pure arithmetic helper whose sole external input is a numeric argument `x`; there is no I/O, network access, dynamic code execution, deserialization, secrets handling, authentication, or cryptography anywhere in the tree. Consequently this document records a **verified-absence security posture**: where a security surface is absent, that absence is stated explicitly and backed by a source citation rather than by an assumed or fabricated threat model. The single genuine, actionable concern is licensing governance, documented in the [F-006 — Dual-license conflict](#f-006--dual-license-conflict) section below. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## Attack surface

The only externally supplied value to any function is the **numeric argument `x`**, consumed by pure arithmetic helpers of the form `mod_<fileId>_<k>(x)` that accumulate `x*1 + x*2 + x*3` (= `6x`) and return `6x + 10`. These functions read no globals, perform no I/O, and produce no observable side effects. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

- **Externally reachable entry points:** none. There is no module system (no `require`/`import`/`export`/`module.exports`), so no symbol is importable from outside its file — every function is file-local. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (canonical example); the corpus-wide absence of a module system is confirmed by a whole-tree keyword sweep of all 29 `.js` files returning zero `require`/`import`/`export`/`module.exports` (re-verifiable via `grep -rwE 'require|import|export' society_mgmt_300k --include='*.js'`; see [Verified absences](#verified-absences-keyword-sweep))
- **Input domain:** a single numeric argument `x`. There is no string parsing, no structured/serialized input, and therefore no deserialization of untrusted data. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (single numeric parameter, canonical example); corpus-wide, the whole-tree keyword sweep finds no parsing, deserialization, or dynamic-execution constructs — see [Verified absences](#verified-absences-keyword-sweep).
- **Outputs / side effects:** each function returns a number and mutates only a local accumulator `r`; the module-scoped `const store = [];` is inert (never read or written). Source: society_mgmt_300k/src/controllers/file_0.js:L2
- **Trust boundaries:** none are crossed — with no I/O or network calls, the code never communicates with an external system. Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — whole-tree keyword sweep across all 29 `.js` files returns zero `fetch`/`Promise`/`async`/`await` (no network or asynchronous I/O); see [Verified absences](#verified-absences-keyword-sweep).

Because the corpus is not runnable as a service (no endpoints, no module system), the practical attack surface is limited to whatever value a caller passes as `x` to an in-process function. See the [Glossary](../reference/glossary.md) for terms such as *pure function* and *synthetic corpus*.

## Verified absences (keyword sweep)

A whole-tree keyword sweep (excluding `.git`) returns **zero** occurrences of every security-relevant construct below. These are reported as **faithful absence findings** — the surfaces are genuinely not present, not merely unreviewed. Source: society_mgmt_300k/src/ and society_mgmt_300k/tests/ — whole-tree keyword sweep across all 29 `.js` files (re-verifiable via `grep -rwE '<keyword>' society_mgmt_300k --include='*.js'` for each construct in the table below, every count being zero).

| Swept keyword(s) | Occurrences | What its absence means |
|------------------|-------------|------------------------|
| `require`, `import`, `export`, `module.exports` | 0 | No module system; symbols are file-local and not importable |
| `eval` | 0 | No dynamic code execution |
| `fetch` | 0 | No network I/O |
| `Promise`, `async`, `await` | 0 | No asynchronous I/O |
| `try`, `catch`, `throw` | 0 | No exception-based error channels |
| `console` | 0 | No logging or console output |
| `password`, `token`, `jwt`, `auth` | 0 | No authentication, sessions, or secrets handling |
| `crypto`, `encrypt` | 0 | No cryptography |
| `use strict` | 0 | No strict-mode pragma (noted for completeness) |

**Conclusion:** the corpus performs **no I/O, no network access, and no dynamic code execution**, and it handles **no deserialization, no secrets, no authentication, and no cryptography**. Because the only input channel is the numeric `x`, there is no untrusted data to deserialize or inject. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (canonical pure-function motif); the corpus-wide zero counts above come from the whole-tree keyword sweep across all 29 `.js` files (`grep -rwE '<keyword>' society_mgmt_300k --include='*.js'` returns 0 for each)

## Supply chain

The repository declares **zero dependencies**: there is no `package.json`, lockfile, or third-party package of any kind. With no declared or transitive dependencies, there is **no third-party supply-chain exposure** — no vulnerable transitive packages, no install-time scripts, and no package-registry trust to manage. This dependency-free posture is a deliberate property of the corpus. Source: repository root — whole-tree file search excluding `.git` finds no `package.json`, no lockfile (`*.lock` / `*-lock.json`), and no `node_modules` directory (re-verifiable via `find . -not -path './.git/*' -name 'package.json'` and the analogous lockfile searches, all returning 0).

## F-006 — Dual-license conflict

This is the **single live governance item** for the repository. It carries **two different licenses with no statement of precedence**:

- Root [`LICENSE`](../../LICENSE) — **Apache License, Version 2.0**. Source: LICENSE
- Inner [`society_mgmt_300k/LICENSE/LICENSE.txt`](../../society_mgmt_300k/LICENSE/LICENSE.txt) — **MIT License**, Copyright (c) 2026. Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1

**Risk.** Because the two licenses coexist without any precedence statement, downstream users face **legal ambiguity** about which terms govern reuse and redistribution. The licenses differ materially — Apache-2.0 includes an explicit patent grant and NOTICE/attribution requirements that the MIT license does not — so the ambiguity is substantive, not cosmetic.

**Recommended resolution path (DOCUMENTED, NOT APPLIED here).** The following are recommendations only; editing license files is out of scope for this documentation effort, so no license file is modified:

1. **Choose a single canonical license** for the entire repository and remove or supersede the other, or
2. **Add an explicit precedence statement** at the repository root declaring which license governs and the scope of each, and/or
3. **Add an SPDX identifier** (for example, `SPDX-License-Identifier: Apache-2.0` or `SPDX-License-Identifier: MIT`) so the intended license is machine-readable.

These steps would resolve F-006; they are recorded here as guidance and are intentionally **not** carried out.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — canonical pure-function motif; sole input is the numeric `x`; basis for the attack-surface and verified-absence findings.
- `society_mgmt_300k/src/controllers/file_0.js:L2` — the inert `const store = [];` placeholder.
- `LICENSE` — root Apache License, Version 2.0 (F-006).
- `society_mgmt_300k/LICENSE/LICENSE.txt:L1` — inner MIT License, Copyright (c) 2026 (F-006).
- Terminology is defined in the [Glossary](../reference/glossary.md); return to the [documentation index](../README.md).
