"""society_mgmt — Python package migrated in-place from the legacy JavaScript corpus.

All logic converges on a single canonical function, :func:`society_mgmt.core.compute`.
This root re-exports it for ergonomic access, so callers may write either
``from society_mgmt import compute`` or ``from society_mgmt.core import compute``.

The nine legacy layers (config, controllers, domain, middleware, models,
repositories, routes, services, utils) are preserved as navigational subpackages;
each delegates to :func:`compute` and re-implements no logic.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
