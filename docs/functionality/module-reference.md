# Module Reference

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)

## Purpose

This document is the authoritative **per-layer module inventory** of the synthetic [`society_mgmt_300k`](../overview.md) JavaScript *corpus* — all **29 `.js` files** and their **33,105 functions**, distributed across **11 layers** (nine `src` layers plus two `tests` layers). Because the layers carry **no inter-module wiring** and every function is **byte-identical**, the inventory is organized **per layer** — listing each layer's file count, function count, and module symbols — rather than enumerating the 33,105 near-identical functions individually (the *representative-pattern* approach). The single canonical *representative function* those symbols implement is documented in [`arithmetic-helpers.md`](./arithmetic-helpers.md). This inventory is the single source of truth for the corpus's structural counts and is reconciled against by [`architecture.md`](../architecture.md), [`corpus-sizing.md`](./corpus-sizing.md), and [`symbol-namespace.md`](./symbol-namespace.md).

## Per-Layer Inventory

The table below lists every layer with its file count, function count, and the module symbols (`mod_<N>`) it contains (Source: Tech Spec §1.2.2 — per-layer file and function counts; representative module header `society_mgmt_300k/src/controllers/file_0.js:L1`).

| Layer (path) | Files | Functions | Module symbols |
| --- | --- | --- | --- |
| `src/config/` | 2 | 2,400 | mod_6, mod_17 |
| `src/controllers/` | 3 | 3,600 | mod_0, mod_11, mod_22 |
| `src/domain/` | 2 | 2,400 | mod_8, mod_19 |
| `src/middleware/` | 3 | 3,105 | mod_5, mod_16, mod_27 (705) |
| `src/models/` | 3 | 3,600 | mod_2, mod_13, mod_24 |
| `src/repositories/` | 2 | 2,400 | mod_7, mod_18 |
| `src/routes/` | 3 | 3,600 | mod_3, mod_14, mod_25 |
| `src/services/` | 3 | 3,600 | mod_1, mod_12, mod_23 |
| `src/utils/` | 3 (+`filler.js`) | 3,600 | mod_4, mod_15, mod_26 |
| `tests/unit/` | 2 | 2,400 | mod_9, mod_20 |
| `tests/integration/` | 2 | 2,400 | mod_10, mod_21 |
| **Total** | **29** | **33,105** | — |

**Reconciliation.** The file counts sum to **29** — `2 + 3 + 2 + 3 + 3 + 2 + 3 + 3 + 3 (+ filler.js) + 2 + 2`, i.e. 28 numbered files plus `src/utils/filler.js` — and the function counts sum to **33,105** (Source: Tech Spec §1.2.2 (per-layer counts); Tech Spec §2.2.6 (corpus total of 33,105 functions)).

- **File → module mapping.** Each file declares its module identity in its header comment `// mod_<N> - society module` on line 1, and files are assigned to layers by a round-robin distribution over the file number (`file_0` → `controllers/mod_0`, `file_1` → `services/mod_1`, …, `file_27` → `middleware/mod_27`) (Source: `society_mgmt_300k/src/controllers/file_0.js:L1` (representative header `// mod_0 - society module`); Tech Spec §1.2.2).

## Notes

The following verified specifics explain the counts above:

- **Standard files contain 1,200 functions each** — `mod_<id>_0` … `mod_<id>_1199`. This uniform count holds for all 28 numbered files except the short variant noted below (Source: `society_mgmt_300k/src/controllers/file_0.js:L3` (first function `mod_0_0`); Tech Spec §1.2.2 — 1,200 functions per standard file).
- **Short variant — `src/middleware/file_27.js` contains 705 functions** (`mod_27_0` … `mod_27_704`). This is the sole deviation from the uniform 1,200, and it is why the `middleware` layer totals **3,105** functions (`= 2 × 1,200 + 705`) rather than 3,600 (Source: `society_mgmt_300k/src/middleware/file_27.js:L1`; Tech Spec §1.2.2 — the 705-function short variant).
- **`src/utils/filler.js` contains 0 functions** — it is comment-only padding (`// filler NNNNNN` on every line) and contributes nothing to the function totals, although it is counted among the 29 `.js` files (Source: `society_mgmt_300k/src/utils/filler.js:L1` and `society_mgmt_300k/src/utils/filler.js:L1999` — comment-only padding; Tech Spec §2.2.6).
- **The `config/` layer holds arithmetic functions, NOT configuration values** — `file_6.js` and `file_17.js` contain the same `6x + 10` functions as every other layer; there are no configuration keys, values, or settings anywhere in the corpus (Source: `society_mgmt_300k/src/config/file_6.js:L1`; Tech Spec §2.2.2 — config-layer files hold the same `6x + 10` arithmetic, not configuration values).
- **The `tests/` files contain NO assertions** — `tests/unit/**` and `tests/integration/**` hold the same arithmetic functions as the `src` layers and are **not** functional tests; they contain no assertion keywords (`expect`, `assert`, `describe`, `it`, or `test`) (Source: Tech Spec §1.2.2 — `tests/unit` and `tests/integration` hold the same arithmetic functions with no assertions or test-runner code; representative `society_mgmt_300k/tests/unit/file_9.js:L3`).
- **Nothing is exported or importable** — there are zero `module.exports` and zero `require(` occurrences across `src` and `tests`, so every module symbol is **file-local** and the corpus exposes no public API. This is a *verified absence*, not an omission from this inventory (Source: Tech Spec §2.2.4 — zero `module.exports` and zero `require(` across the corpus, so every symbol is file-local with no public API).

## Cross-References

- [`symbol-namespace.md`](./symbol-namespace.md) — how the `mod_<fileId>_<k>` module symbols listed above are named and why they are globally unique.
- [`corpus-sizing.md`](./corpus-sizing.md) — how these file and function counts map to the deterministic 300,000-line total.
- [`arithmetic-helpers.md`](./arithmetic-helpers.md) — the single *representative function* contract (`6x + 10`) that every one of the 33,105 functions implements.
- [`README.md`](./README.md) — the functionality index for the topics above.
- [`../README.md`](../README.md) — the top-level documentation hub.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js:L1` (representative header `// mod_0 - society module`); Tech Spec §1.2.2 — the per-file / per-layer file and function counts.
- `society_mgmt_300k/src/config/file_6.js:L1` — the `config/` layer holds arithmetic functions, not configuration values.
- `society_mgmt_300k/src/middleware/file_27.js:L1` — the 705-function short variant that yields the `middleware` total of 3,105.
- `society_mgmt_300k/src/utils/filler.js:L1` and `society_mgmt_300k/src/utils/filler.js:L1999` — comment-only padding with 0 functions.
- `society_mgmt_300k/tests/unit/file_9.js:L3`; Tech Spec §1.2.2 — the test layers contain the same arithmetic functions and no assertions or test-runner code.
- Tech Spec §1.2.2 — the nominal layered scaffold and the non-functional nature of the `tests/` files.

---

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)
