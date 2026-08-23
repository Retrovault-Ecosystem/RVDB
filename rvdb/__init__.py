"""
RVDB - RetroVault Database Foundation

Historical package API retained temporarily during
Foundation 0.2.1 legacy cleanup.
"""

from rvdb.loader import RVDBLoader
from rvdb.registry import Registry, registry
from rvdb.relationships import RelationshipGraph, graph


__all__ = [
    "RVDBLoader",
    "Registry",
    "registry",
    "RelationshipGraph",
    "graph",
]
