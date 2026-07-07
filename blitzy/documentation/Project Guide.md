# Blitzy Project Guide — society_mgmt_300k Documentation

> **Project:** User-friendly functional-flow documentation for the `society_mgmt_300k` JavaScript corpus
> **Branch:** `blitzy-1f386c2e-cddd-41d5-9f36-94bfc911c106` · **HEAD:** `bd67cb5` · **Base:** `32093d3`
> **Type:** Documentation-only (AAP §0) · **Status:** ✅ Production-ready pending human review

---

## 1. Executive Summary

### 1.1 Project Overview

This project scans the `society_mgmt_300k` synthetic JavaScript corpus and produces a complete, **user-friendly** documentation set describing its functional flows — with dedicated coverage of the **critical path** and the **expected behavior** of the code across every input scenario. The corpus is a ~300,000-line teaching/sizing artifact of 33,105 behaviorally identical `mod_N_M(x)` helpers spread across nine nominal namespaces, with **no wiring** (zero `require`/`import`/`export`). The documentation, aimed at first-time readers and maintainers, uses progressive disclosure (overview → quick start → flows → reference), worked examples, Mermaid diagrams, and inline source citations. It is authored entirely in Markdown and ships alongside the code. No application code was in scope.

### 1.2 Completion Status

```mermaid
%%{init: {"theme":"base","themeVariables":{"pie1":"#5B39F3","pie2":"#FFFFFF","pieStrokeColor":"#B23AF2","pieOuterStrokeColor":"#B23AF2","pieStrokeWidth":"2px","pieTitleTextColor":"#B23AF2","pieSectionTextColor":"#111111","pieLegendTextColor":"#111111"}}}%%
pie showData
    title Completion — 93.1% (hours)
    "Completed Work (AI) — 54h" : 54
    "Remaining Work — 4h" : 4
```

**Legend:** Completed Work = Dark Blue `#5B39F3` · Remaining Work = White `#FFFFFF`

| Metric | Value |
|---|---|
| **Total Hours** | **58 h** |
| **Completed Hours (AI + Manual)** | **54 h** (54 h AI · 0 h manual) |
| **Remaining Hours** | **4 h** |
| **Percent Complete** | **93.1%** |

> Completion is computed on AAP-scoped hours only: `54 / (54 + 4) = 93.1%`. All 27 AAP deliverables are complete and validated; the remaining 4 h is path-to-production human-in-the-loop work.

### 1.3 Key Accomplishments

- ✅ **27/27 AAP §0.5.1 files delivered** (26 CREATE + 1 UPDATE + 0 DELETE); 22 documentation `.md` files (1,501 lines) + project `README.md` (126 lines) + 3 tooling-config files.
- ✅ **All six user requirements satisfied** (R1 scan, R2 functional flows, R3 user-friendly, R4 all scenarios, R5 critical path, R6 expectation).
- ✅ **4 Mermaid diagrams** authored (critical-path flowchart, module-invocation sequence, data-flow, module-isolation) — exceeds the AAP minimum of 3.
- ✅ **176 inline `Source:` citations** across all 22 doc files — every technical claim is traceable to source lines.
- ✅ **10-scenario expected-behavior contract** documented and executed (`5→40`, `1→16`, `0→10`, `-2→-2`, `0.5→3`, `2.5→15`, `10→70`, `"2"→22`, `"abc"→NaN`, `undefined→NaN`).
- ✅ **Documentation body byte-identical to source** (`docs/functional-flows/helper-computation.md` == `src/controllers/file_0.js:L3-L10`).
- ✅ **Full validation toolchain** in place and passing: `docs:lint`, `docs:linkcheck`, `docs:build`, `docs:diagram`.
- ✅ **Honest architecture** documentation: nominal layered taxonomy vs. as-implemented flat, import-free module set; `tests/` documented as static fixtures.

### 1.4 Critical Unresolved Issues

| Issue | Impact | Owner | ETA |
|---|---|---|---|
| _None — no release-blocking issues_ | All 5 validation gates pass; 0 lint errors, 0 dead links, 0 example drift | — | — |

