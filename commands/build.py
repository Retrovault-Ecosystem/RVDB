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

from engine.context import (
    get_engine,
)


def cmd_build():

    try:

        engine = get_engine()

        graph = engine.graph

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
