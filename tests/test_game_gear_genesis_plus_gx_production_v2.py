"""
=========================================================
RVDB Game Gear / Genesis Plus GX Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B12-C

Purpose:
    Verify production reuse of the canonical Genesis Plus
    GX Libretro Core across a third canonical Sega Platform.

    Genesis Plus GX already serves Sega Genesis and Sega
    Master System. P2B12-C extends that same Core identity
    to the canonical Sega Game Gear Platform without
    duplicating the Core, creating an Emulator, or
    prematurely creating a Compatibility entity.
=========================================================
"""

from engine.loader import load_entities


GAME_GEAR_ID = "platform.sega.game.gear"
MASTER_ID = "platform.sega.master.system"
GENESIS_ID = "platform.sega.genesis"

CORE_ID = "core.genesis.plus.gx"

FRONTEND_ID = "frontend.retroarch"

GENESIS_PLUS_GX_ID = "core.genesis.plus.gx"


GAME_GEAR_COMPATIBILITY_ID = (
    "compatibility.core.genesis.plus.gx."
    "platform.sega.game.gear"
)


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_game_gear_platform_exists():

    entities = entity_map()

    assert GAME_GEAR_ID in entities

    game_gear = entities[
        GAME_GEAR_ID
    ]

    assert game_gear.entity_type == "platform"
    assert game_gear.name == "Game Gear"


def test_game_gear_supports_genesis_plus_gx():

    entities = entity_map()

    game_gear = entities[
        GAME_GEAR_ID
    ]

    assert game_gear.get(
        "relationships",
        {},
    ).get(
        "supports_core",
        [],
    ) == [
        CORE_ID,
    ]


def test_genesis_still_supports_same_core():

    entities = entity_map()

    genesis = entities[
        GENESIS_ID
    ]

    assert genesis.get(
        "relationships",
        {},
    ).get(
        "supports_core",
        [],
    ) == [
        CORE_ID,
    ]


def test_master_system_still_supports_same_core():

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


def test_genesis_plus_gx_includes_game_gear_reuse():

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

    assert GAME_GEAR_ID in platforms
    assert GENESIS_ID in platforms
    assert MASTER_ID in platforms


def test_genesis_plus_gx_core_is_not_duplicated():

    entities = entity_map()

    matches = [
        entity
        for entity in entities.values()
        if entity.id == CORE_ID
    ]

    assert len(matches) == 1

    core = matches[0]

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


def test_game_gear_compatibility_exists():

    entities = entity_map()

    assert (
        GAME_GEAR_COMPATIBILITY_ID
        in entities
    )


def test_game_gear_compatibility_contract():

    entities = entity_map()

    claim = entities[
        GAME_GEAR_COMPATIBILITY_ID
    ]

    assert (
        claim.entity_type
        == "compatibility"
    )

    assert (
        claim.name
        == "Genesis Plus GX / Sega Game Gear Compatibility"
    )

    assert (
        claim.get(
            "subject"
        )
        == GENESIS_PLUS_GX_ID
    )

    assert (
        claim.get(
            "platform"
        )
        == GAME_GEAR_ID
    )

    assert (
        claim.get(
            "playability"
        )
        == "playable"
    )


def test_game_gear_compatibility_has_three_evidence_records():

    entities = entity_map()

    claim = entities[
        GAME_GEAR_COMPATIBILITY_ID
    ]

    evidence = claim.get(
        "evidence",
        [],
    )

    assert len(evidence) == 3

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


def test_genesis_plus_gx_standalone_emulator_remains_absent():

    entities = entity_map()

    assert (
        "emulator.genesis.plus.gx"
        not in entities
    )
