"""
=========================================================
RVDB Emulator Creation Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_emulator_creation_v2.py

Foundation Release:
    0.2

Checkpoint:
    P2B6-A.1 — Emulator Production Creation Surface

Purpose:
    Verify that Emulator is exposed through RVDB's
    schema/template-driven creation infrastructure without
    creating production Emulator data.

=========================================================
"""

from commands.create import (
    _output_directory,
    get_supported_entity_types,
)
from engine.factory import EntityFactory
from engine.schema_loader import SchemaLoader
from validator.schema import SchemaValidator


TEST_ID = "emulator.test_emulator"
TEST_NAME = "Test Emulator"


def _create_test_emulator():
    factory = EntityFactory()

    return factory.create_entity(
        "emulator",
        TEST_ID,
        TEST_NAME,
    )


def test_emulator_template_exists():
    factory = EntityFactory()

    template = (
        factory.template_directory
        / "emulator.yaml"
    )

    assert template.exists()


def test_emulator_is_supported_creation_type():
    supported = get_supported_entity_types()

    assert "emulator" in supported


def test_emulator_output_directory_is_canonical():
    output = _output_directory(
        "emulator"
    )

    assert output.name == "emulators"


def test_emulator_template_loads():
    factory = EntityFactory()

    template = factory.load_template(
        "emulator"
    )

    assert template["id"] == "emulator.name"
    assert template["type"] == "emulator"
    assert template["name"] == "Emulator Name"
    assert template["aliases"] == []
    assert template["developer"] == []
    assert template["operating_systems"] == []
    assert template["launch_mechanisms"] == []
    assert template["official_website"] == ""
    assert template["source_repository"] == ""
    assert template["status"] == "unknown"

    assert template["relationships"] == {
        "supports_platform": [],
        "supports_core": [],
    }

    assert template["metadata"] == {}


def test_emulator_factory_creates_entity():
    entity = _create_test_emulator()

    assert entity["id"] == TEST_ID
    assert entity["type"] == "emulator"
    assert entity["name"] == TEST_NAME

    assert entity["aliases"] == []
    assert entity["developer"] == []
    assert entity["operating_systems"] == []
    assert entity["launch_mechanisms"] == []
    assert entity["official_website"] == ""
    assert entity["source_repository"] == ""
    assert entity["status"] == "unknown"

    assert entity["relationships"] == {
        "supports_platform": [],
        "supports_core": [],
    }

    assert entity["metadata"] == {}


def test_emulator_template_matches_schema_vocabulary():
    factory = EntityFactory()
    loader = SchemaLoader()

    template = factory.load_template(
        "emulator"
    )

    schema = loader.get_schema(
        "emulator"
    )

    fields = set(
        schema["fields"]
    )

    assert set(template).issubset(
        fields
    )


def test_emulator_template_relationships_match_schema():
    factory = EntityFactory()
    loader = SchemaLoader()

    template = factory.load_template(
        "emulator"
    )

    expected = set(
        loader.get_relationships(
            "emulator"
        )
    )

    actual = set(
        template["relationships"]
    )

    assert actual == expected


def test_factory_created_emulator_validates():
    entity = _create_test_emulator()

    validator = SchemaValidator()

    result = validator.validate(
        entity
    )

    assert result.valid
    assert result.errors == []


def test_emulator_creation_does_not_write_production_data():
    output = _output_directory(
        "emulator"
    )

    assert not (
        output
        / "emulator_test_emulator.yaml"
    ).exists()

    entity = _create_test_emulator()

    assert entity["id"] == TEST_ID

    assert not (
        output
        / "emulator_test_emulator.yaml"
    ).exists()
