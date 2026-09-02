"""
=========================================================
RVDB Mesen Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B9-E — First Production NES Core

Purpose:
    Verify the controlled first production NES core
    topology without introducing speculative emulator or
    compatibility entities.
=========================================================
"""

from engine.loader import load_entities


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_mesen_core_exists():

    entities = entity_map()

    assert "core.mesen" in entities

    mesen = entities["core.mesen"]

    assert mesen.entity_type == "core"
    assert mesen.name == "Mesen"


def test_nes_supports_mesen_core():

    entities = entity_map()

    nes = entities[
        "platform.nintendo.nes"
    ]

    assert nes.get(
        "relationships",
        {},
    )["supports_core"] == [
        "core.mesen",
    ]


def test_retroarch_launches_mesen_core():

    entities = entity_map()

    retroarch = entities[
        "frontend.retroarch"
    ]

    launches = retroarch.get(
        "relationships",
        {},
    )["launches_core"]

    assert "core.mesen" in launches


def test_mesen_population_does_not_create_emulator():

    entities = entity_map()

    assert "emulator.mesen" not in entities
