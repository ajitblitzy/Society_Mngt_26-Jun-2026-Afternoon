# Namespace: models

## Purpose

`src/models/` is a nominal data-model layer in the *corpus* — a set of source *modules* that, despite the folder name, define **no data schema** and instead contain only identical, deterministic arithmetic *helpers* (`mod_N_M`).
`Source: society_mgmt_300k/src/models/file_2.js:L1-L10`

## Modules

- `file_2.js` → `mod_2` → ~1,200 helper functions. Source: society_mgmt_300k/src/models/file_2.js:L1-L10
- `file_13.js` → `mod_13` → ~1,200 helper functions. Source: society_mgmt_300k/src/models/file_13.js:L1-L10
- `file_24.js` → `mod_24` → ~1,200 helper functions. Source: society_mgmt_300k/src/models/file_24.js:L1-L10

## Behavior

Every `mod_N_M(x)` helper in this namespace is identical to the [canonical contract](../../functional-flows/helper-computation.md): it computes `r = 6x` and adds `10` when `6x` is even.
`Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`

## Notes

Despite the folder name, **no data schema exists** in this namespace: there are no ORM models, no table or collection definitions, and no field or column schemas anywhere in `src/models/`. The `models` folder name is nominal only; aside from the *helpers*, the only module-level statement in each *module* is a dead `const store = [];` placeholder that is never read or written.
`Source: society_mgmt_300k/src/models/file_2.js:L1-L10`

## Source Citations

- Source: society_mgmt_300k/src/models/file_2.js:L1-L10
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
