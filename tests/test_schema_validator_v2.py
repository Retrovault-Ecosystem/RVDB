"""
=========================================================
RVDB SchemaValidator Tests
=========================================================
"""

from validator.schema import (
    SchemaValidator,
)


def test_valid_developer():

    validator = SchemaValidator()

    entity = {
        "id": "developer.test",
        "type": "developer",
        "name": "Test Developer",
        "aliases": [],
    }

    result = validator.validate(
        entity
    )

    assert result.valid
    assert result.errors == []


def test_missing_required_common_field():

    validator = SchemaValidator()

    entity = {
        "type": "developer",
        "name": "Test Developer",
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "Missing required field: id"
        in result.errors
    )


def test_unknown_entity_type():

    validator = SchemaValidator()

    entity = {
        "id": "unknown.test",
        "type": "unknown",
        "name": "Unknown",
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "Unknown entity type: unknown"
        in result.errors
    )


def test_unknown_field():

    validator = SchemaValidator()

    entity = {
        "id": "developer.test",
        "type": "developer",
        "name": "Test Developer",
        "unexpected": "value",
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "Unknown field: unexpected"
        in result.errors
    )


def test_invalid_common_field_type():

    validator = SchemaValidator()

    entity = {
        "id": "developer.test",
        "type": "developer",
        "name": 123,
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "name: Expected string"
        in result.errors
    )


def test_valid_platform_reference():

    validator = SchemaValidator()

    entity = {
        "id": "platform.test",
        "type": "platform",
        "name": "Test Platform",

        "manufacturer": [
            "manufacturer.nintendo"
        ],

        "release_year": None,

        "generation": None,

        "category": [
            "console"
        ],
    }

    result = validator.validate(
        entity
    )

    assert result.valid
    assert result.errors == []


def test_platform_reference_wrong_type():

    validator = SchemaValidator()

    entity = {
        "id": "platform.test",
        "type": "platform",
        "name": "Test Platform",

        "manufacturer": [
            "publisher.nintendo"
        ],

        "release_year": None,

        "generation": None,

        "category": [
            "console"
        ],
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "manufacturer: Expected entity_reference_list"
        in result.errors
    )


def test_integer_or_null_rejects_string():

    validator = SchemaValidator()

    entity = {
        "id": "game.test",
        "type": "game",
        "name": "Test Game",
        "release_year": "1990",
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "release_year: Expected integer_or_null"
        in result.errors
    )
