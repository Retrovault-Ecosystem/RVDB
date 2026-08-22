"""
=========================================================
RVDB Foundation Build Package
=========================================================

Project:
    RetroVault Database (RVDB)

Purpose:
    Contains build and serialization components for the
    active RVDB Foundation architecture.

Foundation Release:
    0.2.1

=========================================================
"""

from build.builder import (
    DEFAULT_BUNDLE_PATH,
    build_bundle,
)


__all__ = [
    "DEFAULT_BUNDLE_PATH",
    "build_bundle",
]
