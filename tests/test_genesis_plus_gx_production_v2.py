"""
=========================================================
RVDB Genesis Plus GX Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B10-D — First Production Genesis Core

Purpose:
    Verify the controlled first production Sega Genesis
    core topology without prematurely introducing a
    compatibility or standalone emulator entity.
=========================================================
"""

from engine.loader import load_entities


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


def test_genesis_plus_gx_compatibility_not_yet_created():

    entities = entity_map()

    assert (
        "compatibility.core.genesis.plus.gx."
        "platform.sega.genesis"
        not in entities
    )


def test_genesis_plus_gx_emulator_not_created():

    entities = entity_map()

    assert "emulator.genesis.plus.gx" not in entities
