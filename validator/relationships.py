"""
RVDB Relationship Validator

Validates relationships between RVDB entities.

Relationships are stored from the perspective
of the entity itself.

Example:

game
 |
 └── developed_by
        |
        └── developer
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class RelationshipResult:
    """
    Relationship validation result.
    """

    valid: bool
    errors: list[str]



class RelationshipValidator:
    """
    Validates RVDB entity relationships.
    """


    RELATIONSHIPS = {


        "game": {

            "developed_by": {
                "developer",
            },

            "published_by": {
                "publisher",
            },

            "platform": {
                "platform",
            },

            "genre": {
                "genre",
            },

            "core": {
                "core",
            },

        },


        "platform": {

            "manufacturer": {
                "manufacturer",
            },

            "supports_core": {
                "core",
            },

            "uses_emulator": {
                "emulator",
            },

        },


        "core": {

            "supports_platform": {
                "platform",
            },

        },


        "developer": {

            "develops": {
                "game",
            },

        },


        "publisher": {

            "publishes": {
                "game",
            },

        },


        "manufacturer": {

            "produces": {
                "platform",
                "hardware",
            },

        },

    }



    def validate(
        self,
        source: dict[str, Any],
        relationship: str,
        target: dict[str, Any],
    ) -> RelationshipResult:
        """
        Validate one relationship.
        """


        errors = []


        source_type = source.get(
            "type"
        )

        target_type = target.get(
            "type"
        )


        if not source_type:

            errors.append(
                "Source entity missing type"
            )


        if not target_type:

            errors.append(
                "Target entity missing type"
            )


        allowed_relationships = (
            self.RELATIONSHIPS.get(
                source_type,
                {}
            )
        )


        if relationship not in allowed_relationships:

            errors.append(
                f"Invalid relationship "
                f"'{relationship}' "
                f"for {source_type}"
            )

            return RelationshipResult(
                False,
                errors
            )


        allowed_targets = (
            allowed_relationships[
                relationship
            ]
        )


        if target_type not in allowed_targets:

            errors.append(
                f"{relationship} cannot connect "
                f"{source_type} to {target_type}"
            )


        return RelationshipResult(
            valid=len(errors) == 0,
            errors=errors,
        )
