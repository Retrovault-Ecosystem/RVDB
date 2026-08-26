"""
=========================================================
RVDB Emulator Schema Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_emulator_schema_v2.py

Foundation Release:
    0.2

Checkpoint:
    P2B4-A.3 — Emulator Schema Contract

Purpose:
    Verify the P2B4 Emulator entity schema and its
    relationship definitions without creating production
    Emulator entities.

=========================================================
"""

from engine.schema_loader import SchemaLoader


def test_emulator_schema_exists():
    loader = SchemaLoader()

    assert loader.has_schema("emulator")


def test_emulator_schema_has_expected_fields():
    loader = SchemaLoader()

    schema = loader.get_schema("emulator")

    fields = schema["fields"]

    assert fields["developer"]["type"] == (
        "entity_reference_list"
    )

    assert fields["developer"]["entity_type"] == (
        "developer"
    )

    assert fields["operating_systems"]["type"] == (
        "list"
    )

    assert fields["launch_mechanisms"]["type"] == (
        "list"
    )

    assert fields["official_website"]["type"] == (
        "string"
    )

    assert fields["source_repository"]["type"] == (
        "string"
    )

    assert fields["status"]["type"] == "string"

    assert fields["status"]["enum"] == [
        "active",
        "maintenance",
        "archived",
        "discontinued",
        "experimental",
        "unknown",
    ]


def test_emulator_schema_has_platform_relationship():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "emulator"
    )

    relationship = relationships[
        "supports_platform"
    ]

    assert relationship["type"] == (
        "entity_reference_list"
    )

    assert relationship["entity_type"] == (
        "platform"
    )


def test_emulator_schema_has_core_relationship():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "emulator"
    )

    relationship = relationships[
        "supports_core"
    ]

    assert relationship["type"] == (
        "entity_reference_list"
    )

    assert relationship["entity_type"] == (
        "core"
    )


def test_emulator_schema_relationships_are_schema_driven():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "emulator"
    )

    assert set(relationships) == {
        "supports_platform",
        "supports_core",
    }


def test_emulator_schema_has_only_common_required_fields():
    loader = SchemaLoader()

    schema = loader.get_schema("emulator")

    assert schema["required"] == [
        "id",
        "type",
        "name",
    ]


def test_emulator_schema_resolves_developer_reference():
    loader = SchemaLoader()

    schema = loader.get_schema("emulator")

    developer = schema["fields"]["developer"]

    assert developer["type"] == (
        "entity_reference_list"
    )

    assert developer["entity_type"] == (
        "developer"
    )


def test_existing_platform_schema_remains_compatible():
    loader = SchemaLoader()

    schema = loader.get_schema("platform")

    assert schema["fields"]["manufacturer"][
        "type"
    ] == "entity_reference_list"

    assert schema["fields"]["release_year"][
        "type"
    ] == "integer_or_null"

    assert schema["fields"]["category"][
        "type"
    ] == "list"

    relationships = loader.get_relationships(
        "platform"
    )

    assert relationships["supports_core"][
        "type"
    ] == "entity_reference_list"

    assert relationships["supports_core"][
        "entity_type"
    ] == "core"


def test_existing_core_schema_remains_compatible():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    relationships = loader.get_relationships(
        "core"
    )

    assert relationships["supports"][
        "type"
    ] == "entity_reference_list"

    assert relationships["supports"][
        "entity_type"
    ] == "platform"


def test_emulator_schema_is_listed_with_entity_types():
    loader = SchemaLoader()

    entity_types = loader.list_entity_types()

    assert "emulator" in entity_types
    assert "platform" in entity_types
    assert "core" in entity_types
    assert "developer" in entity_types
