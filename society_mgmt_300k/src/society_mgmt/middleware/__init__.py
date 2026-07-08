"""society_mgmt.middleware — navigational middleware layer subpackage.

Preserves the nominal nine-layer taxonomy of the legacy JavaScript corpus.
"middleware" is a structural label only; no request pipeline, I/O, or state
exists here. All logic delegates to the single canonical function
:func:`society_mgmt.core.compute`; no logic is re-implemented in this layer.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
