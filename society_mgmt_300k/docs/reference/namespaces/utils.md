# Namespace: utils

## Purpose

The `src/utils/` folder is a nominal utilities layer in the *corpus*; despite the name it holds no general-purpose utilities. Its three `mod_N` *module* files each contain identical deterministic arithmetic *helpers*, alongside one comment-only sizing file (`filler.js`) that defines no code at all. `Source: society_mgmt_300k/src/utils/file_4.js:L1-L10`

## Modules

- `file_4.js` → `mod_4` → ~1,200 helper functions. Source: society_mgmt_300k/src/utils/file_4.js:L1-L10
- `file_15.js` → `mod_15` → ~1,200 helper functions. Source: society_mgmt_300k/src/utils/file_15.js:L1-L10
- `file_26.js` → `mod_26` → ~1,200 helper functions. Source: society_mgmt_300k/src/utils/file_26.js:L1-L10
- `filler.js` → (no module id) → **0** functions — comment-only sizing padding. Source: society_mgmt_300k/src/utils/filler.js:L1-L1999

## Behavior

Every `mod_N_M(x)` helper in this namespace is identical to the [canonical contract](../../functional-flows/helper-computation.md): it computes `r = 6x` and adds `10` when `6x` is even. `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10` By contrast, `filler.js` defines no helpers and has no runtime behavior. `Source: society_mgmt_300k/src/utils/filler.js:L1-L1999`

## Notes

- `filler.js` is comment-only sizing padding with **0** functions: every line is a `// filler NNNNNN` comment and its banner (the first line) is exactly `// filler 298001`, running through `// filler 299999`. It exists only to pad the *corpus* toward its 300,000-line target and defines no *helpers*, no exports, and no `store`. `Source: society_mgmt_300k/src/utils/filler.js:L1-L1999`
- The `utils` folder name is nominal only — an organizational label that does not imply any general-purpose utility behavior beyond the identical arithmetic *helpers* described above. `Source: society_mgmt_300k/src/utils/file_4.js:L1-L10`

## Source Citations

- Source: society_mgmt_300k/src/utils/file_4.js:L1-L10
- Source: society_mgmt_300k/src/utils/filler.js:L1-L1999
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
