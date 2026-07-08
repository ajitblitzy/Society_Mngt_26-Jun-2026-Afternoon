"""society_mgmt.utils — navigational *utils* layer subpackage.

Preserves the nominal nine-layer taxonomy of the legacy JavaScript corpus.
All logic delegates to the single canonical :func:`society_mgmt.core.compute`;
this subpackage re-implements nothing. ``compute`` is re-exported here for
ergonomic access, so callers may write ``from society_mgmt.utils import compute``.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
