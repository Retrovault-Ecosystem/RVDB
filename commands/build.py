"""
=========================================================
RVDB Build Command
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    commands/build.py

Purpose:
    Builds the canonical Foundation 0.2 RVDB bundle from
    the active EntityLoader -> RVGraph architecture.

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

from build.builder import (
    build_bundle,
)

from engine.loader import EntityLoader
from engine.paths import DATA_ROOT
from engine.graph import build_graph
from validator.schema import SchemaValidator
from validator.relationships import RelationshipValidator


def cmd_build():

    try:

        # Build from one fresh source snapshot, never a cached query graph.
        entities = EntityLoader(DATA_ROOT).load()
        if not entities:
            raise ValueError("No entities found")
        identities = [entity.id for entity in entities]
        if len(set(identities)) != len(identities):
            raise ValueError("Duplicate entity IDs")
        graph = build_graph(entities)
        schema_validator = SchemaValidator()
        relationship_validator = RelationshipValidator()
        for entity in entities:
            result = schema_validator.validate(entity)
            if not result.valid:
                raise ValueError(f"{entity.id}: {'; '.join(result.errors)}")
            for relationship, targets in entity.get("relationships", {}).items():
                for target_id in targets:
                    target = graph.nodes.get(target_id)
                    if target is None:
                        raise ValueError(f"{entity.id}: Missing target entity: {target_id}")
                    result = relationship_validator.validate(entity, relationship, target)
                    if not result.valid:
                        raise ValueError(f"{entity.id}: {'; '.join(result.errors)}")

        output = build_bundle(
            graph
        )

        print(
            f"Graph Nodes : "
            f"{len(graph.nodes)}"
        )

        print(
            f"Graph Edges : "
            f"{len(graph.edges)}"
        )

        print()

        print(
            f"Bundle      : {output}"
        )

        print()

        print(
            "Build complete."
        )

        return output

    except Exception as error:

        print(
            f"Build error: {error}"
        )

        return None
