# Security

## Overview

The `society_mgmt_300k` corpus presents a **minimal, verified-absent runtime attack surface** and exactly **one live governance item** — a dual-license conflict (feature F-006). Every function in the corpus is a pure arithmetic helper whose sole external input is a numeric argument `x`; there is no I/O, network access, dynamic code execution, deserialization, secrets handling, authentication, or cryptography anywhere in the JavaScript source corpus. Consequently this document records a **verified-absence security posture**: where a security surface is absent, that absence is stated explicitly and backed by a source citation rather than by an assumed or fabricated threat model. The single genuine, actionable concern is licensing governance, documented in the [F-006 — Dual-license conflict](#f-006--dual-license-conflict) section below. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (canonical pure-function motif), docs/reference/corpus-evidence.md:L112-L151 (source-corpus keyword sweep over `society_mgmt_300k/**/*.js` confirming the tree-wide absences)

## Attack surface

The only externally supplied value to any function is the **numeric argument `x`**, consumed by pure arithmetic helpers of the form `mod_<fileId>_<k>(x)` that accumulate `x*1 + x*2 + x*3` (= `6x`) and return `6x + 10`. These functions read no globals, perform no I/O, and produce no observable side effects. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (canonical pure-function motif), docs/reference/corpus-evidence.md:L67-L95 (body uniformity: all 33,105 functions byte-identical apart from names)

- **Externally reachable entry points:** none. There is no module system (no `require`/`import`/`export`/`module.exports`), so no symbol is importable from outside its file — every function is file-local. Source: docs/reference/corpus-evidence.md:L112-L151 (source-corpus keyword sweep over `society_mgmt_300k/**/*.js`: zero module-system keywords)
- **Input domain:** a single numeric argument `x`. There is no string parsing, no structured/serialized input, and therefore no deserialization of untrusted data. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (the sole input is the numeric `x`), docs/reference/corpus-evidence.md:L112-L151 (source-corpus keyword sweep: zero `eval`/module/I/O constructs, so no untrusted data is parsed or deserialized)
- **Outputs / side effects:** each function returns a number and mutates only a local accumulator `r`; the module-scoped `const store = [];` is inert (never read or written). Source: society_mgmt_300k/src/controllers/file_0.js:L2 (the single declaration), docs/reference/corpus-evidence.md:L97-L110 (corpus-wide `store` scan: 28 declarations, zero read/write references)
- **Trust boundaries:** none are crossed — with no I/O or network calls, the code never communicates with an external system. Source: docs/reference/corpus-evidence.md:L112-L151 (source-corpus keyword sweep: zero `fetch`/`Promise`/`async`/`await` and zero module-system keywords)

Because the corpus is not runnable as a service (no endpoints, no module system), the practical attack surface is limited to whatever value a caller passes as `x` to an in-process function. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10 (the in-process numeric input/body), docs/reference/corpus-evidence.md:L112-L151 (no module system — nothing importable or externally reachable). See the [Glossary](../reference/glossary.md) for terms such as *pure function* and *synthetic corpus*.

## Verified absences (keyword sweep)

A **source-corpus keyword sweep over `society_mgmt_300k/**/*.js`** returns **zero** occurrences of every security-relevant construct below. These are reported as **faithful absence findings** — the surfaces are genuinely not present in the JavaScript source corpus, not merely unreviewed. The scope is stated precisely on purpose: the zero counts hold for the JavaScript source files, not for the whole repository tree, because the documentation and license text legitimately mention some of these terms (for example, this very page names `auth` and `crypto`). Source: docs/reference/corpus-evidence.md:L112-L151 (the source-corpus sweep, all zero), docs/reference/corpus-evidence.md:L153-L175 (the whole-tree contrast showing why the scope must be the JS corpus)

| Swept keyword(s) | Occurrences | What its absence means |
| --- | --- | --- |
| `require`, `import`, `export`, `module.exports` | 0 | No module system; symbols are file-local and not importable |
| `eval` | 0 | No dynamic code execution |
| `fetch` | 0 | No network I/O |
| `Promise`, `async`, `await` | 0 | No asynchronous I/O |
| `try`, `catch`, `throw` | 0 | No exception-based error channels |
| `console` | 0 | No logging or console output |
| `password`, `token`, `jwt`, `auth` | 0 | No authentication, sessions, or secrets handling |
| `crypto`, `encrypt` | 0 | No cryptography |
| `use strict` | 0 | No strict-mode pragma (noted for completeness) |

**Conclusion:** the corpus performs **no I/O, no network access, and no dynamic code execution**, and it handles **no deserialization, no secrets, no authentication, and no cryptography**. Because the only input channel is the numeric `x`, there is no untrusted data to deserialize or inject. Source: docs/reference/corpus-evidence.md:L112-L151 (source-corpus keyword sweep confirming every listed absence), society_mgmt_300k/src/controllers/file_0.js:L3-L10 (the single-function input/body behavior)

## Supply chain

The repository declares **zero dependencies**: there is no `package.json`, lockfile, or third-party package of any kind. With no declared or transitive dependencies, there is **no third-party supply-chain exposure** — no vulnerable transitive packages, no install-time scripts, and no package-registry trust to manage. This dependency-free posture is a deliberate property of the corpus. Source: docs/reference/corpus-evidence.md:L234-L246 (dependency-manifest scan: zero `package.json` and zero lockfiles repository-wide)

## F-006 — Dual-license conflict

This is the **single live governance item** for the repository. It carries **two different licenses with no statement of precedence**:

- Root [`LICENSE`](../../LICENSE) — **Apache License, Version 2.0**. Source: LICENSE
- Inner [`society_mgmt_300k/LICENSE/LICENSE.txt`](../../society_mgmt_300k/LICENSE/LICENSE.txt) — **MIT License** (line 1), Copyright (c) 2026 (line 3). Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3

**Risk.** Because the two licenses coexist without any precedence statement, downstream users face **legal ambiguity** about which terms govern reuse and redistribution. The licenses differ materially — Apache-2.0 includes an explicit patent grant and NOTICE/attribution requirements that the MIT license does not — so the ambiguity is substantive, not cosmetic. Source: LICENSE (Apache License, Version 2.0), society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3 (MIT License and copyright)

**Recommended resolution path (DOCUMENTED, NOT APPLIED here).** The following are recommendations only; editing license files is out of scope for this documentation effort, so no license file is modified:

1. **Choose a single canonical license** for the entire repository and remove or supersede the other, or
2. **Add an explicit precedence statement** at the repository root declaring which license governs and the scope of each, and/or
3. **Add an SPDX identifier** (for example, `SPDX-License-Identifier: Apache-2.0` or `SPDX-License-Identifier: MIT`) so the intended license is machine-readable.

These steps would resolve F-006; they are recorded here as guidance and are intentionally **not** carried out.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — canonical pure-function motif; sole input is the numeric `x` (the single-function basis for the attack-surface description).
- `society_mgmt_300k/src/controllers/file_0.js:L2` — the inert `const store = [];` placeholder (single declaration).
- `docs/reference/corpus-evidence.md:L112-L151` — the **source-corpus keyword sweep over `society_mgmt_300k/**/*.js`**: zero occurrences of every module-system, I/O, async, error-channel, logging, secrets, auth, and crypto keyword. This is the corpus-wide basis for the verified-absence posture.
- `docs/reference/corpus-evidence.md:L153-L175` — the whole-tree contrast that explains why the sweep scope must be the JS source corpus and not the whole repository tree.
- `docs/reference/corpus-evidence.md:L97-L110` — the `store` usage scan (28 declarations, zero reads/writes) backing the inert-placeholder claim.
- `docs/reference/corpus-evidence.md:L234-L246` — the dependency-manifest scan (zero `package.json`, zero lockfiles) backing the zero-dependency supply-chain claim.
- `LICENSE` — root Apache License, Version 2.0 (F-006).
- `society_mgmt_300k/LICENSE/LICENSE.txt:L1-L3` — inner MIT License (line 1) and Copyright (c) 2026 (line 3) (F-006).
- Terminology is defined in the [Glossary](../reference/glossary.md); return to the [documentation index](../README.md).
