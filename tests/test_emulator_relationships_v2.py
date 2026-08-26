"""
=========================================================
RVDB Emulator Relationship Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_emulator_relationships_v2.py

Checkpoint:
    P2B4-A.4 — Emulator Relationship Validation

Purpose:
    Verify Emulator relationships against the schema-driven
    relationship validator.

=========================================================
"""

from validator.relationships import (
    RelationshipValidator,
)


def _emulator():
    return {
        "id": "emulator.test",
        "type": "emulator",
        "name": "Test Emulator",
    }


def _platform():
    return {
        "id": "platform.test",
        "type": "platform",
        "name": "Test Platform",
    }


def _core():
    return {
        "id": "core.test",
        "type": "core",
        "name": "Test Core",
    }


def _game():
    return {
        "id": "game.test",
        "type": "game",
        "name": "Test Game",
    }


def test_emulator_supports_platform():
    validator = RelationshipValidator()

    result = validator.validate(
        _emulator(),
        "supports_platform",
        _platform(),
    )

    assert result.valid
    assert result.errors == []


def test_emulator_supports_core():
    validator = RelationshipValidator()

    result = validator.validate(
        _emulator(),
        "supports_core",
        _core(),
    )

    assert result.valid
    assert result.errors == []


def test_emulator_rejects_invalid_platform_target():
    validator = RelationshipValidator()

    result = validator.validate(
        _emulator(),
        "supports_platform",
        _game(),
    )

    assert not result.valid
    assert result.errors == [
        "supports_platform cannot connect "
        "emulator to game"
    ]


def test_emulator_rejects_invalid_core_target():
    validator = RelationshipValidator()

    result = validator.validate(
        _emulator(),
        "supports_core",
        _platform(),
    )

    assert not result.valid
    assert result.errors == [
        "supports_core cannot connect "
        "emulator to platform"
    ]


def test_emulator_rejects_unknown_relationship():
    validator = RelationshipValidator()

    result = validator.validate(
        _emulator(),
        "does_not_exist",
        _platform(),
    )

    assert not result.valid
    assert result.errors == [
        "Invalid relationship "
        "'does_not_exist' "
        "for emulator"
    ]


def test_existing_platform_core_relationship_remains_valid():
    validator = RelationshipValidator()

    result = validator.validate(
        _platform(),
        "supports_core",
        _core(),
    )

    assert result.valid
    assert result.errors == []


def test_existing_core_platform_relationship_remains_valid():
    validator = RelationshipValidator()

    result = validator.validate(
        _core(),
        "supports",
        _platform(),
    )

    assert result.valid
    assert result.errors == []
