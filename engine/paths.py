"""
=========================================================
RVDB Project Paths
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/paths.py

Purpose:
    Provides canonical filesystem paths for RVDB project
    resources.

    Project resources must not depend on the shell's
    current working directory.

Foundation Release:
    0.2

Checkpoint:
    C2 — Generic Entity Builder

=========================================================
"""

from __future__ import annotations

from pathlib import Path


# =====================================================
# Project Root
# =====================================================

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)


# =====================================================
# Project Resource Directories
# =====================================================

DATA_ROOT = (
    PROJECT_ROOT
    / "data"
)

SCHEMA_ROOT = (
    PROJECT_ROOT
    / "schemas"
)

ENTITY_SCHEMA_ROOT = (
    SCHEMA_ROOT
    / "entities"
)

TEMPLATE_ROOT = (
    PROJECT_ROOT
    / "templates"
)

ENTITY_TEMPLATE_ROOT = (
    TEMPLATE_ROOT
    / "entities"
)

CONFIG_ROOT = (
    PROJECT_ROOT
    / "config"
)


# =====================================================
# Helper
# =====================================================

def project_path(
    *parts: str,
) -> Path:
    """
    Return a path located beneath the RVDB project root.
    """

    return PROJECT_ROOT.joinpath(
        *parts
    )
