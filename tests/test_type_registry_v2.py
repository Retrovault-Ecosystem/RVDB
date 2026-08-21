"""
=========================================================
RVDB TypeRegistry Tests
=========================================================
"""

import pytest

from engine.type_registry import (
    TypeRegistry,
    UnknownTypeError,
)


def test_registered_types():

    registry = TypeRegistry()

    expected = {
        "boolean",
        "entity_reference",
        "entity_reference_list",
        "integer",
        "integer_or_null",
        "list",
        "object",
        "string",
    }

    assert expected.issubset(
        set(
            registry.list_types()
        )
    )


def test_string():

    registry = TypeRegistry()

    assert registry.validate(
        "string",
        "Nintendo",
    )

    assert not registry.validate(
        "string",
        123,
    )


def test_integer():

    registry = TypeRegistry()

    assert registry.validate(
        "integer",
        16,
    )

    assert not registry.validate(
        "integer",
        "16",
    )

    assert not registry.validate(
        "integer",
        True,
    )


def test_integer_or_null():

    registry = TypeRegistry()

    assert registry.validate(
        "integer_or_null",
        1990,
    )

    assert registry.validate(
        "integer_or_null",
        None,
    )

    assert not registry.validate(
        "integer_or_null",
        "1990",
    )


def test_list():

    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [],
    )

    assert registry.validate(
        "list",
        [
            "console"
        ],
    )

    assert not registry.validate(
        "list",
        "console",
    )


def test_object():

    registry = TypeRegistry()

    assert registry.validate(
        "object",
        {},
    )

    assert not registry.validate(
        "object",
        [],
    )


def test_boolean():

    registry = TypeRegistry()

    assert registry.validate(
        "boolean",
        True,
    )

    assert registry.validate(
        "boolean",
        False,
    )

    assert not registry.validate(
        "boolean",
        1,
    )


def test_unknown_type():

    registry = TypeRegistry()

    with pytest.raises(
        UnknownTypeError
    ):

        registry.validate(
            "unknown_type",
            "value",
        )
