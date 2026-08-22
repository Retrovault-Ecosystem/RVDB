"""
=========================================================
RVDB Relationship Data Validation Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_relationship_data_validation_v2.py

Foundation Release:
    0.2

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from validator.schema import (
    SchemaValidator,
)


def _game_entity(
    relationships,
):

    return {
        "id": "game.test",
        "type": "game",
        "name": "Test Game",
        "aliases": [],
        "relationships": relationships,
        "metadata": {},
    }


def test_valid_relationship_lists():

    validator = SchemaValidator()

    entity = _game_entity(
        {
            "developed_by": [
                "developer.nintendo.ead",
            ],
            "published_by": [
                "publisher.nintendo",
            ],
            "platform": [
                "platform.nintendo.snes",
            ],
            "genre": [
                "genre.platformer",
            ],
            "core": [
                "core.snes9x",
            ],
        }
    )

    result = validator.validate(
        entity
    )

    assert result.valid


def test_empty_relationship_lists_are_valid():

    validator = SchemaValidator()

    entity = _game_entity(
        {
            "developed_by": [],
            "published_by": [],
            "platform": [],
            "genre": [],
            "core": [],
        }
    )

    result = validator.validate(
        entity
    )

    assert result.valid


def test_unknown_relationship_is_rejected():

    validator = SchemaValidator()

    entity = _game_entity(
        {
            "does_not_exist": [],
        }
    )

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "relationships.does_not_exist: "
        "Unknown relationship"
        in result.errors
    )


def test_relationships_must_be_mapping():

    validator = SchemaValidator()

    entity = {
        "id": "game.test",
        "type": "game",
        "name": "Test Game",
        "aliases": [],
        "relationships": [
            "developed_by",
        ],
        "metadata": {},
    }

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "relationships: Expected object"
        in result.errors
    )


def test_reference_list_rejects_scalar():

    validator = SchemaValidator()

    entity = _game_entity(
        {
            "developed_by":
                "developer.nintendo.ead",
        }
    )

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "relationships.developed_by: "
        "Expected entity_reference_list"
        in result.errors
    )


def test_reference_list_rejects_non_string_item():

    validator = SchemaValidator()

    entity = _game_entity(
        {
            "developed_by": [
                {
                    "id":
                        "developer.nintendo.ead"
                },
            ],
        }
    )

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "relationships.developed_by[0]: "
        "Expected non-empty entity reference string"
        in result.errors
    )


def test_reference_list_rejects_empty_string():

    validator = SchemaValidator()

    entity = _game_entity(
        {
            "developed_by": [
                "",
            ],
        }
    )

    result = validator.validate(
        entity
    )

    assert not result.valid

    assert (
        "relationships.developed_by[0]: "
        "Expected non-empty entity reference string"
        in result.errors
    )
