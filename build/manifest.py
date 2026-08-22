"""
=========================================================
RVDB Foundation Manifest Builder
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    build/manifest.py

Purpose:
    Generates metadata describing an RVDB Foundation build.

    The manifest is derived from the active RVGraph and does
    not depend on the legacy registry or legacy entity model.

Foundation Release:
    0.2.1

Checkpoint:
    D5 — Manifest Migration

=========================================================
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from datetime import (
    datetime,
    timezone,
)
import json
from pathlib import Path
from typing import Any

from engine.paths import (
    PROJECT_ROOT,
)


# =========================================================
# Manifest Constants
# =========================================================

DEFAULT_MANIFEST_PATH = (
    PROJECT_ROOT
    / "dist"
    / "manifest.json"
)

DEFAULT_MANIFEST_VERSION = (
    "0.2.1"
)

PROJECT_NAME = (
    "RetroVault Database"
)


# =========================================================
# Helpers
# =========================================================

def _entity_data(
    entity: Any,
) -> dict[str, Any]:
    """
    Return plain mapping data from a graph node.
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

    return data


def _artifact_name(
    artifact: str | Path,
) -> str:
    """
    Convert an artifact path into a portable manifest path.

    Files beneath the RVDB project root are recorded relative
    to the project root.

    External files are represented by basename only so the
    manifest never embeds machine-specific absolute paths.
    """

    path = Path(
        artifact
    )

    if not path.is_absolute():

        return path.as_posix()

    try:

        return (
            path
            .resolve()
            .relative_to(
                PROJECT_ROOT.resolve()
            )
            .as_posix()
        )

    except ValueError:

        return path.name


def _generated_timestamp() -> str:
    """
    Return an ISO-8601 UTC timestamp.
    """

    return (
        datetime.now(
            timezone.utc
        )
        .isoformat()
        .replace(
            "+00:00",
            "Z",
        )
    )


# =========================================================
# Manifest Builder
# =========================================================

def build_manifest(
    graph,
    artifacts: Iterable[str | Path] = (),
    output: str | Path | None = None,
    version: str = DEFAULT_MANIFEST_VERSION,
) -> Path:
    """
    Build the Foundation RVDB manifest.

    Manifest contract:

        {
            "name": "RetroVault Database",
            "version": "0.2.1",
            "generated": "<UTC timestamp>",
            "statistics": {
                "total_entities": 19,
                "by_type": {
                    ...
                }
            },
            "artifacts": [
                ...
            ]
        }

    Artifact paths are normalized so absolute host paths are
    never written into the manifest.
    """

    if output is None:

        output_path = (
            DEFAULT_MANIFEST_PATH
        )

    else:

        output_path = Path(
            output
        )

    counts = Counter()

    for entity in graph.nodes.values():

        data = _entity_data(
            entity
        )

        entity_type = data.get(
            "type"
        )

        if entity_type:

            counts[
                entity_type
            ] += 1

    artifact_names = sorted(
        {
            _artifact_name(
                artifact
            )
            for artifact in artifacts
        }
    )

    manifest = {
        "name": PROJECT_NAME,
        "version": version,
        "generated": (
            _generated_timestamp()
        ),
        "statistics": {
            "total_entities": len(
                graph.nodes
            ),
            "by_type": {
                entity_type: counts[
                    entity_type
                ]
                for entity_type
                in sorted(
                    counts
                )
            },
        },
        "artifacts": artifact_names,
    }

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            manifest,
            file,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )

        file.write(
            "\n"
        )

    return output_path
