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
    assert result == expected            # value-equality: JS 3 == Python 3.0 (Deviation 1)
    assert isinstance(result, float)     # Python returns float for non-integer input


@pytest.mark.parametrize("x,expected", LARGE_INT_CASES)
def test_compute_large_int_exact(x, expected):
    assert compute(x) == expected        # Deviation 2: Python int stays exact (e.g. 9007199254740993 -> 54043195528445968)


def test_alias_delegates_to_compute():
    # Confirms the ported layer symbols delegate to the single canonical compute.
    from society_mgmt.services.file_1 import mod_1_0
    assert mod_1_0(2) == compute(2)