> The Final Validator and this assessment both confirm **zero unresolved release-blocking issues**. The items in §1.6 / §2.2 are standard path-to-production steps, not defects.

### 1.5 Access Issues

| System/Resource | Type of Access | Issue Description | Resolution Status | Owner |
|---|---|---|---|---|
| Git repository | Read/Write | Full access confirmed; 16 agent commits present on branch | ✅ Resolved | — |
| npm registry (docs devDeps) | Read | 4 pinned devDependencies + lockfile installed; `npm ci` reproducible | ✅ Resolved | — |
| Headless Chrome (diagram render) | Local exec | Sandbox flags required on headless Linux; pre-configured via `.puppeteerrc.cjs` | ✅ Resolved | — |

> **No access issues identified** that block build, validation, or merge.

### 1.6 Recommended Next Steps

1. **[High]** Perform an SME/technical review of the 23 documentation files for accuracy against source and user-friendly tone (2.5 h).
2. **[Medium]** Resolve the Node engine advisory — pin Node 22 LTS (`.nvmrc`/CI) or record an accepted exception so `npm run docs:build` runs advisory-free (0.5 h).
3. **[Medium]** Review and merge the PR to the base branch; confirm Markdown/GitHub rendering of docs and diagrams (1 h).
4. **[Low · backlog]** Add a CI job running `npm run docs:build` on pull requests to prevent future doc regressions (out of scope this pass).
5. **[Low · backlog]** Consider a hosted documentation site (Docusaurus/MkDocs) — explicitly deferred by the AAP (out of scope).

---

## 2. Project Hours Breakdown

### 2.1 Completed Work Detail

| Component | Hours | Description |
|---|---:|---|
| Corpus analysis & ground-truth scan (R1) | 4 | Scanned the 300k-line corpus; confirmed 33,105 identical `mod_N_M(x)` bodies, zero imports; established the canonical contract; validated tool versions |
| Project README + documentation index (R3) | 4 | `society_mgmt_300k/README.md` (overview + quick start) and `docs/README.md` (TOC linking every section) |
| Getting-started guides (R3) | 4 | `getting-started/overview.md` (nominal vs actual) and `getting-started/invoking-a-helper.md` (setup-free quick start) |
| Functional-flow docs + 2 diagrams (R2, R5) | 11 | `critical-path.md` (flowchart of `r % 2 === 0`), `helper-computation.md` (exemplar, step-by-step), `module-invocation-sequence.md` (sequence diagram), `functional-flows/README.md` |
| Reference docs (R6) | 6 | `reference/function-contract.md` (signature/param/return + executed scenario table) and `reference/module-index.md` (all 28 modules mapped) |
| Namespace reference pages | 6 | 9 pages under `reference/namespaces/` with honest "no HTTP/schema/persistence/config" notes and links to the canonical contract |
| Architecture docs + 2 diagrams | 5 | `architecture/overview.md` (module-isolation graph, dead-end `store`) and `architecture/data-flow.md` (single in-process flow) |
| Scenarios + limitations docs (R4) | 5 | `scenarios/expected-behavior.md` (full input envelope) and `limitations-and-caveats.md` (no wiring/framework/persistence) |
| Documentation tooling & config | 5 | `package.json` (docs scripts), `.markdownlint.jsonc`, `.markdown-link-check.json`, `.puppeteerrc.cjs`, `.gitignore`, dependency install + `package-lock.json` |
| Root README update (R3) | 1 | Append-only "Documentation" section pointing to project README and `docs/` (title preserved) |
| Validation & QA | 3 | markdownlint, link-check, diagram render pipeline, worked-example execution verification, final checkpoint review |
| **Total Completed** | **54** | |

### 2.2 Remaining Work Detail

| Category | Hours | Priority |
|---|---:|---|
| Human SME/technical review of documentation accuracy & user-friendly quality | 2.5 | High |
| Resolve Node engine advisory (pin Node 22 LTS or document accepted exception) | 0.5 | Medium |
| PR review & merge to base branch; confirm rendering | 1.0 | Medium |
| **Total Remaining** | **4.0** | |

