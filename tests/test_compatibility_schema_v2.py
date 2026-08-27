"""
=========================================================
RVDB Compatibility Entity Schema Tests
=========================================================

Project:
    RetroVault Database (RVDB)

Purpose:
    Verify the first-class compatibility entity schema
    introduced by P2B4-B.26.78.

These tests verify schema structure only. Production
compatibility data is intentionally not introduced here.
=========================================================
"""

from engine.schema_loader import SchemaLoader


def _schema():
    return SchemaLoader().get_schema(
        "compatibility"
    )


def test_compatibility_schema_is_registered():
    loader = SchemaLoader()

    assert loader.has_schema(
        "compatibility"
    )

    assert (
        "compatibility"
        in loader.list_entity_types()
    )


def test_compatibility_required_fields():
    schema = _schema()

    assert schema["required"] == [
        "id",
        "type",
        "name",
        "subject",
        "platform",
        "playability",
        "evidence",
    ]


def test_compatibility_optional_fields():
    schema = _schema()

    assert schema["optional"] == [
        "aliases",
        "relationships",
        "metadata",
        "version",
        "notes",
    ]


def test_compatibility_subject_contract():
    field = _schema()["fields"]["subject"]

    assert field["type"] == "entity_reference"

    assert field["entity_types"] == [
        "emulator",
        "core",
    ]

    assert "entity_type" not in field


def test_compatibility_platform_contract():
    field = _schema()["fields"]["platform"]

    assert field["type"] == "entity_reference"
    assert field["entity_type"] == "platform"
    assert "entity_types" not in field


def test_compatibility_playability_contract():
    field = _schema()["fields"]["playability"]

    assert field["type"] == "string"

    assert field["enum"] == [
        "playable",
        "playable_limited",
        "experimental",
        "historical_only",
        "unknown",
    ]


def test_compatibility_evidence_is_nonempty_list():
    field = _schema()["fields"]["evidence"]

    assert field["type"] == "list"
    assert field["min_items"] == 1


def test_compatibility_evidence_item_contract():
    item = (
        _schema()
        ["fields"]
        ["evidence"]
        ["items"]
    )

    assert item["type"] == "object"

    assert item["required"] == [
        "source",
        "url",
        "checked_at",
    ]

    assert item["optional"] == [
        "version",
        "notes",
    ]

    assert set(item["fields"]) == {
        "source",
        "url",
        "checked_at",
        "version",
        "notes",
    }

    for field_name in (
        "source",
        "url",
        "checked_at",
        "version",
        "notes",
    ):
        assert (
            item["fields"][field_name]["type"]
            == "string"
        )


def test_compatibility_version_contract():
    field = _schema()["fields"]["version"]

    assert field["type"] == "string"


def test_compatibility_notes_contract():
    field = _schema()["fields"]["notes"]

    assert field["type"] == "string"


def test_compatibility_has_no_entity_relationship_contract():
    schema = _schema()

    assert schema["relationships"] == {}


def test_compatibility_does_not_add_deferred_fields():
    fields = _schema()["fields"]

    deferred = {
        "confidence",
        "compatibility_state",
        "bios",
        "firmware",
    }

    assert deferred.isdisjoint(fields)
