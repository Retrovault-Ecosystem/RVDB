"""
=========================================================
RVDB Mesen / NES Compatibility Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B9-H

Purpose:
    Verify the first evidence-backed compatibility claim
    for the Mesen Libretro core and canonical NES platform.
=========================================================
"""

from engine.loader import load_entities


CLAIM_ID = (
    "compatibility.core.mesen."
    "platform.nintendo.nes"
)


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_mesen_nes_compatibility_claim_exists():

    entities = entity_map()

    assert CLAIM_ID in entities

    claim = entities[CLAIM_ID]

    assert claim.entity_type == "compatibility"


def test_mesen_nes_compatibility_subject():

    claim = entity_map()[CLAIM_ID]

    assert claim.get(
        "subject"
    ) == "core.mesen"


def test_mesen_nes_compatibility_platform():

    claim = entity_map()[CLAIM_ID]

    assert claim.get(
        "platform"
    ) == "platform.nintendo.nes"


def test_mesen_nes_compatibility_is_playable():

    claim = entity_map()[CLAIM_ID]

    assert claim.get(
        "playability"
    ) == "playable"


def test_mesen_nes_compatibility_has_evidence():

    claim = entity_map()[CLAIM_ID]

    evidence = claim.get(
        "evidence",
        [],
    )

    assert len(evidence) == 3

    for item in evidence:
        assert item.get("source")
        assert item.get("url")
        assert item.get("checked_at")


def test_mesen_nes_topology_remains_consistent():

    entities = entity_map()

    nes = entities[
        "platform.nintendo.nes"
    ]

    retroarch = entities[
        "frontend.retroarch"
    ]

    assert nes.get(
        "relationships",
        {},
    ).get(
        "supports_core",
        [],
    ) == [
        "core.mesen",
    ]

    assert "core.mesen" in retroarch.get(
        "relationships",
        {},
    ).get(
        "launches_core",
        [],
    )


def test_mesen_emulator_remains_unmodeled():

    entities = entity_map()

    assert "emulator.mesen" not in entities
