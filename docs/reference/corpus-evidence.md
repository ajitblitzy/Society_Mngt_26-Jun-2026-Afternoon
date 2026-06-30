# Corpus Evidence (reproducible scans)

← Back to the [documentation hub](../README.md)

## Overview

This page is the **authoritative evidence base** for every *corpus-wide* claim
made elsewhere in this documentation set — the file, line, and function counts;
the byte-identical function body; the inert `store` placeholder; the absence of a
module system; and the per-layer composition. A single representative source file
(such as `society_mgmt_300k/src/controllers/file_0.js`) can demonstrate the
*motif* of one function, but it cannot by itself prove a statement about all
**33,105** functions or all **29** files. The reproducible scans below close that
gap: each evidence item records the **exact command** and its **exact output**,
so any reader can re-run it against the source branch and confirm the result.

Other pages cite this file as
`Source: docs/reference/corpus-evidence.md:Lx-Ly` for corpus-wide facts, while
continuing to cite `society_mgmt_300k/src/controllers/file_0.js` for the
single-function motif. The evidence items are stable, numbered anchors (E1–E12).

How to reproduce: run each command from the repository root on the source
branch. Counts reflect the verified corpus state (29 files, 33,105 functions,
300,000 lines); any future change to the corpus requires re-running these scans.

## Evidence items

### E1 — File count (29 `.js` files)

```text
$ find society_mgmt_300k -name '*.js' -type f | wc -l
29
```

**Proves** — the source corpus comprises exactly **29** `.js` files.

### E2 — Total line count (300,000 lines)

```text
$ find society_mgmt_300k -name '*.js' -type f -print0 | xargs -0 wc -l | tail -n 1
 300000 total
```

**Proves** — the 29 `.js` files contain exactly **300,000** lines in aggregate —
the deterministic F-005 sizing target, hit precisely.

### E3 — Function declaration count (33,105 functions)

```text
$ grep -rhoE 'function +mod_[0-9]+_[0-9]+' society_mgmt_300k --include='*.js' | wc -l
33105
```

**Proves** — the corpus declares exactly **33,105** `mod_<fileId>_<k>` functions.

### E4 — Function-name uniqueness (collision-free)

```text
$ grep -rhoE 'function +mod_[0-9]+_[0-9]+' society_mgmt_300k --include='*.js' | sort -u | wc -l
33105
```

**Proves** — the number of **distinct** function names (33,105) equals the total
number of declarations (E3), so every `mod_<fileId>_<k>` name is unique: the
namespace is **collision-free**.

### E5 — Body uniformity (byte-identical apart from names)

The scan normalises whitespace, strips each function's name, and counts the
number of **distinct** function-body signatures across the whole corpus.

```text
$ python3 - <<'PY'
import re, glob, collections
sigs = collections.Counter()
total = 0
for path in glob.glob('society_mgmt_300k/**/*.js', recursive=True):
    txt = open(path).read()
    for m in re.finditer(r'function\s+mod_\d+_\d+\s*\(x\)\s*\{(.*?return r;\s*)\}', txt, re.S):
        sigs[re.sub(r'\s+', '', m.group(1))] += 1
        total += 1
print('functions matched:', total)
print('distinct bodies   :', len(sigs))
for body, count in sigs.most_common():
    print('count=%d body=%r' % (count, body))
PY
functions matched: 33105
distinct bodies   : 1
count=33105 body='letr=0;r+=x*1;r+=x*2;r+=x*3;if(r%2===0){r+=10}returnr;'
```

**Proves** — all **33,105** functions share a single distinct body
(`let r=0; r+=x*1; r+=x*2; r+=x*3; if(r%2===0){r+=10} return r;`); they are
**byte-identical apart from their `mod_<fileId>_<k>` names**, which is why one
documented archetype faithfully and exhaustively covers every function.

### E6 — `store` placeholder (28 declarations, never read or written)

```text
$ grep -rlE 'const store *= *\[\]' society_mgmt_300k --include='*.js' | wc -l
28
$ grep -rnE 'store' society_mgmt_300k --include='*.js' | grep -vcE 'const store = \[\];$'
0
```

