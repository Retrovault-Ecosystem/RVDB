"""
=========================================================
RVDB Core Contract Validation Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_core_validation_v2.py

Checkpoint:
    P2B4-B.8 — Core Contract Validation

Purpose:
    Verify the P2B4 Core fields through the existing
    schema/type validation machinery while preserving
    the existing Core -> Platform relationship.

=========================================================
"""

from pathlib import Path

from services.registry import EntityRegistry
from validator.relationships import RelationshipValidator
from validator.schema import SchemaValidator


def _valid_core():
    return {
        "id": "core.test",
        "type": "core",
        "name": "Test Core",
        "aliases": [],
        "relationships": {
            "supports": [
                "platform.nintendo.snes",
            ],
        },
        "metadata": {},
        "emulator": [
            "emulator.test",
        ],
        "status": "active",
        "official_website": "https://example.com",
        "source_repository": "https://example.com/source",
        "documentation": "https://example.com/docs",
        "evidence": [
            "official documentation",
        ],
    }


def _validator():
    registry = EntityRegistry(
        data_path=Path(
            "/tmp/rvdb-core-validation-empty"
        )
    )

    registry.register(
        {
            "id": "emulator.test",
            "type": "emulator",
            "name": "Test Emulator",
        }
    )

    registry.register(
        {
            "id": "platform.nintendo.snes",
            "type": "platform",
            "name": "Super Nintendo Entertainment System",
        }
    )

    registry.register(
        {
            "id": "core.snes9x",
            "type": "core",
            "name": "Snes9x",
        }
    )

    return SchemaValidator(
        registry=registry
    )


def test_valid_core_contract():
    validator = _validator()

    result = validator.validate(
        _valid_core()
    )

    assert result.valid
    assert result.errors == []


def test_core_accepts_valid_emulator_reference():
    validator = _validator()

    entity = _valid_core()

    entity["emulator"] = [
        "emulator.test",
    ]

    result = validator.validate(
        entity
    )

    assert result.valid


def test_core_rejects_invalid_emulator_reference():
    validator = _validator()

    entity = _valid_core()

    entity["emulator"] = [
        "platform.nintendo.snes",
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_core_accepts_all_valid_status_values():
    validator = _validator()

    valid_statuses = [
        "active",
        "maintenance",
        "archived",
        "discontinued",
        "experimental",
        "unknown",
    ]

    for status in valid_statuses:

        entity = _valid_core()
        entity["status"] = status

        result = validator.validate(
            entity
        )

        assert result.valid, (
            f"Status should be valid: {status}"
        )


def test_core_rejects_invalid_status():
    validator = _validator()

    entity = _valid_core()

    entity["status"] = "unsupported-status"

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_core_accepts_string_evidence_list():
    validator = _validator()

    entity = _valid_core()

    entity["evidence"] = [
        "official documentation",
        "official repository",
        "compatibility database",
    ]

    result = validator.validate(
        entity
    )

    assert result.valid


def test_core_rejects_non_string_evidence():
    validator = _validator()

    entity = _valid_core()

    entity["evidence"] = [
        "official documentation",
        123,
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_core_rejects_non_list_evidence():
    validator = _validator()

    entity = _valid_core()

    entity["evidence"] = "official documentation"

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_core_accepts_existing_platform_relationship():
    validator = _validator()

    entity = _valid_core()

    entity["relationships"] = {
        "supports": [
            "platform.nintendo.snes",
        ],
    }

    result = validator.validate(
        entity
    )

    assert result.valid


def test_core_rejects_wrong_platform_relationship_target():
    validator = RelationshipValidator()

    source = {
        "id": "core.test",
        "type": "core",
        "name": "Test Core",
    }

    target = {
        "id": "core.snes9x",
        "type": "core",
        "name": "Snes9x",
    }

    result = validator.validate(
        source,
        "supports",
        target,
    )

    assert not result.valid
    assert result.errors == [
        "supports cannot connect "
        "core to core"
    ]


def test_core_rejects_unknown_relationship():
    validator = _validator()

    entity = _valid_core()

    entity["relationships"] = {
        "does_not_exist": [
            "platform.nintendo.snes",
        ],
    }

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_core_without_optional_fields_remains_valid():
    validator = _validator()

    entity = {
        "id": "core.minimal",
        "type": "core",
        "name": "Minimal Core",
        "relationships": {
            "supports": [
                "platform.nintendo.snes",
            ],
        },
    }

    result = validator.validate(
        entity
    )

    assert result.valid
    assert result.errors == []
