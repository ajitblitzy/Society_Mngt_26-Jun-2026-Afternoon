"""Shared pytest fixtures and golden-master characterization data for the
society_mgmt test suite.

These ``(input, expected)`` pairs pin the legacy JavaScript ``x -> f(x)``
mapping. Every legacy ``mod_N_M`` body was::

    r = x*1 + x*2 + x*3   # == 6*x
    if r % 2 == 0:
        r += 10
    return r

and the migrated :func:`society_mgmt.core.compute` reproduces it exactly. The
expected values here are the *legacy-observed outputs* captured during the
JavaScript -> Python migration analysis (see AAP section 0.6.2); they are
hard-coded literals on purpose so the characterization tests verify ``compute``
against the pinned legacy behavior rather than against itself.

Domain coverage (AAP section 0.6.2):
  * zero and positive/negative integers  -> exact byte-for-byte equality;
  * floats (0.5 / 2.5 / -2.5)            -> value-equality (JS displayed
    ``3`` / ``15`` / ``-15``; Python returns ``3.0`` / ``15.0`` / ``-15.0``);
  * the 2**53 boundary and large ints    -> Python's arbitrary-precision int
    stays exact where JS silently lost precision.
"""

import pytest

# Integer inputs: exact byte-for-byte equality with the legacy JS results.
INTEGER_CASES = [
    (0, 10),
    (1, 16),
    (2, 22),
    (5, 40),
    (7, 52),
    (100, 610),
    (-3, -8),
    (-100, -590),
]

# Float inputs: value-equality. JS displayed 3 / 15 / -15; Python returns
# 3.0 / 15.0 / -15.0 (identical numeric value, float type).
FLOAT_CASES = [
    (0.5, 3.0),
    (2.5, 15.0),
    (-2.5, -15.0),
]

# Large integers at/after the 2**53 boundary: Python stays exact (JS diverged).
LARGE_INT_CASES = [
    (9007199254740993, 54043195528445968),   # 2**53 + 1
    (12345678901234567, 74074073407407412),
]

# Full golden-master set consumed by the characterization tests.
GOLDEN_CASES = INTEGER_CASES + FLOAT_CASES + LARGE_INT_CASES


@pytest.fixture
def golden_cases():
    """Return the full list of ``(input, expected)`` golden-master pairs."""
    return list(GOLDEN_CASES)


@pytest.fixture
def integer_cases():
    """Return the integer-only ``(input, expected)`` golden-master pairs."""
    return list(INTEGER_CASES)


@pytest.fixture
def float_cases():
    """Return the float ``(input, expected)`` pairs (value-equality)."""
    return list(FLOAT_CASES)


@pytest.fixture
def large_int_cases():
    """Return the large-integer ``(input, expected)`` pairs (Python exact)."""
    return list(LARGE_INT_CASES)
