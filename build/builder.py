"""
=========================================================
RVDB Foundation Bundle Builder
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    build/builder.py

Purpose:
    Serializes the active Foundation 0.2 RVGraph into the
    canonical RVDB bundle artifact.

Bundle contract:

    {
        "nodes": {
            "<entity-id>": {
                ... entity data ...
            }
        },
        "edges": {
            "<entity-id>": {
                ... relationships ...
            }
        }
    }

    Python Entity objects are never written directly.
    Only their YAML-compatible data mappings are exported.

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any

from engine.paths import PROJECT_ROOT


DEFAULT_BUNDLE_PATH = (
    PROJECT_ROOT
    / "rvdb.bundle.json"
)


def _serialize_entity(
    entity: Any,
) -> dict[str, Any]:
    """
    Convert an RVDB entity into plain JSON-compatible data.
    """

    if hasattr(
        entity,
        "data",
    ):

        data = entity.data

    elif isinstance(
        entity,
        dict,
    ):

        data = entity

    else:

        raise TypeError(
            (
                "Unsupported graph node type: "
                f"{type(entity).__name__}"
            )
        )

    if not isinstance(
        data,
        dict,
    ):

        raise TypeError(
            "Entity data must be a mapping"
        )

    return deepcopy(
        data
    )


def build_bundle(
    graph,
    output: str | Path | None = None,
) -> Path:
    """
    Build the canonical Foundation 0.2 RVDB bundle.

    If no output path is supplied, the bundle is written
    to:

        <project-root>/rvdb.bundle.json

    This remains independent of the shell's current
    working directory.
    """

    if output is None:

        output_path = (
            DEFAULT_BUNDLE_PATH
        )

    else:

        output_path = Path(
            output
        )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    nodes = {}

    for (
        entity_id,
        entity,
    ) in sorted(
        graph.nodes.items()
    ):

        nodes[
            entity_id
        ] = _serialize_entity(
            entity
        )

    edges = {}

    for (
        entity_id,
        relationships,
    ) in sorted(
        graph.edges.items()
    ):

        edges[
            entity_id
        ] = deepcopy(
            relationships
        )

    bundle = {
        "nodes": nodes,
        "edges": edges,
    }

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            bundle,
            file,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )

        file.write(
            "\n"
        )

    return output_path
