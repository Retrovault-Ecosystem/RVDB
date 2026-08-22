"""
=========================================================
RVDB Schema-Driven Relationship Validator Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_relationship_validator_v2.py

Foundation Release:
    0.2

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from validator.relationships import (
    RelationshipValidator,
)


def test_game_developed_by_developer():

    validator = RelationshipValidator()

    source = {
        "type": "game",
    }

    target = {
        "type": "developer",
    }

    result = validator.validate(
        source,
        "developed_by",
        target,
    )

    assert result.valid
    assert result.errors == []


def test_game_published_by_publisher():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "game",
        },
        "published_by",
        {
            "type": "publisher",
        },
    )

    assert result.valid


def test_game_platform_relationship():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "game",
        },
        "platform",
        {
            "type": "platform",
        },
    )

    assert result.valid


def test_platform_supports_core():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "platform",
        },
        "supports_core",
        {
            "type": "core",
        },
    )

    assert result.valid


def test_core_supports_platform():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "core",
        },
        "supports",
        {
            "type": "platform",
        },
    )

    assert result.valid


def test_wrong_target_type_is_rejected():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "game",
        },
        "developed_by",
        {
            "type": "publisher",
        },
    )

    assert not result.valid

    assert (
        "developed_by cannot connect "
        "game to publisher"
        in result.errors
    )


def test_unknown_relationship_is_rejected():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "game",
        },
        "does_not_exist",
        {
            "type": "developer",
        },
    )

    assert not result.valid

    assert (
        "Invalid relationship "
        "'does_not_exist' for game"
        in result.errors
    )


def test_missing_source_type():

    validator = RelationshipValidator()

    result = validator.validate(
        {},
        "developed_by",
        {
            "type": "developer",
        },
    )

    assert not result.valid

    assert (
        "Source entity missing type"
        in result.errors
    )


def test_missing_target_type():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "game",
        },
        "developed_by",
        {},
    )

    assert not result.valid

    assert (
        "Target entity missing type"
        in result.errors
    )


def test_unknown_source_entity_type():

    validator = RelationshipValidator()

    result = validator.validate(
        {
            "type": "does_not_exist",
        },
        "relationship",
        {
            "type": "developer",
        },
    )

    assert not result.valid

    assert (
        "Unknown source entity type: "
        "does_not_exist"
        in result.errors
    )
