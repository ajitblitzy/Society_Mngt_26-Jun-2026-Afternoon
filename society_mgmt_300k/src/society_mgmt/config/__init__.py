"""society_mgmt.config — navigational config layer subpackage.

Part of the nine-layer taxonomy preserved for navigation only (AAP section 0.7).
All logic converges on the single canonical function
:func:`society_mgmt.core.compute`; the modules in this subpackage
(``file_6``, ``file_17``) bind their legacy ``mod_N_M`` symbol names as thin
one-line aliases to ``compute`` and re-implement no logic.

``compute`` is re-exported here for ergonomic access
(``from society_mgmt.config import compute``).
"""

from society_mgmt.core import compute

__all__ = ["compute"]
