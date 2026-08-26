"""
=========================================================
RVDB Type Registry
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    engine/type_registry.py

Purpose:
    Centralized validation registry for RVDB schema types.

    SchemaValidator delegates field-type validation here.

Foundation Release:
    0.2 — Schema Engine

Checkpoint:
    A — Schema Foundation

=========================================================
"""

from __future__ import annotations

from typing import Any, Callable

from engine.entity_reference import (
    EntityReferenceValidator,
)


class UnknownTypeError(Exception):
    """
    Raised when a schema requests an unknown field type.
    """


class TypeRegistry:
    """
    Registry of RVDB schema type validators.
    """

    def __init__(
        self,
        reference_validator: EntityReferenceValidator | None = None,
    ) -> None:

        self.reference_validator = (
            reference_validator
            if reference_validator is not None
            else EntityReferenceValidator()
        )

        self._validators: dict[
            str,
            Callable[..., bool],
        ] = {}

        self._register_builtin_types()

    # =====================================================
    # Public API
    # =====================================================

    def register(
        self,
        name: str,
        validator: Callable[..., bool],
    ) -> None:

        self._validators[
            name
        ] = validator

    def unregister(
        self,
        name: str,
    ) -> None:

        self._validators.pop(
            name,
            None,
        )

    def has(
        self,
        name: str,
    ) -> bool:

        return (
            name
            in self._validators
        )

    def list_types(
        self,
    ) -> list[str]:

        return sorted(
            self._validators.keys()
        )

    def validate(
        self,
        type_name: str,
        value: Any,
        **kwargs,
    ) -> bool:

        validator = (
            self._validators.get(
                type_name
            )
        )

        if validator is None:

            raise UnknownTypeError(
                f"Unknown schema type: {type_name}"
            )

        return validator(
            value,
            **kwargs,
        )

    # =====================================================
    # Registration
    # =====================================================

    def _register_builtin_types(
        self,
    ) -> None:

        self.register(
            "string",
            self._string,
        )

        self.register(
            "integer",
            self._integer,
        )

        self.register(
            "integer_or_null",
            self._integer_or_null,
        )

        self.register(
            "list",
            self._list,
        )

        self.register(
            "object",
            self._object,
        )

        self.register(
            "boolean",
            self._boolean,
        )

        self.register(
            "entity_reference",
            self._entity_reference,
        )

        self.register(
            "entity_reference_list",
            self._entity_reference_list,
        )

    # =====================================================
    # Primitive Types
    # =====================================================

    @staticmethod
    def _string(
        value,
        enum=None,
        **_,
    ) -> bool:

        if not isinstance(
            value,
            str,
        ):

            return False

        if (
            enum is not None
            and value not in enum
        ):

            return False

        return True

    @staticmethod
    def _integer(
        value,
        **_,
    ) -> bool:

        return (
            isinstance(
                value,
                int,
            )
            and not isinstance(
                value,
                bool,
            )
        )

    @classmethod
    def _integer_or_null(
        cls,
        value,
        **_,
    ) -> bool:

        return (
            value is None
            or cls._integer(value)
        )

    def _list(
        self,
        value,
        items=None,
        **_,
    ) -> bool:

        if not isinstance(
            value,
            list,
        ):

            return False

        if items is None:

            return True

        if not isinstance(
            items,
            dict,
        ):

            return False

        item_type = items.get(
            "type"
        )

        if not item_type:

            return False

        item_options = {
            key: option
            for key, option
            in items.items()
            if key != "type"
        }

        for item in value:

            if not self.validate(
                item_type,
                item,
                **item_options,
            ):

                return False

        return True

    @staticmethod
    def _object(
        value,
        **_,
    ) -> bool:

        return isinstance(
            value,
            dict,
        )

    @staticmethod
    def _boolean(
        value,
        **_,
    ) -> bool:

        return isinstance(
            value,
            bool,
        )

    # =====================================================
    # RVDB Types
    # =====================================================

    def _entity_reference(
        self,
        value,
        entity_type=None,
        **_,
    ) -> bool:

        return (
            self.reference_validator
            .validate(
                value,
                entity_type,
            )
        )

    def _entity_reference_list(
        self,
        value,
        entity_type=None,
        **_,
    ) -> bool:

        return (
            self.reference_validator
            .validate_list(
                value,
                entity_type,
            )
        )
