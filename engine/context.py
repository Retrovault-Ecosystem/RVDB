"""
=========================================================
RVDB Engine Context
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/context.py

Purpose:
    Provides shared access to:

    - RVEngine
    - EntityResolver

    Uses the Foundation 0.2 EntityLoader architecture and
    canonical project data paths.

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

from engine.graph import build_graph
from engine.loader import EntityLoader
from engine.paths import DATA_ROOT
from engine.query import RVEngine
from engine.resolver import EntityResolver


_engine = None
_resolver = None


def load_entities():

    loader = EntityLoader(
        DATA_ROOT
    )

    return loader.load()


def get_engine():

    global _engine

    if _engine is None:

        entities = load_entities()

        graph = build_graph(
            entities
        )

        _engine = RVEngine(
            graph
        )

    return _engine


def get_resolver():

    global _resolver

    if _resolver is None:

        engine = get_engine()

        _resolver = EntityResolver(
            engine.graph
        )

    return _resolver
