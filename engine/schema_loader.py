"""
=========================================================
RVDB Schema Loader
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/schema_loader.py

Purpose:
    Loads, validates, merges, and caches RVDB schemas.

    Resolved schemas contain:

        required
        optional
        fields
        relationships

    Relationship definitions are validated when schemas
    are loaded so malformed relationship rules cannot
    silently become runtime validation rules.

Foundation Release:
    0.2 — Schema Engine

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from engine.paths import SCHEMA_ROOT


class SchemaNotFoundError(Exception):
    """
    Raised when an entity schema cannot be located.
    """

    pass


class SchemaDefinitionError(Exception):
    """
    Raised when an RVDB schema definition is malformed.
    """

    pass


class SchemaLoader:
    """
    Load and resolve RVDB entity schemas.
    """

    RELATIONSHIP_TYPES = {
        "entity_reference",
        "entity_reference_list",
    }

    FIELD_TYPES = {
        "string",
        "integer",
        "integer_or_null",
        "boolean",
        "list",
        "object",
        "entity_reference",
        "entity_reference_list",
    }

    LIST_ITEM_TYPES = {
        "string",
        "integer",
        "integer_or_null",
        "boolean",
        "object",
    }

    def __init__(
        self,
        schema_root: str | Path | None = None,
    ) -> None:

        if schema_root is None:

            self.schema_root = SCHEMA_ROOT

        else:

            self.schema_root = Path(
                schema_root
            )

        self.common_schema_file = (
            self.schema_root
            / "entity_schema.yaml"
        )

        self.entity_schema_dir = (
            self.schema_root
            / "entities"
        )

        self._common_schema: dict[str, Any] = {}

        self._entity_schemas: dict[
            str,
            dict[str, Any],
        ] = {}

        self._resolved_cache: dict[
            str,
            dict[str, Any],
        ] = {}

        self.reload()

    # =====================================================
    # Public API
    # =====================================================

    def reload(
        self,
    ) -> None:

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
                ] = self._load_yaml(
                    file
                )

        self._validate_schema_definitions()

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
    ) -> bool:

        return (
            entity_type
            in self._resolved_cache
        )

    def list_entity_types(
        self,
    ) -> list[str]:

        return sorted(
            self._resolved_cache.keys()
        )

    def get_schema(
        self,
        entity_type,
    ) -> dict[str, Any]:

        if entity_type not in self._resolved_cache:

            raise SchemaNotFoundError(
                entity_type
            )

        return deepcopy(
            self._resolved_cache[
                entity_type
            ]
        )

    def get_relationships(
        self,
        entity_type,
    ) -> dict[str, Any]:
        """
        Return relationship definitions for one entity type.
        """

        schema = self.get_schema(
            entity_type
        )

        return deepcopy(
            schema.get(
                "relationships",
                {},
            )
        )

    # =====================================================
    # YAML Loading
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
        ) as file:

            data = (
                yaml.safe_load(
                    file
                )
                or {}
            )

        if not isinstance(
            data,
            dict,
        ):

            raise SchemaDefinitionError(
                (
                    "Schema file must contain "
                    f"a YAML mapping: {filename}"
                )
            )

        return data

    # =====================================================
    # Schema Definition Validation
    # =====================================================

    def _validate_schema_definitions(
        self,
    ) -> None:
        """
        Validate schema-level field and relationship definitions.

        This validates the schema itself, not entity data.
        """

        available_types = set(
            self._entity_schemas.keys()
        )

        common_fields = self._common_schema.get(
            "fields",
            {},
        )

        self._validate_field_block(
            "<common>",
            common_fields,
        )

        common_relationships = (
            self._common_schema.get(
                "relationships",
                {},
            )
        )

        self._validate_relationship_block(
            "<common>",
            common_relationships,
            available_types,
        )

        for (
            entity_type,
            schema,
        ) in self._entity_schemas.items():

            fields = schema.get(
                "fields",
                {},
            )

            self._validate_field_block(
                entity_type,
                fields,
            )

            relationships = schema.get(
                "relationships",
                {},
            )

            self._validate_relationship_block(
                entity_type,
                relationships,
                available_types,
            )

    def _validate_field_block(
        self,
        source_type: str,
        fields: Any,
    ) -> None:

        if fields is None:
            return

        if not isinstance(
            fields,
            dict,
        ):

            raise SchemaDefinitionError(
                (
                    f"{source_type}: "
                    "'fields' must be a mapping"
                )
            )

        for (
            field_name,
            definition,
        ) in fields.items():

            if (
                not isinstance(
                    field_name,
                    str,
                )
                or not field_name.strip()
            ):

                raise SchemaDefinitionError(
                    (
                        f"{source_type}: field names "
                        "must be non-empty strings"
                    )
                )

            self._validate_field_definition(
                source_type,
                field_name,
                definition,
            )

    def _validate_field_definition(
        self,
        source_type: str,
        field_name: str,
        definition: Any,
    ) -> None:

        prefix = (
            f"{source_type}.{field_name}"
        )

        if not isinstance(
            definition,
            dict,
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: field definition "
                    "must be a mapping"
                )
            )

        field_type = definition.get(
            "type"
        )

        if field_type not in self.FIELD_TYPES:

            raise SchemaDefinitionError(
                (
                    f"{prefix}: invalid field "
                    f"type '{field_type}'"
                )
            )

        enum = definition.get(
            "enum"
        )

        if enum is not None:

            if field_type != "string":

                raise SchemaDefinitionError(
                    (
                        f"{prefix}: 'enum' is only "
                        "valid for string fields"
                    )
                )

            self._validate_enum_constraint(
                prefix,
                field_type,
                enum,
            )

        items = definition.get(
            "items"
        )

        if items is not None:

            if field_type != "list":

                raise SchemaDefinitionError(
                    (
                        f"{prefix}: 'items' is only "
                        "valid for list fields"
                    )
                )

            self._validate_items_constraint(
                prefix,
                items,
            )

    def _validate_enum_constraint(
        self,
        prefix: str,
        value_type: str,
        enum: Any,
    ) -> None:

        if (
            not isinstance(
                enum,
                list,
            )
            or not enum
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: 'enum' must be "
                    "a non-empty list"
                )
            )

        for value in enum:

            if not self._value_matches_type(
                value_type,
                value,
            ):

                raise SchemaDefinitionError(
                    (
                        f"{prefix}: enum value "
                        f"{value!r} does not match "
                        f"type '{value_type}'"
                    )
                )

    def _validate_items_constraint(
        self,
        prefix: str,
        items: Any,
    ) -> None:

        if not isinstance(
            items,
            dict,
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: 'items' must be "
                    "a mapping"
                )
            )

        item_type = items.get(
            "type"
        )

        if item_type not in self.LIST_ITEM_TYPES:

            raise SchemaDefinitionError(
                (
                    f"{prefix}: invalid item "
                    f"type '{item_type}'"
                )
            )

        enum = items.get(
            "enum"
        )

        if enum is not None:

            if item_type != "string":

                raise SchemaDefinitionError(
                    (
                        f"{prefix}.items: 'enum' is only "
                        "valid for string items"
                    )
                )

            self._validate_enum_constraint(
                f"{prefix}.items",
                item_type,
                enum,
            )

    @staticmethod
    def _value_matches_type(
        value_type: str,
        value: Any,
    ) -> bool:

        if value_type == "string":
            return isinstance(
                value,
                str,
            )

        if value_type == "integer":
            return (
                isinstance(
                    value,
                    int,
                )
                and not isinstance(
                    value,
                    bool,
                )
            )

        if value_type == "integer_or_null":
            return (
                value is None
                or (
                    isinstance(
                        value,
                        int,
                    )
                    and not isinstance(
                        value,
                        bool,
                    )
                )
            )

        if value_type == "boolean":
            return isinstance(
                value,
                bool,
            )

        if value_type == "list":
            return isinstance(
                value,
                list,
            )

        if value_type == "object":
            return isinstance(
                value,
                dict,
            )

        if value_type in {
            "entity_reference",
            "entity_reference_list",
        }:
            return True

        return False

    def _validate_relationship_block(
        self,
        source_type: str,
        relationships: Any,
        available_types: set[str],
    ) -> None:

        if relationships is None:
            return

        if not isinstance(
            relationships,
            dict,
        ):

            raise SchemaDefinitionError(
                (
                    f"{source_type}: "
                    "'relationships' must be a mapping"
                )
            )

        for (
            relationship_name,
            definition,
        ) in relationships.items():

            if not isinstance(
                relationship_name,
                str,
            ) or not relationship_name.strip():

                raise SchemaDefinitionError(
                    (
                        f"{source_type}: "
                        "relationship names must be "
                        "non-empty strings"
                    )
                )

            self._validate_relationship_definition(
                source_type,
                relationship_name,
                definition,
                available_types,
            )

    def _validate_relationship_definition(
        self,
        source_type: str,
        relationship_name: str,
        definition: Any,
        available_types: set[str],
    ) -> None:

        prefix = (
            f"{source_type}.{relationship_name}"
        )

        if not isinstance(
            definition,
            dict,
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: relationship "
                    "definition must be a mapping"
                )
            )

        relationship_type = definition.get(
            "type"
        )

        if relationship_type not in (
            self.RELATIONSHIP_TYPES
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: invalid relationship "
                    f"type '{relationship_type}'"
                )
            )

        entity_type = definition.get(
            "entity_type"
        )

        entity_types = definition.get(
            "entity_types"
        )

        if (
            entity_type is not None
            and entity_types is not None
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: define either "
                    "'entity_type' or 'entity_types', "
                    "not both"
                )
            )

        if (
            entity_type is None
            and entity_types is None
        ):

            raise SchemaDefinitionError(
                (
                    f"{prefix}: relationship must "
                    "define a target entity type"
                )
            )

        targets: list[str] = []

        if entity_type is not None:

            if not isinstance(
                entity_type,
                str,
            ) or not entity_type.strip():

                raise SchemaDefinitionError(
                    (
                        f"{prefix}: 'entity_type' "
                        "must be a non-empty string"
                    )
                )

            targets.append(
                entity_type
            )

        if entity_types is not None:

            if (
                not isinstance(
                    entity_types,
                    list,
                )
                or not entity_types
            ):

                raise SchemaDefinitionError(
                    (
                        f"{prefix}: 'entity_types' "
                        "must be a non-empty list"
                    )
                )

            for target in entity_types:

                if (
                    not isinstance(
                        target,
                        str,
                    )
                    or not target.strip()
                ):

                    raise SchemaDefinitionError(
                        (
                            f"{prefix}: every "
                            "'entity_types' value must "
                            "be a non-empty string"
                        )
                    )

                targets.append(
                    target
                )

        for target in targets:

            if target not in available_types:

                raise SchemaDefinitionError(
                    (
                        f"{prefix}: unknown target "
                        f"entity type '{target}'"
                    )
                )

    # =====================================================
    # Schema Merge
    # =====================================================

    def _merge_schema(
        self,
        entity_type,
    ) -> dict[str, Any]:

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
            "relationships": {},
        }

        resolved["required"] = list(
            dict.fromkeys(

                common.get(
                    "entity",
                    {},
                ).get(
                    "required",
                    [],
                )

                +

                entity.get(
                    "required",
                    [],
                )
            )
        )

        resolved["optional"] = list(
            dict.fromkeys(

                common.get(
                    "entity",
                    {},
                ).get(
                    "optional",
                    [],
                )

                +

                entity.get(
                    "optional",
                    [],
                )
            )
        )

        resolved["fields"].update(

            common.get(
                "fields",
                {},
            )
        )

        resolved["fields"].update(

            entity.get(
                "fields",
                {},
            )
        )

        resolved["relationships"].update(

            common.get(
                "relationships",
                {},
            )
        )

        resolved["relationships"].update(

            entity.get(
                "relationships",
                {},
            )
        )

        return resolved
