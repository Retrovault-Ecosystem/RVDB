"""
=========================================================
RVDB Relationship Lookup
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/relationship_lookup.py

Purpose:
    Resolves human-readable entity names and aliases
    into canonical RVDB entity IDs.

Foundation Release:
    0.2

=========================================================
"""

from __future__ import annotations

from pathlib import Path

import yaml

from engine.paths import DATA_ROOT


class RelationshipLookup:
    """
    Resolves entity names and aliases into canonical RVDB IDs.
    """

    def __init__(
        self,
        data_path: str | Path | None = None,
    ):

        self.lookups = {}

        if data_path is None:

            self.data_path = DATA_ROOT

        else:

            self.data_path = Path(
                data_path
            )

        self.load_entities()

    # =====================================================
    # Load Every Entity
    # =====================================================

    def load_entities(self):

        self.lookups.clear()

        if not self.data_path.exists():

            return

        yaml_files = list(
            self.data_path.rglob(
                "*.yaml"
            )
        )

        yaml_files.extend(
            self.data_path.rglob(
                "*.yml"
            )
        )

        for yaml_file in sorted(
            yaml_files
        ):

            self.load_entity(
                yaml_file
            )

    # =====================================================
    # Load One Entity
    # =====================================================

    def load_entity(
        self,
        filename,
    ):

        try:

            with filename.open(
                "r",
                encoding="utf-8",
            ) as file:

                entity = yaml.safe_load(
                    file
                )

        except Exception:

            return

        if not entity:

            return

        entity_id = entity.get(
            "id"
        )

        entity_type = entity.get(
            "type"
        )

        name = entity.get(
            "name"
        )

        aliases = entity.get(
            "aliases",
            [],
        )

        if not all(
            [
                entity_id,
                entity_type,
                name,
            ]
        ):

            return

        if entity_type not in self.lookups:

            self.lookups[
                entity_type
            ] = {}

        lookup = self.lookups[
            entity_type
        ]

        lookup[
            name.casefold()
        ] = entity_id

        for alias in aliases:

            if not isinstance(
                alias,
                str,
            ):

                continue

            lookup[
                alias.casefold()
            ] = entity_id

    # =====================================================
    # Lookup
    # =====================================================

    def resolve(
        self,
        text,
        entity_type=None,
    ):

        if not text:

            return None

        text = text.casefold()

        # Typed lookup

        if entity_type:

            lookup = self.lookups.get(
                entity_type,
                {},
            )

            return lookup.get(
                text
            )

        # Legacy lookup

        for lookup in self.lookups.values():

            if text in lookup:

                return lookup[
                    text
                ]

        return None