### 2.3 Hours Reconciliation

| Check | Result |
|---|---|
| Section 2.1 total (Completed) | 54 h |
| Section 2.2 total (Remaining) | 4 h |
| Section 2.1 + Section 2.2 | **58 h = Total (§1.2)** ✅ |
| Completion % = 54 / 58 | **93.1%** ✅ |
| Remaining hours identical in §1.2, §2.2, §7 | ✅ |

---

## 3. Test Results

All results below originate from **Blitzy's autonomous validation logs** and were **independently re-executed** during this assessment. For a documentation deliverable, the standard build/test gates map to: dependency resolution, markdown lint ("compilation"), link integrity + worked-example accuracy ("unit tests"), and Mermaid rendering ("runtime").

| Test Category | Framework | Total | Passed | Failed | Coverage % | Notes |
|---|---|---:|---:|---:|---:|---|
| Markdown Lint (style) | markdownlint-cli2 0.23.0 | 23 files | 23 | 0 | 100% | `Summary: 0 error(s)` across 22 docs + project README |
| Link Integrity | markdown-link-check 3.14.2 | 73 links | 73 | 0 | 100% | All internal doc links resolve; exit 0; +2 root-README links verified |
| Worked-Example Accuracy | Node.js execution | 10 | 10 | 0 | 100% | `5→40, 1→16, 0→10, -2→-2, 0.5→3, 2.5→15, 10→70, "2"→22, "abc"→NaN, undefined→NaN` |
| Diagram Render | @mermaid-js/mermaid-cli 11.16.0 | 4 | 4 | 0 | 100% | critical-path rendered to valid 105 KB SVG; 3 others valid Mermaid |
| Source-Identity | byte diff | 1 | 1 | 0 | 100% | Documented body == `src/controllers/file_0.js:L3-L10` |
| **Total** | — | **111** | **111** | **0** | **100%** | Zero failures across all categories |

**Coverage interpretation (AAP §0.7):** because all 33,105 helpers are behaviorally identical, documenting one canonical contract achieves **100% behavioral coverage**; namespace pages + module index provide **100% navigational coverage** (9/9 namespaces, 28/28 modules indexed).

---

## 4. Runtime Validation & UI Verification

This is a documentation deliverable with **no application UI or runtime service**; "runtime" validation therefore covers the documentation toolchain and the executable behavior the docs describe.

- ✅ **Dependency resolution** — `npm ls --depth=0` exits 0 with a consistent tree; all 4 devDependencies at exact AAP-pinned versions.
- ✅ **Reproducible install** — `npm ci --dry-run` exits 0 against `package-lock.json` (385 packages).
- ✅ **Lint pipeline** — `npm run docs:lint` → 23 files, 0 errors.
- ✅ **Link-check pipeline** — `npm run docs:linkcheck` → exit 0; internal links resolve.
- ✅ **Build pipeline** — `npm run docs:build` (lint && linkcheck) → exit 0 end-to-end.
- ✅ **Diagram render** — `npm run docs:diagram` → valid `docs/assets/critical-path.svg` (105 KB) via mermaid-cli + system Chrome.
- ✅ **Documented behavior** — canonical helper re-executed; all 10 scenarios match the published contract exactly.
- ⚠ **Environment advisory (non-blocking)** — Node v20.20.2 triggers a non-fatal `EBADENGINE` warning (`markdownlint-cli2` prefers Node ≥22); linting still succeeds.
- **UI Verification:** ❌ Not applicable — the corpus has no user interface (AAP §7.1); all visuals are text-based Mermaid diagrams.

---

## 5. Compliance & Quality Review

Cross-mapping of AAP deliverables and directives to their quality benchmarks.

