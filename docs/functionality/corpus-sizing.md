# Corpus Sizing (F-005)

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)

## Purpose

The [`society_mgmt_300k`](../overview.md) *corpus* is deliberately sized to **exactly 300,000 lines** — the figure is part of its name and is an intentional, reproducible construction rather than an incidental total. This document shows the **deterministic composition arithmetic** behind that number: the three groups of files that sum to 300,000 lines, the per-file line formula that produces each group, and the function-count reconciliation that ties the line totals back to the corpus's 33,105 functions. Because the total is exact, it also explains *why* the documentation must never edit a source file: adding or removing a single line would break the 300,000-line property (Source: `Tech Spec §2.2.6`; AAP §0.8.2).

Line counts in this document are measured the way `wc -l` measures them — by counting newline (`\n`) characters — across the **29 `.js` files** under `society_mgmt_300k/`, which totals **300,000** (Source: repository scan, `find society_mgmt_300k -name "*.js" | xargs wc -l` total = 300000).

## Composition Breakdown

The 29 `.js` files fall into exactly three groups by line count. The table below lists each group with its file count, per-file line count, and subtotal; the subtotals sum to the 300,000-line total.

| Component | Files | Lines each | Subtotal |
| --- | --- | ---: | ---: |
| Standard module files (`file_0.js` … `file_26.js`) | 27 | 10,802 | 291,654 |
| `src/utils/filler.js` (comment-only padding) | 1 | 1,999 | 1,999 |
| `src/middleware/file_27.js` (short variant) | 1 | 6,347 | 6,347 |
| **Total** | **29** | **—** | **300,000** |

- The line-count distribution was confirmed by a first-hand scan: **27** files measure 10,802 lines, **1** file (`filler.js`) measures 1,999 lines, and **1** file (`file_27.js`) measures 6,347 lines — 29 files in all, with no other line counts present (Source: repository scan, per-file `wc -l` across `society_mgmt_300k/**/*.js`).
- The canonical standard file is `society_mgmt_300k/src/controllers/file_0.js` at **10,802 lines** (Source: `society_mgmt_300k/src/controllers/file_0.js`, `wc -l` = 10802).
- `src/utils/filler.js` is **comment-only padding**: every line is of the form `// filler NNNNNN`, spanning the observed range `// filler 298001` … `// filler 299999`, for **1,999 lines** and **0 functions** (Source: `society_mgmt_300k/src/utils/filler.js:L1`, `:L1999`).
- `src/middleware/file_27.js` is the **short variant** at **6,347 lines** (the only numbered file that is not 10,802 lines) (Source: `society_mgmt_300k/src/middleware/file_27.js`, `wc -l` = 6347).

## Line-Count Arithmetic

The three subtotals sum exactly to the corpus total:

```text
291,654   (27 standard files × 10,802 lines)
+   1,999   (src/utils/filler.js)
+   6,347   (src/middleware/file_27.js)
= 300,000   (29 files total)
```

Equivalently, `27 × 10,802 = 291,654`, and `291,654 + 1,999 + 6,347 = 300,000` (Source: repository scan, `find society_mgmt_300k -name "*.js" | xargs wc -l` total = 300000).

## Per-File Line Formula

The line count of every **numbered** module file follows a single structural formula. Each numbered file begins with **2 prefix lines** and then contributes **9 lines per function**:

- **Line 1** — the module header comment `// mod_<id> - society module` (Source: `society_mgmt_300k/src/controllers/file_0.js:L1`).
- **Line 2** — the module-scoped placeholder `const store = [];` (Source: `society_mgmt_300k/src/controllers/file_0.js:L2`).
- **Per function** — 8 lines of code (the `function` declaration, `let r=0;`, three `r+=x*n;` accumulations, the `if(r%2===0){r+=10}` branch, `return r;`, and the closing `}`) followed by **1 trailing blank line**, for **9 lines per function** (Source: `society_mgmt_300k/src/controllers/file_0.js:L3-L11`).

This yields the formula:

```text
file_lines = 2 + 9 × (function count)
```

The formula is verified against both observed numbered-file sizes:

| File | Function count | `2 + 9 × fn_count` | Measured lines |
| --- | ---: | ---: | ---: |
| Standard (e.g. `src/controllers/file_0.js`) | 1,200 | `2 + 9 × 1,200 = 10,802` | 10,802 |
| Short (`src/middleware/file_27.js`) | 705 | `2 + 9 × 705 = 6,347` | 6,347 |

- Standard files contain 1,200 functions and 1,200 trailing blank lines, giving `2 + 9 × 1,200 = 10,802` (Source: `society_mgmt_300k/src/controllers/file_0.js` — 1,200 functions, 1,200 blank lines).
- The short variant contains 705 functions and 705 trailing blank lines, giving `2 + 9 × 705 = 6,347` (Source: `society_mgmt_300k/src/middleware/file_27.js` — 705 functions).

**`filler.js` is the documented exception to this formula.** It has **no header line, no `store` declaration, and no functions** — it is **1,999 lines** of comment-only padding (`// filler NNNNNN`) and therefore does not follow `2 + 9 × fn_count`. Its sole purpose is to pad the corpus to the exact 300,000-line total. This is a *verified absence* of code, not an omission (Source: `society_mgmt_300k/src/utils/filler.js:L1`, `:L1999`).

## Function-Count Reconciliation

The same file groups reconcile to the corpus's **33,105** functions, confirming the line arithmetic above is consistent with the function inventory:

```text
27 standard files × 1,200 functions = 32,400
src/middleware/file_27.js           =    705
src/utils/filler.js                 =      0
                              total  = 33,105
```

That is, `27 × 1,200 + 705 = 33,105` functions, with `filler.js` contributing **0** functions because it is comment-only padding (Source: repository scan, function total = 33,105; `society_mgmt_300k/src/utils/filler.js` = 0 functions). The per-layer distribution of these counts (which layer each numbered file belongs to) is tabulated in [`./module-reference.md`](./module-reference.md).

## Cross-References

- [`module-reference.md`](./module-reference.md) — the per-layer inventory that maps these 29 files and 33,105 functions onto the 11 layers.
- [`symbol-namespace.md`](./symbol-namespace.md) — the `mod_<fileId>_<k>` naming scheme and the per-file index ranges (`0 … 1199` standard; `0 … 704` for `file_27.js`) implied by the function counts above.
- [`arithmetic-helpers.md`](./arithmetic-helpers.md) — the single *representative function* contract (`6x + 10`) whose 8-line body, plus a trailing blank line, accounts for the 9 lines per function.
- [`README.md`](./README.md) — the functionality index.
- [`../README.md`](../README.md) — the top-level documentation hub.

## Source Citations

- `society_mgmt_300k/src/controllers/file_0.js` — the canonical standard file: 10,802 lines, 1,200 functions; line 1 header, line 2 `const store = [];`, function body `L3-L11`.
- `society_mgmt_300k/src/middleware/file_27.js` — the 6,347-line short variant with 705 functions.
- `society_mgmt_300k/src/utils/filler.js` — 1,999 lines of comment-only padding (`// filler 298001` … `// filler 299999`), 0 functions.
- Repository scan — `find society_mgmt_300k -name "*.js" | xargs wc -l` total = 300,000 lines across 29 files; function total = 33,105.
- `Tech Spec §2.2.6` — the deterministic 300,000-line composition (F-005).

---

← Back to the [functionality index](./README.md) · [documentation hub](../README.md)
