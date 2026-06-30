# society_mgmt_300k documentation

Welcome to the documentation home for `society_mgmt_300k`. This page is the master navigation hub for the entire `docs/` tree: it states what the repository honestly is, notes who these documents are for, and links to every other page in the set.

## Purpose

This is the documentation home for the `society_mgmt_300k` repository, and it exists to orient you before you read anything else. Every page in this tree describes only what a first-hand scan of the source actually confirms — not what the repository's name suggests — and carries an inline `[path:locator]` citation on each technical claim so that any statement can be traced back to the code or the technical specification [Technical Specification §1.2.1]. Read this page first, then follow the documentation map below to the topic you need.

## Summary

Despite its "Society Management" name, `society_mgmt_300k` contains **no society-management — or any other — business logic** [Technical Specification §1.2.1]. It is a **synthetic JavaScript corpus** of exactly **300,000 lines** across **29 `.js` files**, holding **33,105 near-identical functions** whose sole behavior is to return **`6x + 10`** for an integer input `x` [Technical Specification §1.2.2] [society_mgmt_300k/src/config/file_6.js:L3-L10]. The familiar layer names (`controllers`, `services`, `repositories`, and the like) form a nominal scaffold only: there are no imports, exports, or calls between files, so the layering carries no runtime edges [Technical Specification §5.4.2]. Read the name as a label on a box of repeated arithmetic, not as a description of functionality [Technical Specification §1.2.1].

## Audience

These documents are written for engineers and analysts who need to read, navigate, or statically analyze the corpus — for example, to understand its structure, its single behavior, or its scale. There is **nothing to install, build, run, or test**: the repository has no runtime, no framework, no `package.json`, and no entry point, so every page is about reading source rather than operating a system [Technical Specification §1.2.2].

## Documentation map

The table below is the canonical table of contents for the whole documentation set. Each page appears exactly once, paired with the topic it covers.

| Page | What it covers |
| --- | --- |
| [Overview](getting-started/overview.md) | What the repository actually is versus its misleading name; scope and non-goals [Technical Specification §1.2.1]. |
| [Repository tour](getting-started/repository-tour.md) | How to navigate `src/` and `tests/`; why there is no build, run, or test runner; and how the 300,000 lines reconcile [Technical Specification §1.2.2]. |
| [Architecture overview](architecture/overview.md) | The layered directory layout and why the layering is nominal only, with no runtime edges between layers [Technical Specification §5.4.2]. |
| [Module pattern](architecture/module-pattern.md) | The canonical file anatomy — header comment, inert `const store = []`, and the `mod_*` functions — plus the comment-only `filler.js` [society_mgmt_300k/src/config/file_6.js:L1-L10] [society_mgmt_300k/src/utils/filler.js]. |
| [Function reference](reference/function-reference.md) | `mod_<fileId>_<k>(x)`: its signature, the `6x + 10` behavior, the always-true (dead) parity branch, and a worked example [society_mgmt_300k/src/config/file_6.js:L3-L10]. |
| [Source layout](reference/source-layout.md) | The exhaustive per-layer inventory reconciling to 29 files, 33,105 functions, and 300,000 lines [Technical Specification §1.2.2]. |
| [Performance](performance.md) | Per-function `O(1)` behavior, the corpus-scale parse-and-traverse cost, and the explicit absence of any SLAs, KPIs, latency, throughput, or availability targets [Technical Specification §5.4.5]. |
| [Security](security.md) | The verified-absence security posture, the decision to add no authentication or authorization controls, baseline hygiene, and the dual-license governance note [Technical Specification §6.4]. |
| [Glossary](glossary.md) | Definitions of corpus-specific terms — `mod_*`, the inert `store`, `filler`, synthetic corpus, dead branch, and (nominal) layer [society_mgmt_300k/src/config/file_6.js:L1-L10]. |

## Back to the repository

[← Project README](../README.md) — the top-level project overview and licensing note.
