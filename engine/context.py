"""
RVDB Engine Context

Provides shared access to:
- RVEngine
- EntityResolver

Uses the current EntityLoader architecture.
"""

from engine.loader import EntityLoader
from engine.graph import build_graph
from engine.query import RVEngine
from engine.resolver import EntityResolver


_engine = None
_resolver = None


def load_entities():

    loader = EntityLoader(
        "data"
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