| Deliverable / Directive | Benchmark | Status | Progress |
|---|---|:--:|:--:|
| R1 — Scan corpus, cite source | Inline `Source:` citations throughout | ✅ Pass | 100% (176 citations) |
| R2 — Functional flows | ≥1 flow doc + diagram | ✅ Pass | 100% (3 docs) |
| R3 — User-friendly style | Progressive disclosure + worked examples | ✅ Pass | 100% |
| R4 — All scenarios | Full input envelope documented | ✅ Pass | 100% (10 scenarios) |
| R5 — Critical path | Dedicated doc + flowchart of the single decision | ✅ Pass | 100% |
| R6 — Expectation/contract | Signature/param/return + executed table | ✅ Pass | 100% |
| Min 3 Mermaid diagrams | Flowchart + sequence + architecture | ✅ Pass | 133% (4 delivered) |
| Namespace coverage | 9/9 namespace pages | ✅ Pass | 100% |
| Module index | 28/28 modules mapped | ✅ Pass | 100% |
| Markdown lint clean | 0 errors | ✅ Pass | 100% |
| Link integrity | 0 dead links | ✅ Pass | 100% |
| Zero Placeholder Policy | No TODO/FIXME/stub content | ✅ Pass | 100% (0 found) |
| Minimal-change discipline | Only root README modified (append-only) | ✅ Pass | 100% |
| Pinned dependency versions | Exact AAP versions + lockfile | ✅ Pass | 100% |
| User rule `Document code` = "Test" | Placeholder rule, no added constraint | ✅ Pass | N/A |

**Fixes applied during autonomous validation:** none required for content. Prior agents resolved tooling items already committed (diagram output path → AAP-specified `docs/assets/critical-path.svg`; patched system browser for headless render; build-artifact gitignore; single-source-of-truth link consolidation; citation-format normalization; lockfile sync). **Outstanding compliance items:** none.

---

## 6. Risk Assessment

All identified risks are **Low severity**, consistent with a fully-validated documentation deliverable that has no production runtime surface.

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|:--:|:--:|---|:--:|
| Node engine advisory (`EBADENGINE`; markdownlint-cli2 prefers Node ≥22) | Technical | Low | High (occurs) | Pin Node 22 LTS via `.nvmrc`/CI, or accept non-fatal advisory (lint still passes) | Open (minor) |
| Documentation drift if the source corpus changes | Technical | Low | Low (corpus is frozen/synthetic) | Exact source-line citations + re-run worked-example verification on any source change | Mitigated |
| Diagram render depends on headless Chrome + sandbox flags | Technical | Low | Low | `.puppeteerrc.cjs` + `.puppeteer.json` (`--no-sandbox --disable-dev-shm-usage`); SVG pre-committed | Mitigated |
| devDependency supply chain (385 transitive packages) | Security | Low | Low | Exact pinned versions + `package-lock.json` + reproducible `npm ci`; docs-only, no runtime surface | Mitigated |
| No application attack surface (no runtime/network/persistence/auth) | Security | Low | N/A | Documented as intentional; nothing to harden | N/A (informational) |
| No CI pipeline for `docs:build` — future edits could regress | Operational | Low-Med | Medium | Add CI job running `npm run docs:build` on PRs (recommended backlog) | Open (recommendation) |
| No hosted documentation site — Markdown-only discoverability | Operational | Low | N/A | Optional Docusaurus/MkDocs deferred per AAP §0.8.2 | Deferred (out of scope) |
| Corpus has zero inter-module dependencies | Integration | Low | N/A | De-risking factor; documented explicitly as "no integration exists by design" | Documented |
| `npx mermaid-cli` may fetch on demand in offline environments | Integration | Low | Low | Dependency already in `devDependencies` + lockfile; SVG committed | Mitigated |

---

## 7. Visual Project Status

### 7.1 Project Hours Breakdown

```mermaid
%%{init: {"theme":"base","themeVariables":{"pie1":"#5B39F3","pie2":"#FFFFFF","pieStrokeColor":"#B23AF2","pieOuterStrokeColor":"#B23AF2","pieStrokeWidth":"2px","pieTitleTextColor":"#B23AF2","pieSectionTextColor":"#111111","pieLegendTextColor":"#111111"}}}%%
pie showData
    title Project Hours — Completed vs Remaining
    "Completed Work" : 54
    "Remaining Work" : 4
```

