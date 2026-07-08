"""society_mgmt.controllers — navigational controllers-layer subpackage.

Structural label only: there is no HTTP/route/UI wiring in this code — the
legacy corpus was a bank of pure numeric helpers. Every ported module in this
subpackage (``file_0``, ``file_11``, ``file_22``) binds its legacy ``mod_*``
names as one-line aliases of the single canonical function
:func:`society_mgmt.core.compute`; no logic is re-implemented here.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
