"""
=========================================================
RVDB Compatibility Entity Template Tests
=========================================================

Project:
    RetroVault Database (RVDB)

Purpose:
    Verify the compatibility creation template contract
    introduced by P2B4-B.26.85.

These tests establish template/create-surface behavior only.
No production compatibility entity is created here.
=========================================================
"""

from pathlib import Path

import yaml

from commands.create import (
    _output_directory,
    get_supported_entity_types,
)
from engine.factory import EntityFactory
from engine.paths import DATA_ROOT


TEMPLATE_PATH = (
    Path("templates")
    / "entities"
    / "compatibility.yaml"
)


def _template():
    with TEMPLATE_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def test_compatibility_template_exists():
    assert TEMPLATE_PATH.is_file()


def test_compatibility_template_is_mapping():
    assert isinstance(
        _template(),
        dict,
    )


def test_compatibility_template_identity_contract():
    template = _template()

    assert (
        template["id"]
        == "compatibility.subject.platform"
    )

    assert (
        template["type"]
        == "compatibility"
    )

    assert (
        template["name"]
        == "Compatibility Claim"
    )


def test_compatibility_template_common_fields():
    template = _template()

    assert template["aliases"] == []
    assert template["relationships"] == {}
    assert template["metadata"] == {}


def test_compatibility_template_required_claim_fields():
    template = _template()

    assert template["subject"] == ""
    assert template["platform"] == ""
    assert template["playability"] == "unknown"


def test_compatibility_template_evidence_contract():
    template = _template()

    assert template["evidence"] == [
        {
            "source": "",
            "url": "",
            "checked_at": "",
        }
    ]


def test_compatibility_template_optional_claim_fields():
    template = _template()

    assert template["version"] == ""
    assert template["notes"] == ""


def test_compatibility_template_exact_field_set():
    template = _template()

    assert set(template) == {
        "id",
        "type",
        "name",
        "aliases",
        "relationships",
        "metadata",
        "subject",
        "platform",
        "playability",
        "evidence",
        "version",
        "notes",
    }


def test_factory_loads_compatibility_template():
    factory = EntityFactory()

    template = factory.load_template(
        "compatibility"
    )

    assert template == _template()


def test_compatibility_becomes_creatable():
    supported = get_supported_entity_types()

    assert "compatibility" in supported


def test_compatibility_output_directory_is_canonical():
    assert (
        _output_directory(
            "compatibility"
        )
        == (
            DATA_ROOT
            / "compatibilities"
        )
    )


def test_template_does_not_create_production_data():
    assert not (
        DATA_ROOT
        / "compatibility"
    ).exists()

    assert not (
        DATA_ROOT
        / "compatibilities"
    ).exists()
