"""
=========================================================
RVDB Foundation CSV Exporter
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    build/csv_exporter.py

Purpose:
    Exports Foundation RVDB entities to CSV.

    The exporter operates on generic entity mappings rather
    than the legacy Game object model.

    Nested values may be selected using dotted paths such as:

        relationships.platform
        metadata.regions

    Lists and mappings are serialized as deterministic JSON
    strings inside CSV cells.

Foundation Release:
    0.2.1

Checkpoint:
    D3 — CSV Export Migration

=========================================================
"""

from __future__ import annotations

import csv
import json
from collections.abc import (
    Iterable,
    Mapping,
)
from pathlib import Path
from typing import Any

from engine.paths import (
    PROJECT_ROOT,
)


# =========================================================
# Default Output
# =========================================================

DEFAULT_CSV_PATH = (
    PROJECT_ROOT
    / "dist"
    / "entities.csv"
)


# =========================================================
# Entity Mapping
# =========================================================

def _entity_mapping(
    entity: Any,
) -> Mapping[str, Any]:
    """
    Return a dictionary-compatible mapping for an entity.

    Foundation Entity instances expose their YAML data
    through ``entity.data``. Plain mappings are also
    supported directly.
    """

    if hasattr(
        entity,
        "data",
    ):

        data = entity.data

    elif isinstance(
        entity,
        Mapping,
    ):

        data = entity

    else:

        raise TypeError(
            (
                "Unsupported entity type: "
                f"{type(entity).__name__}"
            )
        )

    if not isinstance(
        data,
        Mapping,
    ):

        raise TypeError(
            "Entity data must be a mapping"
        )

    return data


# =========================================================
# Nested Field Resolution
# =========================================================

def _resolve_path(
    data: Mapping[str, Any],
    path: str,
) -> Any:
    """
    Resolve a dotted field path from an entity mapping.

    Example:

        relationships.platform
    """

    value: Any = data

    for part in path.split("."):

        if not isinstance(
            value,
            Mapping,
        ):

            return None

        if part not in value:

            return None

        value = value[
            part
        ]

    return value


# =========================================================
# Cell Serialization
# =========================================================

def _serialize_cell(
    value: Any,
) -> Any:
    """
    Convert a Foundation value into a CSV-safe value.

    Lists and mappings are encoded as JSON so relationship
    arrays and metadata remain machine-readable.
    """

    if value is None:

        return ""

    if isinstance(
        value,
        (
            list,
            dict,
        ),
    ):

        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
        )

    return value


# =========================================================
# Automatic Columns
# =========================================================

def _discover_columns(
    entities: list[Mapping[str, Any]],
) -> dict[str, str]:
    """
    Build deterministic top-level CSV columns.

    Common Foundation identity fields appear first.
    Remaining fields are sorted alphabetically.
    """

    preferred = [
        "id",
        "type",
        "name",
    ]

    discovered = set()

    for entity in entities:

        discovered.update(
            entity.keys()
        )

    columns: dict[str, str] = {}

    for field in preferred:

        if field in discovered:

            columns[
                field
            ] = field

            discovered.remove(
                field
            )

    for field in sorted(
        discovered
    ):

        columns[
            field
        ] = field

    return columns


# =========================================================
# CSV Export
# =========================================================

def export_entities_csv(
    entities: Iterable[Any],
    output: str | Path | None = None,
    columns: Mapping[str, str] | None = None,
) -> Path:
    """
    Export Foundation entities to CSV.

    ``columns`` maps CSV column names to entity field paths.

    Example:

        {
            "id": "id",
            "name": "name",
            "platform": "relationships.platform",
        }

    If no columns are supplied, all top-level fields found
    across the supplied entities are exported.

    If no output path is supplied, the file is written to:

        <project-root>/dist/entities.csv
    """

    entity_data = [
        _entity_mapping(
            entity
        )
        for entity in entities
    ]

    if columns is None:

        column_map = (
            _discover_columns(
                entity_data
            )
        )

    else:

        column_map = dict(
            columns
        )

    if not column_map:

        raise ValueError(
            "CSV export requires at least one column"
        )

    if output is None:

        output_path = (
            DEFAULT_CSV_PATH
        )

    else:

        output_path = Path(
            output
        )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=list(
                column_map.keys()
            ),
        )

        writer.writeheader()

        for entity in entity_data:

            row = {}

            for (
                column_name,
                field_path,
            ) in column_map.items():

                value = _resolve_path(
                    entity,
                    field_path,
                )

                row[
                    column_name
                ] = _serialize_cell(
                    value
                )

            writer.writerow(
                row
            )

    return output_path
