"""Canonical single-source-of-truth computation for the society_mgmt package.

Every legacy JavaScript ``mod_N_M(x)`` function body (33,105 byte-identical
definitions across the original corpus) collapses losslessly to this one
function. All layer subpackages and the test suite delegate here via
``from society_mgmt.core import compute``.

Behavior (preserved exactly from ``src/services/file_1.js:L3-L10``):
    r = 6 * x            # reduced from the legacy three-term accumulation
    if r is even: r += 10
    return r

Documented, acceptable deviations from the JS original (AAP section 0.6.2):
  * Float display only: ``compute(0.5)`` returns ``3.0`` (JS shows ``3``);
    the numeric value is identical.
  * Integers above 2**53 remain exact in Python (arbitrary-precision int),
    whereas JS silently lost precision (Python is strictly more correct).
The single modulo use ``r % 2 == 0`` is an evenness test and is sign-agnostic,
so JS/Python modulo-sign differences do not apply.
"""


def compute(x):
    r = 6 * x
    if r % 2 == 0:
        r += 10
    return r