**Proves** — `const store = [];` is declared in **28** of the 29 files (every
function-bearing file; the comment-only `filler.js` is the sole exception). The
second command finds **0** occurrences of `store` on any line other than the
exact declaration — no `store.push`, no `store[...]`, no reassignment — so the
array is **never read and never written** (F-004, an inert placeholder).

### E7 — Source-corpus keyword sweep over `society_mgmt_300k/**/*.js` (all zero)

This sweep is scoped **precisely** to the JavaScript source corpus
(`society_mgmt_300k/**/*.js`) — not the whole repository, which also contains
documentation and license prose (see E8).

```text
$ for kw in require import export module.exports eval fetch Promise async await \
            try catch throw console password token jwt auth crypto encrypt 'use strict'; do
    printf '%-14s = %s\n' "$kw" "$(grep -rwoE "$kw" society_mgmt_300k --include='*.js' | wc -l)"
  done
require        = 0
import         = 0
export         = 0
module.exports = 0
eval           = 0
fetch          = 0
Promise        = 0
async          = 0
await          = 0
try            = 0
catch          = 0
throw          = 0
console        = 0
password       = 0
token          = 0
jwt            = 0
auth           = 0
crypto         = 0
encrypt        = 0
use strict     = 0
```

**Proves** — within the JavaScript source corpus there is **no module system**
(`require`/`import`/`export`/`module.exports` = 0, so symbols are file-local and
not importable and there are no inter-layer edges), **no dynamic code execution**
(`eval` = 0), **no I/O or async** (`fetch`/`Promise`/`async`/`await` = 0), **no
exception channels** (`try`/`catch`/`throw` = 0), **no logging** (`console` = 0),
**no secrets/auth** (`password`/`token`/`jwt`/`auth` = 0), and **no cryptography**
(`crypto`/`encrypt` = 0).

### E8 — Whole-tree contrast (why the sweep scope matters)

The same keywords are **not** absent from the whole repository: documentation and
license files legitimately mention them. The zero counts in E7 therefore hold
**only** for the JavaScript source corpus, which is why security wording must say
"source-corpus sweep over `society_mgmt_300k/**/*.js`" rather than "whole-tree".

```text
$ for kw in auth token crypto import; do
    w=$(grep -rwoE "$kw" . --include='*' --exclude-dir=.git | wc -l)
    j=$(grep -rwoE "$kw" society_mgmt_300k --include='*.js' | wc -l)
    printf '%-7s whole-tree(excl .git)=%s  society_mgmt_300k/**/*.js=%s\n' "$kw" "$w" "$j"
  done
auth    whole-tree(excl .git)=15  society_mgmt_300k/**/*.js=0
token   whole-tree(excl .git)=34  society_mgmt_300k/**/*.js=0
crypto  whole-tree(excl .git)=1   society_mgmt_300k/**/*.js=0
import  whole-tree(excl .git)=54  society_mgmt_300k/**/*.js=0
```

**Proves** — a repository-wide sweep (excluding `.git`) finds many occurrences of
these terms in non-source files (this documentation and the license texts), while
the source corpus has zero. The verified-absence posture is accurate **for the JS
source corpus** and must be scoped as such.

### E9 — Per-layer composition

```text
$ for d in config middleware models controllers routes domain services repositories utils; do
    f=$(find society_mgmt_300k/src/$d -name '*.js' | wc -l)
    n=$(grep -rhoE 'function +mod_[0-9]+_[0-9]+' society_mgmt_300k/src/$d --include='*.js' | wc -l)
    l=$(find society_mgmt_300k/src/$d -name '*.js' -exec cat {} + | wc -l)
    printf 'src/%-13s files=%s fns=%s lines=%s\n' "$d" "$f" "$n" "$l"
  done
  for d in unit integration; do
    f=$(find society_mgmt_300k/tests/$d -name '*.js' | wc -l)
    n=$(grep -rhoE 'function +mod_[0-9]+_[0-9]+' society_mgmt_300k/tests/$d --include='*.js' | wc -l)
    l=$(find society_mgmt_300k/tests/$d -name '*.js' -exec cat {} + | wc -l)
    printf 'tests/%-11s files=%s fns=%s lines=%s\n' "$d" "$f" "$n" "$l"
  done
```

The command above yields the following roll-up:

