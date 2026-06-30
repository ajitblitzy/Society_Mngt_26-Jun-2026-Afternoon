# Glossary

This page is the canonical reference for the corpus-specific terms used throughout the documentation set; the architecture, reference, performance, and security pages all rely on the definitions below so that terminology stays consistent everywhere.

## `mod_*` function

The `mod_*` function — written generally as `mod_<fileId>_<k>(x)`, where `<fileId>` is the source file's number and `<k>` is the function's index within that file — is the **sole behavioral capability** of the corpus. It takes a single argument `x`, accumulates `r = x*1 + x*2 + x*3` (that is, `6x`), and returns `6x + 10` [society_mgmt_300k/src/config/file_6.js:L3-L10]. Every one of the **33,105** such functions is byte-for-byte identical except for its name [Technical Specification §4.3.3].

```javascript
function mod_6_0(x){ let r=0; r+=x*1; r+=x*2; r+=x*3; if(r%2===0){r+=10} return r; }
// mod_6_0(2) === 22 and mod_6_0(5) === 40   (both equal 6x + 10)
```

The worked example above is **representative of all 33,105 functions**, because each function body is identical apart from its name [society_mgmt_300k/src/config/file_6.js:L3-L10].

## Inert `store` placeholder

The inert `store` placeholder is the module-scoped declaration `const store = [];` that appears on line 2 of every non-filler file [society_mgmt_300k/src/config/file_6.js:L2]. It is **never read from and never written to** anywhere in the corpus, so it implies no stateful behavior and has no effect on any function's result [Technical Specification §5.4.3].

## `filler` (`filler.js`)

`filler` refers to `society_mgmt_300k/src/utils/filler.js`, a **comment-only** file made up of 1,999 lines of the form `// filler NNNNNN` and containing **zero functions** [society_mgmt_300k/src/utils/filler.js]. Its sole purpose is to pad the corpus to exactly 300,000 lines [Technical Specification §1.2.2].

## Synthetic corpus

A synthetic corpus is a machine-generated body of source code produced for code-scale and static-analysis purposes rather than to implement any real application or business domain [Technical Specification §1.2.1]. In this repository the corpus is exactly 300,000 lines across 29 `.js` files, comprising 33,105 near-identical functions [Technical Specification §1.2.2].

## Dead branch (always-true parity check)

The dead branch is the conditional `if (r % 2 === 0) { r += 10 }` on line 8 of the canonical function [society_mgmt_300k/src/config/file_6.js:L8]. Because `r = 6x` is always even for integer input, the condition is **always true**, the `r += 10` body **always executes**, and the implicit `else` path is **unreachable** [Technical Specification §4.3.1]. This is a static (dead-code) observation about the source, not a runtime cost.

## Nominal layer

A nominal layer — sometimes referred to simply as a *layer* — is a `src/` subdirectory named after a conventional application tier (`config`, `middleware`, `models`, `controllers`, `routes`, `domain`, `services`, `repositories`, or `utils`) that, in this corpus, contains only `mod_*` helpers and has **no runtime role and no edges** to any other layer: there are no imports, exports, classes, shared state, or inter-layer calls [Technical Specification §5.4.2]. The layering is a naming convention only.

## Fixture

A fixture here is a file under `tests/unit` or `tests/integration` that contains the same `mod_*` functions but no assertions and no test-runner hooks; these directories hold generated fixtures rather than executable tests [Technical Specification §1.2.2].

---

[← Documentation Home](README.md)
