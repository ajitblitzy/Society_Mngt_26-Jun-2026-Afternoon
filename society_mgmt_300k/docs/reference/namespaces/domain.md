# Namespace: domain

## Purpose

`src/domain/` is a nominal domain-logic layer in the *corpus*; despite the name it holds no domain model or business rules — only identical, deterministic arithmetic *helpers* (`mod_N_M`) spread across its *module* files. Source: society_mgmt_300k/src/domain/file_8.js:L1-L10

## Modules

- `file_8.js` → `mod_8` → ~1,200 helper functions. Source: society_mgmt_300k/src/domain/file_8.js
- `file_19.js` → `mod_19` → ~1,200 helper functions. Source: society_mgmt_300k/src/domain/file_19.js

## Behavior

Every `mod_N_M(x)` helper in this namespace is identical to the [canonical contract](../../functional-flows/helper-computation.md): it computes `r = 6x` and adds `10` when `6x` is even. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## Notes

The `domain` folder name is a **nominal layer only** — the modules are identical arithmetic *helpers*, not domain logic, and nothing here defines an entity, aggregate, or business rule. Each *module* also declares a dead `const store = [];` placeholder at the top that is never read or written. Source: society_mgmt_300k/src/domain/file_8.js:L2

## Source Citations

- Source: society_mgmt_300k/src/domain/
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
