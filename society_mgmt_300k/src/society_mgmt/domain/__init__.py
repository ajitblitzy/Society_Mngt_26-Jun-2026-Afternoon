"""society_mgmt.domain — navigational domain-layer subpackage.

Preserves the nominal nine-layer taxonomy of the legacy corpus. All logic
delegates to the single canonical :func:`society_mgmt.core.compute`;
no business logic is re-implemented in this layer. ``compute`` is re-exported
here for ergonomic access (``from society_mgmt.domain import compute``).
"""

from society_mgmt.core import compute

__all__ = ["compute"]
