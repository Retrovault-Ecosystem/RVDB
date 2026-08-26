"""
=========================================================
RVDB Generic Entity Builder
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/entity_builder.py

Purpose:
    Builds RVDB entities interactively from YAML schemas.

    Both ordinary entity fields and relationships are
    driven by SchemaLoader.

    Templates provide structural/default data only.
    Relationship vocabulary is defined by schemas.

Foundation Release:
    0.2

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from __future__ import annotations

from typing import Any

import yaml

from engine.entity_reference import (
    EntityReferenceValidator,
)
from engine.factory import EntityFactory
from engine.id_generator import IDGenerator
from engine.relationship_lookup import (
    RelationshipLookup,
)
from engine.type_registry import TypeRegistry

from engine.schema_loader import (
    SchemaLoader,
    SchemaNotFoundError,
)


class EntityBuilder:
    """
    Generic schema-driven interactive entity builder.
    """

    COMMON_FIELDS = {
        "id",
        "type",
        "name",
        "aliases",
        "relationships",
        "metadata",
    }

    def __init__(self) -> None:

        self.factory = EntityFactory()

        self.schemas = SchemaLoader()

        self.lookup = RelationshipLookup()

        self.reference_validator = (
            EntityReferenceValidator()
        )

    # =====================================================
    # Public API
    # =====================================================

    def build(
        self,
        entity_type: str,
    ) -> dict[str, Any] | None:
        """
        Build an entity interactively using its schema.
        """

        if not self.schemas.has_schema(
            entity_type
        ):

            print(
                f"No schema available for "
                f"'{entity_type}'."
            )

            return None

        try:

            schema = self.schemas.get_schema(
                entity_type
            )

            entity = self._create_base_entity(
                entity_type
            )

        except (
            SchemaNotFoundError,
            FileNotFoundError,
        ) as error:

            print(error)

            return None

        self._populate_schema_fields(
            entity,
            schema,
        )

        self._populate_schema_relationships(
            entity,
            schema,
        )

        if not self.preview(
            entity
        ):

            return None

        return entity

    # =====================================================
    # Base Entity
    # =====================================================

    def _create_base_entity(
        self,
        entity_type: str,
    ) -> dict[str, Any]:
        """
        Ask for the entity name, generate its canonical ID,
        and create the entity from its template.
        """

        print()

        title = (
            entity_type
            .replace("_", " ")
            .title()
        )

        print(
            f"RVDB {title} Builder"
        )

        print(
            "-" * (
                len(title)
                + 13
            )
        )

        name = self._prompt_required_string(
            "Name"
        )

        entity_id = IDGenerator.generate(
            entity_type,
            name,
        )

        print()

        print(
            "Generated ID:"
        )

        print(
            entity_id
        )

        entity = self.factory.create_entity(
            entity_type,
            entity_id,
            name,
        )

        self._clear_template_placeholders(
            entity
        )

        return entity

    # =====================================================
    # Schema Fields
    # =====================================================

    def _populate_schema_fields(
        self,
        entity: dict[str, Any],
        schema: dict[str, Any],
    ) -> None:
        """
        Prompt for ordinary fields defined by the schema.
        """

        fields = schema.get(
            "fields",
            {},
        )

        required_fields = set(
            schema.get(
                "required",
                [],
            )
        )

        for (
            field_name,
            field_schema,
        ) in fields.items():

            if field_name in self.COMMON_FIELDS:
                continue

            if not isinstance(
                field_schema,
                dict,
            ):
                continue

            field_type = field_schema.get(
                "type"
            )

            if not field_type:
                continue

            required = (
                field_name
                in required_fields
            )

            value = self._prompt_field(
                field_name,
                field_schema,
                required,
            )

            if value is _SKIP_FIELD:

                entity.pop(
                    field_name,
                    None,
                )

                continue

            entity[
                field_name
            ] = value

    # =====================================================
    # Schema Relationships
    # =====================================================

    def _populate_schema_relationships(
        self,
        entity: dict[str, Any],
        schema: dict[str, Any],
    ) -> None:
        """
        Populate entity relationships directly from schema
        relationship definitions.

        Template relationship placeholders are not used as
        the source of relationship vocabulary.
        """

        definitions = schema.get(
            "relationships",
            {},
        )

        entity[
            "relationships"
        ] = {}

        if not isinstance(
            definitions,
            dict,
        ):

            return

        relationships = entity[
            "relationships"
        ]

        for (
            relationship_name,
            relationship_schema,
        ) in definitions.items():

            if not isinstance(
                relationship_schema,
                dict,
            ):

                continue

            value = self._prompt_field(
                relationship_name,
                relationship_schema,
                required=False,
            )

            if value is _SKIP_FIELD:
                continue

            relationships[
                relationship_name
            ] = value

    # =====================================================
    # Generic Field Dispatcher
    # =====================================================

    def _prompt_field(
        self,
        field_name: str,
        field_schema: dict[str, Any],
        required: bool,
    ) -> Any:

        field_type = field_schema.get(
            "type"
        )

        label = self._field_label(
            field_name
        )

        description = field_schema.get(
            "description"
        )

        if description:

            print()

            print(
                f"{label}: {description}"
            )

        if field_type == "string":

            return self._prompt_string(
                label,
                required,
            )

        if field_type == "integer":

            return self._prompt_integer(
                label,
                required,
                allow_null=False,
            )

        if field_type == "integer_or_null":

            return self._prompt_integer(
                label,
                required,
                allow_null=True,
            )

        if field_type == "boolean":

            return self._prompt_boolean(
                label,
                required,
            )

        if field_type == "list":

            return self._prompt_list(
                label,
                required,
                field_schema,
            )

        if field_type == "object":

            return self._prompt_object(
                label,
                required,
            )

        if field_type == "entity_reference":

            return self._prompt_reference(
                label,
                field_schema,
                required,
                multiple=False,
            )

        if field_type == "entity_reference_list":

            return self._prompt_reference(
                label,
                field_schema,
                required,
                multiple=True,
            )

        print()

        print(
            f"Unsupported builder field type "
            f"'{field_type}' for '{field_name}'."
        )

        return _SKIP_FIELD

    # =====================================================
    # String
    # =====================================================

    def _prompt_required_string(
        self,
        label: str,
    ) -> str:

        while True:

            value = input(
                f"{label}: "
            ).strip()

            if value:
                return value

            print(
                f"{label} is required."
            )

    def _prompt_string(
        self,
        label: str,
        required: bool,
    ) -> str | object:

        if required:

            return self._prompt_required_string(
                label
            )

        value = input(
            f"{label} (optional): "
        ).strip()

        if not value:
            return _SKIP_FIELD

        return value

    # =====================================================
    # Integer
    # =====================================================

    def _prompt_integer(
        self,
        label: str,
        required: bool,
        allow_null: bool,
    ) -> int | None | object:

        while True:

            suffix = (
                ""
                if required
                else " (optional)"
            )

            value = input(
                f"{label}{suffix}: "
            ).strip()

            if not value:

                if allow_null:
                    return None

                if not required:
                    return _SKIP_FIELD

                print(
                    f"{label} is required."
                )

                continue

            try:

                return int(
                    value
                )

            except ValueError:

                print(
                    f"{label} must be an integer."
                )

    # =====================================================
    # Boolean
    # =====================================================

    def _prompt_boolean(
        self,
        label: str,
        required: bool,
    ) -> bool | object:

        while True:

            suffix = (
                ""
                if required
                else " (optional)"
            )

            value = input(
                f"{label}{suffix} (y/n): "
            ).strip().casefold()

            if not value:

                if not required:
                    return _SKIP_FIELD

                print(
                    f"{label} is required."
                )

                continue

            if value in {
                "y",
                "yes",
                "true",
                "1",
            }:

                return True

            if value in {
                "n",
                "no",
                "false",
                "0",
            }:

                return False

            print(
                "Enter y or n."
            )

    # =====================================================
    # List
    # =====================================================

    def _prompt_list(
        self,
        label: str,
        required: bool,
        field_schema: dict[str, Any] | None = None,
    ) -> list[str]:

        while True:

            suffix = (
                ""
                if required
                else " (optional)"
            )

            value = input(
                f"{label}{suffix} "
                "(comma separated): "
            ).strip()

            if not value:

                if required:

                    print(
                        f"{label} is required."
                    )

                    continue

                return []

            values = [
                item.strip()
                for item
                in value.split(",")
                if item.strip()
            ]

            if values:

                if field_schema is not None:

                    type_options = {
                        key: option
                        for key, option
                        in field_schema.items()
                        if key
                        not in {
                            "type",
                            "description",
                            "required",
                        }
                    }

                    registry = TypeRegistry()

                    if not registry.validate(
                        "list",
                        values,
                        **type_options,
                    ):

                        print(
                            f"{label} contains an invalid value."
                        )

                        continue

                return values

            if not required:
                return []

    # =====================================================
    # Object
    # =====================================================

    def _prompt_object(
        self,
        label: str,
        required: bool,
    ) -> dict[str, Any] | object:

        while True:

            suffix = (
                ""
                if required
                else " (optional)"
            )

            value = input(
                f"{label}{suffix} "
                "(YAML mapping): "
            ).strip()

            if not value:

                if not required:
                    return {}

                print(
                    f"{label} is required."
                )

                continue

            try:

                result = yaml.safe_load(
                    value
                )

            except yaml.YAMLError:

                print(
                    f"{label} must be a valid "
                    "YAML mapping."
                )

                continue

            if isinstance(
                result,
                dict,
            ):

                return result

            print(
                f"{label} must be a YAML mapping."
            )

    # =====================================================
    # Entity References
    # =====================================================

    def _prompt_reference(
        self,
        label: str,
        field_schema: dict[str, Any],
        required: bool,
        multiple: bool,
    ) -> str | list[str] | object:

        entity_type = field_schema.get(
            "entity_type"
        )

        while True:

            suffix = (
                ""
                if required
                else " (optional)"
            )

            if multiple:

                prompt = (
                    f"{label}{suffix} "
                    "(comma separated): "
                )

            else:

                prompt = (
                    f"{label}{suffix}: "
                )

            raw_value = input(
                prompt
            ).strip()

            if not raw_value:

                if required:

                    print(
                        f"{label} is required."
                    )

                    continue

                return (
                    []
                    if multiple
                    else _SKIP_FIELD
                )

            if multiple:

                values = [
                    value.strip()
                    for value
                    in raw_value.split(",")
                    if value.strip()
                ]

            else:

                values = [
                    raw_value
                ]

            resolved = []

            unresolved = []

            for value in values:

                entity_id = (
                    self._resolve_reference_value(
                        value,
                        entity_type,
                    )
                )

                if entity_id:

                    resolved.append(
                        entity_id
                    )

                else:

                    unresolved.append(
                        value
                    )

            if unresolved:

                print()

                for value in unresolved:

                    print(
                        f"No {entity_type or 'entity'} "
                        f"found for: {value}"
                    )

                print(
                    "Please enter a valid existing "
                    "entity name, alias, or canonical ID."
                )

                if not required:

                    retry = input(
                        "Try again? (Y/n): "
                    ).strip().casefold()

                    if retry in {
                        "n",
                        "no",
                    }:

                        return (
                            []
                            if multiple
                            else _SKIP_FIELD
                        )

                continue

            for entity_id in resolved:

                print(
                    f"Resolved -> {entity_id}"
                )

            if multiple:
                return resolved

            return resolved[0]

    def _resolve_reference_value(
        self,
        value: str,
        entity_type: str | None,
    ) -> str | None:
        """
        Accept either a canonical ID or a human-readable
        name/alias.
        """

        if self.reference_validator.validate(
            value,
            entity_type,
        ):

            return value

        return self.lookup.resolve(
            value,
            entity_type,
        )

    # =====================================================
    # Template Cleanup
    # =====================================================

    def _clear_template_placeholders(
        self,
        entity: dict[str, Any],
    ) -> None:
        """
        Remove example placeholder values from template
        fields that should begin empty.

        Relationship structure is reconstructed later
        directly from the schema.
        """

        if isinstance(
            entity.get("aliases"),
            list,
        ):

            entity[
                "aliases"
            ] = []

    # =====================================================
    # Preview / Confirmation
    # =====================================================

    def preview(
        self,
        entity: dict[str, Any],
    ) -> bool:

        print()

        print(
            "----------------------------------------"
        )

        print(
            "Entity Preview"
        )

        print(
            "----------------------------------------"
        )

        print()

        print(
            yaml.safe_dump(
                entity,
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False,
            ).rstrip()
        )

        print(
            "----------------------------------------"
        )

        print()

        response = input(
            "Save entity? (Y/n): "
        ).strip().casefold()

        if response in {
            "",
            "y",
            "yes",
        }:

            return True

        print()

        print(
            "Entity creation cancelled."
        )

        return False

    # =====================================================
    # Utility
    # =====================================================

    @staticmethod
    def _field_label(
        field_name: str,
    ) -> str:

        return (
            field_name
            .replace("_", " ")
            .title()
        )


class _SkipField:
    """
    Internal sentinel used when an optional field should
    not be added to the entity.
    """


_SKIP_FIELD = _SkipField()
