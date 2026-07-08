"""Characterization tests migrated from tests/unit/file_9.js.

The legacy fixture declared 1,200 byte-identical ``mod_9_*`` helpers with NO
assertions. Their shared behavior (``r = 6*x; if r % 2 == 0: r += 10``) now
lives once in :func:`society_mgmt.core.compute`; this module pins the legacy
outputs and asserts equivalence (golden-master / characterization testing).
"""

import pytest

from society_mgmt.core import compute
from tests.conftest import GOLDEN_CASES, FLOAT_CASES, LARGE_INT_CASES


@pytest.mark.parametrize("x,expected", GOLDEN_CASES)
def test_compute_matches_golden(x, expected):
    assert compute(x) == expected


@pytest.mark.parametrize("x,expected", FLOAT_CASES)
def test_compute_float_value_equality_and_type(x, expected):
    result = compute(x)
    # value-equality: JS 3 == Python 3.0 (Deviation 1).
    assert result == expected
    # Python returns a float for non-integer input.
    assert isinstance(result, float)


@pytest.mark.parametrize("x,expected", LARGE_INT_CASES)
def test_compute_large_int_exact(x, expected):
    # Deviation 2: Python int stays exact
    # (e.g. 9007199254740993 -> 54043195528445968).
    assert compute(x) == expected


def test_alias_delegates_to_compute():
    # The ported layer symbol, the package re-export, and the core
    # function must all be the SAME object (single source of truth,
    # not independent copies).
    from society_mgmt.services.file_1 import mod_1_0
    from society_mgmt import compute as pkg_compute

    # Object identity is the migration's acceptance criterion.
    assert mod_1_0 is compute is pkg_compute
    # Return-value equality retained as an explicit behavioral check.
    assert mod_1_0(2) == compute(2) == pkg_compute(2)
