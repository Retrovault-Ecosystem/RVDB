"""
=========================================================
RVDB Genesis Plus GX / Master System Compatibility Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B11-E

Purpose:
    Verify the evidence-backed operational compatibility
    claim between the canonical Genesis Plus GX Libretro
    Core and the canonical Sega Master System / Mark III
    Platform family.

    This follows the P2B11 topology checkpoint that first
    demonstrated reuse of one canonical Core across
    multiple canonical Platforms.
=========================================================
"""

from engine.loader import load_entities


CLAIM_ID = (
    "compatibility.core.genesis.plus.gx."
    "platform.sega.master.system"
)

CORE_ID = "core.genesis.plus.gx"

MASTER_ID = "platform.sega.master.system"


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_genesis_plus_gx_master_system_claim_exists():

    entities = entity_map()

    assert CLAIM_ID in entities

    claim = entities[
        CLAIM_ID
    ]

    assert claim.entity_type == "compatibility"


def test_genesis_plus_gx_master_system_subject():

    entities = entity_map()

    claim = entities[
        CLAIM_ID
    ]

    assert claim.get(
        "subject"
    ) == CORE_ID


def test_genesis_plus_gx_master_system_platform():

    entities = entity_map()

    claim = entities[
        CLAIM_ID
    ]

    assert claim.get(
        "platform"
    ) == MASTER_ID


def test_genesis_plus_gx_master_system_is_playable():

    entities = entity_map()

    claim = entities[
        CLAIM_ID
    ]

    assert claim.get(
        "playability"
    ) == "playable"


def test_genesis_plus_gx_master_system_has_evidence():

    entities = entity_map()

    claim = entities[
        CLAIM_ID
    ]

    evidence = claim.get(
        "evidence",
        [],
    )

    assert len(evidence) == 3

    for item in evidence:

        assert item.get(
            "source"
        )

        assert item.get(
            "url"
        )

        assert item.get(
            "checked_at"
        ) == "2026-09-02"

        assert item.get(
            "notes"
        )


def test_genesis_plus_gx_master_system_topology_matches_claim():

    entities = entity_map()

    master = entities[
        MASTER_ID
    ]

    assert master.get(
        "relationships",
        {},
    ).get(
        "supports_core",
        [],
    ) == [
        CORE_ID,
    ]


def test_genesis_plus_gx_master_system_reuses_existing_core():

    entities = entity_map()

    matches = [
        entity
        for entity in entities.values()
        if entity.id == CORE_ID
    ]

    assert len(matches) == 1

    assert matches[
        0
    ].entity_type == "core"


def test_genesis_plus_gx_master_system_does_not_create_emulator():

    entities = entity_map()

    assert (
        "emulator.genesis.plus.gx"
        not in entities
    )
