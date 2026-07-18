"""
RVDB Type Validator

Provides centralized type checking for
schema-driven validation.
"""

from __future__ import annotations


class TypeValidator:
    """
    Validates Python values against
    RVDB schema type definitions.
    """

    def validate(
        self,
        value,
        schema_type: str,
    ) -> bool:

        match schema_type:

            case "string":
                return isinstance(
                    value,
                    str
                )

            case "integer":
                return isinstance(
                    value,
                    int
                )

            case "boolean":
                return isinstance(
                    value,
                    bool
                )

            case "list":
                return isinstance(
                    value,
                    list
                )

            case "object":
                return isinstance(
                    value,
                    dict
                )

            case "integer_or_null":

                return (
                    value is None
                    or isinstance(
                        value,
                        int
                    )
                )

            case "string_or_list":

                return isinstance(
                    value,
                    (
                        str,
                        list,
                    )
                )

            case _:

                raise ValueError(
                    f"Unknown schema type: {schema_type}"
                )
