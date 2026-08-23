"""
=========================================================
RVDB Pytest Configuration
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/conftest.py

Purpose:
    Configure Foundation 0.2 automated tests.

    The original legacy tests target the inner rvdb/
    package and are temporarily excluded from pytest
    collection.

    They are preserved for review during:

        Foundation Release 0.2.1
        Legacy Cleanup

Foundation Release:
    0.2

Checkpoint:
    B — Type System Test Foundation

=========================================================
"""


collect_ignore = [

    "test_loader.py",

    "test_builder.py",


]
