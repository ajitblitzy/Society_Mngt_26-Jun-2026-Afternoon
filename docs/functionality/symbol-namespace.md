# Symbol Namespace (F-002)

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)

## Purpose

This document describes **F-002**, the module-function symbol naming scheme of the synthetic [`society_mgmt_300k`](../overview.md) JavaScript *corpus*. Every one of the corpus's **33,105 functions** is byte-identical and computes the same `6x + 10` expression (see [`arithmetic-helpers.md`](./arithmetic-helpers.md)), so the deterministic name `mod_<fileId>_<k>` is the **only thing that distinguishes one function from another** — it is the corpus's sole per-function differentiator and the means by which each function is individually addressable (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L10`; Tech Spec §2.2.3).

## Naming Scheme

Every function in the corpus is named **`mod_<fileId>_<k>`**, composed of two parts:

- **`<fileId>`** — the *module* identifier, derived from the file's number. Each file opens with a header comment of the form `// mod_<fileId> - society module` on line 1, which fixes the module id: `file_0.js` → `mod_0`, `file_3.js` → `mod_3`, `file_6.js` → `mod_6`, and `file_27.js` → `mod_27` (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`; `society_mgmt_300k/src/middleware/file_27.js:L1`).
- **`<k>`** — the zero-based function index *within* that file. The first function declared in a file is `mod_<fileId>_0`, the next `mod_<fileId>_1`, and so on, incrementing by one for each declaration (Source: `society_mgmt_300k/src/controllers/file_0.js:L3` (`mod_0_0`), `:L12` (`mod_0_1`); Tech Spec §2.2.3).

For example, the first function declared in `file_0.js` is **`mod_0_0(x)`**, appearing immediately after the header comment and the module-scoped `store` placeholder (Source: `society_mgmt_300k/src/controllers/file_0.js:L3`). The body that each `mod_<fileId>_<k>(x)` symbol names is the single *representative function* documented in [`arithmetic-helpers.md`](./arithmetic-helpers.md); only the name varies from one declaration to the next.

## Index Ranges

The per-file index `k` runs from `0` up to one less than the file's function count. All numbered files use the uniform range `0..1199` (1,200 functions each) with a single exception — the **short variant** `src/middleware/file_27.js`, whose index stops at `mod_27_704` (Source: Tech Spec §2.2.3 (index scheme); Tech Spec §1.2.2 (per-file counts, including the `file_27.js` short variant)).

| File type | `k` range | Functions per file | First → last symbol |
| --- | --- | --- | --- |
| Standard file (e.g. `file_0.js`) | `0 .. 1199` | 1,200 | `mod_<id>_0` → `mod_<id>_1199` |
| Short variant `src/middleware/file_27.js` | `0 .. 704` | 705 | `mod_27_0` → `mod_27_704` |

- **Standard files** contain 1,200 functions, so the index range is `k = 0 .. 1199` and the last symbol in such a file is `mod_<id>_1199` — for instance, the last function in `file_0.js` is `mod_0_1199` (Source: `society_mgmt_300k/src/controllers/file_0.js:L3` (first function `mod_0_0`); Tech Spec §1.2.2 — 1,200 functions per standard file; last `mod_0_1199`).
- **The short variant** `src/middleware/file_27.js` contains only 705 functions, so its index range is `k = 0 .. 704` and its last symbol is **`mod_27_704`** (Source: `society_mgmt_300k/src/middleware/file_27.js:L1` (header `// mod_27 - society module`); Tech Spec §1.2.2 — the `file_27.js` short variant has 705 functions; last `mod_27_704`).

This single short range is the sole deviation from the uniform 1,200-per-file pattern, and it is precisely why the corpus totals **33,105** functions (27 standard files × 1,200 + 705) rather than 33,600. The full per-layer rollup of files, function counts, and module symbols is maintained in [`./module-reference.md`](./module-reference.md).

## Uniqueness and File-Locality

Because `<fileId>` is unique per file and `<k>` is unique within a file, every `mod_<fileId>_<k>` symbol is **globally unique** across the entire corpus — no two functions share a name (Source: Tech Spec §2.2.3; representative `society_mgmt_300k/src/controllers/file_0.js:L3` and `society_mgmt_300k/src/middleware/file_27.js:L3`).

These symbols are nonetheless **file-local**. There are **zero** `module.exports` and **zero** `require(` occurrences anywhere across the corpus's `src/` and `tests/` trees, so no function is exported from its file and none is imported into another (Source: Tech Spec §2.2.4 — 0 `module.exports`, 0 `require(` across the corpus; representative `society_mgmt_300k/src/controllers/file_0.js`). As a *verified absence*, the `mod_<fileId>_<k>` names therefore do **not** form an importable or public API — each is addressable only as an identifier within its own source file, never across module boundaries.

## Module-to-Layer Mapping

For context, file numbers are distributed **round-robin** across the corpus's eleven layers, so a module id maps deterministically to a layer — for example `mod_0` lives in `controllers`, `mod_6` in `config`, and `mod_27` in `middleware` (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`, `society_mgmt_300k/src/config/file_6.js:L1`, `society_mgmt_300k/src/middleware/file_27.js:L1` (module headers); Tech Spec §1.2.2). This document covers only the naming scheme; the complete per-layer table of every module symbol is maintained in [`./module-reference.md`](./module-reference.md).

## Cross-References

- [`./module-reference.md`](./module-reference.md) — the full per-layer inventory of all 29 files and the module symbols (`mod_<N>`) each contains.
- [`./arithmetic-helpers.md`](./arithmetic-helpers.md) — the *representative function* contract `mod_<fileId>_<k>(x) → 6x + 10` that every named symbol implements.
- [`./README.md`](./README.md) — the functionality index.
- [`../README.md`](../README.md) — the top-level documentation hub.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1,L3` — the header comment `// mod_0 - society module` (line 1) that fixes the module id, and the first function `mod_0_0(x)` (line 3).
- `society_mgmt_300k/src/controllers/file_0.js:L3` (first function `mod_0_0`); Tech Spec §1.2.2 — standard files contain 1,200 functions (`k = 0 .. 1199`; last `mod_0_1199`).
- `society_mgmt_300k/src/middleware/file_27.js:L1` — the header comment `// mod_27 - society module`; this file is the short variant with 705 functions (`k = 0 .. 704`; last `mod_27_704`).
- Tech Spec §2.2.4 — 0 `module.exports` and 0 `require(` across the corpus; the symbols are file-local and not part of any importable API (*verified absence*).
- `society_mgmt_300k/src/controllers/file_0.js:L1`, `society_mgmt_300k/src/config/file_6.js:L1`, `society_mgmt_300k/src/middleware/file_27.js:L1` (module headers); Tech Spec §1.2.2 — the round-robin module-to-layer distribution (`mod_0` → controllers, `mod_6` → config, `mod_27` → middleware).
- Tech Spec §2.2.3 — the module-function symbol namespace.

---

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)
