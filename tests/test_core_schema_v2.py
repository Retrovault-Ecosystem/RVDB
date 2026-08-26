"""
=========================================================
RVDB Core Schema Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_core_schema_v2.py

Checkpoint:
    P2B4-B.7 — Core Schema Contract

Purpose:
    Verify the P2B4 Core entity schema, its fields, and
    preservation of the existing platform relationship.

=========================================================
"""

from engine.schema_loader import SchemaLoader


def test_core_schema_exists():
    loader = SchemaLoader()

    assert loader.has_schema("core")


def test_core_schema_has_only_common_required_fields():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    assert schema["required"] == [
        "id",
        "type",
        "name",
    ]


def test_core_schema_has_expected_fields():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    fields = schema["fields"]

    assert fields["emulator"]["type"] == (
        "entity_reference_list"
    )

    assert fields["emulator"]["entity_type"] == (
        "emulator"
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

    assert fields["official_website"]["type"] == (
        "string"
    )

    assert fields["source_repository"]["type"] == (
        "string"
    )

    assert fields["documentation"]["type"] == (
        "string"
    )

    assert fields["evidence"]["type"] == "list"


def test_core_evidence_is_string_list():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    evidence = schema["fields"]["evidence"]

    assert evidence["type"] == "list"
    assert evidence["items"]["type"] == "string"


def test_core_schema_has_platform_relationship():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "core"
    )

    relationship = relationships["supports"]

    assert relationship["type"] == (
        "entity_reference_list"
    )

    assert relationship["entity_type"] == (
        "platform"
    )


def test_core_schema_relationships_are_schema_driven():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "core"
    )

    assert set(relationships) == {
        "supports",
    }


def test_core_schema_has_no_unexpected_relationships():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    assert set(
        schema["relationships"].keys()
    ) == {
        "supports",
    }


def test_core_schema_lists_emulator_as_optional_field():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    assert "emulator" in schema["optional"]


def test_core_schema_lists_metadata_fields_as_optional():
    loader = SchemaLoader()

    schema = loader.get_schema("core")

    assert "status" in schema["optional"]
    assert "official_website" in schema["optional"]
    assert "source_repository" in schema["optional"]
    assert "documentation" in schema["optional"]
    assert "evidence" in schema["optional"]


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


def test_core_schema_is_listed_with_entity_types():
    loader = SchemaLoader()

    entity_types = loader.list_entity_types()

    assert "core" in entity_types
    assert "emulator" in entity_types
    assert "platform" in entity_types
    assert "developer" in entity_types
