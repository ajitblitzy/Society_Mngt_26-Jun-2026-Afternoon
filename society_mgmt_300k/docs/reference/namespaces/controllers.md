# Namespace: controllers

## Purpose

The `src/controllers/` namespace is a nominal application layer in the *corpus*. Despite the "controllers" name it holds no request handling, routing, or application logic — each *module* contains only identical, deterministic arithmetic *helpers* of the form `mod_N_M`. Source: society_mgmt_300k/src/controllers/file_0.js:L1-L10

## Modules

- `file_0.js` → `mod_0` → ~1,200 helper functions. Source: society_mgmt_300k/src/controllers/file_0.js
- `file_11.js` → `mod_11` → ~1,200 helper functions. Source: society_mgmt_300k/src/controllers/file_11.js
- `file_22.js` → `mod_22` → ~1,200 helper functions. Source: society_mgmt_300k/src/controllers/file_22.js

## Behavior

Every `mod_N_M(x)` helper in this namespace is identical to the [canonical contract](../../functional-flows/helper-computation.md): it computes `r = 6x` and adds `10` when `6x` is even. Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10

## Notes

- The `controllers` folder name is a **nominal layer only**: the *modules* are identical arithmetic *helpers*, not controllers, and none of them handles requests or holds application logic. Source: society_mgmt_300k/src/controllers/file_0.js:L1
- Each *module* declares a module-level `const store = [];` that is never read or written — a vestigial dead placeholder. Source: society_mgmt_300k/src/controllers/file_0.js:L2

## Source Citations

- Source: society_mgmt_300k/src/controllers/
- Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10
