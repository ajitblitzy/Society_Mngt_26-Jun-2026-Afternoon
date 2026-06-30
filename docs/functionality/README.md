# Functionality

← Back to the [documentation index](../README.md).

## Purpose

This page is the **functionality index** for the synthetic [`society_mgmt_300k`](../overview.md) JavaScript corpus. It catalogues the corpus's verifiable functionalities (Requirement R1) and links to the detailed topic documents that describe each one. Start here and follow the links in the [documentation map](#documentation-map) below.

## About the Corpus

`society_mgmt_300k` is a **synthetic JavaScript corpus** of **300,000 lines** spread across **29 `.js` files** and containing **33,105 functions** (Source: Tech Spec §1.2.2; Tech Spec §2.2.6). Every function is **byte-identical** and computes `6x + 10` for an integer input `x` — the body accumulates `r = x*1 + x*2 + x*3` (`= 6x`) and then adds `10` because the parity branch is always taken for integer `x` (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`; Tech Spec §2.2.2). The files are arranged as a **nominal layered scaffold** — nine `src` layers and two `tests` layers — with **no inter-layer wiring**: nothing is exported or imported anywhere (0 `module.exports`, 0 `require(`), so the corpus is **not a runnable application** (Source: Tech Spec §2.2.4; Tech Spec §1.2.2). Full system context lives in [`../overview.md`](../overview.md) and in the topic documents below.

## Documentation Map

Because every function is byte-identical, these documents use a **representative-pattern** approach: one canonical function and per-layer rollups stand in for all 33,105 functions — they are never enumerated individually (Source: Tech Spec §2.2.2 — byte-identical bodies across all 33,105 functions; `society_mgmt_300k/src/controllers/file_0.js:L3-L10`). The map below indexes all six catalogued functionalities (**F-001** through **F-006**); two of them — **F-003** (the layered scaffold) and **F-006** (the licensing artifacts) — are documented in dedicated files elsewhere in the `docs/` tree and are linked here with `../` paths.

| Document | Topic | What it covers |
| --- | --- | --- |
| [`arithmetic-helpers.md`](./arithmetic-helpers.md) | **F-001** | The representative `mod_<fileId>_<k>(x) → 6x + 10` contract, its behavior, the dead (always-true) parity branch, a worked example, and the computation flowchart. (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`; Tech Spec §2.2.2) |
| [`symbol-namespace.md`](./symbol-namespace.md) | **F-002** | The `mod_<fileId>_<k>` symbol naming scheme, the per-file index ranges, and global uniqueness. (Source: Tech Spec §2.2.3) |
| [`../architecture.md`](../architecture.md) | **F-003** | The nominal layered scaffold — nine `src` layers and two `tests` layers — and the verified absence of inter-layer wiring (0 imports/exports/calls), with the edge-less containment diagram. (Source: Tech Spec §2.2.4) |
| [`module-reference.md`](./module-reference.md) | Inventory | The per-layer module inventory of all 29 files (files, function counts, and module symbols). (Source: Tech Spec §1.2.2) |
| [`store-placeholder.md`](./store-placeholder.md) | **F-004** | The unused module-scoped `const store = []` placeholder present in every numbered file. (Source: `society_mgmt_300k/src/controllers/file_0.js:L2`; Tech Spec §2.2.5) |
| [`corpus-sizing.md`](./corpus-sizing.md) | **F-005** | The deterministic 300,000-line composition arithmetic. (Source: Tech Spec §2.2.6) |
| [`../governance/licensing.md`](../governance/licensing.md) | **F-006** | The repository licensing artifacts and the Apache-vs-MIT license inconsistency between the root `LICENSE` (Apache License 2.0) and the nested `society_mgmt_300k/LICENSE/LICENSE.txt` (MIT). (Source: `/LICENSE:L1-L2`; `society_mgmt_300k/LICENSE/LICENSE.txt:L1`; Tech Spec §2.2.7) |

## Documentation Conventions

All functionality documents follow the same conventions:

- **Verified-absence framing** — only behavior present in the source is documented. The corpus has no runtime, framework, server, database, network, or dependencies, and the documentation never implies a capability the code does not have (Source: Tech Spec §2.2.4 — no wiring / not runnable; Tech Spec §2.5.4 — no network or database; AAP §0.2.1 — zero dependencies (no manifest)).
- **Source citations on every claim** — each technical statement cites a `path:line` location or a Technical Specification section.
- **Representative-pattern approach** — one canonical function stands in for all 33,105 byte-identical functions (Source: Tech Spec §2.2.2).
- **GitHub-native rendering** — plain Markdown with Mermaid diagrams in fenced `mermaid` code blocks; no build step is required.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — canonical function body (`6x + 10`), representative of all 33,105 byte-identical functions.
- Tech Spec §1.2.2 and §2.2.6 — 29 `.js` files, 33,105 functions, 300,000 lines. Tech Spec §2.2.4 — 0 `module.exports`, 0 `require(`.
- Tech Spec §2.2.4 — no exported/public interface; Tech Spec §1.2.2 — the corpus is not a runnable application.
- Tech Spec §2.2.2 — byte-identical functions underpinning the representative-pattern documentation approach.
- Sibling topic documents — [`arithmetic-helpers.md`](./arithmetic-helpers.md), [`symbol-namespace.md`](./symbol-namespace.md), [`module-reference.md`](./module-reference.md), [`store-placeholder.md`](./store-placeholder.md), [`corpus-sizing.md`](./corpus-sizing.md).
- Related functionality documents (elsewhere in the `docs/` tree) — [`../architecture.md`](../architecture.md) (**F-003**, the layered scaffold), [`../governance/licensing.md`](../governance/licensing.md) (**F-006**, the licensing artifacts).

---

← Back to the [documentation index](../README.md).
