# Namespace: middleware

## Purpose

The `src/middleware/` namespace is a nominal middleware layer within the *corpus*; despite the name, it defines no request/response middleware pipeline and instead exposes only identical deterministic arithmetic *helpers* (`mod_N_M`) organized into its *module* files. Source: society_mgmt_300k/src/middleware/file_5.js:L1-L10

## Modules

- `file_5.js` → `mod_5` → ~1,200 helper functions. Source: society_mgmt_300k/src/middleware/file_5.js:L1-L10
- `file_16.js` → `mod_16` → ~1,200 helper functions. Source: society_mgmt_300k/src/middleware/file_16.js:L1-L10
- `file_27.js` → `mod_27` → **705** helper functions (smaller than the ~1,200 full modules). Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10

## Behavior

Every `mod_N_M(x)` helper in this namespace is identical to the [canonical contract](../../functional-flows/helper-computation.md): it computes `r = 6x` and adds `10` when `6x` is even. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## Notes

- **`file_27.js` (`mod_27`) contains 705 functions, which is smaller than the ~1,200 helpers in the full modules.** Only the count differs — the bodies are still byte-identical to the canonical contract. Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10
- The `middleware` folder name is a nominal layer only: there is no real request/response middleware, and each *module* declares a dead `const store = [];` that is never read or written. Source: society_mgmt_300k/src/controllers/file_0.js:L2

## Source Citations

- Source: society_mgmt_300k/src/middleware/file_5.js:L1-L10
- Source: society_mgmt_300k/src/middleware/file_27.js:L1-L10
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
