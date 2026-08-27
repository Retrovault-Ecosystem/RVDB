"""
=========================================================
RVDB Schema Validator
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    validator/schema.py

Purpose:
    Schema-driven validation of RVDB entities.

    Entity structure is obtained from SchemaLoader.
    Ordinary field-type validation is delegated to
    TypeRegistry.

    Relationship containers are additionally validated
    against schema-defined relationship vocabulary and
    cardinality.

    Relationship target existence and source/target type
    compatibility remain the responsibility of the
    relationship-validation layer.

Foundation Release:
    0.2 — Schema Engine

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from engine.schema_loader import (
    SchemaLoader,
    SchemaNotFoundError,
)

from engine.type_registry import (
    TypeRegistry,
    UnknownTypeError,
)

from engine.entity_reference import (
    EntityReferenceValidator,
)


@dataclass(slots=True)
class ValidationResult:
    """
    Result returned by SchemaValidator.
    """

    valid: bool
    errors: list[str]


class SchemaValidator:
    """
    Validate RVDB entities against resolved YAML schemas.
    """

    def __init__(
        self,
        registry=None,
    ) -> None:

        self.loader = SchemaLoader()

        reference_validator = (
            EntityReferenceValidator(registry)
            if registry is not None
            else None
        )

        self.types = TypeRegistry(
            reference_validator=reference_validator,
        )

    # =====================================================
    # Public API
    # =====================================================

    def validate(
        self,
        entity: Any,
    ) -> ValidationResult:

        if hasattr(
            entity,
            "data",
        ):

            entity = entity.data

        errors: list[str] = []

        if not isinstance(
            entity,
            dict,
        ):

            return ValidationResult(
                valid=False,
                errors=[
                    "Entity must be a mapping"
                ],
            )

        entity_type = entity.get(
            "type"
        )

        if not entity_type:

            return ValidationResult(
                valid=False,
                errors=[
                    "Missing required field: type"
                ],
            )

        try:

            schema = self.loader.get_schema(
                entity_type
            )

        except SchemaNotFoundError:

            return ValidationResult(
                valid=False,
                errors=[
                    (
                        "Unknown entity type: "
                        f"{entity_type}"
                    )
                ],
            )

        self._validate_required(
            entity,
            schema,
            errors,
        )

        self._validate_unknown_fields(
            entity,
            schema,
            errors,
        )

        self._validate_types(
            entity,
            schema,
            errors,
        )

        self._validate_relationships(
            entity,
            schema,
            errors,
        )

        return ValidationResult(
            valid=(
                len(errors) == 0
            ),
            errors=errors,
        )

    # =====================================================
    # Required Fields
    # =====================================================

    def _validate_required(
        self,
        entity,
        schema,
        errors,
    ) -> None:

        required = schema.get(
            "required",
            [],
        )

        for field in required:

            if field not in entity:

                errors.append(
                    (
                        "Missing required field: "
                        f"{field}"
                    )
                )

    # =====================================================
    # Unknown Fields
    # =====================================================

    def _validate_unknown_fields(
        self,
        entity,
        schema,
        errors,
    ) -> None:

        fields = schema.get(
            "fields",
            {},
        )

        allowed = set(
            fields.keys()
        )

        for field in entity:

            if field not in allowed:

                errors.append(
                    (
                        "Unknown field: "
                        f"{field}"
                    )
                )

    # =====================================================
    # Ordinary Field Type Validation
    # =====================================================

    def _validate_types(
        self,
        entity,
        schema,
        errors,
    ) -> None:

        fields = schema.get(
            "fields",
            {},
        )

        for (
            field_name,
            field_schema,
        ) in fields.items():

            if field_name not in entity:
                continue

            if not isinstance(
                field_schema,
                dict,
            ):

                errors.append(
                    (
                        f"{field_name}: "
                        "Invalid schema definition"
                    )
                )

                continue

            expected_type = (
                field_schema.get(
                    "type"
                )
            )

            if not expected_type:

                errors.append(
                    (
                        f"{field_name}: "
                        "Schema type is missing"
                    )
                )

                continue

            type_options = {
                key: value
                for key, value
                in field_schema.items()
                if key
                not in {
                    "type",
                    "description",
                    "required",
                }
            }

            if isinstance(
                type_options.get("items"),
                dict,
            ):
                type_options.pop(
                    "items"
                )

            try:

                valid = (
                    self.types.validate(
                        expected_type,
                        entity[
                            field_name
                        ],
                        **type_options,
                    )
                )

            except UnknownTypeError:

                errors.append(
                    (
                        f"{field_name}: "
                        "Unknown schema type "
                        f"'{expected_type}'"
                    )
                )

                continue

            if not valid:

                errors.append(
                    (
                        f"{field_name}: "
                        f"Expected {expected_type}"
                    )
                )

                continue

            self._validate_structured_value(
                entity[field_name],
                field_schema,
                field_name,
                errors,
            )

    # =====================================================
    # Structured Field Validation
    # =====================================================

    def _validate_structured_value(
        self,
        value: Any,
        definition: dict[str, Any],
        path: str,
        errors: list[str],
    ) -> None:
        """
        Recursively validate opt-in list/object structure.

        Primitive type validity is still owned by
        TypeRegistry. This layer adds structural contracts
        and deterministic nested error paths.
        """

        value_type = definition.get(
            "type"
        )

        if value_type == "list":

            items = definition.get(
                "items"
            )

            if (
                not isinstance(value, list)
                or not isinstance(items, dict)
            ):
                return

            for index, item in enumerate(value):

                item_path = (
                    f"{path}[{index}]"
                )

                self._validate_nested_definition(
                    item,
                    items,
                    item_path,
                    errors,
                )

            return

        if value_type == "object":

            if not isinstance(value, dict):
                return

            if "fields" not in definition:
                return

            self._validate_object_contract(
                value,
                definition,
                path,
                errors,
            )

    def _validate_nested_definition(
        self,
        value: Any,
        definition: dict[str, Any],
        path: str,
        errors: list[str],
    ) -> None:

        expected_type = definition.get(
            "type"
        )

        if not expected_type:
            return

        type_options = {
            key: option
            for key, option
            in definition.items()
            if key
            not in {
                "type",
                "description",
                "required",
                "optional",
                "fields",
                "items",
            }
        }

        try:

            valid = self.types.validate(
                expected_type,
                value,
                **type_options,
            )

        except UnknownTypeError:

            errors.append(
                (
                    f"{path}: "
                    "Unknown schema type "
                    f"'{expected_type}'"
                )
            )

            return

        if not valid:

            errors.append(
                (
                    f"{path}: "
                    f"Expected {expected_type}"
                )
            )

            return

        self._validate_structured_value(
            value,
            definition,
            path,
            errors,
        )

    def _validate_object_contract(
        self,
        value: dict[str, Any],
        definition: dict[str, Any],
        path: str,
        errors: list[str],
    ) -> None:

        fields = definition.get(
            "fields",
            {},
        )

        required = definition.get(
            "required",
            [],
        )

        for field_name in required:

            if field_name not in value:

                errors.append(
                    (
                        f"{path}.{field_name}: "
                        "Missing required field"
                    )
                )

        allowed = set(
            fields.keys()
        )

        for field_name in value:

            if field_name not in allowed:

                errors.append(
                    (
                        f"{path}.{field_name}: "
                        "Unknown field"
                    )
                )

        for (
            field_name,
            field_definition,
        ) in fields.items():

            if field_name not in value:
                continue

            self._validate_nested_definition(
                value[field_name],
                field_definition,
                f"{path}.{field_name}",
                errors,
            )

    # =====================================================
    # Relationship Container Validation
    # =====================================================

    def _validate_relationships(
        self,
        entity: dict[str, Any],
        schema: dict[str, Any],
        errors: list[str],
    ) -> None:
        """
        Validate the structure of an entity's relationships.

        This layer checks:

        - relationships is a mapping
        - relationship names are declared by the schema
        - relationship values match declared cardinality
        - stored references are non-empty strings

        It does NOT check whether target entities exist.
        It does NOT check source/target type compatibility.

        Those checks belong to RelationshipValidator and
        the graph-validation workflow.
        """

        if "relationships" not in entity:
            return

        relationships = entity.get(
            "relationships"
        )

        # TypeRegistry already reports:
        #
        #     relationships: Expected object
        #
        # Avoid producing a duplicate error here.

        if not isinstance(
            relationships,
            dict,
        ):

            return

        definitions = schema.get(
            "relationships",
            {},
        )

        if not isinstance(
            definitions,
            dict,
        ):

            return

        for (
            relationship_name,
            value,
        ) in relationships.items():

            definition = definitions.get(
                relationship_name
            )

            if definition is None:

                errors.append(
                    (
                        "relationships."
                        f"{relationship_name}: "
                        "Unknown relationship"
                    )
                )

                continue

            if not isinstance(
                definition,
                dict,
            ):

                errors.append(
                    (
                        "relationships."
                        f"{relationship_name}: "
                        "Invalid relationship schema"
                    )
                )

                continue

            expected_type = definition.get(
                "type"
            )

            if (
                expected_type
                == "entity_reference_list"
            ):

                self._validate_relationship_list(
                    relationship_name,
                    value,
                    errors,
                )

                continue

            if (
                expected_type
                == "entity_reference"
            ):

                self._validate_relationship_reference(
                    relationship_name,
                    value,
                    errors,
                )

                continue

            # Normally unreachable because SchemaLoader
            # validates relationship schema types first.

            errors.append(
                (
                    "relationships."
                    f"{relationship_name}: "
                    "Unsupported relationship type "
                    f"'{expected_type}'"
                )
            )

    # =====================================================
    # Relationship List
    # =====================================================

    def _validate_relationship_list(
        self,
        relationship_name: str,
        value: Any,
        errors: list[str],
    ) -> None:

        prefix = (
            "relationships."
            f"{relationship_name}"
        )

        if not isinstance(
            value,
            list,
        ):

            errors.append(
                (
                    f"{prefix}: "
                    "Expected entity_reference_list"
                )
            )

            return

        for (
            index,
            reference,
        ) in enumerate(
            value
        ):

            if (
                not isinstance(
                    reference,
                    str,
                )
                or not reference.strip()
            ):

                errors.append(
                    (
                        f"{prefix}[{index}]: "
                        "Expected non-empty "
                        "entity reference string"
                    )
                )

    # =====================================================
    # Single Relationship Reference
    # =====================================================

    def _validate_relationship_reference(
        self,
        relationship_name: str,
        value: Any,
        errors: list[str],
    ) -> None:

        prefix = (
            "relationships."
            f"{relationship_name}"
        )

        if (
            not isinstance(
                value,
                str,
            )
            or not value.strip()
        ):

            errors.append(
                (
                    f"{prefix}: "
                    "Expected non-empty "
                    "entity reference string"
                )
            )