| Layer | Files | Functions | Lines |
| --- | --- | --- | --- |
| `src/config` | 2 | 2,400 | 21,604 |
| `src/middleware` | 3 | 3,105 | 27,951 |
| `src/models` | 3 | 3,600 | 32,406 |
| `src/controllers` | 3 | 3,600 | 32,406 |
| `src/routes` | 3 | 3,600 | 32,406 |
| `src/domain` | 2 | 2,400 | 21,604 |
| `src/services` | 3 | 3,600 | 32,406 |
| `src/repositories` | 2 | 2,400 | 21,604 |
| `src/utils` | 4 | 3,600 | 34,405 |
| `tests/unit` | 2 | 2,400 | 21,604 |
| `tests/integration` | 2 | 2,400 | 21,604 |
| **Totals** | **29** | **33,105** | **300,000** |

**Proves** — the per-layer file, function, and line counts sum to exactly **29**
files, **33,105** functions, and **300,000** lines, matching E1–E3. `src/utils`
holds 4 files (one is the comment-only `filler.js`) yet still 3,600 functions;
`src/middleware` holds 3,105 functions because of the `file_27.js` short variant
(E10).

### E10 — File shapes (standard, short variant, filler)

```text
$ for f in $(find society_mgmt_300k -name '*.js'); do
    printf '%s %s %s\n' "$(grep -coE 'function +mod_' "$f")" "$(wc -l < "$f")" "$f"
  done | sort -n | uniq -c -w5
     27 1200 10802 ...   # 27 standard files: 1,200 functions / 10,802 lines each
      1  705  6347 society_mgmt_300k/src/middleware/file_27.js
      1    0  1999 society_mgmt_300k/src/utils/filler.js
```

**Proves** — the corpus is built from exactly three file shapes: **27 standard
files** (1,200 functions / 10,802 lines each), the single **short variant**
`file_27.js` (705 / 6,347), and the single **comment-only** `filler.js`
(0 / 1,999). The arithmetic closes exactly: functions 27 × 1,200 + 705 + 0 =
**33,105**; lines 27 × 10,802 + 6,347 + 1,999 = **300,000**.

### E11 — Dependency-manifest absence (zero dependencies)

```text
$ find . -path ./.git -prune -o -name 'package.json' -print | wc -l
0
$ find . -path ./.git -prune -o \( -name 'package-lock.json' -o -name 'yarn.lock' \
        -o -name 'pnpm-lock.yaml' \) -print | wc -l
0
```

**Proves** — the repository declares **zero dependencies**: there is no
`package.json` and no lockfile of any kind anywhere (excluding `.git`), so there
is no third-party supply-chain surface to manage.

### E12 — Header-comment scan (`// mod_<n> - society module`)

```text
$ grep -rhcE '^// mod_[0-9]+ - society module' society_mgmt_300k --include='*.js' \
    | awk '{s+=$1} END{print s}'
28
$ grep -cE 'society' society_mgmt_300k/src/utils/filler.js
0
```

**Proves** — the `// mod_<n> - society module` header appears in **28** files
(every function-bearing file), and the word "society" appears **0** times in the
comment-only `filler.js`. "Society management" is therefore only a **nominal
label** carried by behavior-bearing module headers (and the repository name), not
implemented domain functionality.

## How these items are cited

- Corpus-wide **counts** (files, lines, functions) → E1, E2, E3, E9, E10.
- **Uniqueness / byte-identity** of the family → E4, E5.
- The inert **`store`** placeholder → E6.
- **No module system / no I/O / no secrets / no crypto** (security and
  no-inter-layer-edges claims) → E7, with scope justified by E8.
- **Zero dependencies** (supply chain) → E11.
- The **nominal "society" label** → E12.

Single-function behavior — the `6x + 10` body, the dead always-true branch, the
header comment, and the inert `store` line — remains cited to the representative
file `society_mgmt_300k/src/controllers/file_0.js`, since one file is sufficient
and authoritative evidence for the motif of one function.

## See also

- [File inventory](file-inventory.md) — the per-file table that this evidence
  base substantiates.
- [Corpus composition](../functionality/corpus-composition.md) — the per-layer
  roll-up and the deterministic 300,000-line arithmetic.
- [Glossary](glossary.md) — definitions of the corpus terminology.

---

← Back to the [documentation hub](../README.md)
