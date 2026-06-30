# Module Reference

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)

## Purpose

This document is the authoritative **per-layer module inventory** of the synthetic [`society_mgmt_300k`](../overview.md) JavaScript *corpus* — all **29 `.js` files** and their **33,105 functions**, distributed across **11 layers** (nine `src` layers plus two `tests` layers). Because the layers carry **no inter-module wiring** and every function is **byte-identical**, the inventory is organized **per layer** — listing each layer's file count, function count, and module symbols — rather than enumerating the 33,105 near-identical functions individually (the *representative-pattern* approach). The single canonical *representative function* those symbols implement is documented in [`arithmetic-helpers.md`](./arithmetic-helpers.md). This inventory is the single source of truth for the corpus's structural counts and is reconciled against by [`architecture.md`](../architecture.md), [`corpus-sizing.md`](./corpus-sizing.md), and [`symbol-namespace.md`](./symbol-namespace.md).

## Per-Layer Inventory

The table below lists every layer with its file count, function count, and the module symbols (`mod_<N>`) it contains. Counts were confirmed by a first-hand scan (`grep -c '^function mod_'` per file and a recursive `find`/listing for the file set).

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

**Reconciliation.** The file counts sum to **29** — `2 + 3 + 2 + 3 + 3 + 2 + 3 + 3 + 3 (+ filler.js) + 2 + 2`, i.e. 28 numbered files plus `src/utils/filler.js` — and the function counts sum to **33,105**. Source: first-hand repository scan of `society_mgmt_300k/src/**` and `society_mgmt_300k/tests/**`.

- **File → module mapping.** Each file declares its module identity in its header comment `// mod_<N> - society module` on line 1, and files are assigned to layers by a round-robin distribution over the file number (`file_0` → `controllers/mod_0`, `file_1` → `services/mod_1`, …, `file_27` → `middleware/mod_27`). Source: `society_mgmt_300k/src/**` (file headers, line 1).

## Notes

The following verified specifics explain the counts above:

- **Standard files contain 1,200 functions each** — `mod_<id>_0` … `mod_<id>_1199`. This uniform count holds for all 28 numbered files except the short variant noted below. Source: `society_mgmt_300k/src/controllers/file_0.js` (`grep -c '^function mod_'` = 1,200).
- **Short variant — `src/middleware/file_27.js` contains 705 functions** (`mod_27_0` … `mod_27_704`). This is the sole deviation from the uniform 1,200, and it is why the `middleware` layer totals **3,105** functions (`= 2 × 1,200 + 705`) rather than 3,600. Source: `society_mgmt_300k/src/middleware/file_27.js`.
- **`src/utils/filler.js` contains 0 functions** — it is comment-only padding (`// filler NNNNNN` on every line) and contributes nothing to the function totals, although it is counted among the 29 `.js` files. Source: `society_mgmt_300k/src/utils/filler.js`.
- **The `config/` layer holds arithmetic functions, NOT configuration values** — `file_6.js` and `file_17.js` contain the same `6x + 10` functions as every other layer; there are no configuration keys, values, or settings anywhere in the corpus. Source: `society_mgmt_300k/src/config/file_6.js:L1`.
- **The `tests/` files contain NO assertions** — `tests/unit/**` and `tests/integration/**` hold the same arithmetic functions as the `src` layers and are **not** functional tests; an assertion-keyword scan finds zero `expect`, `assert`, `describe`, `it`, or `test` occurrences. Source: `society_mgmt_300k/tests/**` (assertion-keyword scan = 0); Tech Spec §1.2.2.
- **Nothing is exported or importable** — there are zero `module.exports` and zero `require(` occurrences across `src` and `tests`, so every module symbol is **file-local** and the corpus exposes no public API. This is a *verified absence*, not an omission from this inventory. Source: repository scan (0 exports / 0 imports across `society_mgmt_300k/src/**` and `society_mgmt_300k/tests/**`).

## Cross-References

- [`symbol-namespace.md`](./symbol-namespace.md) — how the `mod_<fileId>_<k>` module symbols listed above are named and why they are globally unique.
- [`corpus-sizing.md`](./corpus-sizing.md) — how these file and function counts map to the deterministic 300,000-line total.
- [`arithmetic-helpers.md`](./arithmetic-helpers.md) — the single *representative function* contract (`6x + 10`) that every one of the 33,105 functions implements.
- [`README.md`](./README.md) — the functionality index for the topics above.
- [`../README.md`](../README.md) — the top-level documentation hub.

## Source Citations

- `society_mgmt_300k/src/**` — file headers (`// mod_<N> - society module`, line 1) and the per-file / per-layer file and function counts.
- `society_mgmt_300k/src/config/file_6.js:L1` — the `config/` layer holds arithmetic functions, not configuration values.
- `society_mgmt_300k/src/middleware/file_27.js` — the 705-function short variant that yields the `middleware` total of 3,105.
- `society_mgmt_300k/src/utils/filler.js` — comment-only padding with 0 functions.
- `society_mgmt_300k/tests/**` — the test layers contain the same arithmetic functions and zero assertions.
- Tech Spec §1.2.2 — the nominal layered scaffold and the non-functional nature of the `tests/` files.

---

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)