**Legend:** Completed Work = Dark Blue `#5B39F3` (54 h) · Remaining Work = White `#FFFFFF` (4 h). **Remaining = 4 h**, identical to §1.2 and the §2.2 total.

### 7.2 Remaining Work by Priority

```mermaid
%%{init: {"theme":"base","themeVariables":{"pie1":"#5B39F3","pie2":"#A8FDD9","pie3":"#FFFFFF","pieStrokeColor":"#B23AF2","pieStrokeWidth":"2px","pieTitleTextColor":"#B23AF2","pieSectionTextColor":"#111111","pieLegendTextColor":"#111111"}}}%%
pie showData
    title Remaining 4h by Priority
    "High (SME review)" : 2.5
    "Medium (merge)" : 1.0
    "Medium (engine advisory)" : 0.5
```

### 7.3 Remaining Hours per Category (bar view)

| Category | Hours | Bar |
|---|---:|---|
| SME documentation review (High) | 2.5 | `█████████████████████████` |
| PR review & merge (Medium) | 1.0 | `██████████` |
| Node engine advisory (Medium) | 0.5 | `█████` |
| **Total** | **4.0** | |

---

## 8. Summary & Recommendations

**Achievements.** The project is **93.1% complete** (54 h of 58 h). Every AAP-scoped deliverable — all 27 files (§0.5.1) and all six user requirements (R1–R6) — is complete and independently validated. The documentation scans the corpus, documents its single genuine functional flow, calls out the **critical path** (the lone `r % 2 === 0` decision), and specifies the **expected behavior** across the full input envelope with executed worked examples. Four Mermaid diagrams, 176 source citations, honest nominal-vs-actual architecture framing, and a clean lint/link/render toolchain round out a production-grade deliverable.

**Remaining gaps.** The outstanding **4 h** is entirely path-to-production and human-in-the-loop: a subject-matter review of documentation accuracy and tone, resolution of a non-fatal Node engine advisory, and PR review & merge. No defects, dead links, example drift, or dependency conflicts remain.

**Critical path to production.** (1) SME review → (2) resolve/accept the engine advisory → (3) merge. Estimated wall-clock: well under one working day.

**Success metrics.** 0 lint errors · 0 dead links · 10/10 worked examples exact · 4/4 diagrams render · 27/27 files present · 100% behavioral + navigational coverage.

**Production-readiness assessment.** ✅ **Ready to merge pending human review.** The deliverable meets the AAP's definition of done (clean `markdownlint-cli2`, passing `markdown-link-check`, and worked-example outputs matching execution of the canonical body). Per policy, completion is capped below 100% to reflect the genuine human review/merge step that must precede production.

| Metric | Value |
|---|---|
| Completion | 93.1% |
| Completed / Total hours | 54 / 58 |
| Release-blocking issues | 0 |
| Validation gates passed | 5 / 5 |
| Autonomous checks passed | 111 / 111 |

---

## 9. Development Guide

> All commands below were executed during this assessment and exit 0 in the target environment (Node v20.20.2, npm 11.1.0). Run them from the `society_mgmt_300k/` directory.

### 9.1 System Prerequisites

- **Node.js** ≥ 18 LTS (**Node 22.x recommended** to avoid the non-fatal `markdownlint-cli2` engine advisory).
- **npm** ≥ 9 (tested with 11.1.0).
- **Google Chrome / Chromium** — required **only** for `docs:diagram` (Mermaid → SVG rendering via puppeteer).
- **git**; a Markdown viewer (VS Code, GitHub) to read the docs.
- **No** database, server, message queue, or environment variables — this is a documentation-only project.

### 9.2 Environment Setup

```bash
# From the repository root
cd society_mgmt_300k

# No .env file or environment variables are required.
# Headless-Linux diagram rendering flags are pre-configured in:
#   .puppeteerrc.cjs        (puppeteer launch args: --no-sandbox --disable-dev-shm-usage)
#   docs/assets/.puppeteer.json  (generated on demand by docs:diagram)
```

