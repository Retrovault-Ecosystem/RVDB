"""
RVDB Schema Validator

Validates RVDB entities loaded from YAML.

Supports:
- Entity objects
- dictionaries
- expanded RVDB entity model
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ValidationResult:
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
        "genre",
        "region",
        "controller",
        "bios",
        "shader",
        "overlay",
        "theme",
    }


    REQUIRED_FIELDS = {
        "id",
        "type",
        "name",
    }


    FIELD_TYPES = {

        "id": str,
        "type": str,
        "name": str,

        "manufacturer": (str, list),

        "release_year": int,
        "generation": int,

        "aliases": list,

        "relationships": dict,

        "platform": (str, list),
        "core": (str, list),

        "developer": (str, list),
        "publisher": (str, list),

        "genres": list,
        "regions": list,

        "rom_path": str,

        "category": str,

        "media": list,
        "extensions": list,
    }


    def validate(
        self,
        entity: Any,
    ) -> ValidationResult:

        if hasattr(entity, "data"):
            entity = entity.data


        errors = []


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
            errors=errors
        )


    def _validate_required(
        self,
        entity,
        errors
    ):

        for field in self.REQUIRED_FIELDS:

            if field not in entity:

                errors.append(
                    f"Missing required field: {field}"
                )


    def _validate_types(
        self,
        entity,
        errors
    ):

        for field, expected in self.FIELD_TYPES.items():

            if field not in entity:
                continue


            value = entity[field]


            if not isinstance(
                value,
                expected
            ):

                errors.append(
                    f"{field} has invalid type"
                )


    def _validate_entity_type(
        self,
        entity,
        errors
    ):

        entity_type = entity.get("type")


        if entity_type not in self.ENTITY_TYPES:

            errors.append(
                f"Unsupported entity type: {entity_type}"
            )


    def _validate_unknown_fields(
        self,
        entity,
        errors
    ):

        for field in entity:

            if field not in self.FIELD_TYPES:

                errors.append(
                    f"Unknown field: {field}"
                )
