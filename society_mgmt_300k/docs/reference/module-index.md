# Module Index

## Purpose

This page enumerates every *module* in the *corpus* and maps each file to its
`mod_N` id and approximate *helper* (`mod_N_M`) count. Because every *helper*
shares one byte-identical body, this index links to the *canonical contract*
instead of repeating the behavior or listing all 33,105 functions.
`Source: society_mgmt_300k/src/**`, `society_mgmt_300k/tests/**`. Reference:
`[1.2 System Overview §1.2.2]`.

## Modules by namespace

The table below lists every *module* file, its `mod_N` id, and its approximate
`mod_N_M(x)` *helper* count. Every full *module* holds `~1,200` identical
*helpers*; the only exceptions are `middleware/file_27.js` (`705`) and the
comment-only `utils/filler.js` (`0`).
`Source: society_mgmt_300k/src/**`, `society_mgmt_300k/tests/**`.

| Namespace | File | Module id | Approx. functions |
| --- | --- | --- | --- |
| `src/controllers` | `file_0.js` | `mod_0` | `~1,200` |
| `src/controllers` | `file_11.js` | `mod_11` | `~1,200` |
| `src/controllers` | `file_22.js` | `mod_22` | `~1,200` |
| `src/services` | `file_1.js` | `mod_1` | `~1,200` |
| `src/services` | `file_12.js` | `mod_12` | `~1,200` |
| `src/services` | `file_23.js` | `mod_23` | `~1,200` |
| `src/routes` | `file_3.js` | `mod_3` | `~1,200` |
| `src/routes` | `file_14.js` | `mod_14` | `~1,200` |
| `src/routes` | `file_25.js` | `mod_25` | `~1,200` |
| `src/models` | `file_2.js` | `mod_2` | `~1,200` |
| `src/models` | `file_13.js` | `mod_13` | `~1,200` |
| `src/models` | `file_24.js` | `mod_24` | `~1,200` |
| `src/domain` | `file_8.js` | `mod_8` | `~1,200` |
| `src/domain` | `file_19.js` | `mod_19` | `~1,200` |
| `src/repositories` | `file_7.js` | `mod_7` | `~1,200` |
| `src/repositories` | `file_18.js` | `mod_18` | `~1,200` |
| `src/middleware` | `file_5.js` | `mod_5` | `~1,200` |
| `src/middleware` | `file_16.js` | `mod_16` | `~1,200` |
| `src/middleware` | `file_27.js` | `mod_27` | `705` |
| `src/config` | `file_6.js` | `mod_6` | `~1,200` |
| `src/config` | `file_17.js` | `mod_17` | `~1,200` |
| `src/utils` | `file_4.js` | `mod_4` | `~1,200` |
| `src/utils` | `file_15.js` | `mod_15` | `~1,200` |
| `src/utils` | `file_26.js` | `mod_26` | `~1,200` |
| `src/utils` | `filler.js` | `(none)` | `0` |
| `tests/unit` | `file_9.js` | `mod_9` | `~1,200` |
| `tests/unit` | `file_20.js` | `mod_20` | `~1,200` |
| `tests/integration` | `file_10.js` | `mod_10` | `~1,200` |
| `tests/integration` | `file_21.js` | `mod_21` | `~1,200` |

Across the *corpus* there are 28 `mod_*` *modules* — 24 under `src/` plus 4
static fixtures under `tests/` — alongside the comment-only `utils/filler.js`,
which is not a `mod_*` *module*. The `src/` *modules* define 28,305 *helpers*
(23 full *modules* at `~1,200` each, plus `file_27.js`'s `705`) and the `tests/`
fixtures add 4,800 (4 at `~1,200`), for a grand total of 33,105 *helper*
functions. `Source: society_mgmt_300k/src/**`, `society_mgmt_300k/tests/**`.
Reference: `[1.2 System Overview §1.2.2]`.

## Namespace reference pages

Each of the nine `src/` namespaces has a dedicated reference page:

- [controllers](namespaces/controllers.md)
- [services](namespaces/services.md)
- [routes](namespaces/routes.md)
- [models](namespaces/models.md)
- [domain](namespaces/domain.md)
- [repositories](namespaces/repositories.md)
- [middleware](namespaces/middleware.md)
- [config](namespaces/config.md)
- [utils](namespaces/utils.md)

## Notes

- `utils/filler.js` is comment-only sizing padding with `0` functions; its
  banner (the first line) is exactly `// filler 298001`. It defines no *helper*,
  no `mod_N` id, and no `store`.
  `Source: society_mgmt_300k/src/utils/filler.js`.
- `middleware/file_27.js` (`mod_27`) has `705` *helper* functions — smaller than
  the `~1,200` in every full *module*. Only the count differs; the bodies remain
  byte-identical. `Source: society_mgmt_300k/src/middleware/file_27.js`.
- The `tests/unit/**` and `tests/integration/**` *modules* are static fixtures
  that contain the same identical *helpers* — no assertions, no runner, and no
  imports — so they are not an executable suite.
  `Source: society_mgmt_300k/tests/unit/file_9.js:L1-L10`. Reference:
  `[4.1 System Workflows §4.1.2]`.
- All *helpers* are behaviorally identical; for the behavior itself, see the
  *canonical contract* linked below.
  `Source: society_mgmt_300k/src/controllers/file_0.js:L3-L10`.
- Behavior (single *canonical contract*): [Helper Computation](../functional-flows/helper-computation.md).
- Input/output contract: [Function contract](function-contract.md).

## Source Citations

- `society_mgmt_300k/src/**` — the nine `src/` namespaces and their `mod_N`
  *module* files enumerated in the table above.
- `society_mgmt_300k/tests/**` — the four static test-fixture *modules* under
  `tests/unit/` and `tests/integration/`.
- `society_mgmt_300k/src/middleware/file_27.js` — the smaller `705`-*helper*
  *module* (`mod_27`).
- `society_mgmt_300k/src/utils/filler.js` — the comment-only sizing file
  (`0` functions, banner `// filler 298001`).
- `society_mgmt_300k/src/controllers/file_0.js:L3-L10` — the *canonical
  contract* *helper* body that every *module* shares.
- `[1.2 System Overview §1.2.2]` — the corpus-wide *module* and function totals.
