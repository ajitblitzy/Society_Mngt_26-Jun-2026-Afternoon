"""society_mgmt.services — navigational services-layer subpackage.

Migrated in-place from the legacy JavaScript ``src/services/*.js`` modules
(``file_1.js``, ``file_12.js``, ``file_23.js``). Every legacy ``mod_N_M(x)``
helper collapses to a one-line alias of the single canonical
:func:`society_mgmt.core.compute`; no logic is re-implemented in this layer.

The layer name is a navigational label only — the original corpus had no
cross-layer coupling. ``compute`` is re-exported here for ergonomic access
(``from society_mgmt.services import compute``).
"""

from society_mgmt.core import compute

__all__ = ["compute"]
