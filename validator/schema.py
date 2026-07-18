"""
RVDB Schema Validator

Schema-driven validation engine.

Loads validation rules from YAML schemas
instead of hardcoded Python dictionaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from validator.loader import SchemaLoader
from validator.types import TypeValidator


@dataclass(slots=True)
class ValidationResult:

    valid: bool
    errors: list[str]


class SchemaValidator:

    def __init__(self):

        self.loader = SchemaLoader()

        self.types = TypeValidator()

    # =====================================================
    # Public Validation
    # =====================================================

    def validate(
        self,
        entity: Any,
    ) -> ValidationResult:

        if hasattr(entity, "data"):

            entity = entity.data

        errors = []

        entity_type = entity.get("type")

        if not entity_type:

            errors.append(
                "Missing required field: type"
            )

            return ValidationResult(
                False,
                errors
            )

        common = (
            self.loader.common_schema
            .get("entity", {})
        )

        typed = (
            self.loader.get_entity_schema(
                entity_type
            )
        )

        self.validate_required(
            entity,
            common,
            typed,
            errors
        )

        self.validate_fields(
            entity,
            common,
            typed,
            errors
        )

        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors
        )

    # =====================================================
    # Required Fields
    # =====================================================

    def validate_required(
        self,
        entity,
        common,
        typed,
        errors,
    ):

        required = set(
            common.get(
                "required",
                []
            )
        )

        required.update(
            typed.get(
                "required",
                []
            )
        )

        for field in sorted(required):

            if field not in entity:

                errors.append(
                    f"Missing required field: {field}"
                )

    # =====================================================
    # Field Validation
    # =====================================================

    def validate_fields(
        self,
        entity,
        common,
        typed,
        errors,
    ):

        fields = {}

        fields.update(
            common.get(
                "fields",
                {}
            )
        )

        fields.update(
            typed.get(
                "fields",
                {}
            )
        )

        allowed = set(fields.keys())

        allowed.update(
            {
                "id",
                "type",
                "name",
            }
        )

        for field, value in entity.items():

            if field not in allowed:

                errors.append(
                    f"Unknown field: {field}"
                )

                continue

            definition = fields.get(field)

            if not definition:

                continue

            schema_type = definition.get("type")

            if not schema_type:

                continue

            if not self.types.validate(
                value,
                schema_type
            ):

                errors.append(
                    f"{field} has invalid type"
                )
