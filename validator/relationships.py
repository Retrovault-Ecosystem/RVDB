"""
=========================================================
RVDB Relationship Validator
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    validator/relationships.py

Purpose:
    Validates relationships between RVDB entities using
    relationship definitions supplied by SchemaLoader.

    Relationship rules are no longer hardcoded in Python.

Foundation Release:
    0.2

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


@dataclass(slots=True)
class RelationshipResult:
    """
    Relationship validation result.
    """

    valid: bool
    errors: list[str]


class RelationshipValidator:
    """
    Validate one relationship edge using entity schemas.
    """

    def __init__(
        self,
        schema_loader: SchemaLoader | None = None,
    ) -> None:

        self.schemas = (
            schema_loader
            if schema_loader is not None
            else SchemaLoader()
        )

    # =====================================================
    # Validate
    # =====================================================

    def validate(
        self,
        source: Any,
        relationship: str,
        target: Any,
    ) -> RelationshipResult:
        """
        Validate one relationship between two entities.
        """

        errors: list[str] = []

        source_type = self._get(
            source,
            "type",
        )

        target_type = self._get(
            target,
            "type",
        )

        if not source_type:

            errors.append(
                "Source entity missing type"
            )

        if not target_type:

            errors.append(
                "Target entity missing type"
            )

        if errors:

            return RelationshipResult(
                valid=False,
                errors=errors,
            )

        try:

            relationships = (
                self.schemas.get_relationships(
                    source_type
                )
            )

        except SchemaNotFoundError:

            return RelationshipResult(
                valid=False,
                errors=[
                    (
                        "Unknown source entity type: "
                        f"{source_type}"
                    )
                ],
            )

        definition = relationships.get(
            relationship
        )

        if definition is None:

            return RelationshipResult(
                valid=False,
                errors=[
                    (
                        "Invalid relationship "
                        f"'{relationship}' "
                        f"for {source_type}"
                    )
                ],
            )

        if not isinstance(
            definition,
            dict,
        ):

            return RelationshipResult(
                valid=False,
                errors=[
                    (
                        "Invalid relationship schema "
                        f"for '{relationship}'"
                    )
                ],
            )

        allowed_targets = (
            self._allowed_target_types(
                definition
            )
        )

        if not allowed_targets:

            return RelationshipResult(
                valid=False,
                errors=[
                    (
                        "Relationship "
                        f"'{relationship}' "
                        "does not define a target "
                        "entity type"
                    )
                ],
            )

        if target_type not in allowed_targets:

            return RelationshipResult(
                valid=False,
                errors=[
                    (
                        f"{relationship} cannot connect "
                        f"{source_type} to {target_type}"
                    )
                ],
            )

        return RelationshipResult(
            valid=True,
            errors=[],
        )

    # =====================================================
    # Target Types
    # =====================================================

    @staticmethod
    def _allowed_target_types(
        definition: dict[str, Any],
    ) -> set[str]:
        """
        Support either:

            entity_type: developer

        or future multi-target definitions:

            entity_types:
              - platform
              - hardware
        """

        allowed: set[str] = set()

        entity_type = definition.get(
            "entity_type"
        )

        if isinstance(
            entity_type,
            str,
        ):

            allowed.add(
                entity_type
            )

        entity_types = definition.get(
            "entity_types"
        )

        if isinstance(
            entity_types,
            list,
        ):

            for value in entity_types:

                if isinstance(
                    value,
                    str,
                ):

                    allowed.add(
                        value
                    )

        return allowed

    # =====================================================
    # Entity Access
    # =====================================================

    @staticmethod
    def _get(
        entity: Any,
        key: str,
    ) -> Any:
        """
        Support both dictionaries and engine.loader.Entity.
        """

        if hasattr(
            entity,
            "get",
        ):

            return entity.get(
                key
            )

        return None
