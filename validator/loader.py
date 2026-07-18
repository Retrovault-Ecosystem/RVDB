"""
RVDB Schema Loader

Loads the common entity schema and
entity-specific schemas.
"""

from pathlib import Path

import yaml


class SchemaLoader:

    def __init__(self):

        self.schema_root = Path(
            "schemas"
        )

        self.entity_root = (
            self.schema_root /
            "entities"
        )

        self.common_schema = (
            self.load_yaml(
                self.schema_root /
                "entity_schema.yaml"
            )
        )

        self.entity_schemas = {}

    # =====================================================
    # Generic YAML Loader
    # =====================================================

    def load_yaml(
        self,
        filename
    ):

        if not filename.exists():

            return {}

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return yaml.safe_load(file) or {}

    # =====================================================
    # Entity Schema
    # =====================================================

    def get_entity_schema(
        self,
        entity_type
    ):

        if entity_type in self.entity_schemas:

            return self.entity_schemas[
                entity_type
            ]

        filename = (
            self.entity_root /
            f"{entity_type}.yaml"
        )

        schema = self.load_yaml(
            filename
        )

        self.entity_schemas[
            entity_type
        ] = schema

        return schema
