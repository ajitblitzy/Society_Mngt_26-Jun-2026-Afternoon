"""society_mgmt.routes — navigational "routes" layer of the migrated package.

Preserved from the legacy nine-layer JavaScript taxonomy purely for
navigation; "routes" is a structural label only — there is no HTTP routing,
handler, or framework wiring here (AAP section 0.3.4).

Every module in this subpackage (``file_3``, ``file_14``, ``file_25``) delegates
to the single canonical function :func:`society_mgmt.core.compute`; no logic is
re-implemented. This package initializer re-exports ``compute`` for ergonomic
access (``from society_mgmt.routes import compute``).
"""

from society_mgmt.core import compute

__all__ = ["compute"]
