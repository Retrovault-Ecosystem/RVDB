"""
RVDB Relationship Validator

Validates relationships between RVDB entities.

Relationships are directional:

source entity
      |
      relationship
      |
target entity
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
    Validates entity relationships.
    """

    RELATIONSHIPS = {
        "manufacturer": {
            "produces": {
                "platform",
                "hardware",
            }
        },

        "developer": {
            "develops": {
                "game",
            }
        },

        "publisher": {
            "publishes": {
                "game",
            }
        },

        "platform": {
            "uses_emulator": {
                "emulator",
            },

            "uses_core": {
                "core",
            },
        },

        "game": {
            "belongs_to": {
                "platform",
            }
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

        errors: list[str] = []

        source_type = source.get("type")
        target_type = target.get("type")

        if not source_type:
            errors.append(
                "Source entity missing type"
            )

        if not target_type:
            errors.append(
                "Target entity missing type"
            )

        if relationship not in self.RELATIONSHIPS.get(
            source_type,
            {}
        ):
            errors.append(
                f"Invalid relationship '{relationship}' "
                f"for {source_type}"
            )

            return RelationshipResult(
                False,
                errors
            )

        allowed_targets = (
            self.RELATIONSHIPS
            [source_type]
            [relationship]
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
