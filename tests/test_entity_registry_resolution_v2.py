"""
=========================================================
RVDB EntityRegistry Resolution Tests
=========================================================

Checkpoint:
    P2B8-B.3 — EntityRegistry Ambiguous Term Hardening
=========================================================
"""

from pathlib import Path

import yaml

from services.registry import EntityRegistry


def _write_entity(
    root,
    relative_path,
    entity,
):

    path = root / relative_path

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:

        yaml.safe_dump(
            entity,
            file,
            sort_keys=False,
        )


def test_registry_duplicate_exact_name_is_ambiguous(
    tmp_path,
):

    data_root = (
        tmp_path
        / "data"
    )

    _write_entity(
        data_root,
        Path("cores/bsnes.yaml"),
        {
            "id": "core.bsnes",
            "type": "core",
            "name": "bsnes",
            "aliases": [],
        },
    )

    _write_entity(
        data_root,
        Path("emulators/bsnes.yaml"),
        {
            "id": "emulator.bsnes",
            "type": "emulator",
            "name": "bsnes",
            "aliases": [],
        },
    )

    registry = EntityRegistry(
        data_root
    )

    assert (
        registry.resolve(
            "bsnes"
        )
        is None
    )

    assert registry.by_name[
        "bsnes"
    ] == [
        "core.bsnes",
        "emulator.bsnes",
    ]


def test_registry_unique_exact_name_resolves(
    tmp_path,
):

    data_root = (
        tmp_path
        / "data"
    )

    _write_entity(
        data_root,
        Path("platforms/snes.yaml"),
        {
            "id": "platform.nintendo.snes",
            "type": "platform",
            "name": "Super Nintendo",
            "aliases": [],
        },
    )

    registry = EntityRegistry(
        data_root
    )

    assert (
        registry.resolve(
            "Super Nintendo"
        )
        == "platform.nintendo.snes"
    )


def test_registry_duplicate_exact_alias_is_ambiguous(
    tmp_path,
):

    data_root = (
        tmp_path
        / "data"
    )

    _write_entity(
        data_root,
        Path("manufacturers/example.yaml"),
        {
            "id": "manufacturer.example",
            "type": "manufacturer",
            "name": "Example Hardware",
            "aliases": [
                "Example Company"
            ],
        },
    )

    _write_entity(
        data_root,
        Path("publishers/example.yaml"),
        {
            "id": "publisher.example",
            "type": "publisher",
            "name": "Example Software",
            "aliases": [
                "Example Company"
            ],
        },
    )

    registry = EntityRegistry(
        data_root
    )

    assert (
        registry.resolve(
            "Example Company"
        )
        is None
    )

    assert registry.by_alias[
        "example company"
    ] == [
        "manufacturer.example",
        "publisher.example",
    ]


def test_registry_get_remains_exact_id_authoritative(
    tmp_path,
):

    data_root = (
        tmp_path
        / "data"
    )

    _write_entity(
        data_root,
        Path("cores/bsnes.yaml"),
        {
            "id": "core.bsnes",
            "type": "core",
            "name": "bsnes",
            "aliases": [],
        },
    )

    _write_entity(
        data_root,
        Path("emulators/bsnes.yaml"),
        {
            "id": "emulator.bsnes",
            "type": "emulator",
            "name": "bsnes",
            "aliases": [],
        },
    )

    registry = EntityRegistry(
        data_root
    )

    assert (
        registry.get(
            "core.bsnes"
        )["id"]
        == "core.bsnes"
    )

    assert (
        registry.get(
            "emulator.bsnes"
        )["id"]
        == "emulator.bsnes"
    )


def test_registry_production_duplicate_names_are_ambiguous():

    registry = EntityRegistry()

    assert (
        registry.resolve(
            "Nintendo"
        )
        is None
    )

    assert (
        registry.resolve(
            "Snes9x"
        )
        is None
    )

    assert (
        registry.get(
            "manufacturer.nintendo"
        )["id"]
        == "manufacturer.nintendo"
    )

    assert (
        registry.get(
            "publisher.nintendo"
        )["id"]
        == "publisher.nintendo"
    )

    assert (
        registry.get(
            "core.snes9x"
        )["id"]
        == "core.snes9x"
    )

    assert (
        registry.get(
            "emulator.snes9x"
        )["id"]
        == "emulator.snes9x"
    )
