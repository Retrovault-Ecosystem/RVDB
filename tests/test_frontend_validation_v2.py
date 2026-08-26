"""
=========================================================
RVDB Frontend Contract Validation Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_frontend_validation_v2.py

Checkpoint:
    P2B4-B.26.42 — Frontend Contract Validation

Purpose:
    Verify the Frontend fields through the existing
    schema/type validation machinery while enforcing
    the Frontend -> Emulator and Frontend -> Core
    relationship boundaries.

=========================================================
"""

from pathlib import Path

from services.registry import EntityRegistry
from validator.relationships import RelationshipValidator
from validator.schema import SchemaValidator


def _registry():
    registry = EntityRegistry(
        data_path=Path(
            "/tmp/rvdb-frontend-validation-empty"
        )
    )

    registry.register(
        {
            "id": "developer.test",
            "type": "developer",
            "name": "Test Developer",
        }
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
            "id": "core.test",
            "type": "core",
            "name": "Test Core",
        }
    )

    registry.register(
        {
            "id": "platform.test",
            "type": "platform",
            "name": "Test Platform",
        }
    )

    return registry


def _validator():
    return SchemaValidator(
        registry=_registry()
    )


def _valid_frontend():
    return {
        "id": "frontend.test",
        "type": "frontend",
        "name": "Test Frontend",
        "aliases": [],
        "relationships": {
            "launches_emulator": [
                "emulator.test",
            ],
            "launches_core": [
                "core.test",
            ],
        },
        "metadata": {},
        "developer": [
            "developer.test",
        ],
        "operating_systems": [
            "Linux",
            "Windows",
        ],
        "launch_mechanisms": [
            "command line",
        ],
        "official_website": "https://example.com",
        "source_repository": "https://example.com/source",
        "status": "active",
        "evidence": [
            "official documentation",
        ],
    }


def test_valid_frontend_contract():
    validator = _validator()

    result = validator.validate(
        _valid_frontend()
    )

    assert result.valid
    assert result.errors == []


def test_frontend_accepts_valid_developer_reference():
    validator = _validator()

    entity = _valid_frontend()

    entity["developer"] = [
        "developer.test",
    ]

    result = validator.validate(
        entity
    )

    assert result.valid


def test_frontend_rejects_wrong_developer_reference_type():
    validator = _validator()

    entity = _valid_frontend()

    entity["developer"] = [
        "emulator.test",
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_rejects_unknown_developer_reference():
    validator = _validator()

    entity = _valid_frontend()

    entity["developer"] = [
        "developer.does_not_exist",
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_accepts_string_operating_system_list():
    validator = _validator()

    entity = _valid_frontend()

    entity["operating_systems"] = [
        "Linux",
        "Windows",
        "macOS",
    ]

    result = validator.validate(
        entity
    )

    assert result.valid


def test_frontend_rejects_non_string_operating_system():
    validator = _validator()

    entity = _valid_frontend()

    entity["operating_systems"] = [
        "Linux",
        123,
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_accepts_string_launch_mechanisms():
    validator = _validator()

    entity = _valid_frontend()

    entity["launch_mechanisms"] = [
        "command line",
        "desktop launcher",
        "file association",
    ]

    result = validator.validate(
        entity
    )

    assert result.valid


def test_frontend_rejects_non_string_launch_mechanism():
    validator = _validator()

    entity = _valid_frontend()

    entity["launch_mechanisms"] = [
        "command line",
        123,
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_accepts_all_valid_status_values():
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

        entity = _valid_frontend()
        entity["status"] = status

        result = validator.validate(
            entity
        )

        assert result.valid, (
            f"Status should be valid: {status}"
        )


def test_frontend_rejects_invalid_status():
    validator = _validator()

    entity = _valid_frontend()

    entity["status"] = "unsupported-status"

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_accepts_string_evidence_list():
    validator = _validator()

    entity = _valid_frontend()

    entity["evidence"] = [
        "official documentation",
        "official repository",
        "integration documentation",
    ]

    result = validator.validate(
        entity
    )

    assert result.valid


def test_frontend_rejects_non_string_evidence():
    validator = _validator()

    entity = _valid_frontend()

    entity["evidence"] = [
        "official documentation",
        123,
    ]

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_rejects_non_list_evidence():
    validator = _validator()

    entity = _valid_frontend()

    entity["evidence"] = "official documentation"

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_accepts_valid_emulator_relationship():
    validator = RelationshipValidator()

    source = {
        "id": "frontend.test",
        "type": "frontend",
        "name": "Test Frontend",
    }

    target = {
        "id": "emulator.test",
        "type": "emulator",
        "name": "Test Emulator",
    }

    result = validator.validate(
        source,
        "launches_emulator",
        target,
    )

    assert result.valid
    assert result.errors == []


def test_frontend_rejects_wrong_emulator_relationship_target():
    validator = RelationshipValidator()

    source = {
        "id": "frontend.test",
        "type": "frontend",
        "name": "Test Frontend",
    }

    target = {
        "id": "core.test",
        "type": "core",
        "name": "Test Core",
    }

    result = validator.validate(
        source,
        "launches_emulator",
        target,
    )

    assert not result.valid
    assert result.errors == [
        "launches_emulator cannot connect "
        "frontend to core"
    ]


def test_frontend_accepts_valid_core_relationship():
    validator = RelationshipValidator()

    source = {
        "id": "frontend.test",
        "type": "frontend",
        "name": "Test Frontend",
    }

    target = {
        "id": "core.test",
        "type": "core",
        "name": "Test Core",
    }

    result = validator.validate(
        source,
        "launches_core",
        target,
    )

    assert result.valid
    assert result.errors == []


def test_frontend_rejects_wrong_core_relationship_target():
    validator = RelationshipValidator()

    source = {
        "id": "frontend.test",
        "type": "frontend",
        "name": "Test Frontend",
    }

    target = {
        "id": "emulator.test",
        "type": "emulator",
        "name": "Test Emulator",
    }

    result = validator.validate(
        source,
        "launches_core",
        target,
    )

    assert not result.valid
    assert result.errors == [
        "launches_core cannot connect "
        "frontend to emulator"
    ]


def test_frontend_rejects_platform_relationship_target():
    validator = RelationshipValidator()

    source = {
        "id": "frontend.test",
        "type": "frontend",
        "name": "Test Frontend",
    }

    target = {
        "id": "platform.test",
        "type": "platform",
        "name": "Test Platform",
    }

    result = validator.validate(
        source,
        "launches_core",
        target,
    )

    assert not result.valid
    assert result.errors == [
        "launches_core cannot connect "
        "frontend to platform"
    ]


def test_frontend_rejects_unknown_relationship():
    validator = _validator()

    entity = _valid_frontend()

    entity["relationships"] = {
        "does_not_exist": [
            "core.test",
        ],
    }

    result = validator.validate(
        entity
    )

    assert not result.valid


def test_frontend_without_optional_fields_remains_valid():
    validator = _validator()

    entity = {
        "id": "frontend.minimal",
        "type": "frontend",
        "name": "Minimal Frontend",
        "relationships": {},
    }

    result = validator.validate(
        entity
    )

    assert result.valid
    assert result.errors == []
