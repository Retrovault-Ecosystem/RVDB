"""
RVDB Entity Registry

Provides a centralized in-memory registry
of all RVDB entities.

This becomes the single source of truth
for entity lookup throughout RVDB.
"""

from pathlib import Path

import yaml


class EntityRegistry:

    def __init__(self):

        self.by_id = {}

        self.by_name = {}

        self.by_alias = {}

        self.by_type = {}

        self.load()

    # =====================================================
    # Load Database
    # =====================================================

    def load(self):

        data_path = Path("data")

        if not data_path.exists():

            return

        for yaml_file in data_path.rglob("*.yaml"):

            entity = self.load_entity(
                yaml_file
            )

            if entity:

                self.register(entity)

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
                encoding="utf-8"
            ) as file:

                entity = yaml.safe_load(file)

        except Exception:

            return None

        if not entity:

            return None

        return entity

    # =====================================================
    # Register
    # =====================================================

    def register(
        self,
        entity,
    ):

        entity_id = entity.get("id")

        entity_type = entity.get("type")

        name = entity.get("name")

        aliases = entity.get(
            "aliases",
            []
        )

        if not all([
            entity_id,
            entity_type,
            name,
        ]):

            return

        # ID lookup
        self.by_id[
            entity_id
        ] = entity

        # Name lookup
        self.by_name[
            name.casefold()
        ] = entity_id

        # Alias lookup
        for alias in aliases:

            self.by_alias[
                alias.casefold()
            ] = entity_id

        # Type lookup
        self.by_type.setdefault(
            entity_type,
            []
        ).append(
            entity_id
        )

    # =====================================================
    # Public API
    # =====================================================

    def exists(
        self,
        entity_id,
    ):

        return entity_id in self.by_id

    def get(
        self,
        entity_id,
    ):

        return self.by_id.get(
            entity_id
        )

    def resolve(
        self,
        name,
    ):

        if not name:

            return None

        key = name.casefold()

        if key in self.by_name:

            return self.by_name[key]

        if key in self.by_alias:

            return self.by_alias[key]

        return None

    def entities_of_type(
        self,
        entity_type,
    ):

        return self.by_type.get(
            entity_type,
            []
        )
