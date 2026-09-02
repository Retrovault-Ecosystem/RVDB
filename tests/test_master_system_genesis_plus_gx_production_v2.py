"""
=========================================================
RVDB Master System / Genesis Plus GX Production Tests
=========================================================

Phase:
    2B

Checkpoint:
    P2B11-B

Purpose:
    Verify the first production reuse of one canonical
    Libretro Core across multiple canonical Platforms.

    Genesis Plus GX already serves Sega Genesis.
    P2B11-B extends the same Core identity to the
    canonical Sega Master System platform without
    duplicating the Core, creating an Emulator, or
    prematurely creating a Compatibility entity.
=========================================================
"""

from engine.loader import load_entities


MASTER_ID = "platform.sega.master.system"
GENESIS_ID = "platform.sega.genesis"
CORE_ID = "core.genesis.plus.gx"
FRONTEND_ID = "frontend.retroarch"

MASTER_COMPATIBILITY_ID = (
    "compatibility.core.genesis.plus.gx."
    "platform.sega.master.system"
)


def entity_map():

    return {
        entity.id: entity
        for entity in load_entities()
    }


def test_master_system_platform_exists():

    entities = entity_map()

    assert MASTER_ID in entities

    master = entities[
        MASTER_ID
    ]

    assert master.entity_type == "platform"
    assert master.name == "Sega Master System"


def test_master_system_supports_genesis_plus_gx():

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


def test_genesis_still_supports_same_genesis_plus_gx_core():

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


def test_genesis_plus_gx_is_reused_across_two_platforms():

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
        GENESIS_ID,
        MASTER_ID,
    ]


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


def test_retroarch_launches_reused_core_without_new_frontend_edge():

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


def test_master_system_compatibility_and_emulator_remain_deferred():

    entities = entity_map()

    assert (
        MASTER_COMPATIBILITY_ID
        not in entities
    )

    assert (
        "emulator.genesis.plus.gx"
        not in entities
    )
