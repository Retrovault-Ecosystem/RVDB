"""
=========================================================
RVDB Frontend Schema Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_frontend_schema_v2.py

Checkpoint:
    P2B4-B.26.34 — Frontend Schema Contract

Purpose:
    Verify the P2B4 Frontend entity schema, its fields,
    relationships, and registration with the existing
    schema loader.

=========================================================
"""

from engine.schema_loader import SchemaLoader


def test_frontend_schema_exists():
    loader = SchemaLoader()

    assert loader.has_schema("frontend")


def test_frontend_schema_has_only_common_required_fields():
    loader = SchemaLoader()

    schema = loader.get_schema("frontend")

    assert schema["required"] == [
        "id",
        "type",
        "name",
    ]


def test_frontend_schema_has_expected_fields():
    loader = SchemaLoader()

    schema = loader.get_schema("frontend")

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

    assert fields["operating_systems"]["items"][
        "type"
    ] == "string"

    assert fields["launch_mechanisms"]["type"] == (
        "list"
    )

    assert fields["launch_mechanisms"]["items"][
        "type"
    ] == "string"

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

    assert fields["evidence"]["type"] == "list"

    assert fields["evidence"]["items"]["type"] == (
        "string"
    )


def test_frontend_schema_lists_metadata_fields_as_optional():
    loader = SchemaLoader()

    schema = loader.get_schema("frontend")

    assert "developer" in schema["optional"]
    assert "operating_systems" in schema["optional"]
    assert "launch_mechanisms" in schema["optional"]
    assert "official_website" in schema["optional"]
    assert "source_repository" in schema["optional"]
    assert "status" in schema["optional"]
    assert "evidence" in schema["optional"]


def test_frontend_schema_has_launches_emulator_relationship():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "frontend"
    )

    relationship = relationships[
        "launches_emulator"
    ]

    assert relationship["type"] == (
        "entity_reference_list"
    )

    assert relationship["entity_type"] == (
        "emulator"
    )


def test_frontend_schema_has_launches_core_relationship():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "frontend"
    )

    relationship = relationships[
        "launches_core"
    ]

    assert relationship["type"] == (
        "entity_reference_list"
    )

    assert relationship["entity_type"] == (
        "core"
    )


def test_frontend_schema_relationships_are_schema_driven():
    loader = SchemaLoader()

    relationships = loader.get_relationships(
        "frontend"
    )

    assert set(relationships) == {
        "launches_emulator",
        "launches_core",
    }


def test_frontend_schema_has_no_platform_relationship():
    loader = SchemaLoader()

    schema = loader.get_schema("frontend")

    assert "supports_platform" not in (
        schema["relationships"]
    )

    assert "platform" not in (
        {
            definition.get("entity_type")
            for definition in schema["relationships"].values()
            if isinstance(definition, dict)
        }
    )


def test_frontend_schema_does_not_define_emulator_as_a_field():
    loader = SchemaLoader()

    schema = loader.get_schema("frontend")

    assert "emulator" not in schema["fields"]


def test_frontend_schema_does_not_define_core_as_a_field():
    loader = SchemaLoader()

    schema = loader.get_schema("frontend")

    assert "core" not in schema["fields"]


def test_frontend_schema_is_listed_with_entity_types():
    loader = SchemaLoader()

    entity_types = loader.list_entity_types()

    assert "frontend" in entity_types
    assert "emulator" in entity_types
    assert "core" in entity_types
    assert "platform" in entity_types
    assert "developer" in entity_types


def test_frontend_schema_preserves_existing_entity_types():
    loader = SchemaLoader()

    entity_types = set(
        loader.list_entity_types()
    )

    expected = {
        "core",
        "developer",
        "emulator",
        "frontend",
        "game",
        "genre",
        "manufacturer",
        "platform",
        "publisher",
    }

    assert expected.issubset(entity_types)
