"""society_mgmt.repositories — repositories layer subpackage (navigational only).

Part of the nominal nine-layer taxonomy preserved from the legacy JavaScript
corpus. The label is structural only: there is NO database, persistence, or I/O
of any kind. Every ``mod_18_*`` and ``mod_7_*`` symbol in this subpackage's
modules is a one-line alias of the single canonical
:func:`society_mgmt.core.compute`; no logic is re-implemented here.

``compute`` is re-exported for ergonomic access, so callers may write
``from society_mgmt.repositories import compute``.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
