"""Integration characterization tests migrated from
``tests/integration/file_10.js``.

The legacy fixture declared 1,200 byte-identical ``mod_10_*`` helpers with NO
assertions. This module pins the legacy ``x -> f(x)`` mapping via
:func:`society_mgmt.core.compute` and additionally verifies that the ported
layer aliases across subpackages all delegate to that one function.
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
    assert isinstance(result, float)


@pytest.mark.parametrize("x,expected", LARGE_INT_CASES)
def test_compute_large_int_exact(x, expected):
    assert compute(x) == expected        # Deviation 2: Python int stays exact


def test_layer_aliases_delegate_to_single_compute():
    # The layer alias, the package re-export, and the core function
    # must all resolve to ONE canonical function object.
    from society_mgmt.services.file_1 import mod_1_0
    from society_mgmt import compute as pkg_compute

    # Object identity across all three import paths (single source).
    assert mod_1_0 is compute is pkg_compute
    # Return-value equality retained as an explicit behavioral check.
    assert mod_1_0(2) == compute(2) == pkg_compute(2)
