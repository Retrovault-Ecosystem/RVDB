from engine.loader import load_entities
from engine.graph import build_graph
from engine.query import RVEngine
from engine.resolver import EntityResolver


_engine = None
_resolver = None



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