### 9.3 Dependency Installation

```bash
# Preferred: reproducible install from the committed lockfile (385 packages)
npm ci

# Alternative:
npm install

# Verify the toolchain (expect exit 0 and 4 pinned devDependencies)
npm ls --depth=0
# ├── @mermaid-js/mermaid-cli@11.16.0
# ├── markdown-link-check@3.14.2
# ├── markdownlint-cli2@0.23.0
# └── mermaid@11.16.0
```

### 9.4 Build / Validation Pipeline (no server to start)

```bash
# Lint all markdown (expect "Summary: 0 error(s)" across 23 files)
npm run docs:lint

# Check internal link integrity (expect exit 0)
npm run docs:linkcheck

# Run the full docs build (lint && linkcheck)
npm run docs:build

# Render the critical-path Mermaid diagram to docs/assets/critical-path.svg
npm run docs:diagram
```

### 9.5 Verification Steps

| Command | Expected result |
|---|---|
| `npm ls --depth=0` | Exit 0; 4 devDependencies at pinned versions |
| `npm run docs:lint` | `markdownlint-cli2 v0.23.0` … `Summary: 0 error(s)` |
| `npm run docs:linkcheck` | Exit 0; all links report `[✓]` |
| `npm run docs:build` | Exit 0 end-to-end |
| `npm run docs:diagram` | `✅ ./critical-path-1.svg`; valid ~105 KB `docs/assets/critical-path.svg` |

To read the docs, start at `society_mgmt_300k/README.md`, then the index at `society_mgmt_300k/docs/README.md`.

### 9.6 Example Usage — Invoking a Helper

The documented behavior can be reproduced directly (helpers are top-level symbols; the files have no exports):

```bash
node -e 'function mod_0_0(x){let r=0;r+=x*1;r+=x*2;r+=x*3;if(r%2===0){r+=10}return r} console.log(mod_0_0(5))'
# -> 40
```

| Input `x` | Output | Rule |
|---|---|---|
| `5` | `40` | `6·5=30` (even) `+10` |
| `1` | `16` | `6·1=6` (even) `+10` |
| `0` | `10` | `6·0=0` (even) `+10` |
| `-2` | `-2` | `6·-2=-12` (even) `+10` |
| `0.5` | `3` | `6·0.5=3` (odd) → unchanged |
| `2.5` | `15` | `6·2.5=15` (odd) → unchanged |
| `10` | `70` | `6·10=60` (even) `+10` |
| `"2"` | `22` | string coercion: `"0"+2+4+6`… → numeric `12`+10 |
| `"abc"` | `NaN` | non-numeric → `NaN` |
| `undefined` | `NaN` | non-numeric → `NaN` |

### 9.7 Troubleshooting

- **`EBADENGINE` warning on install/lint (Node < 22):** non-fatal; linting still succeeds. To silence, use Node 22 LTS: `nvm install 22 && nvm use 22`.
- **`docs:diagram` fails on headless Linux (Chrome sandbox):** ensure the puppeteer args are present — `.puppeteerrc.cjs` and the generated `docs/assets/.puppeteer.json` supply `--no-sandbox --disable-dev-shm-usage` (already configured).
- **`docs:diagram` cannot find a browser:** install Chrome/Chromium; mermaid-cli launches it through puppeteer.
- **Link-check flags an external URL:** internal links are authoritative; external-link handling is configured in `.markdown-link-check.json`.
- **Regenerated SVG shows as untracked/ignored:** expected — `docs/assets/` and `node_modules/` are gitignored by design; the SVG is a regenerated build artifact.

---

## 10. Appendices

### Appendix A — Command Reference

