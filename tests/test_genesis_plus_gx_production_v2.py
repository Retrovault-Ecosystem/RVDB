"""
=========================================================
RVDB Genesis Plus GX Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B10-G — Genesis Plus GX Compatibility

Purpose:
    Verify the controlled production Sega Genesis core
    topology after introducing its evidence-backed
    compatibility claim while continuing to defer any
    standalone emulator entity.
=========================================================
"""

from engine.loader import load_entities


CLAIM_ID = (
    "compatibility.core.genesis.plus.gx."
    "platform.sega.genesis"
)


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_genesis_plus_gx_core_exists():

    entities = entity_map()

    assert "core.genesis.plus.gx" in entities

    core = entities[
        "core.genesis.plus.gx"
    ]

    assert core.entity_type == "core"
    assert core.name == "Genesis Plus GX"


def test_genesis_supports_genesis_plus_gx():

    entities = entity_map()

    genesis = entities[
        "platform.sega.genesis"
    ]

    assert genesis.get(
        "relationships",
        {},
    ).get(
        "supports_core",
        [],
    ) == [
        "core.genesis.plus.gx",
    ]


def test_retroarch_launches_genesis_plus_gx():

    entities = entity_map()

    retroarch = entities[
        "frontend.retroarch"
    ]

    launches = retroarch.get(
        "relationships",
        {},
    ).get(
        "launches_core",
        [],
    )

    assert "core.genesis.plus.gx" in launches


def test_genesis_plus_gx_compatibility_exists():

    entities = entity_map()

    assert CLAIM_ID in entities

    claim = entities[
        CLAIM_ID
    ]

    assert claim.entity_type == "compatibility"


def test_genesis_plus_gx_emulator_not_created():

    entities = entity_map()

    assert "emulator.genesis.plus.gx" not in entities
