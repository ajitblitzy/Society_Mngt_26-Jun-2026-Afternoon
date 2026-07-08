"""Test package for society_mgmt.

Marks ``tests`` as an importable package so pytest (configured with
``testpaths = ["tests"]`` in ``pyproject.toml``) collects the unit and
integration characterization suites, and so the shared golden-master data in
``tests/conftest.py`` is importable as ``tests.conftest``.
"""
