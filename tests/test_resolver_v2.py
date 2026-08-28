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
