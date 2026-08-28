"""
=========================================================
RVDB Project Path Integration Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_project_paths_v2.py

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

from commands.validate import (
    cmd_validate,
)

from engine.context import (
    load_entities as context_load_entities,
)

from engine.loader import (
    load_entities,
)

from services.registry import (
    EntityRegistry,
)


def test_registry_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    monkeypatch.chdir(
        tmp_path
    )

    registry = (
        EntityRegistry()
    )

    assert registry.exists(
        "platform.nintendo.snes"
    )

    assert registry.exists(
        "manufacturer.nintendo"
    )


def test_loader_default_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    monkeypatch.chdir(
        tmp_path
    )

    entities = (
        load_entities()
    )

    assert len(
        entities
    ) == 42

    ids = {
        entity.id
        for entity in entities
    }

    assert (
        "platform.nintendo.snes"
        in ids
    )


def test_context_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    monkeypatch.chdir(
        tmp_path
    )

    entities = (
        context_load_entities()
    )

    assert len(
        entities
    ) == 42


def test_validate_command_is_cwd_independent(
    tmp_path,
    monkeypatch,
    capsys,
):

    monkeypatch.chdir(
        tmp_path
    )

    cmd_validate()

    output = (
        capsys
        .readouterr()
        .out
    )

    assert (
        "Entities checked: 42"
        in output
    )

    assert (
        "Valid: 42"
        in output
    )

    assert (
        "Schema Errors: 0"
        in output
    )

    assert (
        "Relationship Errors: 0"
        in output
    )

    assert (
        "Validation OK"
        in output
    )
