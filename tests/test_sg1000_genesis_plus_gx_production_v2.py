"""
=========================================================
RVDB SG-1000 / Genesis Plus GX Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B13-D

Purpose:
    Verify production reuse of the canonical Genesis Plus
    GX Libretro Core across a fourth canonical Sega Platform.

    Genesis Plus GX already serves Sega Genesis, Sega
    Master System, and Sega Game Gear. P2B13-D extends the
    same Core identity to the canonical Sega SG-1000
    Platform without duplicating the Core, creating an
    Emulator, or prematurely creating a Compatibility
    entity.
=========================================================
"""

from engine.loader import load_entities


SG1000_ID = "platform.sega.sg1000"

GAME_GEAR_ID = "platform.sega.game.gear"
GENESIS_ID = "platform.sega.genesis"
MASTER_ID = "platform.sega.master.system"

CORE_ID = "core.genesis.plus.gx"

FRONTEND_ID = "frontend.retroarch"

SG1000_COMPATIBILITY_ID = (
    "compatibility.core.genesis.plus.gx."
    "platform.sega.sg1000"
)


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_sg1000_platform_exists():

    entities = entity_map()

    assert SG1000_ID in entities

    sg1000 = entities[
        SG1000_ID
    ]

    assert sg1000.entity_type == "platform"
    assert sg1000.name == "Sega SG-1000"


def test_sg1000_supports_genesis_plus_gx():

    entities = entity_map()

    sg1000 = entities[
        SG1000_ID
    ]

    assert sg1000.get(
        "relationships",
        {},
    ).get(
        "supports_core",
        [],
    ) == [
        CORE_ID,
    ]


def test_existing_platforms_still_support_same_core():

    entities = entity_map()

    for platform_id in [
        GAME_GEAR_ID,
        GENESIS_ID,
        MASTER_ID,
    ]:

        platform = entities[
            platform_id
        ]

        assert CORE_ID in platform.get(
            "relationships",
            {},
        ).get(
            "supports_core",
            [],
        )


def test_genesis_plus_gx_is_reused_across_four_platforms():

    entities = entity_map()

    platforms = []

    for entity in entities.values():

        if entity.entity_type != "platform":
            continue

        cores = entity.get(
            "relationships",
            {},
        ).get(
            "supports_core",
            [],
        )

        if isinstance(
            cores,
            str,
        ):
            cores = [
                cores,
            ]

        if CORE_ID in cores:
            platforms.append(
                entity.id
            )

    assert sorted(
        platforms
    ) == [
        GAME_GEAR_ID,
        GENESIS_ID,
        MASTER_ID,
        SG1000_ID,
    ]


def test_genesis_plus_gx_core_is_not_duplicated():

    entities = entity_map()

    matches = [
        entity
        for entity in entities.values()
        if entity.id == CORE_ID
    ]

    assert len(matches) == 1

    core = matches[
        0
    ]

    assert core.entity_type == "core"
    assert core.name == "Genesis Plus GX"


def test_retroarch_launches_reused_core_without_new_edge():

    entities = entity_map()

    retroarch = entities[
        FRONTEND_ID
    ]

    launches = retroarch.get(
        "relationships",
        {},
    ).get(
        "launches_core",
        [],
    )

    assert launches == [
        "core.bsnes",
        "core.snes9x",
        "core.mesen",
        CORE_ID,
    ]


def test_sg1000_compatibility_exists():

    entities = entity_map()

    assert (
        SG1000_COMPATIBILITY_ID
        in entities
    )


def test_sg1000_compatibility_contract():

    entities = entity_map()

    claim = entities[
        SG1000_COMPATIBILITY_ID
    ]

    assert (
        claim.entity_type
        == "compatibility"
    )

    assert (
        claim.name
        == "Genesis Plus GX / Sega SG-1000 Compatibility"
    )

    assert (
        claim.get(
            "subject"
        )
        == CORE_ID
    )

    assert (
        claim.get(
            "platform"
        )
        == SG1000_ID
    )

    assert (
        claim.get(
            "playability"
        )
        == "playable"
    )


def test_sg1000_compatibility_has_three_evidence_records():

    entities = entity_map()

    claim = entities[
        SG1000_COMPATIBILITY_ID
    ]

    evidence = claim.get(
        "evidence",
        [],
    )

    assert len(evidence) == 3

    sources = []
    urls = []

    for record in evidence:

        assert record.get(
            "source"
        )

        assert record.get(
            "url"
        )

        assert (
            record.get(
                "checked_at"
            )
            == "2026-09-02"
        )

        assert record.get(
            "notes"
        )

        sources.append(
            record.get(
                "source"
            )
        )

        urls.append(
            record.get(
                "url"
            )
        )

    assert len(
        set(
            sources
        )
    ) == 3

    assert len(
        set(
            urls
        )
    ) == 3


def test_genesis_plus_gx_standalone_emulator_remains_absent():

    entities = entity_map()

    assert (
        "emulator.genesis.plus.gx"
        not in entities
    )