| Command | Purpose |
|---|---|
| `npm ci` | Reproducible install from `package-lock.json` |
| `npm ls --depth=0` | Verify pinned devDependencies |
| `npm run docs:lint` | markdownlint over `docs/**/*.md` + `README.md` |
| `npm run docs:linkcheck` | Validate internal doc links |
| `npm run docs:build` | `docs:lint && docs:linkcheck` |
| `npm run docs:diagram` | Render `docs/assets/critical-path.svg` via mermaid-cli |
| `node -e '…mod_0_0(5)'` | Execute the canonical helper (→ 40) |

### Appendix B — Port Reference

**Not applicable.** The project runs no server or network service; there are no ports to configure or expose.

### Appendix C — Key File Locations

| Path | Role |
|---|---|
| `society_mgmt_300k/README.md` | Project overview + quick start |
| `society_mgmt_300k/docs/README.md` | Documentation index (table of contents) |
| `society_mgmt_300k/docs/functional-flows/helper-computation.md` | Canonical contract (single source of truth / structural exemplar) |
| `society_mgmt_300k/docs/functional-flows/critical-path.md` | Critical-path narrative + Mermaid flowchart |
| `society_mgmt_300k/docs/reference/function-contract.md` | Signature + executed scenario table |
| `society_mgmt_300k/docs/reference/module-index.md` | All 28 modules mapped by namespace |
| `society_mgmt_300k/docs/reference/namespaces/*.md` | 9 namespace reference pages |
| `society_mgmt_300k/docs/architecture/{overview,data-flow}.md` | Architecture + data-flow docs |
| `society_mgmt_300k/docs/scenarios/expected-behavior.md` | Full input-scenario envelope |
| `society_mgmt_300k/docs/limitations-and-caveats.md` | Limitations (no wiring/framework/persistence) |
| `society_mgmt_300k/src/controllers/file_0.js` | REFERENCE — canonical `mod_N_M(x)` body (read-only) |
| `society_mgmt_300k/package.json` · `.markdownlint.jsonc` · `.markdown-link-check.json` · `.puppeteerrc.cjs` · `.gitignore` | Documentation tooling & config |
| `README.md` (repo root) | UPDATED (append-only "Documentation" section) |

### Appendix D — Technology Versions

| Component | Version |
|---|---|
| Node.js (tested) | v20.20.2 (Node 22.x recommended) |
| npm | 11.1.0 |
| @mermaid-js/mermaid-cli | 11.16.0 |
| mermaid | 11.16.0 |
| markdownlint-cli2 | 0.23.0 (markdownlint 0.41.0) |
| markdown-link-check | 3.14.2 |
| Corpus language | JavaScript (ES2015 baseline) |

### Appendix E — Environment Variable Reference

**None required.** The documentation project uses no environment variables, `.env` files, secrets, or credentials.

### Appendix F — Developer Tools Guide

| Tool | Role | Notes |
|---|---|---|
| markdownlint-cli2 | Enforce consistent Markdown style | Config in `.markdownlint.jsonc`; prefers Node ≥ 22 (advisory only) |
| markdown-link-check | Validate documentation links | Config in `.markdown-link-check.json` |
| @mermaid-js/mermaid-cli | Render Mermaid diagrams to SVG | Uses puppeteer + system Chrome |
| puppeteer config | Headless Chrome launch args | `.puppeteerrc.cjs` / generated `docs/assets/.puppeteer.json` (`--no-sandbox`) |

### Appendix G — Glossary

| Term | Meaning |
|---|---|
| **Corpus** | The full `society_mgmt_300k` source + test set (~300,000 lines) |
| **Module** | A single `file_N.js` carrying a `// mod_N` banner and many helpers |
| **Helper** | A top-level `mod_N_M(x)` function; the unit of documented behavior |
| **Canonical contract** | The one behavior shared by all 33,105 helpers: `r = 6x`, then `+10` if `r` is even |
| **Critical path** | The single decision point `r % 2 === 0` — the corpus's only conditional |
| **Namespace** | A nominal `src/` folder (controllers, services, …) implying MVC layering that is organizational only |
| **Nominal vs as-implemented** | Folder names suggest a layered app; the runtime is a flat, import-free set of isolated modules |