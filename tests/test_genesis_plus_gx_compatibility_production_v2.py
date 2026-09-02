"""
=========================================================
RVDB Genesis Plus GX / Genesis Compatibility Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B10-G

Purpose:
    Verify the evidence-backed operational compatibility
    claim for the Genesis Plus GX Libretro core and the
    canonical Sega Genesis platform.
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


def test_genesis_plus_gx_genesis_claim_exists():

    entities = entity_map()

    assert CLAIM_ID in entities

    claim = entities[
        CLAIM_ID
    ]

    assert claim.entity_type == "compatibility"


def test_genesis_plus_gx_genesis_subject():

    claim = entity_map()[
        CLAIM_ID
    ]

    assert claim.get(
        "subject"
    ) == "core.genesis.plus.gx"


def test_genesis_plus_gx_genesis_platform():

    claim = entity_map()[
        CLAIM_ID
    ]

    assert claim.get(
        "platform"
    ) == "platform.sega.genesis"


def test_genesis_plus_gx_genesis_is_playable():

    claim = entity_map()[
        CLAIM_ID
    ]

    assert claim.get(
        "playability"
    ) == "playable"


def test_genesis_plus_gx_genesis_has_evidence():

    claim = entity_map()[
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
        )


def test_genesis_plus_gx_genesis_topology_remains_consistent():

    entities = entity_map()

    genesis = entities[
        "platform.sega.genesis"
    ]

    retroarch = entities[
        "frontend.retroarch"
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

    assert (
        "core.genesis.plus.gx"
        in retroarch.get(
            "relationships",
            {},
        ).get(
            "launches_core",
            [],
        )
    )


def test_genesis_plus_gx_emulator_remains_unmodeled():

    entities = entity_map()

    assert (
        "emulator.genesis.plus.gx"
        not in entities
    )
