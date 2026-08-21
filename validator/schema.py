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
    Field-type validation is delegated to TypeRegistry.

    This module intentionally contains no hardcoded
    entity-type list and no hardcoded field definitions.

Foundation Release:
    0.2 — Schema Engine

Checkpoint:
    A — Schema Foundation

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

    def __init__(self) -> None:

        self.loader = SchemaLoader()

        self.types = TypeRegistry()

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
    # Type Validation
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
