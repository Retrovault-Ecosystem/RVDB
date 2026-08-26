"""
=========================================================
RVDB Generic EntityBuilder Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_entity_builder_v2.py

Foundation Release:
    0.2

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from engine.entity_builder import (
    EntityBuilder,
)


def _mock_inputs(
    monkeypatch,
    values,
):

    responses = iter(
        values
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _="": next(
            responses
        ),
    )


def test_build_developer(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Example Developer",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "developer"
    )

    assert entity is not None

    assert (
        entity["id"]
        == "developer.example.developer"
    )

    assert (
        entity["type"]
        == "developer"
    )

    assert (
        entity["name"]
        == "Example Developer"
    )

    assert entity["aliases"] == []

    assert entity["relationships"] == {}


def test_build_manufacturer(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Example Hardware",
            "Japan",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "manufacturer"
    )

    assert entity is not None

    assert (
        entity["id"]
        == "manufacturer.example.hardware"
    )

    assert (
        entity["country"]
        == "Japan"
    )

    assert entity["relationships"] == {}


def test_build_game_with_empty_relationships(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Example Game",
            "1994",
            "",
            "",
            "",
            "",
            "",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "game"
    )

    assert entity is not None

    assert (
        entity["id"]
        == "game.example.game"
    )

    assert (
        entity["release_year"]
        == 1994
    )

    assert entity[
        "relationships"
    ] == {
        "developed_by": [],
        "published_by": [],
        "platform": [],
        "genre": [],
        "core": [],
    }


def test_build_game_with_relationships(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Relationship Test Game",
            "1994",
            "developer.nintendo.ead",
            "publisher.nintendo",
            "platform.nintendo.snes",
            "genre.platformer",
            "core.snes9x",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "game"
    )

    assert entity is not None

    relationships = entity[
        "relationships"
    ]

    assert relationships[
        "developed_by"
    ] == [
        "developer.nintendo.ead"
    ]

    assert relationships[
        "published_by"
    ] == [
        "publisher.nintendo"
    ]

    assert relationships[
        "platform"
    ] == [
        "platform.nintendo.snes"
    ]

    assert relationships[
        "genre"
    ] == [
        "genre.platformer"
    ]

    assert relationships[
        "core"
    ] == [
        "core.snes9x"
    ]


def test_build_platform(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Example Console",
            "Nintendo",
            "",
            "1990",
            "4",
            "console",
            "",
            "cartridge",
            "rom, bin",
            "",
            "",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "platform"
    )

    assert entity is not None

    assert (
        entity["id"]
        == "platform.example.console"
    )

    assert entity[
        "manufacturer"
    ] == [
        "manufacturer.nintendo"
    ]

    assert (
        entity["release_year"]
        == 1990
    )

    assert (
        entity["generation"]
        == 4
    )

    assert entity[
        "category"
    ] == [
        "console"
    ]

    assert entity[
        "media"
    ] == [
        "cartridge"
    ]

    assert entity[
        "extensions"
    ] == [
        "rom",
        "bin",
    ]

    assert entity[
        "relationships"
    ] == {
        "supports_core": [],
    }


def test_build_platform_relationship(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Core Test Console",
            "manufacturer.nintendo",
            "",
            "",
            "",
            "console",
            "",
            "",
            "",
            "",
            "core.snes9x",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "platform"
    )

    assert entity is not None

    assert entity[
        "relationships"
    ][
        "supports_core"
    ] == [
        "core.snes9x"
    ]


def test_build_platform_accepts_canonical_reference(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Canonical Test",
            "manufacturer.sega",
            "",
            "",
            "",
            "console",
            "",
            "",
            "",
            "",
            "",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "platform"
    )

    assert entity is not None

    assert entity[
        "manufacturer"
    ] == [
        "manufacturer.sega"
    ]


def test_build_core_relationship(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Example Core",
            "",
            "",
            "",
            "",
            "",
            "",
            "platform.nintendo.snes",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "core"
    )

    assert entity is not None

    assert entity[
        "relationships"
    ] == {
        "supports": [
            "platform.nintendo.snes"
        ],
    }


def test_build_frontend_relationships(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Example Frontend",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "frontend"
    )

    assert entity is not None

    assert entity[
        "relationships"
    ] == {
        "launches_emulator": [],
        "launches_core": [],
    }


def test_cancel_creation(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Cancelled Developer",
            "n",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "developer"
    )

    assert entity is None


def test_unknown_entity_type():

    builder = EntityBuilder()

    entity = builder.build(
        "does_not_exist"
    )

    assert entity is None


def test_build_platform_rejects_invalid_category(
    monkeypatch,
):

    _mock_inputs(
        monkeypatch,
        [
            "Constraint Test Console",
            "manufacturer.nintendo",
            "",
            "",
            "",
            "toaster",
            "console",
            "",
            "",
            "",
            "",
            "",
            "y",
        ],
    )

    builder = EntityBuilder()

    entity = builder.build(
        "platform"
    )

    assert entity is not None

    assert entity[
        "category"
    ] == [
        "console"
    ]
