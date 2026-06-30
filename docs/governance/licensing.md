# Licensing Governance

## Purpose

This document records the **single open governance concern** for the `society_mgmt_300k` corpus: a **license inconsistency** between the repository root and the project subfolder. The repository declares two different licenses in two locations — an Apache License 2.0 at the root and an MIT License inside the project folder (Source: /LICENSE:L1-L2; Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1; Tech Spec §2.2.7).

This document **flags and recommends only; it does not change, select, rewrite, or delete any license file** (Source: Tech Spec §6.4.6.2 — Licensing Governance (Open Issue F-006)). The choice of a governing license is left to the repository owners. Consistent with the security posture documentation, licensing is treated here as the lone *governance* item rather than a security flaw — see the [security posture](../security.md) document.

## The License Inconsistency

The repository declares **two different, legally distinct licenses** in two separate locations (Source: /LICENSE:L1-L2; Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1; Tech Spec §2.2.7):

- The repository-root file `LICENSE` is the **Apache License, Version 2.0** — its header reads "Apache License" followed by "Version 2.0, January 2004" (Source: /LICENSE:L1-L2).
- The project-subfolder file `society_mgmt_300k/LICENSE/LICENSE.txt` is the **MIT License**, bearing "Copyright (c) 2026" (Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1, :L3).

| Location | Path | License | Citation |
| --- | --- | --- | --- |
| Repository root | `LICENSE` | Apache License 2.0 | `Source: /LICENSE:L1-L2` |
| Project subfolder | `society_mgmt_300k/LICENSE/LICENSE.txt` | MIT License | `Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1` |

Both the Apache License 2.0 and the MIT License are permissive open-source licenses, but they are **legally distinct**: the Apache License 2.0 carries an explicit patent grant and NOTICE/attribution obligations that the MIT License does not (Source: /LICENSE:L73 — the "Grant of Patent License" clause; /LICENSE:L106-L108 — the NOTICE-file attribution requirement; society_mgmt_300k/LICENSE/LICENSE.txt:L1 — the MIT License, which states neither). The documented concern is this **license-type mismatch (Apache vs MIT)**. The MIT notice in the subfolder is also abbreviated — a brief notice rather than the conventional full permission text — but completeness is secondary to the license-type mismatch itself (Source: society_mgmt_300k/LICENSE/LICENSE.txt:L5 — the abbreviated "Permission is hereby granted..." line stands in for the conventional full MIT permission paragraph). Neither file declares an SPDX license identifier (Source: /LICENSE:L1-L2; Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1), so each license is identified here by name and line number rather than by an SPDX tag.

## Why It Matters (Impact)

The co-existence of two distinct licenses is a governance and clarity issue, not a security vulnerability (Tech Spec §6.4):

- **Ambiguous redistribution terms.** A downstream consumer cannot determine with certainty which license governs the repository as a whole, creating uncertainty about which obligations apply when redistributing — for example, whether the Apache 2.0 NOTICE/attribution handling and patent grant apply, or only the simpler MIT terms (Source: /LICENSE:L73, :L106-L108 — the Apache patent-grant and NOTICE/attribution clauses; society_mgmt_300k/LICENSE/LICENSE.txt:L1 — the simpler MIT terms).
- **Automated license scanners will report a conflict.** SPDX/compliance tooling that scans the tree will detect two distinct licenses and flag a conflict or a "multiple/ambiguous license" finding (Tech Spec §6.4).

This remains a governance/clarity matter rather than a security flaw; the [security posture](../security.md) documentation classifies it accordingly as the lone open governance item (Tech Spec §6.4).

## Recommended Resolution (Guidance Only)

The following is **neutral guidance**, not an action taken by this document (Source: Tech Spec §6.4.6.2 — Licensing Governance (Open Issue F-006)):

1. **Standardize on a single license.** Choose **one** license to apply repository-wide and align both files so that the root `LICENSE` and `society_mgmt_300k/LICENSE/LICENSE.txt` declare the same license (Source: /LICENSE:L1-L2; Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1).
2. **Make copyright notices consistent.** Once a single license is chosen, ensure the copyright holder and year notices are consistent across the repository (Source: society_mgmt_300k/LICENSE/LICENSE.txt:L3 — the "Copyright (c) 2026" notice).
3. **Optionally add an SPDX identifier.** After a single license is settled, adding an SPDX identifier in source or release metadata can help automated tooling recognize the license unambiguously. This is an optional aid, not a requirement (Tech Spec §6.4).

This document does **not** select Apache over MIT (or vice-versa), nor does it modify, rewrite, or delete any license file — standardization itself is the recommendation, and the decision rests with the repository owners (Source: Tech Spec §6.4.6.2 — Licensing Governance (Open Issue F-006)).

## Related Documentation

- [Security posture](../security.md) — lists this licensing item as the lone open governance concern.
- [Documentation index](../README.md) — the documentation hub for the corpus.

## Source Citations

- `Source: /LICENSE:L1-L2` — Apache License, Version 2.0, repository root.
- `Source: /LICENSE:L73` — the Apache "Grant of Patent License" clause; `Source: /LICENSE:L106-L108` — the Apache NOTICE-file attribution requirement (obligations the MIT License does not carry).
- `Source: society_mgmt_300k/LICENSE/LICENSE.txt:L1` — MIT License title; `:L3` — the copyright notice; `:L5` — the abbreviated permission text, project subfolder.
- `Tech Spec §2.2.7` (F-006: Repository Licensing Artifacts) and `Tech Spec §6.4.6.2` (Licensing Governance, Open Issue F-006) — the authoritative governance references for the licensing inconsistency.
