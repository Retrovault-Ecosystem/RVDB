"""
=========================================================
RVDB Entity Reference Validator
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/entity_reference.py

Purpose:
    Validates canonical RVDB entity references against
    the centralized EntityRegistry.

    RelationshipLookup is intentionally NOT used here.
    RelationshipLookup resolves human-readable names and
    aliases during interactive entry.

    EntityReferenceValidator validates canonical IDs that
    are already stored in RVDB entity data.

Foundation Release:
    0.2 — Schema Engine

Checkpoint:
    A — Schema Foundation

=========================================================
"""

from __future__ import annotations

from services.registry import EntityRegistry


class EntityReferenceValidator:
    """
    Validates canonical RVDB entity references.
    """

    def __init__(
        self,
        registry: EntityRegistry | None = None,
    ) -> None:

        self.registry = (
            registry
            if registry is not None
            else EntityRegistry()
        )

    # =====================================================
    # Single Reference
    # =====================================================

    def validate(
        self,
        value,
        entity_type=None,
    ) -> bool:
        """
        Validate one canonical entity ID.

        If entity_type is supplied, the referenced entity
        must also match that type.
        """

        if not isinstance(
            value,
            str,
        ):
            return False

        entity = self.registry.get(
            value
        )

        if entity is None:
            return False

        if entity_type is None:
            return True

        return (
            entity.get("type")
            == entity_type
        )

    # =====================================================
    # Reference List
    # =====================================================

    def validate_list(
        self,
        values,
        entity_type=None,
    ) -> bool:
        """
        Validate a list of canonical entity IDs.
        """

        if not isinstance(
            values,
            list,
        ):
            return False

        for value in values:

            if not self.validate(
                value,
                entity_type,
            ):
                return False

        return True
