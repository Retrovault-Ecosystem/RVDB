"""
RVDB Schema Validator

Validates entity structures loaded from YAML.

This module validates:
- required fields
- field types
- supported entity types
- unknown fields

Relationship validation is handled separately.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ValidationResult:
    """
    Result returned from validation.
    """

    valid: bool
    errors: list[str]


class SchemaValidator:
    """
    Validates RVDB entities.
    """

    ENTITY_TYPES = {
        "platform",
        "game",
        "manufacturer",
        "developer",
        "publisher",
        "emulator",
        "core",
    }

    SCHEMA = {
        "id": str,
        "type": str,
        "name": str,
    }

    OPTIONAL_FIELDS = {
        "manufacturer": str,
        "release_year": int,
        "generation": int,
        "media": list,
        "extensions": list,
    }

    def validate(
        self,
        entity: dict[str, Any],
    ) -> ValidationResult:
        """
        Validate one entity.
        """

        errors: list[str] = []

        self._validate_required(
            entity,
            errors
        )

        self._validate_types(
            entity,
            errors
        )

        self._validate_entity_type(
            entity,
            errors
        )

        self._validate_unknown_fields(
            entity,
            errors
        )

        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
        )

    def _validate_required(
        self,
        entity: dict[str, Any],
        errors: list[str],
    ) -> None:

        for field in self.SCHEMA:

            if field not in entity:
                errors.append(
                    f"Missing required field: {field}"
                )

    def _validate_types(
        self,
        entity: dict[str, Any],
        errors: list[str],
    ) -> None:

        fields = {
            **self.SCHEMA,
            **self.OPTIONAL_FIELDS,
        }

        for field, expected_type in fields.items():

            if field not in entity:
                continue

            if not isinstance(
                entity[field],
                expected_type
            ):
                errors.append(
                    f"{field} must be "
                    f"{expected_type.__name__}"
                )

    def _validate_entity_type(
        self,
        entity: dict[str, Any],
        errors: list[str],
    ) -> None:

        entity_type = entity.get("type")

        if entity_type not in self.ENTITY_TYPES:
            errors.append(
                f"Unsupported entity type: {entity_type}"
            )

    def _validate_unknown_fields(
        self,
        entity: dict[str, Any],
        errors: list[str],
    ) -> None:

        allowed = {
            *self.SCHEMA.keys(),
            *self.OPTIONAL_FIELDS.keys(),
        }

        for field in entity:

            if field not in allowed:
                errors.append(
                    f"Unknown field: {field}"
                )
