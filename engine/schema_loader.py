"""
=========================================================
RVDB Schema Loader
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/schema_loader.py

Purpose:
    Loads, merges and caches RVDB schemas.

Foundation Release:
    0.2 — Schema Engine

=========================================================
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


class SchemaNotFoundError(Exception):
    """
    Raised when an entity schema
    cannot be located.
    """
    pass


class SchemaLoader:

    def __init__(
        self,
        schema_root: str | Path = "schemas",
    ):

        self.schema_root = Path(
            schema_root
        )

        self.common_schema_file = (
            self.schema_root /
            "entity_schema.yaml"
        )

        self.entity_schema_dir = (
            self.schema_root /
            "entities"
        )

        self._common_schema = {}

        self._entity_schemas = {}

        self._resolved_cache = {}

        self.reload()

    # =====================================================
    # Public API
    # =====================================================

    def reload(self):

        self._common_schema = (
            self._load_yaml(
                self.common_schema_file
            )
        )

        self._entity_schemas = {}

        if self.entity_schema_dir.exists():

            for file in sorted(
                self.entity_schema_dir.glob(
                    "*.yaml"
                )
            ):

                self._entity_schemas[
                    file.stem
                ] = self._load_yaml(file)

        self._resolved_cache.clear()

        for entity_type in self._entity_schemas:

            self._resolved_cache[
                entity_type
            ] = self._merge_schema(
                entity_type
            )

    def has_schema(
        self,
        entity_type,
    ):

        return (
            entity_type
            in self._resolved_cache
        )

    def list_entity_types(
        self,
    ):

        return sorted(
            self._resolved_cache.keys()
        )

    def get_schema(
        self,
        entity_type,
    ):

        if entity_type not in self._resolved_cache:

            raise SchemaNotFoundError(
                entity_type
            )

        return deepcopy(
            self._resolved_cache[
                entity_type
            ]
        )

    # =====================================================
    # Internal
    # =====================================================

    def _load_yaml(
        self,
        filename: Path,
    ) -> dict[str, Any]:

        if not filename.exists():

            return {}

        with filename.open(
            "r",
            encoding="utf-8",
        ) as f:

            return (
                yaml.safe_load(f)
                or {}
            )

    def _merge_schema(
        self,
        entity_type,
    ):

        common = (
            self._common_schema
        )

        entity = (
            self._entity_schemas[
                entity_type
            ]
        )

        resolved = {

            "required": [],

            "optional": [],

            "fields": {},

        }

        resolved["required"] = list(
            dict.fromkeys(

                common.get(
                    "entity",
                    {}
                ).get(
                    "required",
                    []
                )

                +

                entity.get(
                    "required",
                    []
                )

            )
        )

        resolved["optional"] = list(
            dict.fromkeys(

                common.get(
                    "entity",
                    {}
                ).get(
                    "optional",
                    []
                )

                +

                entity.get(
                    "optional",
                    []
                )

            )
        )

        resolved["fields"].update(

            common.get(
                "fields",
                {}
            )

        )

        resolved["fields"].update(

            entity.get(
                "fields",
                {}
            )

        )

        return resolved
