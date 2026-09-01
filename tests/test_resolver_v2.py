"""
=========================================================
RVDB Entity Resolver Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_resolver_v2.py

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

from engine.context import (
    get_resolver,
)


def test_resolve_exact_id():

    resolver = get_resolver()

    entity = resolver.resolve(
        "platform.nintendo.snes"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_resolve_exact_name():

    resolver = get_resolver()

    entity = resolver.resolve(
        "Super Nintendo"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_resolve_alias():

    resolver = get_resolver()

    entity = resolver.resolve(
        "SNES"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_resolve_alias_is_case_insensitive():

    resolver = get_resolver()

    entity = resolver.resolve(
        "sNeS"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_resolve_partial_name():

    resolver = get_resolver()

    entity = resolver.resolve(
        "Super Nint"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_resolve_developer_alias():

    resolver = get_resolver()

    entity = resolver.resolve(
        "EAD"
    )

    assert entity is not None

    assert (
        entity.id
        == "developer.nintendo.ead"
    )


def test_resolve_missing_entity():

    resolver = get_resolver()

    entity = resolver.resolve(
        "this entity definitely does not exist"
    )

    assert entity is None


def test_resolver_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    monkeypatch.chdir(
        tmp_path
    )

    resolver = get_resolver()

    entity = resolver.resolve(
        "platform.nintendo.snes"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_partial_name_prefers_canonical_entity_over_compatibility():

    resolver = get_resolver()

    entity = resolver.resolve(
        "Super Nint"
    )

    assert entity is not None

    assert (
        entity.id
        == "platform.nintendo.snes"
    )


def test_compatibility_remains_resolvable_by_exact_id():

    resolver = get_resolver()

    entity = resolver.resolve(
        (
            "compatibility.core.snes9x."
            "platform.nintendo.snes"
        )
    )

    assert entity is not None

    assert (
        entity.id
        == (
            "compatibility.core.snes9x."
            "platform.nintendo.snes"
        )
    )

    assert (
        entity.get("type")
        == "compatibility"
    )


def test_duplicate_exact_name_is_ambiguous():

    from pathlib import Path

    from engine.graph import build_graph
    from engine.loader import Entity
    from engine.resolver import EntityResolver

    entities = [
        Entity(
            source=Path(
                "/tmp/core.bsnes.yaml"
            ),
            data={
                "id": "core.bsnes",
                "type": "core",
                "name": "bsnes",
                "aliases": [],
                "relationships": {},
                "metadata": {},
            },
        ),
        Entity(
            source=Path(
                "/tmp/emulator.bsnes.yaml"
            ),
            data={
                "id": "emulator.bsnes",
                "type": "emulator",
                "name": "bsnes",
                "aliases": [],
                "relationships": {},
                "metadata": {},
            },
        ),
    ]

    resolver = EntityResolver(
        build_graph(
            entities
        )
    )

    assert (
        resolver.resolve(
            "bsnes"
        )
        is None
    )


def test_duplicate_exact_name_ids_remain_resolvable():

    from pathlib import Path

    from engine.graph import build_graph
    from engine.loader import Entity
    from engine.resolver import EntityResolver

    entities = [
        Entity(
            source=Path(
                "/tmp/core.bsnes.yaml"
            ),
            data={
                "id": "core.bsnes",
                "type": "core",
                "name": "bsnes",
                "aliases": [],
                "relationships": {},
                "metadata": {},
            },
        ),
        Entity(
            source=Path(
                "/tmp/emulator.bsnes.yaml"
            ),
            data={
                "id": "emulator.bsnes",
                "type": "emulator",
                "name": "bsnes",
                "aliases": [],
                "relationships": {},
                "metadata": {},
            },
        ),
    ]

    resolver = EntityResolver(
        build_graph(
            entities
        )
    )

    core = resolver.resolve(
        "core.bsnes"
    )

    emulator = resolver.resolve(
        "emulator.bsnes"
    )

    assert core is not None
    assert emulator is not None

    assert core.id == "core.bsnes"

    assert (
        emulator.id
        == "emulator.bsnes"
    )


def test_duplicate_exact_alias_is_ambiguous():

    from pathlib import Path

    from engine.graph import build_graph
    from engine.loader import Entity
    from engine.resolver import EntityResolver

    entities = [
        Entity(
            source=Path(
                "/tmp/manufacturer.yaml"
            ),
            data={
                "id": "manufacturer.example",
                "type": "manufacturer",
                "name": "Example Hardware",
                "aliases": [
                    "Example Company"
                ],
                "relationships": {},
                "metadata": {},
            },
        ),
        Entity(
            source=Path(
                "/tmp/publisher.yaml"
            ),
            data={
                "id": "publisher.example",
                "type": "publisher",
                "name": "Example Software",
                "aliases": [
                    "Example Company"
                ],
                "relationships": {},
                "metadata": {},
            },
        ),
    ]

    resolver = EntityResolver(
        build_graph(
            entities
        )
    )

    assert (
        resolver.resolve(
            "Example Company"
        )
        is None
    )
