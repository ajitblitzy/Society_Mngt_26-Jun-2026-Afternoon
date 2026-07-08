"""society_mgmt.models — navigational models-layer subpackage.

Migrated in place from the legacy models-layer modules. The "models"
label is structural only: there is no ORM, schema, or persistence in this
codebase. Every module in this subpackage (``file_2``, ``file_13``,
``file_24``) delegates to the single canonical function
:func:`society_mgmt.core.compute` and re-implements no logic.

This module marks the package for setuptools discovery and re-exports
``compute`` for ergonomic access.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
