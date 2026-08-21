"""
=========================================================
RVDB SchemaLoader Tests
=========================================================
"""

import pytest

from engine.schema_loader import (
    SchemaLoader,
    SchemaNotFoundError,
)


def test_platform_schema_exists():

    loader = SchemaLoader()

    assert loader.has_schema(
        "platform"
    )


def test_active_entity_schemas_exist():

    loader = SchemaLoader()

    expected = {
        "core",
        "developer",
        "game",
        "genre",
        "manufacturer",
        "platform",
        "publisher",
    }

    assert expected.issubset(
        set(
            loader.list_entity_types()
        )
    )


def test_common_fields_are_merged():

    loader = SchemaLoader()

    schema = loader.get_schema(
        "platform"
    )

    fields = schema[
        "fields"
    ]

    assert "id" in fields
    assert "type" in fields
    assert "name" in fields
    assert "aliases" in fields
    assert "relationships" in fields
    assert "metadata" in fields


def test_platform_fields_are_merged():

    loader = SchemaLoader()

    schema = loader.get_schema(
        "platform"
    )

    fields = schema[
        "fields"
    ]

    assert "manufacturer" in fields
    assert "release_year" in fields
    assert "generation" in fields
    assert "category" in fields


def test_platform_manufacturer_type():

    loader = SchemaLoader()

    schema = loader.get_schema(
        "platform"
    )

    manufacturer = (
        schema[
            "fields"
        ][
            "manufacturer"
        ]
    )

    assert (
        manufacturer["type"]
        == "entity_reference_list"
    )

    assert (
        manufacturer["entity_type"]
        == "manufacturer"
    )


def test_unknown_schema_raises():

    loader = SchemaLoader()

    with pytest.raises(
        SchemaNotFoundError
    ):

        loader.get_schema(
            "does_not_exist"
        )


def test_get_schema_returns_copy():

    loader = SchemaLoader()

    schema = loader.get_schema(
        "platform"
    )

    schema[
        "fields"
    ][
        "temporary_test_field"
    ] = {
        "type": "string"
    }

    fresh_schema = loader.get_schema(
        "platform"
    )

    assert (
        "temporary_test_field"
        not in fresh_schema["fields"]
    )
